import os
import re
import json
import argparse
import pdfplumber

def parse_moex_exam_pdf(pdf_path):
    """
    Parses a MOEX exam PDF into a structured list of questions and options.
    """
    questions = []
    current_question = None
    
    # 匹配題號 (例如 "1 關於..." 或 "1." 或 "1 ")
    q_pattern = re.compile(r'^(\d{1,2})[\s\.、]+(.*)')
    
    # 匹配選項：(A)、A.、A)；MOEX PDF 常會把選項接在題幹同一行。
    opt_pattern = re.compile(r'(?<![A-Za-z0-9])(?:\(([A-D])\)|([A-D])[\.\)])\s*')

    def split_options(text):
        matches = list(opt_pattern.finditer(text))
        if not matches:
            return text.strip(), {}

        stem = text[: matches[0].start()].strip()
        options = {}
        for i, match in enumerate(matches):
            letter = match.group(1) or match.group(2)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            options[letter] = text[match.end() : end].strip()
        return stem, options

    def append_text(question, text):
        stem, options = split_options(text)
        if options:
            if stem:
                question["question_text"] += " " + stem
            question["options"].update(options)
        elif question["options"]:
            last_opt = list(question["options"].keys())[-1]
            question["options"][last_opt] += " " + text
        else:
            question["question_text"] += " " + text
    
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 排除頁首頁尾常見干擾 (如：代號：xxx, 頁次：xxx)
        if "代號：" in line or "頁次：" in line or line.startswith("類別：") or line.startswith("科目："):
            continue

        # 嘗試匹配新題目。PDF 換行時可能把「90 mmHg」這類行首數字誤判成題號；
        # 醫師二階每科 80 題，且題號應遞增，因此不符合者視為前一題續文。
        q_match = q_pattern.match(line)
        if q_match:
            q_num = int(q_match.group(1))
            q_text = q_match.group(2).strip()
            if re.fullmatch(r'[\d\s]+', q_text):
                if current_question:
                    current_question["question_text"] += " " + line
                continue
            expected_q_num = 1 if not current_question else current_question["question_number"] + 1
            if q_num > 80 or q_num != expected_q_num:
                if current_question:
                    append_text(current_question, line)
                continue

            # 如果發現新題目，把舊題目收尾存入
            if current_question:
                questions.append(current_question)

            q_text, options = split_options(q_text)
            
            current_question = {
                "question_number": q_num,
                "question_text": q_text,
                "options": options,
                "answer": "" # 將由獨立的解答處理函數提供
            }
            continue
            
        # 處理選項或題目延續的文字
        if current_question:
            append_text(current_question, line)

    if current_question:
        questions.append(current_question)

    return questions

def parse_moex_answer_pdf(ans_pdf_path):
    """
    Parses MOEX answer PDFs. The official typically puts answers in a horizontal table format.
    Return a dict: { question_number: "answer_letter" }
    """
    answers = {}
    # 全形轉半形
    full_to_half = str.maketrans('ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ＃', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#')
    with pdfplumber.open(ans_pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for i in range(len(table) - 1):
                    row1 = table[i]
                    row2 = table[i+1]
                    if not row1 or not row2:
                        continue
                    if str(row1[0]).strip() in ('題序', '題號') and str(row2[0]).strip() == '答案':
                        for q, a in zip(row1[1:], row2[1:]):
                            if q and a and str(q).strip().isdigit():
                                ans_val = str(a).strip().translate(full_to_half)
                                answers[int(str(q).strip())] = ans_val
    return answers

def main():
    parser = argparse.ArgumentParser(description="Parse MOEX Exam PDFs to JSON/Markdown for AI Agents.")
    parser.add_argument("exam_year_session", help="e.g., 112_1")
    parser.add_argument("subject", help="e.g., 醫學三")
    parser.add_argument("--ques_pdf", required=True, help="Path to the question PDF")
    parser.add_argument("--ans_pdf", help="Path to the answer PDF (optional)")
    parser.add_argument("--out_dir", default="../02_past_exams/parsed", help="Output directory")

    args = parser.parse_args()

    print(f"Parsing [ {args.exam_year_session} {args.subject} ] ...")
    
    # 1. Parse questions
    questions = parse_moex_exam_pdf(args.ques_pdf)
    print(f"Extracted {len(questions)} questions.")

    # 2. Parse answers if provided
    if args.ans_pdf:
        answers = parse_moex_answer_pdf(args.ans_pdf)
        print(f"Extracted {len(answers)} answers.")
        for q in questions:
            q_num = q["question_number"]
            if q_num in answers:
                q["answer"] = answers[q_num]

    # 3. Output formats
    # 將輸出資料夾加上年份梯次的子目錄
    target_out_dir = os.path.join(args.out_dir, args.exam_year_session)
    os.makedirs(target_out_dir, exist_ok=True)
    
    # 修改原本的檔名只保留科目，不再帶年份前綴（因為已經在年份資料夾了）
    basename = f"{args.exam_year_session}_{args.subject}"
    
    # JSON output
    json_path = os.path.join(target_out_dir, f"{basename}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    # Markdown Output (Agent Friendly)
    md_path = os.path.join(target_out_dir, f"{basename}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {args.exam_year_session} {args.subject} 考古題與解答\n\n")
        f.write("> 本檔案由 parser 自動生成，用於 Agent 萃取重點知識。\n\n")
        
        for q in questions:
            f.write(f"### Q{q['question_number']}. {q['question_text']}\n")
            for opt_k, opt_v in q["options"].items():
                f.write(f"- ({opt_k}) {opt_v}\n")
            f.write(f"\n**標準答案**: {q.get('answer', '未提供')}\n\n")
            f.write("---\n")

    print(f"Successfully generated:\n- {md_path}\n- {json_path}")

if __name__ == "__main__":
    main()
