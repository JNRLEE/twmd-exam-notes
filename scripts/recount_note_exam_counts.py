import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES = [
    ROOT / "01_notes" / "醫學三" / "note_3.md",
    ROOT / "01_notes" / "醫學四" / "note_4.md",
    ROOT / "01_notes" / "醫學五" / "note_5.md",
    ROOT / "01_notes" / "醫學六" / "note_6.md",
]
FOCUSED = ROOT / "03_focused_topics"

COUNT_SUFFIX = re.compile(r"[（(]考題\d+[）)]$")
TRAILING_ENGLISH_AFTER_CJK = re.compile(r"(?<=[\u4e00-\u9fff])\s*[A-Za-z][A-Za-z0-9/ -]*$")


def strip_count(title: str) -> str:
    title = COUNT_SUFFIX.sub("", title or "").strip()
    return title.rstrip(":：").strip()


def title_key(title: str) -> str:
    title = unicodedata.normalize("NFKC", strip_count(title))
    title = COUNT_SUFFIX.sub("", title).strip()
    title = title.rstrip(":：").strip()
    return re.sub(r"\s+", "", title)


def candidate_title_keys(title: str) -> list[str]:
    normalized = unicodedata.normalize("NFKC", strip_count(title)).strip()
    keys = [title_key(normalized)]
    stripped = TRAILING_ENGLISH_AFTER_CJK.sub("", normalized).strip()
    if stripped != normalized:
        keys.append(title_key(stripped))
    return keys


def lookup_count(section_counts: Counter, rel: str, specialty: str, topic: str) -> int:
    for topic_key in candidate_title_keys(topic):
        count = section_counts.get((rel, specialty, topic_key), 0)
        if count:
            return count
    return 0


def load_section_counts() -> Counter:
    counts = Counter()
    for path in FOCUSED.glob("*/*_逐題解析.json"):
        rows = json.loads(path.read_text(encoding="utf-8"))
        for row in rows:
            note_path = row.get("matched_note_path")
            specialty = title_key(row.get("classified_specialty", ""))
            topic = title_key(row.get("classified_topic", ""))
            if note_path and specialty and topic and topic != title_key("未匹配"):
                counts[(note_path, specialty, topic)] += 1
    return counts


def recount_note(path: Path, section_counts: Counter) -> tuple[int, int]:
    rel = str(path.relative_to(ROOT))
    lines = path.read_text(encoding="utf-8").splitlines()

    h2_counts_by_index = {}
    h1_children = defaultdict(list)
    current_h1 = None
    current_specialty = ""
    h1_indices = []

    for idx, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            current_h1 = idx
            current_specialty = title_key(line[2:].strip())
            h1_indices.append(idx)
            continue
        if line.startswith("## "):
            count = lookup_count(section_counts, rel, current_specialty, line[3:].strip())
            h2_counts_by_index[idx] = count
            if current_h1 is not None:
                h1_children[current_h1].append(idx)

    for idx, count in h2_counts_by_index.items():
        title = strip_count(lines[idx][3:].strip())
        lines[idx] = f"## {title}（考題{count}）"

    for idx in h1_indices:
        total = sum(h2_counts_by_index.get(child, 0) for child in h1_children.get(idx, []))
        title = strip_count(lines[idx][2:].strip())
        lines[idx] = f"# {title}（考題{total}）"

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(h1_indices), len(h2_counts_by_index)


def main():
    section_counts = load_section_counts()
    print(f"matched_questions={sum(section_counts.values())}")
    print(f"matched_sections={len(section_counts)}")
    total_h1 = total_h2 = 0
    for note in NOTES:
        h1, h2 = recount_note(note, section_counts)
        total_h1 += h1
        total_h2 += h2
        print(f"{note.relative_to(ROOT)}: h1={h1}，h2={h2}")
    print(f"updated_h1={total_h1}")
    print(f"updated_h2={total_h2}")


if __name__ == "__main__":
    main()
