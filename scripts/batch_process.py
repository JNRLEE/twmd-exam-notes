import os
import shutil
import glob
import subprocess

RAW_DIR = "../02_past_exams/raw_pdfs"
PARSED_DIR = "../02_past_exams/parsed"

# 對應考選部常見編號到學科名稱
SUBJECT_MAP = {
    '0103': '醫學三',
    '0104': '醫學四',
    '0105': '醫學五',
    '0106': '醫學六'
}

def main():
    print("=== TWMD 國考題目自動整理與轉換系統 ===")
    
    # 掃描並找出尚未進入年份分類資料夾的 pdf
    loose_pdfs = [f for f in glob.glob(os.path.join(RAW_DIR, '*.pdf')) if os.path.isfile(f)]
    
    if not loose_pdfs:
        print("目前在 raw_pdfs 根目錄沒有找到散落的未命名官方 PDF。")
        print("注意：請將新下載的檔案直接放在 raw_pdfs 下，不需手動建資料夾。")
    
    # 1. 整理散落的 PDF 到年份資料夾
    # 考選部檔名的固定規則，例如：115020_0103_xxx.pdf 或 115020_MOD0103_xxx.pdf
    # 115020 = 115年第2次 (通常010或020代表梯次，我們以使用者提示或簡單邏輯轉譯)
    for pdf_path in loose_pdfs:
        filename = os.path.basename(pdf_path)
        parts = filename.split('_')
        
        exam_code = parts[0] # e.g. 115020
        # 簡單邏輯: 前三碼為年份，後三碼決定梯次 (020=第二次, 010=第一次，如果不是再微調)
        if len(exam_code) >= 6:
            year = exam_code[:3]
            session = "2" if "20" in exam_code[3:] else "1"
            year_session = f"{year}_{session}"
        else:
            year_session = "Uncategorized"
            
        target_dir = os.path.join(RAW_DIR, year_session)
        os.makedirs(target_dir, exist_ok=True)
        
        # 移入特定年份資料夾 (保留考選部的原始檔名也可，但為了維持架構，我們可以保持亂碼檔名，以腳本直接讀取)
        new_pdf_path = os.path.join(target_dir, filename)
        shutil.move(pdf_path, new_pdf_path)
        print(f"已分類：{filename} -> {year_session}/")

    # 2. 針對「所有年份資料夾」啟動 moex_parser.py 執行轉換
    year_folders = [d for d in os.listdir(RAW_DIR) if os.path.isdir(os.path.join(RAW_DIR, d))]
    
    for yf in year_folders:
        yf_path = os.path.join(RAW_DIR, yf)
        pdfs_in_yf = [f for f in os.listdir(yf_path) if f.endswith('.pdf')]
        
        # 找出該年度的所有考科 (根據 0103, 0104...來配對)
        subjects_found = set()
        for pdf in pdfs_in_yf:
            for code in SUBJECT_MAP.keys():
                if code in pdf:
                    subjects_found.add(code)
                    
        for code in subjects_found:
            subject_name = SUBJECT_MAP[code]
            # 尋找 題目PDF、更正解答PDF、原始解答PDF
            q_pdf = next((os.path.join(yf_path, f) for f in pdfs_in_yf if f'_{code}_' in f or f == f'q_med{code[-1]}.pdf'), None)
            
            # 解答優先順序：更正解答 (MOD) > 原始解答 (ANS)
            a_pdf = next((os.path.join(yf_path, f) for f in pdfs_in_yf if f'MOD{code}' in f or f == f'mod_ans_med{code[-1]}.pdf'), None)
            if not a_pdf:
                a_pdf = next((os.path.join(yf_path, f) for f in pdfs_in_yf if f'ANS{code}' in f or f == f'ans_med{code[-1]}.pdf'), None)
                
            if q_pdf:
                print(f"[{yf}] 開始解析 {subject_name} ...")
                cmd = ["python", "moex_parser.py", yf, subject_name, "--ques_pdf", q_pdf]
                if a_pdf:
                    cmd.extend(["--ans_pdf", a_pdf])
                
                # 執行解析腳本
                subprocess.run(cmd)

    print("=== 所有考題已處理完畢 ===")

if __name__ == "__main__":
    main()
