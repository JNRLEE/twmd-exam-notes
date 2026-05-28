import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
NOTES = {
    "醫學三": ROOT / "01_notes" / "醫學三" / "note_3.md",
    "醫學四": ROOT / "01_notes" / "醫學四" / "note_4.md",
    "醫學五": ROOT / "01_notes" / "醫學五" / "note_5.md",
    "醫學六": ROOT / "01_notes" / "醫學六" / "note_6.md",
}
PARSED_DIR = ROOT / "02_past_exams" / "parsed"
FOCUSED_DIR = ROOT / "03_focused_topics"
EXAM_SCOPES = {
    "醫學三": "內科、家庭醫學科等科目及其相關臨床實例與醫學倫理",
    "醫學四": "小兒科、皮膚科、神經科、精神科等科目及其相關臨床實例與醫學倫理",
    "醫學五": "外科、骨科、泌尿科等科目及其相關臨床實例與醫學倫理",
    "醫學六": "麻醉科、眼科、耳鼻喉科、婦產科、復健科等科目及其相關臨床實例與醫學倫理",
}

AUTO_EXPLANATION_MARKERS = (
    "題幹關鍵字最接近",
    "可用筆記重點判斷",
    "本題尚未在 01_notes 找到可靠對應段落",
    "目前 01_notes 沒有可靠",
    "本題重新對應到",
)

STOP_TOKENS = {
    "下列",
    "何者",
    "關於",
    "有關",
    "敘述",
    "正確",
    "錯誤",
    "最不",
    "適當",
    "病人",
    "患者",
    "病患",
    "治療",
    "診斷",
    "檢查",
    "使用",
    "用藥",
    "藥物",
    "發現",
    "發炎",
    "抗發炎",
    "類固醇",
    "非類固醇",
    "造成",
    "可能",
    "下列何者",
    "何者正確",
    "何者錯誤",
}

ALIASES = {
    "hyperlipidemia": ["高脂血症", "高血脂", "statin", "fibrate"],
    "hypocalcemia": ["低血鈣", "血鈣", "calcium", "pth", "vitamin d"],
    "hypercalcemia": ["高血鈣", "血鈣", "calcium", "pth", "pthrp"],
    "calcium": ["血鈣", "鈣", "calcium"],
    "pth": ["副甲狀腺", "血鈣", "calcium"],
    "hyperkalemia": ["高血鉀", "血鉀", "potassium"],
    "hypokalemia": ["低血鉀", "血鉀", "potassium"],
    "hyponatremia": ["低血鈉", "血鈉", "sodium"],
    "hypernatremia": ["高血鈉", "血鈉", "sodium"],
    "insulinoma": ["胰島素瘤", "低血糖", "insulin", "c-peptide"],
    "men": ["multiple endocrine neoplasia", "甲狀腺髓質癌", "嗜鉻細胞瘤"],
    "cisatracurium": ["神經肌肉阻斷劑", "肌肉鬆弛"],
    "rocuronium": ["神經肌肉阻斷劑", "肌肉鬆弛"],
    "vecuronium": ["神經肌肉阻斷劑", "肌肉鬆弛"],
    "sugammadex": ["神經肌肉阻斷劑", "肌肉鬆弛"],
    "bispectral": ["bis", "麻醉監測", "麻醉深度"],
    "bpp": ["biophysical profile", "產前胎兒評估"],
    "nst": ["nonstress test", "產前胎兒評估"],
    "hsv": ["疱疹", "角膜炎", "樹枝狀"],
    "volvulus": ["腸扭轉"],
    "duchenne": ["肌肉失養症", "dystrophin", "心肌"],
    "sma": ["脊髓性肌肉萎縮", "smn1"],
}

BROAD_TOPIC_ANCHORS = {
    "高脂血症": ("hyperlipidemia",),
    "高血脂": ("hyperlipidemia",),
    "hyperkalemia": ("離子平衡",),
    "高血鉀": ("離子平衡",),
    "hypokalemia": ("離子平衡",),
    "低血鉀": ("離子平衡",),
    "hyponatremia": ("離子平衡",),
    "hypernatremia": ("離子平衡",),
    "低血鈉": ("離子平衡",),
    "高血鈉": ("離子平衡",),
    "hypocalcemia": ("calcium metabolism",),
    "hypercalcemia": ("calcium metabolism",),
    "低血鈣": ("calcium metabolism",),
    "高血鈣": ("calcium metabolism",),
    "osteoporosis": ("calcium metabolism",),
    "骨質疏鬆": ("calcium metabolism",),
    "gout": ("arthritis",),
    "痛風": ("arthritis",),
    "nsaid": ("離子平衡", "arthritis", "pericarditis"),
    "nsaids": ("離子平衡", "arthritis", "pericarditis"),
}

GENERIC_ANCHORS_EN = {
    "about",
    "adult",
    "after",
    "before",
    "blood",
    "cause",
    "clinical",
    "disease",
    "drugs",
    "error",
    "female",
    "human",
    "male",
    "normal",
    "patient",
    "patients",
    "risk",
    "syndrome",
    "test",
    "therapy",
    "treatment",
    "tumor",
    "tumour",
    "cancer",
    "acute",
    "chronic",
    "surgery",
    "surgical",
    "injury",
    "wrong",
}

GENERIC_ANCHORS_ZH = {
    "下列",
    "何者",
    "正確",
    "錯誤",
    "適當",
    "病人",
    "患者",
    "病患",
    "治療",
    "診斷",
    "檢查",
    "處置",
    "敘述",
    "使用",
    "症狀",
    "疾病",
    "臨床",
    "發生",
    "造成",
    "可能",
    "風險",
    "危險",
}

KNOWN_ZH_ANCHORS = {
    "高脂血症",
    "高血壓",
    "低血壓",
    "高血鉀",
    "低血鉀",
    "高血鈣",
    "低血鈣",
    "高血鈉",
    "低血鈉",
    "糖尿病",
    "甲狀腺",
    "副甲狀腺",
    "腎上腺",
    "肝炎",
    "肝硬化",
    "黃疸",
    "腹水",
    "膽結石",
    "膽囊炎",
    "胰臟炎",
    "腸阻塞",
    "腸扭轉",
    "吞嚥困難",
    "胃食道逆流",
    "消化性潰瘍",
    "敗血症",
    "腦膜炎",
    "蜂窩性組織炎",
    "肺炎",
    "結核",
    "氣喘",
    "肺栓塞",
    "貧血",
    "淋巴瘤",
    "白血病",
    "痛風",
    "類風濕",
    "紅斑性狼瘡",
    "骨質疏鬆",
    "昏厥",
    "心衰竭",
    "心包膜炎",
    "主動脈剝離",
    "心律不整",
    "瓣膜",
    "腎移植",
    "透析",
    "水痘",
    "麻疹",
    "百日咳",
    "川崎",
    "新生兒黃疸",
    "壞死性腸炎",
    "胎便吸入",
    "腦性麻痺",
    "癲癇",
    "失智",
    "巴金森",
    "思覺失調",
    "憂鬱",
    "焦慮",
    "青光眼",
    "白內障",
    "視網膜",
    "角膜",
    "鼻咽癌",
    "中耳炎",
    "麻醉監測",
    "麻醉深度",
    "局部麻醉",
    "神經肌肉阻斷",
    "剖腹產",
    "子癲前症",
    "產後出血",
    "子宮內膜異位",
    "子宮肌瘤",
    "卵巢",
    "不孕",
    "攝護腺",
    "睪丸",
    "尿路結石",
    "脊椎",
    "骨折",
    "骨腫瘤",
}


@dataclass
class NoteSection:
    subject: str
    path: str
    line: int
    specialty: str
    topic: str
    content: str
    tokens: Counter


def normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text or "").lower()


def tokenize(text: str) -> Counter:
    text = normalize(text)
    tokens = []
    if "非類固醇抗發炎" in text or "non-steroidal anti-inflammatory" in text:
        tokens.extend(["nsaid", "nsaids"])
    if "高血鉀" in text or "hyperkalemia" in text:
        tokens.extend(["hyperkalemia", "高血鉀", "血鉀", "potassium"])
    if "低血鉀" in text or "hypokalemia" in text:
        tokens.extend(["hypokalemia", "低血鉀", "血鉀", "potassium"])
    if "高血鈣" in text or "hypercalcemia" in text:
        tokens.extend(["hypercalcemia", "高血鈣", "血鈣", "calcium"])
    if "低血鈣" in text or "hypocalcemia" in text:
        tokens.extend(["hypocalcemia", "低血鈣", "血鈣", "calcium"])
    for token in re.findall(r"[a-z][a-z0-9+-]{1,}", text):
        if len(token) >= 3 or token in {"ca", "na", "k"}:
            tokens.append(token)
            tokens.extend(ALIASES.get(token, []))

    for chunk in re.findall(r"[\u4e00-\u9fff]+", text):
        max_n = min(7, len(chunk))
        for n in range(2, max_n + 1):
            tokens.extend(chunk[i : i + n] for i in range(len(chunk) - n + 1))

    cleaned = []
    for token in tokens:
        if token in STOP_TOKENS:
            continue
        if len(token.strip()) < 2:
            continue
        cleaned.append(token)
    return Counter(cleaned)


def anchor_tokens(text: str) -> set[str]:
    text = normalize(text)
    anchors = set()
    phrase_aliases = {
        "非類固醇抗發炎": ["nsaid", "nsaids"],
        "non-steroidal anti-inflammatory": ["nsaid", "nsaids"],
        "高血鉀": ["hyperkalemia", "高血鉀"],
        "低血鉀": ["hypokalemia", "低血鉀"],
        "高血鈣": ["hypercalcemia", "高血鈣"],
        "低血鈣": ["hypocalcemia", "低血鈣"],
    }
    for phrase, values in phrase_aliases.items():
        if phrase in text:
            anchors.update(values)

    for token in re.findall(r"[a-z][a-z0-9+-]{1,}", text):
        if token in GENERIC_ANCHORS_EN:
            continue
        if len(token) >= 4 or token in {"pth", "hcg", "hiv", "hbv", "hcv", "bis", "bpp", "nst"}:
            anchors.add(token)
            anchors.update(ALIASES.get(token, []))

    for token in KNOWN_ZH_ANCHORS:
        if token in text:
            anchors.add(token)

    return {anchor for anchor in anchors if len(anchor) >= 3 or anchor in {"pth", "hcg", "hiv", "hbv", "hcv", "bis", "bpp", "nst"}}


def has_anchor_match(query_text: str, section: NoteSection) -> bool:
    anchors = anchor_tokens(query_text)
    if not anchors:
        return False
    section_text = normalize(" ".join([section.specialty, section.topic, section.content]))
    for anchor in anchors:
        normalized_anchor = normalize(anchor)
        if normalized_anchor in section_text:
            return True
        for broad_topic in BROAD_TOPIC_ANCHORS.get(normalized_anchor, ()):
            if broad_topic in section_text:
                return True
    return False


def has_topic_anchor_match(query_text: str, section: NoteSection) -> bool:
    anchors = anchor_tokens(query_text)
    if not anchors:
        return False
    topic_text = normalize(" ".join([section.specialty, section.topic]))
    for anchor in anchors:
        normalized_anchor = normalize(anchor)
        if normalized_anchor in topic_text:
            return True
        for broad_topic in BROAD_TOPIC_ANCHORS.get(normalized_anchor, ()):
            if broad_topic in topic_text:
                return True
    return False


def split_note_sections(subject: str, path: Path) -> list[NoteSection]:
    sections = []
    specialty = ""
    current = None
    lines = path.read_text(encoding="utf-8").splitlines()

    def flush():
        if not current:
            return
        content = "\n".join(current["lines"]).strip()
        if not content:
            return
        searchable = " ".join([current["specialty"], current["topic"], content])
        sections.append(
            NoteSection(
                subject=subject,
                path=str(path.relative_to(ROOT)),
                line=current["line"],
                specialty=current["specialty"],
                topic=current["topic"],
                content=content,
                tokens=tokenize(searchable),
            )
        )

    for lineno, line in enumerate(lines, 1):
        if line.startswith("# "):
            flush()
            current = None
            specialty = line[2:].strip()
            continue
        if line.startswith("## "):
            flush()
            current = {
                "line": lineno,
                "specialty": specialty,
                "topic": line[3:].strip(),
                "lines": [line],
            }
            continue
        if current is not None:
            current["lines"].append(line)
    flush()
    return sections


def load_sections() -> dict[str, list[NoteSection]]:
    return {subject: split_note_sections(subject, path) for subject, path in NOTES.items()}


def build_idf(sections: list[NoteSection]) -> dict[str, float]:
    df = defaultdict(int)
    for section in sections:
        for token in section.tokens:
            df[token] += 1
    total = len(sections)
    return {token: math.log((total + 1) / (count + 0.5)) + 1 for token, count in df.items()}


def useful_explanation(text: str) -> str:
    if not text:
        return ""
    if any(marker in text for marker in AUTO_EXPLANATION_MARKERS):
        return ""
    return text


def question_search_text(question: dict, old_row: Optional[dict]) -> str:
    question_text = question.get("question_text", "")
    parts = [question_text, question_text, question_text]
    answer = question.get("answer") or ""
    options = question.get("options") or {}
    negative_stem = any(marker in question_text for marker in ("錯誤", "最不適當", "不包括", "不是", "不恰當"))
    if not negative_stem:
        for key, value in options.items():
            if key == answer:
                parts.extend([value, value])
    return "\n".join(parts)


def score_section(query: Counter, section: NoteSection, idf: dict[str, float]) -> float:
    if not query:
        return 0.0
    score = 0.0
    for token, q_count in query.items():
        tf = section.tokens.get(token, 0)
        if not tf:
            continue
        score += min(q_count, 4) * (1 + math.log(tf)) * idf.get(token, 1.0)

    topic_text = normalize(section.topic)
    content_text = normalize(section.content)
    for token in query:
        if len(token) >= 4 and token in topic_text:
            score += 10
        elif len(token) >= 4 and token in content_text:
            score += 2

    score = score / (1 + math.log(60 + sum(section.tokens.values())))
    return score


def select_section(subject: str, query_text: str, sections_by_subject: dict[str, list[NoteSection]], idf_by_subject: dict[str, dict[str, float]]):
    query = tokenize(query_text)
    primary_sections = sections_by_subject[subject]
    scored = [
        (score_section(query, section, idf_by_subject[subject]), section)
        for section in primary_sections
    ]
    scored = [(score, section) for score, section in scored if score > 0]
    scored.sort(key=lambda item: item[0], reverse=True)
    if not scored:
        return None, [], "unmatched"

    candidates = scored[:5]
    anchored = [(score, section) for score, section in scored if has_anchor_match(query_text, section)]
    if not anchored:
        return None, candidates, "unmatched_no_anchor"
    best_score, best = anchored[0]
    second_score = anchored[1][0] if len(anchored) > 1 else 0.0

    confident = best_score >= 4.8 and (best_score - second_score >= 0.75 or best_score >= second_score * 1.22)
    very_confident = best_score >= 8.0 and best_score >= second_score * 1.08
    topic_confident = has_topic_anchor_match(query_text, best)
    content_only_confident = best_score >= 14.0 and (best_score - second_score >= 2.0 or best_score >= second_score * 1.35)
    topic_low_confident = topic_confident and best_score >= 3.5 and (best_score - second_score >= 0.4 or best_score >= second_score * 1.12)
    if (topic_confident and (confident or very_confident)) or topic_low_confident or content_only_confident:
        return best, candidates, "primary_reaudited"
    return None, candidates, "unmatched_low_confidence"


def note_location(section: NoteSection) -> str:
    return f"{section.path}:{section.line} > # {section.specialty} > ## {section.topic}"


def build_reason(section: Optional[NoteSection], candidates, scope: str) -> str:
    if section is None:
        if candidates:
            top = "、".join(f"{candidate.topic}({score:.1f})" for score, candidate in candidates[:3])
            return f"重新審核後，候選段落分數接近或不夠高（{top}），先不硬配。"
        return "重新審核後，題幹與選項在 01_notes 找不到足夠相近的整個 ## 段落。"
    return (
        "重新審核題幹、選項與正答後，此題核心概念和本 ## 段落的標題/內容最相近；"
        f"本段落為「{section.topic}」。"
    )


def build_reference_explanation(row: dict, section: Optional[NoteSection]) -> str:
    old = useful_explanation(row.get("reference_explanation", ""))
    if old:
        return old
    answer = row.get("answer") or "未提供"
    if section is None:
        return f"答案為 {answer}。目前 01_notes 沒有可靠整段對應；建議回到題幹與標準答案補人工詳解。"
    return f"答案為 {answer}。本題重新對應到「{section.topic}」，可先用該 ## 段落複習相關考點。"


def section_candidate_json(candidates):
    rows = []
    for score, section in candidates:
        rows.append(
            {
                "score": round(score, 2),
                "exam_subject": section.subject,
                "source_note": section.path,
                "line": section.line,
                "specialty": section.specialty,
                "topic": section.topic,
            }
        )
    return rows


def render_md(exam_session: str, subject: str, rows: list[dict]) -> str:
    out = [
        f"# {exam_session}_{subject} 逐題解析",
        "",
        f"> 範圍：{EXAM_SCOPES.get(subject, subject)}",
        "> 來源：02_past_exams/parsed；專科對應已重新審核為整個 ## 章節，並附對應理由。",
        "",
    ]
    for row in rows:
        out.extend(
            [
                f"## Q{row['question_number']}",
                "",
                row.get("question_text", "").strip(),
                "",
                f"**標準答案**：{row.get('answer') or '未提供'}",
                "",
                "### 參考詳解",
                "",
                row.get("reference_explanation", "").strip(),
                "",
                "### 專科與筆記對應",
                "",
            ]
        )
        if row.get("matched_note_full_section"):
            out.extend(
                [
                    f"筆記位置：{row['matched_note_path']}:{row['matched_note_line']} > # {row['classified_specialty']} > ## {row['classified_topic']}",
                    "",
                    f"對應理由：{row['match_reason']}",
                    "",
                    row["matched_note_full_section"].strip(),
                    "",
                ]
            )
        else:
            out.extend(
                [
                    "目前四本 note 尚無明確對應段落。",
                    "",
                    f"對應理由：{row['match_reason']}",
                    "",
                ]
            )
        out.extend(["---", ""])
    return "\n".join(out)


def rebuild_file(exam_session: str, subject: str, sections_by_subject, idf_by_subject):
    parsed_path = PARSED_DIR / exam_session / f"{exam_session}_{subject}.json"
    focused_path = FOCUSED_DIR / exam_session / f"{exam_session}_{subject}_逐題解析.json"
    old_rows = {}
    if focused_path.exists():
        old_rows = {
            row.get("question_number"): row
            for row in json.loads(focused_path.read_text(encoding="utf-8"))
        }

    parsed_questions = json.loads(parsed_path.read_text(encoding="utf-8"))
    rows = []
    changed = Counter()
    for question in parsed_questions:
        qn = question.get("question_number")
        old_row = old_rows.get(qn, {})
        section, candidates, scope = select_section(
            subject,
            question_search_text(question, old_row),
            sections_by_subject,
            idf_by_subject,
        )
        old_path = old_row.get("matched_note_path") or ""
        old_line = old_row.get("matched_note_line")
        if section is None:
            new_path = ""
            new_line = None
            changed["unmatched"] += 1
        else:
            new_path = section.path
            new_line = section.line
            if old_path != new_path or old_line != new_line:
                changed["remapped"] += 1
            else:
                changed["kept"] += 1

        row = {
            "exam_session": exam_session,
            "exam_subject": subject,
            "question_number": qn,
            "question_text": question.get("question_text", ""),
            "options": question.get("options", {}),
            "answer": question.get("answer", ""),
            "reference_explanation": build_reference_explanation({**question, **old_row}, section),
            "classified_specialty": section.specialty if section else "未匹配",
            "classified_topic": section.topic if section else "未匹配",
            "matched_note_subheading": section.topic if section else "未匹配",
            "matched_note_heading_path": f"# {section.specialty} > ## {section.topic}" if section else "",
            "matched_note_excerpt": section.content if section else "",
            "matched_note_path": new_path,
            "matched_note_line": new_line,
            "matched_note_scope": scope,
            "searched_primary_note": str(NOTES[subject].relative_to(ROOT)),
            "candidate_matches": section_candidate_json(candidates),
            "match_reason": build_reason(section, candidates, scope),
            "matched_note_full_section": section.content if section else "",
        }
        rows.append(row)

    focused_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path = FOCUSED_DIR / exam_session / f"{exam_session}_{subject}_逐題解析.md"
    md_path.write_text(render_md(exam_session, subject, rows), encoding="utf-8")
    return changed


def main():
    sections_by_subject = load_sections()
    idf_by_subject = {
        subject: build_idf(sections)
        for subject, sections in sections_by_subject.items()
    }

    total = Counter()
    sessions = sorted(path.name for path in PARSED_DIR.iterdir() if path.is_dir())
    for session in sessions:
        for subject in NOTES:
            parsed_path = PARSED_DIR / session / f"{session}_{subject}.json"
            if not parsed_path.exists():
                continue
            changed = rebuild_file(session, subject, sections_by_subject, idf_by_subject)
            total.update(changed)
            print(f"{session} {subject}: {dict(changed)}")
    print(f"TOTAL: {dict(total)}")


if __name__ == "__main__":
    main()
