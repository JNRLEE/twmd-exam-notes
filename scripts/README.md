# 考古題解析與自動分類系統 (MOEX Auto-Processor)

這支工具組主要用來將考選部（MOEX）下載下來的大量官方題庫與答案 PDF，自動分類年份並無痛轉換為對 AI Agent 友善的格式（Markdown 文本及 JSON 檔案）。

## 目錄結構架構 (維持整潔的關鍵)

系統會自動維護以下的樹狀結構：
```text
02_past_exams/
  ├── raw_pdfs/
  │   ├── 112_1/                 # 系統會自動根據考選部檔名的前綴(如:112010)建立資料夾
  │   ├── ...
  │   └── <請把自己從考選部下載的一堆雜亂名稱PDF直接丟在這裡>
  └── parsed/
      ├── 112_1/
      │   ├── 112_1_醫學三.md      # 解析完成的乾淨 Agent 可讀檔
      │   └── 112_1_醫學三.json
```

## 安裝依賴

第一次使用前，請確保您的環境安裝了相關套件：
```bash
cd scripts
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 日常操作流 (Daily Workflow)

您**不需**像之前那樣手動重新命名長長的亂碼檔名，或是手控輸入指令建立年份。

**只需兩步：**

1. 將考選部下載的「試題 PDF」、「標準答案 PDF」甚至是「更正解答 PDF」，全部丟進 `02_past_exams/raw_pdfs` 中。
2. 啟動一鍵整理與轉檔腳本：

```bash
cd scripts
source .venv/bin/activate
python batch_process.py
```

`batch_process.py` 會自動判斷它們的年份、梯次、以及科目 (醫學三～六)，先幫您把它們分類歸檔進整潔的年份資料夾中，接著自動呼叫 PDF parser，在 `parsed/年份_梯次/` 目錄下生出完美的 Markdown 檔與 JSON！

## 產生 03_focused_topics 逐題解析

當 `02_past_exams/parsed/<年份_梯次>/` 已經有醫學三～六的 JSON 後，可執行：

```bash
cd scripts
python3 generate_focused_review.py 113_2
```

系統會讀取：

```text
02_past_exams/parsed/113_2/113_2_醫學三.json
02_past_exams/parsed/113_2/113_2_醫學四.json
02_past_exams/parsed/113_2/113_2_醫學五.json
02_past_exams/parsed/113_2/113_2_醫學六.json
```

並輸出到：

```text
03_focused_topics/113_2/
```

每一題會包含：

- 題目與標準答案
- 參考詳解
- 對應的 `01_notes` 原文摘錄
- JSON 中也會保留候選對應段落，方便之後人工校正

Markdown 版只顯示筆記原文摘錄；專科、大主題、小標題、來源行號等 metadata 只保留在 JSON 裡，避免閱讀時干擾。

## 產生 04_daily_review note 缺口分析

當 `03_focused_topics/<年份_梯次>/` 已經有逐題解析 JSON 後，可執行：

```bash
cd scripts
python3 generate_note_gap_analysis.py 113_2
```

系統會輸出到：

```text
04_daily_review/113_2/
```

分析會把每題分成三類：

- `recommend_add`：建議補回 `01_notes`。會列出原本 note 位置、原本 note 內容、推薦增加內容。
- `covered`：現有 note 已大致涵蓋，暫不需要新增。
- `skip_too_fine`：題目太細、依賴附圖/單題細節，或不夠泛化，暫不建議補進總筆記。
