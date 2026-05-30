import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOCUSED_DIR = ROOT / "03_focused_topics"
OUT_DIR = ROOT / "04_daily_review"


HIGH_YIELD_TERMS = {
    "診斷",
    "治療",
    "首選",
    "禁忌",
    "定義",
    "分類",
    "分級",
    "併發症",
    "危險因子",
    "預後",
    "手術",
    "抗生素",
    "懷孕",
    "篩檢",
    "急症",
    "高血壓",
    "糖尿病",
    "腎衰竭",
    "癌",
    "感染",
    "血栓",
}

ADD_STRONG_TERMS = {
    "首選",
    "禁忌",
    "診斷標準",
    "定義",
    "分級",
    "治療",
    "手術",
    "死亡率",
    "預後",
    "篩檢",
    "急症",
    "懷孕",
}

TOO_FINE_TERMS = {
    "percentile",
    "百分位",
    "第99",
    "單一基因",
    "罕見",
    "圖形如下",
    "附圖",
    "試題代號",
    "某研究",
    "統計",
    "百分位",
    "cyp3a",
    "grapefruit",
    "葡萄柚",
    "第幾型心肌梗塞",
}

STOP_WORDS = {
    "下列",
    "何者",
    "關於",
    "有關",
    "錯誤",
    "正確",
    "最不",
    "最適",
    "敘述",
    "患者",
    "病人",
    "治療",
    "診斷",
    "檢查",
    "使用",
    "可能",
    "包括",
    "標準答案",
    "答案",
}


def normalize(text):
    return unicodedata.normalize("NFKC", text or "").lower()


def terms(text):
    text = normalize(text)
    found = []
    found.extend(re.findall(r"[a-z][a-z0-9+-]{2,}", text))
    for chunk in re.findall(r"[\u4e00-\u9fff]{2,}", text):
        max_n = min(5, len(chunk))
        for n in range(2, max_n + 1):
            found.extend(chunk[i : i + n] for i in range(len(chunk) - n + 1))
    return Counter(t for t in found if t not in STOP_WORDS)


def coverage_score(explanation, note_excerpt):
    exp_terms = key_terms(explanation)
    note_terms = key_terms(note_excerpt)
    if not exp_terms:
        return 0.0

    overlap = sum(1 for term in exp_terms if term in note_terms)
    return overlap / len(exp_terms)


def key_terms(text):
    norm = normalize(text)
    found = set(re.findall(r"[a-z][a-z0-9+-]{3,}", norm))
    found.update(re.findall(r"\d+(?:\.\d+)?\s*(?:mg|g|ml|mmhg|週|天|月|年|%)?", norm))

    medical_patterns = [
        r"[\u4e00-\u9fff]{0,6}(?:診斷|治療|手術|禁忌|分級|分類|定義|篩檢|首選|併發症|危險因子|預後)[\u4e00-\u9fff]{0,6}",
        r"[\u4e00-\u9fff]{0,6}(?:高血壓|糖尿病|懷孕|腎衰竭|血栓|感染|癌|腫瘤|心肌梗塞|腦膜炎|甲狀腺|副甲狀腺|低血鈣|高血鈣)[\u4e00-\u9fff]{0,6}",
    ]
    for pattern in medical_patterns:
        found.update(re.findall(pattern, norm))

    return {term.strip() for term in found if term.strip() and term.strip() not in STOP_WORDS}


def high_yield_score(row):
    text = f"{row.get('question_text', '')} {row.get('reference_explanation', '')}"
    norm = normalize(text)
    score = 0
    for term in HIGH_YIELD_TERMS:
        if normalize(term) in norm:
            score += 1
    if re.search(r"\b(first|initial|gold standard|contraindication|management)\b", norm):
        score += 2
    if any(token in norm for token in ["首選", "禁忌", "定義", "分級", "診斷標準"]):
        score += 2
    return score


def is_too_fine(row, repeated_key_count):
    text = f"{row.get('question_text', '')} {row.get('reference_explanation', '')}"
    norm = normalize(text)
    if any(normalize(term) in norm for term in TOO_FINE_TERMS):
        return True, "題目依賴附圖、百分位或過度細節，較不適合直接寫進總筆記。"

    key = topic_key(row)
    if repeated_key_count[key] >= 2:
        return False, ""

    if high_yield_score(row) >= 4:
        return False, ""

    explanation = row.get("reference_explanation", "")
    if not any(term in explanation for term in ADD_STRONG_TERMS):
        return True, "單題知識點較窄，且未包含首選、禁忌、診斷標準、分級等可泛化考點。"

    return False, ""


def topic_key(row):
    return (
        row.get("exam_subject", ""),
        row.get("classified_specialty", ""),
        row.get("classified_topic", ""),
        row.get("matched_note_subheading", ""),
    )


def recommendation_text(row):
    explanation = row.get("reference_explanation", "").strip()
    answer = row.get("answer") or "未提供"
    qn = row.get("question_number")
    text = re.sub(r"^標準答案為\s*[^。]+。", "", explanation).strip()
    text = re.sub(r"^答案為\s*[^。]+。", "", text).strip()
    if not text:
        text = explanation

    if len(text) > 320:
        text = text[:320].rstrip("，。；,; ") + "。"

    return f"補充（{row.get('exam_session')} {row.get('exam_subject')} Q{qn}, 答案{answer}）：{text}"


def classify_row(row, repeated_key_count):
    coverage = coverage_score(row.get("reference_explanation", ""), row.get("matched_note_excerpt", ""))
    too_fine, reason = is_too_fine(row, repeated_key_count)
    repeated = repeated_key_count[topic_key(row)]
    high_yield = high_yield_score(row)

    if too_fine:
        status = "skip_too_fine"
    elif coverage >= 0.28:
        status = "covered"
        reason = "現有 note 已涵蓋解析主要關鍵字，暫不需新增。"
    elif high_yield < 4 and repeated < 2:
        status = "skip_too_fine"
        reason = "目前只在單題出現且可泛化程度不足，先不補進總筆記。"
    else:
        status = "recommend_add"
        reason = "現有 note 有相關位置，但缺少本題可泛化的考點。"

    return {
        "exam_session": row.get("exam_session"),
        "exam_subject": row.get("exam_subject"),
        "question_number": row.get("question_number"),
        "answer": row.get("answer"),
        "status": status,
        "reason": reason,
        "coverage_score": round(coverage, 3),
        "high_yield_score": high_yield,
        "topic_repeat_count": repeated,
        "specialty": row.get("classified_specialty"),
        "topic": row.get("classified_topic"),
        "subheading": row.get("matched_note_subheading"),
        "note_path": row.get("matched_note_path"),
        "note_line": row.get("matched_note_line"),
        "note_content": row.get("matched_note_excerpt"),
        "question_text": row.get("question_text"),
        "reference_explanation": row.get("reference_explanation"),
        "recommended_addition": recommendation_text(row) if status == "recommend_add" else "",
    }


def load_rows(exam_session):
    rows = []
    for path in sorted((FOCUSED_DIR / exam_session).glob(f"{exam_session}_醫學*_逐題解析.json")):
        rows.extend(json.loads(path.read_text(encoding="utf-8")))
    return rows


def write_markdown(exam_session, analyses):
    target = OUT_DIR / exam_session
    target.mkdir(parents=True, exist_ok=True)
    path = target / f"{date.today().isoformat()}_{exam_session}_note缺口分析.md"

    grouped_recommend = defaultdict(list)
    grouped_skip = defaultdict(list)
    grouped_covered = defaultdict(list)
    for item in analyses:
        key = (item["exam_subject"], item["specialty"], item["topic"])
        if item["status"] == "recommend_add":
            grouped_recommend[key].append(item)
        elif item["status"] == "skip_too_fine":
            grouped_skip[key].append(item)
        else:
            grouped_covered[key].append(item)

    with path.open("w", encoding="utf-8") as f:
        f.write(f"# {exam_session} note 缺口分析\n\n")
        f.write("> 來源：03_focused_topics 逐題解析。目的：判斷 01_notes 是否完整，以及哪些內容值得補回筆記。\n\n")
        f.write("## 總覽\n\n")
        f.write(f"- 總題數：{len(analyses)}\n")
        f.write(f"- 建議補筆記：{sum(1 for x in analyses if x['status'] == 'recommend_add')}\n")
        f.write(f"- 已覆蓋：{sum(1 for x in analyses if x['status'] == 'covered')}\n")
        f.write(f"- 太細略過：{sum(1 for x in analyses if x['status'] == 'skip_too_fine')}\n\n")

        f.write("## 建議補進 01_notes\n\n")
        if not grouped_recommend:
            f.write("目前沒有明確需要新增的項目。\n\n")
        for (subject, specialty, topic), items in sorted(grouped_recommend.items()):
            f.write(f"### {subject}｜{specialty}｜{topic}\n\n")
            for item in items:
                f.write(f"#### Q{item['question_number']}（答案 {item['answer'] or '未提供'}）\n\n")
                f.write(f"理由：{item['reason']} 覆蓋率 {item['coverage_score']}\n\n")
                f.write("原本 note 位置：")
                if item["note_path"]:
                    f.write(f"`{item['note_path']}:{item['note_line']}`\n\n")
                else:
                    f.write("未找到\n\n")
                f.write("原本 note 內容：\n\n")
                f.write((item["note_content"] or "目前無對應內容").strip() + "\n\n")
                f.write("推薦增加內容：\n\n")
                f.write(item["recommended_addition"].strip() + "\n\n")

        f.write("## 太細，暫不建議補進總筆記\n\n")
        if not grouped_skip:
            f.write("目前沒有被判定為太細的項目。\n\n")
        for (subject, specialty, topic), items in sorted(grouped_skip.items()):
            f.write(f"### {subject}｜{specialty}｜{topic}\n\n")
            for item in items:
                f.write(
                    f"- Q{item['question_number']}（答案 {item['answer'] or '未提供'}）："
                    f"{item['reason']}\n"
                )
            f.write("\n")

        f.write("## 已覆蓋，不需優先新增\n\n")
        for (subject, specialty, topic), items in sorted(grouped_covered.items()):
            qlist = ", ".join(f"Q{x['question_number']}" for x in items)
            f.write(f"- {subject}｜{specialty}｜{topic}：{qlist}\n")

    return path


def main():
    parser = argparse.ArgumentParser(description="Generate 04 note gap analysis from 03 focused review.")
    parser.add_argument("exam_session", help="e.g. 113_2")
    args = parser.parse_args()

    rows = load_rows(args.exam_session)
    repeated = Counter(topic_key(row) for row in rows)
    analyses = [classify_row(row, repeated) for row in rows]

    target = OUT_DIR / args.exam_session
    target.mkdir(parents=True, exist_ok=True)
    json_path = target / f"{date.today().isoformat()}_{args.exam_session}_note缺口分析.json"
    json_path.write_text(json.dumps(analyses, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path = write_markdown(args.exam_session, analyses)

    print(f"Generated {len(analyses)} gap analysis rows")
    print(f"- {md_path.relative_to(ROOT)}")
    print(f"- {json_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
