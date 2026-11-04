# -*- coding: utf-8 -*-
"""產生 evidence/basal-insulin-titration-evidence.xlsx
用法：python3 -I build_xlsx.py <data.py 路徑> <輸出 xlsx>
"""
import importlib.util
import math
import sys
import unicodedata

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

src, out = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("data", src)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

SEARCH_DATE = "2026-11-04"
FONT = "Microsoft JhengHei"
NAVY = "1F3A56"
CAT_FILL = {1: "E3EEF9", 2: "E3F2E6", 3: "FFF0D4", 4: "ECE5F6", 5: "FBE2E3"}
CAT_TAG = {1: "2F6DB5", 2: "2E8B57", 3: "B7791F", 4: "6B4FA3", 5: "B23A48"}
SHEET_NAMES = {1: "1 Treat-to-target", 2: "2 自我滴定", 3: "3 數位與遠距", 4: "4 CGM 輔助", 5: "5 演算法與AI"}

# (標題, 欄寬, key)
COLS = [
    ("類別", 15, "cat"),
    ("第一作者", 15, "author"),
    ("年份", 7, "year"),
    ("期刊（卷(期):頁）", 24, "journal"),
    ("PMID", 11, "pmid"),
    ("研究設計", 26, "design"),
    ("樣本數", 13, "n"),
    ("族群", 30, "pop"),
    ("介入（滴定規則：起始劑量、調整幅度、頻率、目標空腹血糖）", 46, "intv"),
    ("對照", 24, "comp"),
    ("主要結果（HbA1c 變化、達標率）", 44, "result"),
    ("低血糖結果", 34, "hypo"),
    ("追蹤期間", 12, "fu"),
    ("偏誤風險簡評", 32, "bias"),
    ("一句話重點", 32, "key"),
    ("PubMed 連結", 38, "url"),
    ("DOI", 28, "doi"),
    ("萃取依據", 10, "source"),
]

thin = Side(style="thin", color="C9D3DD")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def disp_len(s):
    s = str(s)
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in s)


def est_lines(text, width):
    usable = max(width - 1.5, 4)
    lines = 0
    for part in str(text).split("\n"):
        lines += max(1, math.ceil(disp_len(part) / usable))
    return lines


def header(ws, cols, row=1):
    for i, (title, width, _) in enumerate(cols, start=1):
        c = ws.cell(row=row, column=i, value=title)
        c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.row_dimensions[row].height = 44


def write_rows(ws, arts, start_row=2):
    for r, a in enumerate(arts, start=start_row):
        fill = PatternFill("solid", fgColor=CAT_FILL[a["cat"]])
        max_lines = 1
        for c, (_, width, key) in enumerate(COLS, start=1):
            if key == "cat":
                val = d.CATS[a["cat"]]
            elif key == "url":
                val = f"https://pubmed.ncbi.nlm.nih.gov/{a['pmid']}/"
            else:
                val = a.get(key, "")
            cell = ws.cell(row=r, column=c, value=val)
            cell.font = Font(name=FONT, size=9)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = BORDER
            cell.fill = fill
            if key == "cat":
                cell.font = Font(name=FONT, size=9, bold=True, color=CAT_TAG[a["cat"]])
            if key in ("year", "pmid", "source"):
                cell.alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)
            if key == "url":
                cell.hyperlink = val
                cell.font = Font(name=FONT, size=9, color="0563C1", underline="single")
            if key == "doi":
                cell.hyperlink = f"https://doi.org/{val}"
                cell.font = Font(name=FONT, size=9, color="0563C1", underline="single")
            if key == "key":
                cell.font = Font(name=FONT, size=9, bold=True)
            max_lines = max(max_lines, est_lines(val, width))
        ws.row_dimensions[r].height = min(409, max(30, max_lines * 12.5 + 6))


def data_sheet(ws, arts):
    header(ws, COLS)
    write_rows(ws, arts)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(COLS))}{len(arts) + 1}"
    ws.sheet_view.zoomScale = 90


wb = Workbook()
ws = wb.active
ws.title = "總表"
arts = sorted(d.ARTICLES, key=lambda a: (a["cat"], a["year"]))
data_sheet(ws, arts)
ws.sheet_properties.tabColor = NAVY

for cat in range(1, 6):
    w = wb.create_sheet(SHEET_NAMES[cat])
    data_sheet(w, [a for a in arts if a["cat"] == cat])
    w.sheet_properties.tabColor = CAT_TAG[cat]

# ---------- 檢索紀錄 ----------
ws2 = wb.create_sheet("檢索紀錄")
ws2.column_dimensions["A"].width = 24
ws2.column_dimensions["B"].width = 96
ws2.column_dimensions["C"].width = 12
t = ws2.cell(row=1, column=1, value="檢索與納入紀錄")
t.font = Font(name=FONT, bold=True, size=13, color=NAVY)
info = [
    ("資料庫", "PubMed（透過 NCBI E-utilities 之 PubMed 連接器查詢；PMC 全文僅用於 2 篇）"),
    ("檢索日期", SEARCH_DATE),
    ("核對方式", "每一篇皆以 PubMed 紀錄（get_article_metadata）逐筆確認 PMID、標題、期刊、出版年與 DOI；本表數值取自 PubMed 摘要，EDITION 3 與 BEGIN Once Long 另讀 PMC 全文以補滴定規則"),
    ("篩選檢視之 PubMed 紀錄數", f"{len(d.ARTICLES) + len(d.EXCLUDED)}（皆讀過標題與摘要）"),
    ("納入本表", f"{len(d.ARTICLES)} 篇（類別 1：8、類別 2：6、類別 3：8、類別 4：6、類別 5：10）"),
    ("讀過但排除", f"{len(d.EXCLUDED)} 篇（見「排除清單」工作表）"),
    ("納入條件", "第二型糖尿病（或以 T2D 為主）之基礎胰島素滴定；RCT、系統性回顧／統合分析為主，必要時納入重要真實世界研究、概念驗證或模擬研究（第 5 類）"),
    ("排除條件", "第一型或妊娠糖尿病、僅餐時胰島素、試驗計畫書／設計論文、評論與讀者來函、與滴定策略無關之藥物比較"),
    ("年份定義", "PubMed 紀錄之首次出版日期（含電子優先出版）；期刊欄附卷(期):頁，紙本年份可能晚 1–2 年"),
]
for i, (k, v) in enumerate(info, start=3):
    a = ws2.cell(row=i, column=1, value=k)
    a.font = Font(name=FONT, bold=True, size=10, color=NAVY)
    a.fill = PatternFill("solid", fgColor="EEF3F8")
    a.alignment = Alignment(vertical="top", wrap_text=True)
    b = ws2.cell(row=i, column=2, value=v)
    b.font = Font(name=FONT, size=10)
    b.alignment = Alignment(vertical="top", wrap_text=True)
    ws2.row_dimensions[i].height = max(18, est_lines(v, 96) * 14 + 4)

r0 = len(info) + 5
for j, h in enumerate(["類別", "PubMed 檢索式", "命中數"], start=1):
    c = ws2.cell(row=r0, column=j, value=h)
    c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
    c.fill = PatternFill("solid", fgColor=NAVY)
    c.border = BORDER
QUERIES = [
    ("1", "Riddle MC[Author] AND treat-to-target AND glargine AND NPH", 2),
    ("1", "EDITION insulin glargine 300 U/mL type 2 diabetes randomized", 29),
    ("1", "EDITION 2 glargine 300 basal insulin oral agents Yki-Järvinen", 4),
    ("1", "Bolli GB[Author] AND glargine 300 AND insulin-naive AND EDITION 3", 5),
    ("1", "degludec glargine insulin-naive type 2 diabetes BEGIN Once Long", 5),
    ("1", "Philis-Tsimikas A[Author] AND degludec AND (simple OR stepwise) AND titration", 1),
    ("1", "BRIGHT insulin glargine 300 degludec insulin-naive type 2 diabetes", 7),
    ("1", "Philis-Tsimikas A[Author] AND degludec AND CONCLUDE", 2),
    ("2", "Davies M[Author] AND glargine AND algorithm AND 2005", 1),
    ("2", "Meneghini L[Author] AND detemir AND simplified titration", 1),
    ("2", "Blonde L[Author] AND detemir AND TITRATE", 1),
    ("2", "Gerstein HC[Author] AND INSIGHT AND glargine AND self-titration", 1),
    ("2", "ATLAS Asian treat to target Lantus study patient-led physician-led titration", 3),
    ("2", "patient-led titration basal insulin systematic review", 2),
    ("2", "self-titration versus physician-led titration basal insulin type 2 diabetes meta-analysis", 0),
    ("3", "TeleDiab-2 telemonitoring basal insulin initiation type 2 diabetes", 1),
    ("3", "Mobile Insulin Titration Intervention MITI glargine", 3),
    ("3", "(smartphone OR app OR telemedicine OR \"text message\" OR digital) AND \"basal insulin\" AND titration AND randomized AND type 2 diabetes", 13),
    ("3", "digital health insulin titration type 2 diabetes systematic review meta-analysis", 0),
    ("4", "continuous glucose monitoring basal insulin type 2 diabetes randomized MOBILE Martens", 4),
    ("4", "(CGM OR \"continuous glucose monitoring\" OR \"flash glucose\") AND \"basal insulin\" AND (titration OR titrate OR \"dose adjustment\") AND type 2 diabetes", 35),
    ("4", "同上 AND (Randomized Controlled Trial[Publication Type] OR Meta-Analysis[Publication Type])", 14),
    ("4", "flash glucose monitoring basal insulin type 2 diabetes real-world HbA1c retrospective", 6),
    ("4", "Jancev M[Author] AND continuous glucose monitoring AND type 2 diabetes", 1),
    ("5", "Bergenstal RM[Author] AND automated insulin dosing guidance AND randomised", 1),
    ("5", "\"reinforcement learning\" AND \"type 2 diabetes\" AND Nat Med[Journal]", 1),
    ("5", "reinforcement learning[Title/Abstract] AND insulin[Title] AND type 2 diabetes", 1),
    ("5", "(machine learning OR artificial intelligence OR model-based OR Bayesian) AND basal insulin AND (titration OR dose guidance) AND type 2 diabetes AND (trial OR randomized OR feasibility)", 3),
    ("5", "(artificial intelligence OR machine learning OR deep learning OR reinforcement learning) AND insulin titration AND type 2 diabetes（2023 年起）", 15),
    ("5", "Aradóttir TB[Author] AND basal insulin", 3),
    ("5", "(\"large language model\" OR ChatGPT OR GPT-4) AND insulin AND (dose OR titration) AND diabetes", 3),
]
for i, (cat, q, n) in enumerate(QUERIES, start=r0 + 1):
    for j, v in enumerate([cat, q, n], start=1):
        c = ws2.cell(row=i, column=j, value=v)
        c.font = Font(name=FONT, size=9)
        c.alignment = Alignment(vertical="top", wrap_text=True, horizontal="center" if j != 2 else "left")
        c.border = BORDER
    ws2.row_dimensions[i].height = max(16, est_lines(q, 96) * 13 + 3)
note_r = r0 + len(QUERIES) + 2
n = ws2.cell(row=note_r, column=1,
             value="說明：命中數為檢索當日 PubMed 回傳之 total_count；另有數個以試驗暱稱或作者組合之檢索命中 0 筆，已改用其他檢索式找到。"
                   "數值皆由 AI 自 PubMed 摘要（2 篇為 PMC 全文）萃取，演講引用前請回原文核對；標為「摘要未載明」者代表摘要無此資訊，並非原研究未做。")
n.font = Font(name=FONT, size=9, italic=True, color="51677C")
n.alignment = Alignment(vertical="top", wrap_text=True)
ws2.merge_cells(start_row=note_r, start_column=1, end_row=note_r + 2, end_column=3)
ws2.freeze_panes = "A2"

# ---------- 排除清單 ----------
ws3 = wb.create_sheet("排除清單")
ecols = [("PMID", 11, None), ("書目", 46, None), ("排除理由", 60, None), ("PubMed 連結", 38, None)]
header(ws3, ecols)
for i, (pmid, cite, why) in enumerate(d.EXCLUDED, start=2):
    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    for j, v in enumerate([pmid, cite, why, url], start=1):
        c = ws3.cell(row=i, column=j, value=v)
        c.font = Font(name=FONT, size=9)
        c.alignment = Alignment(vertical="top", wrap_text=True)
        c.border = BORDER
        if j == 4:
            c.hyperlink = url
            c.font = Font(name=FONT, size=9, color="0563C1", underline="single")
    ws3.row_dimensions[i].height = max(18, max(est_lines(cite, 46), est_lines(why, 60)) * 13 + 4)
ws3.freeze_panes = "A2"

# ---------- 說明 ----------
ws4 = wb.create_sheet("說明")
ws4.column_dimensions["A"].width = 26
ws4.column_dimensions["B"].width = 90
ws4.cell(row=1, column=1, value="欄位與顏色說明").font = Font(name=FONT, bold=True, size=13, color=NAVY)
legend = [(d.CATS[k], CAT_FILL[k]) for k in range(1, 6)]
for i, (name, color) in enumerate(legend, start=3):
    c = ws4.cell(row=i, column=1, value=name)
    c.fill = PatternFill("solid", fgColor=color)
    c.font = Font(name=FONT, size=10, bold=True)
    c.border = BORDER
DEFS = [
    ("介入", "盡量寫出起始劑量、調整幅度、調整頻率、目標空腹血糖；摘要沒寫的項目會標「摘要未載明」"),
    ("主要結果", "先寫 HbA1c 變化與組間差（95% CI），再寫達標率；主要終點不是 HbA1c 的研究會註明"),
    ("低血糖結果", "依原研究定義（例如 ≤70 mg/dL 確認、<54 mg/dL、嚴重低血糖），事件率單位照抄原文"),
    ("偏誤風險簡評", "非正式 RoB 2 評分，只列最影響解讀的問題：盲性、樣本、追蹤長度、終點性質、資助與利益衝突（僅寫 PubMed 紀錄可見者）"),
    ("萃取依據", "「摘要」= PubMed 摘要；「PMC全文」= 另讀 PubMed Central 全文"),
    ("年份", "PubMed 首次出版日期（含電子優先出版）"),
]
for i, (k, v) in enumerate(DEFS, start=10):
    a = ws4.cell(row=i, column=1, value=k)
    a.font = Font(name=FONT, bold=True, size=10, color=NAVY)
    a.alignment = Alignment(vertical="top")
    b = ws4.cell(row=i, column=2, value=v)
    b.font = Font(name=FONT, size=10)
    b.alignment = Alignment(vertical="top", wrap_text=True)
    ws4.row_dimensions[i].height = max(18, est_lines(v, 90) * 14 + 4)

wb.save(out)
print(f"wrote {out}: {len(arts)} articles, {len(d.EXCLUDED)} excluded")
