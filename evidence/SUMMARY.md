# 第二型糖尿病基礎胰島素滴定：證據重點

- 檢索日期：2026-11-04；資料來源：PubMed（每篇都用 PubMed 紀錄核對過 PMID、標題、期刊、年份）
- 共納入 38 篇：固定規則／treat-to-target 8 篇、自我滴定 6 篇、數位工具 8 篇、CGM 6 篇、演算法／AI 10 篇
- 完整欄位見 [`basal-insulin-titration-evidence.xlsx`](basal-insulin-titration-evidence.xlsx)；方法與假設見 [`NOTES.md`](NOTES.md)
- 網頁版：[`summary.html`](summary.html)；已發布為私人成品 https://claude.ai/artifact/Uzy9C56QMWUUy3J46r26ya（需由擁有者分享後他人才能開啟）
- 數值大多取自 PubMed 摘要，只有 2 篇讀了 PMC 全文；放進投影片之前，請先回原文核對

---

## 一、各類證據重點

### 1. 固定規則／treat-to-target（glargine U100、U300、degludec）

1. Treat-to-Target Trial 確立了現在的滴定方式：用簡單規則把空腹血糖推到 ≤100 mg/dL，約六成病人可達 HbA1c ≤7%（PMID 14578243）。
2. 第二代基礎胰島素在相同目標下，HbA1c 降幅與 glargine U100 相當：EDITION 3 的 LSMD 是 0.04%（PMID 25641260），BEGIN Once Long 的 ETD 是 0.09%（PMID 23043166），BRIGHT 中 U300 對 degludec 的 LSMD 是 −0.05%（PMID 30104294）。三者的差異主要在低血糖，尤其是夜間與滴定初期。
3. EDITION 3 全文寫出了可直接教的 U300 規則：起始 0.2 U/kg，每週調一次；空腹 100–<140 mg/dL 加 3 U、≥140 加 6 U、60–<80 減 3 U；最後 U300 的劑量比 U100 多約 17%（PMID 25641260）。
4. 規則可以再簡化：degludec 每週只看一次早餐前血糖來調整，效果不輸看三天平均（PMID 23812875）。目標值的設定會改變低血糖風險：icodec 的目標設在 70–108 mg/dL 時，level 2 低血糖最多（PMID 33875484）。
5. 解讀時要記得兩件事。第一，treat-to-target 試驗刻意把兩組的 HbA1c 拉到一樣，所以真正在比的是低血糖。第二，這些試驗多為開放標籤、廠商參與，回診也比門診密集得多。CONCLUDE 的主要低血糖終點沒有達到顯著差異（PMID 31984443）。

### 2. 病人自我滴定 vs 醫療人員主導

1. 讓病人依規則自己調劑量，HbA1c 和醫師主導一樣好，或略好約 0.1–0.15%，嚴重低血糖沒有增加：AT.LANTUS 的降幅是 −1.22% vs −1.08%（PMID 15920040），亞洲 ATLAS 是 −1.40% vs −1.25%（PMID 25297660）。
2. 代價是輕度、夜間或症狀性低血糖可能稍多：PREDICTIVE 303 為 6.44 vs 4.95 次/人/年（PMID 17924873），ATLAS 也觀察到同樣趨勢。
3. 極簡規則就有效。例如每天加 1 U 直到空腹 ≤100 mg/dL（PMID 16842477），或「303 規則」：每 3 天調一次、每次 ±3 U、目標 80–110 mg/dL（PMID 17924873）。
4. 2025 年的網絡統合分析顯示，「每週自調 ≥2 次＋醫療人員支援」降 HbA1c 最多，嚴重低血糖不增加（PMID 40273351）。這是目前最直接的策略比較證據。

### 3. 數位工具／App／遠距協助

1. 數位工具主要解決的是滴定惰性，也就是劑量遲遲沒有調到位。只用簡訊加護理師電話，12 週內調到最佳劑量的比例就從 37% 升到 88%（PMID 26187303）；轉成常規照護後，仍有 84% 平均 24 天調到位（PMID 29555621）。
2. 和一般照護相比，App、語音系統或遠距平台多降 HbA1c 約 0.4–1.2%：TeleDiab-2（PMID 31173451）、台灣 Insultrate 多中心 RCT −0.87% vs −0.43%（PMID 42067440）、雲端共享決策（PMID 26645932）。即使對照組也是病人自調的紙本滴定表，App 仍多降約 0.3%（PMID 37954005）。
3. ONWARDS 5 是最大的 App 引導滴定試驗，52 週 HbA1c 差 −0.38%（PMID 37748181），但它同時換成了每週胰島素，無法分出 App 本身貢獻多少。
4. 限制很一致：幾乎都是開放標籤，追蹤多半只有 12–24 週，對照組往往是本來就調得不夠的一般照護，多數有廠商參與。

### 4. CGM 輔助的基礎胰島素調整

1. 只打基礎胰島素的 T2D 改用即時 CGM，HbA1c 比指尖血糖多降 0.4%、TIR 多 15%（MOBILE，PMID 34077499）。
2. 在已經使用 GLP-1RA 或 SGLT2i 的族群，CGM 搭配病人自調基礎胰島素，16 週仍多降 0.6%（FreeDM2，PMID 42035781）。統合分析的整體效果約為 −0.31%（PMID 38363342）。
3. 把 CGM 數值直接當成滴定依據，目前只有概念驗證與藥物試驗中的應用。用 CGM 每天調劑量，3–4 天即可讓夜間血糖達標（PMID 19120433）；每週胰島素 BIF 的試驗也以 CGM 空腹值滴定（PMID 36758572）。
4. 真實世界 flash 研究顯示 HbA1c 降 1.1–1.4%，但沒有對照組（PMID 35058312）。目前還找不到直接比較「CGM 導向滴定規則」與「指尖血糖滴定規則」的 RCT。

### 5. 演算法／機器學習／強化學習／AI

1. 人體 RCT 中，證據最強的是 d-Nav 自動劑量引導：6 個月 HbA1c −1.0% vs −0.3%，低血糖相同（PMID 30808512）。不過它的演算法屬於廠商專有，多位作者是廠商人員。
2. 2025 年的 iNCDSS 是設計最完整的 AI 滴定 RCT：住院 5 天內 TIR 不輸資深內分泌科醫師，76.4% vs 73.6%（PMID 40332936）。
3. 其他多為概念驗證：語音 AI 只有 32 人、追蹤 8 週（PMID 38039007）；強化學習 RL-DITR 是 16 位住院病人的單臂試驗（PMID 37710000）；模型由 2 週 CGM 資料預估劑量，共 8 人，中位數低估約 27%（PMID 31941361）。
4. 兩篇系統性回顧的結論相同：數學／機器學習模型的證據最少（PMID 36562599）；AI 胰島素管理的 RCT 截至 2025 年只有 7 篇，而且多為小型、短期研究（PMID 42930005）。

---

## 二、AI 滴定目前的證據到哪裡

**一句話：AI 滴定目前做到了「可行、短期內不輸醫師、沒看到安全訊號」，但還沒證明比「好的固定規則＋好的支援」更好。**

- **已經有的證據**
  - d-Nav 有一篇 6 個月的門診 RCT（PMID 30808512），以及 600 人的真實世界資料（PMID 38452101）。
  - iNCDSS 有一篇住院 5 天的非劣性 RCT（PMID 40332936）。
  - 語音 AI 有一篇 8 週的小型 RCT（PMID 38039007）。
  - 強化學習只有一篇 16 人的單臂試驗（PMID 37710000）。
- **還沒有的證據**
  - 除了演算法不公開的 d-Nav 之外，沒有任何門診、追蹤 ≥6 個月、以 HbA1c 為主要終點的機器學習或強化學習基礎胰島素滴定 RCT。
  - 沒有正面比較「AI」與「好的固定規則加病人自調」的試驗。現有 RCT 的對照組多半是本來就調得不夠的一般照護，或醫師單次判斷。
  - 這次的 PubMed 檢索中，沒有找到大型語言模型（LLM）直接調胰島素劑量的臨床試驗，也沒有找到以貝氏方法做 T2D 基礎胰島素滴定的人體試驗。這是檢索結果，不代表完全不存在。
- **方法學上的限制**
  - 前瞻性試驗樣本小（n=8–181），追蹤短（5 天–6 個月）。
  - 多在住院或單一學術中心進行，外推到台灣門診有限。
  - 大多開放標籤，廠商人員常為作者。
  - 終點多為替代指標，例如 TIR、達最佳劑量的時間、劑量誤差。
  - 樣本量不足以評估嚴重低血糖。
  - 部分系統的演算法不公開。
- **比較公平的說法**：比 AI 更早就有證據的，是「讓病人每週自調 ≥2 次，並提供醫療人員支援」（PMID 40273351）。AI 要被廣泛採用，至少得在這個標準上證明有額外好處，例如更快、更少低血糖，或更省人力。

---

## 三、台下最可能問的 5 個問題

**Q1. 讓病人自己調胰島素安全嗎？低血糖會不會比較多？**

> 嚴重低血糖沒有增加：4,961 人的 AT.LANTUS 中，自調組 1.1%、醫師組 0.9%，HbA1c 還多降 0.14%（PMID 15920040）；亞洲 ATLAS 的嚴重低血糖兩組都是 0.7%（PMID 25297660）。但輕度或夜間低血糖可能稍多，PREDICTIVE 303 是 6.44 vs 4.95 次/人/年（PMID 17924873）。所以重點是先教會病人「怎麼減量」，並有人可以問；網絡統合分析也顯示，有醫療人員支援的自調效果最好（PMID 40273351）。

**Q2. 空腹目標到底要設 80–100、80–130，還是更低？**

> 試驗中，目標越低，HbA1c 降得越多。TITRATE 把目標從 80–110 降到 70–90 mg/dL，HbA1c 多降 0.27%，整體低血糖沒有明顯增加（PMID 19515182）。不過 icodec 試驗中目標 70–108 的組 level 2 低血糖最多（PMID 33875484）；BEGIN Once Long 以 <5 mmol/L 為目標，一年後也只有 38% 真正達標（PMID 23043166）。反過來，BIF 試驗把目標放寬到 ≤120–140 mg/dL，HbA1c 仍達非劣性，低血糖少約 25%（PMID 36758572）。因此，試驗常用的 80–100 mg/dL（PMID 25641260）可以當作起點；低血糖風險高的人再個別放寬，這一步屬臨床判斷，本表沒有收錄相關指引。

**Q3. glargine U300、degludec、U100，哪一個比較好調？**

> 三者的 HbA1c 效果相當，差別在低血糖與劑量。U300 對 U100 的 HbA1c 差 0.04%，前 8 週低血糖事件率 RR 0.61，但劑量多約 17%（PMID 25641260）。U300 對 degludec 的 HbA1c 差 −0.05%，只有前 12 週滴定期 U300 的低血糖較少（PMID 30104294）。在高低血糖風險族群，degludec U200 與 U300 的主要低血糖終點沒有差異，夜間與嚴重低血糖較少只是探索性結果（PMID 31984443）。

**Q4. App 或 CGM 這些數位工具真的有用嗎？台灣有資料嗎？**

> 台灣有：2026 年發表的多中心 RCT，用醫師設定規則、Health2Sync App 執行，24 週 HbA1c −0.87% vs −0.43%（PMID 42067440）；德國 My Dose Coach 對紙本滴定表也多降 0.31%（PMID 37954005）。CGM 方面，只打基礎胰島素的病人改用即時 CGM，8 個月多降 0.4%（PMID 34077499），搭配自調 16 週多降 0.6%（PMID 42035781）。這些試驗多為開放標籤、追蹤半年以內，對照組又多是一般照護，因此很難分清楚效果來自工具本身，還是來自追蹤頻率增加。

**Q5. AI 可以取代醫師調胰島素嗎？**

> 現在還不行，目前的證據只到「短期不輸醫師」。最完整的 RCT 是住院 5 天、149 人，TIR 76.4% vs 73.6%，達到非劣性（PMID 40332936）；門診只有 d-Nav 一篇 6 個月 RCT，HbA1c 多降 0.7%（PMID 30808512）。系統性回顧指出，AI 胰島素管理的 RCT 只有 7 篇，而且多為小型短期研究（PMID 42930005）。比較實際的定位是：讓 AI 協助醫療團隊更頻繁地依規則調整，而不是取代臨床判斷。

---

## 四、引用文獻（依 PMID；DOI 取自 PubMed 紀錄）

| PMID | 第一作者 年份 | 期刊 | DOI |
|---|---|---|---|
| [14578243](https://pubmed.ncbi.nlm.nih.gov/14578243/) | Riddle 2003 | Diabetes Care | [10.2337/diacare.26.11.3080](https://doi.org/10.2337/diacare.26.11.3080) |
| [15920040](https://pubmed.ncbi.nlm.nih.gov/15920040/) | Davies 2005 | Diabetes Care | [10.2337/diacare.28.6.1282](https://doi.org/10.2337/diacare.28.6.1282) |
| [16842477](https://pubmed.ncbi.nlm.nih.gov/16842477/) | Gerstein 2006 | Diabet Med | [10.1111/j.1464-5491.2006.01881.x](https://doi.org/10.1111/j.1464-5491.2006.01881.x) |
| [17924873](https://pubmed.ncbi.nlm.nih.gov/17924873/) | Meneghini 2007 | Diabetes Obes Metab | [10.1111/j.1463-1326.2007.00804.x](https://doi.org/10.1111/j.1463-1326.2007.00804.x) |
| [19120433](https://pubmed.ncbi.nlm.nih.gov/19120433/) | King 2009 | Diabetes Obes Metab | [10.1111/j.1463-1326.2008.01014.x](https://doi.org/10.1111/j.1463-1326.2008.01014.x) |
| [19515182](https://pubmed.ncbi.nlm.nih.gov/19515182/) | Blonde 2009 | Diabetes Obes Metab | [10.1111/j.1463-1326.2009.01060.x](https://doi.org/10.1111/j.1463-1326.2009.01060.x) |
| [23043166](https://pubmed.ncbi.nlm.nih.gov/23043166/) | Zinman 2012 | Diabetes Care | [10.2337/dc12-1205](https://doi.org/10.2337/dc12-1205) |
| [23812875](https://pubmed.ncbi.nlm.nih.gov/23812875/) | Philis-Tsimikas 2013 | Adv Ther | [10.1007/s12325-013-0036-1](https://doi.org/10.1007/s12325-013-0036-1) |
| [25193531](https://pubmed.ncbi.nlm.nih.gov/25193531/) | Yki-Järvinen 2014 | Diabetes Care | [10.2337/dc14-0990](https://doi.org/10.2337/dc14-0990) |
| [25297660](https://pubmed.ncbi.nlm.nih.gov/25297660/) | Garg 2015 | Endocr Pract | [10.4158/EP14079.OR](https://doi.org/10.4158/EP14079.OR) |
| [25641260](https://pubmed.ncbi.nlm.nih.gov/25641260/) | Bolli 2015 | Diabetes Obes Metab | [10.1111/dom.12438](https://doi.org/10.1111/dom.12438) |
| [26187303](https://pubmed.ncbi.nlm.nih.gov/26187303/) | Levy 2015 | J Med Internet Res | [10.2196/jmir.4716](https://doi.org/10.2196/jmir.4716) |
| [26645932](https://pubmed.ncbi.nlm.nih.gov/26645932/) | Hsu 2015 | Diabetes Technol Ther | [10.1089/dia.2015.0160](https://doi.org/10.1089/dia.2015.0160) |
| [29555621](https://pubmed.ncbi.nlm.nih.gov/29555621/) | Levy 2018 | J Med Internet Res | [10.2196/jmir.9515](https://doi.org/10.2196/jmir.9515) |
| [30104294](https://pubmed.ncbi.nlm.nih.gov/30104294/) | Rosenstock 2018 | Diabetes Care | [10.2337/dc18-0559](https://doi.org/10.2337/dc18-0559) |
| [30808512](https://pubmed.ncbi.nlm.nih.gov/30808512/) | Bergenstal 2019 | Lancet | [10.1016/S0140-6736(19)30368-X](https://doi.org/10.1016/S0140-6736(19)30368-X) |
| [31173451](https://pubmed.ncbi.nlm.nih.gov/31173451/) | Franc 2019 | Diabetes Obes Metab | [10.1111/dom.13806](https://doi.org/10.1111/dom.13806) |
| [31941361](https://pubmed.ncbi.nlm.nih.gov/31941361/) | Aradóttir 2020 | J Diabetes Sci Technol | [10.1177/1932296819900240](https://doi.org/10.1177/1932296819900240) |
| [31984443](https://pubmed.ncbi.nlm.nih.gov/31984443/) | Philis-Tsimikas 2020 | Diabetologia | [10.1007/s00125-019-05080-9](https://doi.org/10.1007/s00125-019-05080-9) |
| [33875484](https://pubmed.ncbi.nlm.nih.gov/33875484/) | Lingvay 2021 | Diabetes Care | [10.2337/dc20-2878](https://doi.org/10.2337/dc20-2878) |
| [34077499](https://pubmed.ncbi.nlm.nih.gov/34077499/) | Martens 2021 | JAMA | [10.1001/jama.2021.7444](https://doi.org/10.1001/jama.2021.7444) |
| [35058312](https://pubmed.ncbi.nlm.nih.gov/35058312/) | Carlson 2022 | BMJ Open Diabetes Res Care | [10.1136/bmjdrc-2021-002590](https://doi.org/10.1136/bmjdrc-2021-002590) |
| [36562599](https://pubmed.ncbi.nlm.nih.gov/36562599/) | Thomsen 2022 | J Diabetes Sci Technol | [10.1177/19322968221145964](https://doi.org/10.1177/19322968221145964) |
| [36758572](https://pubmed.ncbi.nlm.nih.gov/36758572/) | Frias 2023 | Lancet Diabetes Endocrinol | [10.1016/S2213-8587(22)00388-6](https://doi.org/10.1016/S2213-8587(22)00388-6) |
| [37528510](https://pubmed.ncbi.nlm.nih.gov/37528510/) | Luo 2023 | Clin Endocrinol (Oxf) | [10.1111/cen.14956](https://doi.org/10.1111/cen.14956) |
| [37710000](https://pubmed.ncbi.nlm.nih.gov/37710000/) | Wang 2023 | Nat Med | [10.1038/s41591-023-02552-9](https://doi.org/10.1038/s41591-023-02552-9) |
| [37748181](https://pubmed.ncbi.nlm.nih.gov/37748181/) | Bajaj 2023 | Ann Intern Med | [10.7326/M23-1288](https://doi.org/10.7326/M23-1288) |
| [37786283](https://pubmed.ncbi.nlm.nih.gov/37786283/) | Thomsen 2023 | J Diabetes Sci Technol | [10.1177/19322968231201400](https://doi.org/10.1177/19322968231201400) |
| [37954005](https://pubmed.ncbi.nlm.nih.gov/37954005/) | Hermanns 2023 | Lancet Reg Health Eur | [10.1016/j.lanepe.2023.100702](https://doi.org/10.1016/j.lanepe.2023.100702) |
| [38039007](https://pubmed.ncbi.nlm.nih.gov/38039007/) | Nayak 2023 | JAMA Netw Open | [10.1001/jamanetworkopen.2023.40232](https://doi.org/10.1001/jamanetworkopen.2023.40232) |
| [38363342](https://pubmed.ncbi.nlm.nih.gov/38363342/) | Jancev 2024 | Diabetologia | [10.1007/s00125-024-06107-6](https://doi.org/10.1007/s00125-024-06107-6) |
| [38452101](https://pubmed.ncbi.nlm.nih.gov/38452101/) | Warren 2024 | Diabetes Technol Ther | [10.1089/dia.2024.0041](https://doi.org/10.1089/dia.2024.0041) |
| [40273351](https://pubmed.ncbi.nlm.nih.gov/40273351/) | Boonpattharatthiti 2025 | Diabetes Care | [10.2337/dc24-2661](https://doi.org/10.2337/dc24-2661) |
| [40332936](https://pubmed.ncbi.nlm.nih.gov/40332936/) | Ying 2025 | JAMA Netw Open | [10.1001/jamanetworkopen.2025.8910](https://doi.org/10.1001/jamanetworkopen.2025.8910) |
| [41336645](https://pubmed.ncbi.nlm.nih.gov/41336645/) | Arentsen 2025 | IEEE EMBC | [10.1109/EMBC58623.2025.11252793](https://doi.org/10.1109/EMBC58623.2025.11252793) |
| [42035781](https://pubmed.ncbi.nlm.nih.gov/42035781/) | Wilmot 2026 | Lancet Diabetes Endocrinol | [10.1016/S2213-8587(26)00076-8](https://doi.org/10.1016/S2213-8587(26)00076-8) |
| [42067440](https://pubmed.ncbi.nlm.nih.gov/42067440/) | Lu 2026 | Prim Care Diabetes | [10.1016/j.pcd.2026.04.012](https://doi.org/10.1016/j.pcd.2026.04.012) |
| [42930005](https://pubmed.ncbi.nlm.nih.gov/42930005/) | Rodrigues 2026 | Diseases (Basel) | [10.3390/diseases14100378](https://doi.org/10.3390/diseases14100378) |
