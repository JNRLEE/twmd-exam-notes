# Git Worktree 運作流程指南

這個專案包含許多由 AI Agent 生成的檔案，為了避免這些大量、可能需要頻繁砍掉重練的檔案污染主線 (main)，我們採用 Git Worktree。

## 概念
Git Worktree 允許你在同一個 Git Repository 中開啟多個不同的實體資料夾（綁定不同分支），讓你可以在各自獨立的資料夾中工作，互不干擾。

## 初始化 Agent 工作區
假設你在主資料夾 `/Users/jnrle/Documents/Projects/TWMD_EXAM`：

1. 建立用於分析考古題的分支與工作區：
   ```bash
   git branch agent/analysis
   git worktree add ../TWMD_EXAM_Analysis agent/analysis
   ```
2. 建立用於生成每日複習的分支與工作區：
   ```bash
   git branch agent/review_gen
   git worktree add ../TWMD_EXAM_Review agent/review_gen
   ```

這樣一來，你可以把 Gemini 的執行目錄設定在 `../TWMD_EXAM_Analysis`，他產生的檔案如果是錯的，你可以直接 `git reset --hard` 或不管它。
當他在該工作區生成了完美的 `03_focused_topics` 內容並 commit 後，你可以回到主資料夾 `TWMD_EXAM`：
```bash
git merge agent/analysis
```
如此便能乾淨地整合 Agent 產出的價值檔案。
