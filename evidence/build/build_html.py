# -*- coding: utf-8 -*-
"""由 summary_template.html 與 data.py 產生 evidence/summary.html
用法：python3 -I build_html.py <data.py> <template> <output>
"""
import html
import importlib.util
import re
import sys

src, tpl, out = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("data", src)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
by_pmid = {a["pmid"]: a for a in d.ARTICLES}

DESIGN = {}
for p in ("14578243 25193531 25641260 23043166 23812875 30104294 31984443 33875484 15920040 17924873 "
          "19515182 16842477 25297660 26187303 26645932 31173451 37954005 37748181 37528510 42067440 "
          "34077499 42035781 36758572 19120433 30808512 38039007 40332936").split():
    DESIGN[p] = "rct"
for p in "40273351 38363342 36562599 42930005".split():
    DESIGN[p] = "ma"
for p in "29555621 35058312 38452101".split():
    DESIGN[p] = "rw"
for p in "37710000 31941361 37786283 41336645".split():
    DESIGN[p] = "poc"
assert set(DESIGN) == set(by_pmid), set(DESIGN) ^ set(by_pmid)

ORDER = ["rct", "ma", "rw", "poc"]
DLABEL = {"rct": "RCT", "ma": "系統性回顧／統合分析", "rw": "真實世界", "poc": "概念驗證／模型／模擬"}
SHORT = {1: "固定規則", 2: "自我滴定", 3: "數位工具", 4: "CGM 輔助", 5: "演算法／AI"}
MAXN = 10

rows = []
for cat in range(1, 6):
    arts = [a for a in d.ARTICLES if a["cat"] == cat]
    arts.sort(key=lambda a: (ORDER.index(DESIGN[a["pmid"]]), a["year"]))
    segs = "".join(
        f'<span class="seg-{DESIGN[a["pmid"]]}" style="width:{100 / MAXN:.1f}%" '
        f'title="{html.escape(a["author"])} {a["year"]} · {DLABEL[DESIGN[a["pmid"]]]}"></span>'
        for a in arts)
    counts = {k: sum(1 for a in arts if DESIGN[a["pmid"]] == k) for k in ORDER}
    aria = "、".join(f"{DLABEL[k]} {v} 篇" for k, v in counts.items() if v)
    rows.append(
        f'      <div class="map-row c{cat}"><span class="label">{cat} {SHORT[cat]}</span>'
        f'<div class="bar" role="img" aria-label="{aria}">{segs}</div>'
        f'<span class="count">{len(arts)}</span></div>')

ref_rows = []
for a in sorted(d.ARTICLES, key=lambda a: (a["cat"], a["year"], a["author"])):
    url = f"https://pubmed.ncbi.nlm.nih.gov/{a['pmid']}/"
    ref_rows.append(
        f'          <tr class="c{a["cat"]}"><td><span class="dot"></span>{a["cat"]} {SHORT[a["cat"]]}</td>'
        f'<td>{html.escape(a["author"])}　<span class="num">{a["year"]}</span></td>'
        f'<td>{html.escape(a["journal"])}</td>'
        f'<td class="mono"><a href="{url}" target="_blank" rel="noopener">{a["pmid"]}</a></td>'
        f'<td class="mono doi"><a href="https://doi.org/{html.escape(a["doi"])}" target="_blank" rel="noopener">{html.escape(a["doi"])}</a></td></tr>')

page = open(tpl, encoding="utf-8").read()
page = page.replace("{{MAP_ROWS}}", "\n".join(rows)).replace("{{REF_ROWS}}", "\n".join(ref_rows))

cited = set()


def link(m):
    p = m.group(1)
    if p not in by_pmid:
        raise SystemExit(f"PMID {p} cited but not in evidence table")
    cited.add(p)
    return (f'<a class="pmid" href="https://pubmed.ncbi.nlm.nih.gov/{p}/" target="_blank" rel="noopener">'
            f'PMID {p}</a>')


page = re.sub(r"\[\[(\d{7,8})\]\]", link, page)
assert "{{" not in page and "[[" not in page
open(out, "w", encoding="utf-8").write(page)
print(f"wrote {out}; inline-cited PMIDs: {len(cited)}; table rows: {len(ref_rows)}")
