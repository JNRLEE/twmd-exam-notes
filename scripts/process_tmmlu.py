import json
import os

def main():
    raw_path = "/Users/jnrle/Documents/Projects/TWMD_EXAM/02_past_exams/parsed/tmmlu_raw.json"
    out_dir = "/Users/jnrle/Documents/Projects/TWMD_EXAM/02_past_exams/parsed"
    
    with open(raw_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = []
    
    if "rows" in data:
        for idx, row in enumerate(data["rows"]):
            item = row["row"]
            q_data = {
                "question_number": idx + 1,
                "question_text": item.get("question", "").strip(),
                "options": {
                    "A": str(item.get("A", "")).strip(),
                    "B": str(item.get("B", "")).strip(),
                    "C": str(item.get("C", "")).strip(),
                    "D": str(item.get("D", "")).strip()
                },
                "answer": str(item.get("answer", "")).strip()
            }
            questions.append(q_data)
            
    # Markdown
    md_path = os.path.join(out_dir, "TMMLU_Medical_License.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# 歷屆醫師國考綜合題庫 (Hugging Face TMMLU+)\n\n")
        f.write("> 此為由 HuggingFace 擷取下來的綜合國考題庫（共 100 題），已轉換為 Agent 可解析的格式。\n\n")
        for q in questions:
            f.write(f"### Q{q['question_number']}. {q['question_text']}\n")
            for k, v in q["options"].items():
                if v:
                    f.write(f"- ({k}) {v}\n")
            f.write(f"\n**標準答案**: {q.get('answer', '未提供')}\n\n")
            f.write("---\n")
            
    # JSON
    json_path = os.path.join(out_dir, "TMMLU_Medical_License.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        
    # Clean up raw
    os.remove(raw_path)
    print(f"Successfully generated {len(questions)} questions.")

if __name__ == "__main__":
    main()
