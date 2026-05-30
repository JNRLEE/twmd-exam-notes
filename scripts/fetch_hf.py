import os
import json
from datasets import load_dataset

def main():
    print("Loading TMMLU+ (medical_license) dataset from Hugging Face...")
    # 載入醫學國考資料集 (test split)
    ds = load_dataset("MIAMAI/TMMLUplus", "medical_license", split="test")
    valid_ds = load_dataset("MIAMAI/TMMLUplus", "medical_license", split="val")
    
    # 為了資料量稍微大一點，我們把 test 跟 val 合併，大概有數百題
    questions = []
    
    def process_split(dataset, start_q_num):
        q_num = start_q_num
        for item in dataset:
            # TMMLU+ schema: 'question', 'A', 'B', 'C', 'D', 'answer'
            data = {
                "question_number": q_num,
                "question_text": item["question"].strip(),
                "options": {
                    "A": str(item.get("A", "")).strip(),
                    "B": str(item.get("B", "")).strip(),
                    "C": str(item.get("C", "")).strip(),
                    "D": str(item.get("D", "")).strip()
                },
                "answer": item["answer"].strip() # A, B, C, or D
            }
            questions.append(data)
            q_num += 1
        return q_num

    next_q = process_split(ds, 1)
    process_split(valid_ds, next_q)
    
    print(f"Extracted {len(questions)} questions from TMMLU+.")

    out_dir = "../02_past_exams/parsed"
    os.makedirs(out_dir, exist_ok=True)
    
    basename = "TMMLU_Medical_License"
    
    # JSON 輸出
    json_path = os.path.join(out_dir, f"{basename}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        
    # Markdown 輸出
    md_path = os.path.join(out_dir, f"{basename}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# 歷屆醫師國考綜合題庫 (Hugging Face TMMLU+ 版本)\n\n")
        f.write("> 來源：MIAMAI/TMMLUplus (medical_license)。此為供 Agent 分析的大型開源混合題庫，雖未精細區分年份或醫學三～六，但具備完整題型與解答。\n\n")
        for q in questions:
            f.write(f"### Q{q['question_number']}. {q['question_text']}\n")
            for k, v in q["options"].items():
                if v:
                    f.write(f"- ({k}) {v}\n")
            f.write(f"\n**標準答案**: {q.get('answer', '未提供')}\n\n")
            f.write("---\n")

    print(f"Successfully saved to:\n- {md_path}\n- {json_path}")

if __name__ == "__main__":
    main()
