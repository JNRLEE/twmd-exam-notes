import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES = {
    "醫學三": ROOT / "01_notes" / "醫學三" / "note_3.md",
    "醫學四": ROOT / "01_notes" / "醫學四" / "note_4.md",
    "醫學五": ROOT / "01_notes" / "醫學五" / "note_5.md",
    "醫學六": ROOT / "01_notes" / "醫學六" / "note_6.md",
}
PARSED_DIR = ROOT / "02_past_exams" / "parsed"
OUT_DIR = ROOT / "03_focused_topics"
EXAM_SCOPES = {
    "醫學三": "內科、家庭醫學科等科目及其相關臨床實例與醫學倫理",
    "醫學四": "小兒科、皮膚科、神經科、精神科等科目及其相關臨床實例與醫學倫理",
    "醫學五": "外科、骨科、泌尿科等科目及其相關臨床實例與醫學倫理",
    "醫學六": "麻醉科、眼科、耳鼻喉科、婦產科、復健科等科目及其相關臨床實例與醫學倫理",
}
AUTO_EXPLANATION_PHRASES = (
    "本題最接近 01_notes",
    "目前 01_notes 沒有找到足夠相近",
)
MIN_MATCH_SCORE = 8.0
CROSS_NOTE_SCORE_RATIO = 1.8
CROSS_NOTE_SCORE_DELTA = 12.0


def normalize_text(text):
    text = unicodedata.normalize("NFKC", text or "")
    return text.lower()


def token_counter(text):
    text = normalize_text(text)
    tokens = []
    english = re.findall(r"[a-z][a-z0-9+-]{2,}", text)
    tokens.extend(english)
    tokens.extend(re.findall(r"\d+(?:\.\d+)?", text))

    aliases = []
    for token in english:
        if token.endswith("statin") and token not in {"somatostatin"}:
            aliases.extend(["statin", "高血脂", "膽固醇"])
        if token in {"cyp", "cyp3a", "cytochrome"}:
            aliases.extend(["cyp450", "藥物代謝"])
        if token in {"dysphagia", "aphagia", "odynophagia", "phagophobia"}:
            aliases.extend(["吞嚥困難", "吞嚥"])
        if token in {"brudzinski", "kernig"}:
            aliases.extend(["腦膜炎", "中樞感染"])
        if token in {"hyperparathyroidism", "hypoparathyroidism"}:
            aliases.extend(["副甲狀腺", "高鈣", "低鈣"])
        if token in {"hyperthyroidism", "hypothyroidism", "thyroxine", "tsh", "hcg"}:
            aliases.extend(["甲狀腺", "thyroid"])
        if token in {"sugammadex", "rocuronium", "vecuronium", "pancuronium"}:
            aliases.extend(["神經肌肉阻斷劑", "肌肉鬆弛"])
        if token in {"bis", "bispectral", "eeg"}:
            aliases.extend(["麻醉監測", "麻醉深度"])
        if token in {"acromegaly", "pituitary", "transsphenoidal", "somatostatin"}:
            aliases.extend(["肢端肥大", "腦垂", "pituitary"])
    tokens.extend(aliases)

    for chunk in re.findall(r"[\u4e00-\u9fff]{2,}", text):
        max_n = min(5, len(chunk))
        for n in range(2, max_n + 1):
            tokens.extend(chunk[i : i + n] for i in range(len(chunk) - n + 1))

    stop = {
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
    }
    return Counter(t for t in tokens if t not in stop)


def split_note_blocks(subject, path):
    blocks = []
    current_specialty = ""
    current_topic = ""
    current_block = None

    def flush():
        if current_block and current_block["content"].strip():
            current_block["content"] = current_block["content"].strip()
            current_block["tokens"] = token_counter(
                " ".join(
                    [
                        current_block["specialty"],
                        current_block["topic"],
                        current_block["subheading"],
                        current_block["content"],
                    ]
                )
            )
            blocks.append(current_block)

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("# "):
            flush()
            current_block = None
            current_specialty = line[2:].strip()
            current_topic = ""
            continue
        if line.startswith("## "):
            flush()
            current_block = None
            current_topic = line[3:].strip()
            continue
        if line.startswith("- "):
            flush()
            raw = line[2:].strip()
            subheading = re.split(r"[：:＝=]", raw, maxsplit=1)[0].strip() or raw[:40]
            current_block = {
                "exam_subject": subject,
                "source_note": str(path.relative_to(ROOT)),
                "line": lineno,
                "specialty": current_specialty,
                "topic": current_topic,
                "subheading": subheading,
                "content": raw,
            }
            continue
        if current_block and (line.startswith("  ") or line.startswith("\t") or not line.strip()):
            current_block["content"] += "\n" + line

    flush()
    return blocks


def load_note_index(subjects):
    blocks = []
    for subject in subjects:
        path = NOTES[subject]
        blocks.extend(split_note_blocks(subject, path))
    return blocks


def score_block(question_tokens, block):
    score = 0.0
    block_tokens = block["tokens"]
    block_text = normalize_text(
        " ".join([block["specialty"], block["topic"], block["subheading"], block["content"]])
    )
    for token, count in question_tokens.items():
        if token in block_tokens:
            score += min(count, 3) * (1.0 + min(len(token), 8) / 8)

    q_text = " ".join(question_tokens.keys())
    for field, boost in (("specialty", 8), ("topic", 6), ("subheading", 4)):
        value = normalize_text(block[field])
        if value and value in q_text:
            score += boost

    if question_tokens.get("statin") and "hyperlipedemia" in normalize_text(block["topic"]):
        score += 35
    elif question_tokens.get("statin") and "statin" in block_text:
        score += 18
    if question_tokens.get("吞嚥困難") and "吞嚥困難" in block_text:
        score += 18
    if question_tokens.get("腦膜炎") and "meningitis" in block_text:
        score += 18
    if question_tokens.get("副甲狀腺") and ("副甲狀腺" in block_text or "calcium metabolism" in block_text):
        score += 12
    if question_tokens.get("麻醉監測") and "麻醉監測" in block_text:
        score += 12
    if question_tokens.get("神經肌肉阻斷劑") and "神經肌肉阻斷劑" in block_text:
        score += 12
    if question_tokens.get("肢端肥大") and ("pituitary" in block_text or "肢端肥大" in block_text or "腦垂" in block_text):
        score += 30

    return score


def best_note_matches(question, blocks, limit=3):
    q_tokens = token_counter(question["question_text"])
    scored = []
    for block in blocks:
        score = score_block(q_tokens, block)
        if score > 0:
            scored.append((score, block))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [
        {
            "score": round(score, 2),
            "exam_subject": block["exam_subject"],
            "source_note": block["source_note"],
            "line": block["line"],
            "specialty": block["specialty"],
            "topic": block["topic"],
            "subheading": block["subheading"],
            "content": block["content"],
        }
        for score, block in scored[:limit]
        if score >= MIN_MATCH_SCORE
    ]


def select_note_matches(question, subject, note_blocks_by_subject, all_note_blocks):
    primary_matches = best_note_matches(question, note_blocks_by_subject[subject])
    all_matches = best_note_matches(question, all_note_blocks)
    if not primary_matches:
        if all_matches:
            return all_matches, "cross_note_fallback"
        return [], "unmatched"

    if not all_matches:
        return primary_matches, "primary_note"

    primary_best = primary_matches[0]
    all_best = all_matches[0]
    primary_source = primary_best["source_note"]
    all_source = all_best["source_note"]
    primary_score = primary_best["score"]
    all_score = all_best["score"]
    if (
        all_source != primary_source
        and all_score >= primary_score * CROSS_NOTE_SCORE_RATIO
        and all_score - primary_score >= CROSS_NOTE_SCORE_DELTA
    ):
        return all_matches, "cross_note_stronger"
    return primary_matches, "primary_note"


def build_explanation(question, matches):
    answer = question.get("answer") or "未提供"
    if not matches:
        return (
            f"答案為 {answer}。本題尚未在 01_notes 找到可靠對應段落，"
            "需要回到題幹關鍵字人工補齊詳解。"
        )

    best = matches[0]
    note = best["content"].replace("\n", " ")
    return (
        f"答案為 {answer}。題幹關鍵字最接近「{best['subheading']}」。"
        f"可用筆記重點判斷：{note[:220]}"
    )


def should_preserve_explanation(text):
    if not text:
        return False
    return not any(phrase in text for phrase in AUTO_EXPLANATION_PHRASES)


def load_existing_explanations(exam_session, subject):
    path = OUT_DIR / exam_session / f"{exam_session}_{subject}_逐題解析.json"
    if not path.exists():
        return {}
    rows = json.loads(path.read_text(encoding="utf-8"))
    preserved = {}
    for row in rows:
        explanation = row.get("reference_explanation", "")
        if should_preserve_explanation(explanation):
            preserved[row.get("question_number")] = explanation
    return preserved


def note_heading_path(match):
    if not match:
        return ""
    parts = []
    if match.get("specialty"):
        parts.append(f"# {match['specialty']}")
    if match.get("topic"):
        parts.append(f"## {match['topic']}")
    if match.get("subheading"):
        parts.append(f"- {match['subheading']}")
    return " > ".join(parts)


def enrich_exam_file(exam_session, subject, note_blocks_by_subject, all_note_blocks):
    src = PARSED_DIR / exam_session / f"{exam_session}_{subject}.json"
    questions = json.loads(src.read_text(encoding="utf-8"))
    existing_explanations = load_existing_explanations(exam_session, subject)

    enriched = []
    for question in questions:
        matches, match_scope = select_note_matches(
            question, subject, note_blocks_by_subject, all_note_blocks
        )
        best = matches[0] if matches else None
        question_number = question.get("question_number")
        reference_explanation = existing_explanations.get(
            question_number, build_explanation(question, matches)
        )
        enriched.append(
            {
                "exam_session": exam_session,
                "exam_subject": subject,
                "question_number": question_number,
                "question_text": question.get("question_text", ""),
                "options": question.get("options", {}),
                "answer": question.get("answer", ""),
                "reference_explanation": reference_explanation,
                "classified_specialty": best["specialty"] if best else "未匹配",
                "classified_topic": best["topic"] if best else "未匹配",
                "matched_note_subheading": best["subheading"] if best else "未匹配",
                "matched_note_heading_path": note_heading_path(best),
                "matched_note_excerpt": best["content"] if best else "",
                "matched_note_path": best["source_note"] if best else "",
                "matched_note_line": best["line"] if best else None,
                "matched_note_scope": match_scope,
                "searched_primary_note": str(NOTES[subject].relative_to(ROOT)),
                "candidate_matches": matches,
            }
        )
    return enriched


def write_outputs(exam_session, subject, rows):
    target = OUT_DIR / exam_session
    target.mkdir(parents=True, exist_ok=True)

    json_path = target / f"{exam_session}_{subject}_逐題解析.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = target / f"{exam_session}_{subject}_逐題解析.md"
    with md_path.open("w", encoding="utf-8") as f:
        f.write(f"# {exam_session} {subject} 逐題解析\n\n")
        f.write(f"> 範圍：{EXAM_SCOPES.get(subject, subject)}\n")
        f.write("> 來源：02_past_exams/parsed，自動對照 01_notes 的小標題內容。\n\n")
        for row in rows:
            f.write(f"## Q{row['question_number']}\n\n")
            f.write(f"{row['question_text']}\n\n")
            f.write(f"**標準答案**：{row['answer'] or '未提供'}\n\n")
            f.write("### 參考詳解\n\n")
            f.write(f"{row['reference_explanation']}\n\n")
            f.write("### 專科與筆記對應\n\n")
            if row["matched_note_excerpt"]:
                if row.get("matched_note_heading_path"):
                    location = row["matched_note_heading_path"]
                    if row.get("matched_note_path"):
                        location = f"{row['matched_note_path']}:{row['matched_note_line']} > {location}"
                    f.write(f"筆記位置：{location}\n\n")
                f.write(row["matched_note_excerpt"].strip())
                f.write("\n\n")
            else:
                f.write("目前四本 note 尚無明確對應段落。\n\n")
            f.write("---\n\n")

    return md_path, json_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate per-question focused review files from parsed past exams."
    )
    parser.add_argument("exam_session", help="e.g. 113_2")
    parser.add_argument(
        "--subjects",
        nargs="+",
        default=["醫學三", "醫學四", "醫學五", "醫學六"],
        choices=list(NOTES.keys()),
    )
    parser.add_argument(
        "--note-subjects",
        nargs="+",
        default=list(NOTES.keys()),
        choices=list(NOTES.keys()),
        help="01_notes subjects to search for note matching. Defaults to all notes.",
    )
    args = parser.parse_args()

    note_blocks_by_subject = {
        subject: load_note_index([subject]) for subject in args.note_subjects
    }
    all_note_blocks = [
        block for blocks in note_blocks_by_subject.values() for block in blocks
    ]
    print(
        "Loaded "
        f"{len(all_note_blocks)} note blocks from "
        f"{', '.join('01_notes/' + subject for subject in args.note_subjects)}."
    )

    for subject in args.subjects:
        if subject not in note_blocks_by_subject:
            note_blocks_by_subject[subject] = load_note_index([subject])
            all_note_blocks.extend(note_blocks_by_subject[subject])
        rows = enrich_exam_file(
            args.exam_session, subject, note_blocks_by_subject, all_note_blocks
        )
        md_path, json_path = write_outputs(args.exam_session, subject, rows)
        print(f"Generated {subject}: {len(rows)} questions")
        print(f"- {md_path.relative_to(ROOT)}")
        print(f"- {json_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
