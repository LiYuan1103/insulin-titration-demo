# NOTES：方法、假設與已知限制

依指示，過程中沒有發問。所有不確定之處都在這裡寫明我採用的做法。

## 1. PubMed 的存取與核對方式

- **shell 連不到 PubMed**：`eutils.ncbi.nlm.nih.gov`、`pubmed.ncbi.nlm.nih.gov`、Europe PMC（`www.ebi.ac.uk`）都被環境的網路代理拒絕（HTTP 403）。改用網頁讀取工具開 `pubmed.ncbi.nlm.nih.gov/<PMID>/`，38 個網址也全部失敗（主機名稱無法解析）。
- **實際做法**：檢索、取書目紀錄、讀 PMC 全文，全部透過本工作環境的 PubMed 連接器完成。它直接查 NCBI 的 PubMed／PMC 資料庫（E-utilities）。
- **「實際查到 PubMed 頁面」的解讀**：每一篇都從 PubMed 取回該 PMID 的官方紀錄，並逐一比對標題、期刊、出版年與 DOI。沒有任何一篇是憑記憶列入的。
- **兩次核對**：
  1. 萃取時，把每筆 PubMed 紀錄的重點記到檢索筆記。
  2. 產表前，用腳本把資料檔中 38 筆的 PMID、第一作者、年份、DOI 和筆記再對一次，全部相符。
- **建議**：投影片要直接引用數字的那幾篇，請在可連上 PubMed 的電腦再點一次表中的連結。

## 2. 年份與書目

- **年份**：一律採 PubMed 紀錄的首次出版日期，包括電子優先出版。有些期刊的紙本年份會晚 1–2 年，因此「期刊」欄附上卷(期):頁，方便對照：
  - Hsu 2015 → 紙本卷 18(2)
  - Aradóttir 2020 → 紙本卷 15(2)
  - Thomsen 2022 → 紙本卷 18(5)
  - Thomsen 2023 → 紙本卷 19(3)
  - 正式引用時，請依您使用的引用格式決定用哪一個年份。
- **第一作者**：寫法依 PubMed，格式為「姓＋名縮寫」。

## 3. 數值萃取

- **來源**：38 篇中，36 篇的數值取自 PubMed 摘要。EDITION 3（PMID 25641260）與 BEGIN Once Long（PMID 23043166）另讀了 PMC 全文，用來補滴定規則細節。
- **摘要沒寫的不補**：起始劑量、調整級距、頻率等，摘要沒寫的就標「摘要未載明」，即使該試驗的規則廣為人知（例如 Treat-to-Target Trial、AT.LANTUS 的演算法），也不憑記憶補上。要做教學投影片的規則細節，請查原文或補充資料。
- **單位與數字**：單位照原文（mg/dL 或 mmol/L）。必要時括號附上換算，例如 3.9–4.9 mmol/L ≈ 70–88 mg/dL；換算值為四捨五入的近似。HbA1c 組間差與 95% CI 照摘要抄錄，未重新計算。
- **My Dose Coach（PMID 37954005）**：摘要的 95% CI 寫作「0.01%–0.69%」，和點估計 −0.31% 的正負號不一致，疑似原文誤植。表中照錄並加註，引用前請看全文。
- **ONWARDS 5 事後分析（PMID 40803997）**：未單獨列為一筆，重點併入 ONWARDS 5 那一列的「偏誤風險簡評」。
- **MOBILE 基線資料（PMID 33118309）**：未納入主表，列在排除清單。

## 4. 分類時的判斷

| 研究 | 放在哪一類 | 理由 |
|---|---|---|
| d-Nav（PMID 30808512、38452101） | 5 演算法／AI | 核心是自動決定劑量的演算法，廠商稱為 AI 驅動。但演算法不公開，Lancet RCT 本身用的詞是 automated insulin dosing guidance。族群包含非單純基礎胰島素方案 |
| icodec 三種滴定法（PMID 33875484） | 1 固定規則 | 研究問題是「規則怎麼訂」 |
| TITRATE（PMID 19515182） | 2 自我滴定 | 兩組都是病人自調，比較的是目標值 |
| ONWARDS 5（PMID 37748181） | 3 數位工具 | 介入是 App 引導滴定，但混雜了每週胰島素的效果 |
| FreeDM2（PMID 42035781） | 4 CGM | 前 16 週明確要求病人自調基礎胰島素 |
| BIF（PMID 36758572） | 4 CGM | 以 CGM 空腹值作為滴定依據 |

- **住院研究**：Luo 2023、RL-DITR、iNCDSS 都是住院情境。因為與滴定工具直接相關而納入，表中已標明。

## 5. 納入與排除

- **篇數**：目標 25–40 篇，最後納入 38 篇，每類至少 6 篇。另有 38 篇讀過 PubMed 紀錄但排除，理由見 Excel 的「排除清單」。
- **研究設計**：第 1–2 類以 RCT 與統合分析為主。第 3–4 類各納入 1–2 篇重要的真實世界研究（MITI 實施研究、Carlson flash 研究）。第 5 類依指示「含概念驗證」，所以也納入：
  - 模型開發（Thomsen 2023）
  - 小型可行性研究（Aradóttir 2020）
  - 一篇純模擬研究（Arentsen 2025），用來說明「很多演算法還停在模擬」
- **貝氏方法與 LLM**：這次的 PubMed 檢索沒有找到以貝氏方法做 T2D 基礎胰島素滴定的人體試驗，也沒有找到大型語言模型直接調劑量的臨床試驗。SUMMARY 中如實寫為「本次檢索未找到」，不代表完全不存在。
- **未找到而未列入**：有些試驗印象中存在，但這次用 PubMed 找不到對應紀錄，例如某些 U300 自我滴定試驗的暱稱檢索。依「寧缺勿濫」原則，一律不列入。

## 6. 偏誤風險簡評的寫法

- 這不是正式的 RoB 2／ROBINS-I 評分。只列出最影響解讀的問題，例如盲性、樣本、追蹤長度、終點性質、對照組是否本來就調得不夠。
- 資助與利益衝突只寫 PubMed 紀錄看得到的部分，包括資助聲明與作者單位（例如作者單位是廠商）。看不到的就不推測。

## 7. 檔案與版本控制

- 只新增 `evidence/` 資料夾，內含 xlsx、SUMMARY.md、NOTES.md、summary.html，沒有修改任何既有檔案。
- 開發分支為 `claude/eager-cannon-fu70ji`。這個分支建立時，main 已經多了 `bayes.html`、`start.html`、`qr/` 等提交。因為本次只新增 `evidence/`，所以先把這次的提交改接到最新的 main 之後再合併，不會和既有檔案衝突。
- 網頁版為 `evidence/summary.html`，內容與 SUMMARY.md 相同，另發布成私人的 claude.ai 成品（artifact）。
- `evidence/build/` 放的是產生檔案用的原始資料與腳本，之後要增修文獻時可以直接重跑：
  - `data.py`：38 筆納入文獻與排除清單
  - `build_xlsx.py`：產生 Excel
  - `build_html.py` 加 `summary_template.html`：產生網頁版

  重跑方式：

  ```bash
  python3 -I evidence/build/build_xlsx.py evidence/build/data.py evidence/basal-insulin-titration-evidence.xlsx
  ```

  ```bash
  python3 -I evidence/build/build_html.py evidence/build/data.py evidence/build/summary_template.html evidence/summary.html
  ```
