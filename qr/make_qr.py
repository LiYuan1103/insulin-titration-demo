#!/usr/bin/env python3
"""產生 start.html 的 QR code（PNG、SVG）與 1920×1080 投影片圖，並自動解碼驗證。

需要：segno、Pillow；驗證另需 zxing-cpp、opencv-python-headless（缺少時略過該解碼器）。
字型：Noto Sans CJK / Noto Serif CJK（Debian/Ubuntu 套件 fonts-noto-cjk）。

用法：
    python3 qr/make_qr.py            # 產生並驗證
    python3 qr/make_qr.py --verify   # 只驗證既有檔案
"""
import math
import sys
from pathlib import Path

URL = "https://liyuan1103.github.io/insulin-titration-demo/start.html"
HERE = Path(__file__).resolve().parent
PNG = HERE / "start-qr.png"
SVG = HERE / "start-qr.svg"
SLIDE = HERE / "slide-qr.png"

QUIET = 4            # QR 規格建議的最小留白（模組數）
MIN_PNG = 1000       # 需求：至少 1000×1000
TARGET_PNG = 1200

FONT_DIR = Path("/usr/share/fonts/opentype/noto")
SANS_REG = (FONT_DIR / "NotoSansCJK-Regular.ttc", 3)      # index 3 = Noto Sans CJK TC
SANS_BOLD = (FONT_DIR / "NotoSansCJK-Bold.ttc", 3)
MONO_BOLD = (FONT_DIR / "NotoSansCJK-Bold.ttc", 8)       # index 8 = Noto Sans Mono CJK TC
SERIF_BOLD = (FONT_DIR / "NotoSerifCJK-Bold.ttc", 3)      # index 3 = Noto Serif CJK TC

# 與 start.html 淺色模式相同的色票
BG = (238, 242, 245)       # --bg
INK = (10, 22, 32)         # --ink
INK2 = (47, 63, 75)        # --ink-2
MUTED = (82, 97, 108)      # --muted
LINE = (201, 211, 218)     # --line
ACCENT = (28, 92, 171)     # --accent
MARK = (250, 178, 25)      # --banner-mark


def make_qr():
    import segno
    qr = segno.make_qr(URL, error="H", boost_error=False)
    assert qr.error == "H", qr.error
    return qr


def write_png_svg(qr):
    modules = qr.symbol_size(scale=1, border=QUIET)[0]
    scale = math.ceil(TARGET_PNG / modules)
    qr.save(str(PNG), kind="png", scale=scale, border=QUIET, dark="#000000", light="#ffffff")
    qr.save(
        str(SVG), kind="svg", scale=10, border=QUIET, dark="#000000", light="#ffffff",
        title="控糖之巔｜基礎胰島素 × AI 示範工具：start.html",
        desc=URL, xmldecl=True, nl=True,
    )
    # 補上 viewBox，讓 SVG 放進簡報軟體後可任意縮放
    side = modules * 10
    text = SVG.read_text(encoding="utf-8")
    tag = f'width="{side}" height="{side}"'
    assert tag in text, "segno SVG 格式改變了"
    SVG.write_text(text.replace(tag, f'{tag} viewBox="0 0 {side} {side}"', 1), encoding="utf-8")
    return modules, scale


def font(spec, size):
    from PIL import ImageFont
    path, index = spec
    return ImageFont.truetype(str(path), size, index=index)


def fit(draw, text, spec, size, max_w):
    """字級太大放不下時逐步縮小，確保不超出右欄。"""
    while size > 10:
        f = font(spec, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(spec, size)


def write_slide(qr):
    from PIL import Image, ImageDraw

    W, H = 1920, 1080
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # 左：白底面板＋放大 QR（面板本身就是 QR 的留白區）
    panel = 920
    px, py = 80, (H - panel) // 2
    d.rounded_rectangle([px, py, px + panel, py + panel], radius=36, fill=(255, 255, 255))
    matrix = [list(row) for row in qr.matrix]
    n = len(matrix)
    total = n + 2 * QUIET
    s = panel // total
    qr_px = s * total
    ox = px + (panel - qr_px) // 2 + QUIET * s
    oy = py + (panel - qr_px) // 2 + QUIET * s
    for r, row in enumerate(matrix):
        for c, v in enumerate(row):
            if v:
                d.rectangle([ox + c * s, oy + r * s, ox + (c + 1) * s - 1, oy + (r + 1) * s - 1], fill=(0, 0, 0))

    # 右：標題、講者、行動句、網址
    x0 = px + panel + 90
    max_w = W - 80 - x0

    eyebrow = fit(d, "演講現場工具", SANS_BOLD, 34, max_w)
    t1 = fit(d, "控糖之巔", SERIF_BOLD, 150, max_w)
    t2 = fit(d, "基礎胰島素 × AI 示範工具", SANS_BOLD, 60, max_w)
    spk_label = font(SANS_REG, 32)
    spk = font(SANS_BOLD, 40)
    cta = fit(d, "掃描即可使用今天示範的工具", SANS_BOLD, 54, max_w)
    url_f = fit(d, "insulin-titration-demo/start.html", MONO_BOLD, 38, max_w)
    note = fit(d, "教學示範與模擬工具，非臨床決策工具，實際劑量請依醫師指示", SANS_REG, 26, max_w)

    # 以基線排版：先算總高度再垂直置中
    rows = [
        ("eyebrow", 34, 0),
        ("t1", 150, 40),
        ("t2", 60, 30),
        ("spk", 40, 36),
        ("rule", 0, 56),
        ("cta", 54, 70),
        ("url1", 38, 40),
        ("url2", 38, 14),
        ("note", 26, 64),
    ]
    total_h = sum(size + gap for _, size, gap in rows)
    y = (H - total_h) // 2
    base = {}
    for key, size, gap in rows:
        y += gap + size
        base[key] = y

    d.text((x0, base["eyebrow"]), "演講現場工具", font=eyebrow, fill=ACCENT, anchor="ls")
    d.text((x0 - 6, base["t1"]), "控糖之巔", font=t1, fill=INK, anchor="ls")
    d.text((x0, base["t2"]), "基礎胰島素 × AI 示範工具", font=t2, fill=INK, anchor="ls")
    lw = d.textlength("講者", font=spk_label)
    d.text((x0, base["spk"]), "講者", font=spk_label, fill=MUTED, anchor="ls")
    d.text((x0 + lw + 22, base["spk"]), "郭力源 醫師", font=spk, fill=INK, anchor="ls")
    ry = base["rule"] - 20
    d.rectangle([x0, ry, x0 + 120, ry + 7], fill=MARK)
    d.text((x0, base["cta"]), "掃描即可使用今天示範的工具", font=cta, fill=INK, anchor="ls")
    d.text((x0, base["url1"]), "liyuan1103.github.io/", font=url_f, fill=ACCENT, anchor="ls")
    d.text((x0, base["url2"]), "insulin-titration-demo/start.html", font=url_f, fill=ACCENT, anchor="ls")
    d.text((x0, base["note"]), "教學示範與模擬工具，非臨床決策工具，實際劑量請依醫師指示", font=note, fill=MUTED, anchor="ls")

    img.save(str(SLIDE), optimize=True)
    return s, n


# ---------------------------------------------------------------- 驗證
def decoders():
    found = []
    try:
        import zxingcpp
        def zx(img):
            res = zxingcpp.read_barcodes(img)
            return [(r.text, getattr(r, "ec_level", "?")) for r in res if r.format == zxingcpp.BarcodeFormat.QRCode]
        found.append(("zxing-cpp", zx))
    except ImportError:
        print("  （未安裝 zxing-cpp，略過）")
    try:
        import cv2
        import numpy as np
        det = cv2.QRCodeDetector()
        def cv(img):
            arr = cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)
            text, _, _ = det.detectAndDecode(arr)
            return [(text, "?")] if text else []
        found.append(("OpenCV", cv))
    except ImportError:
        print("  （未安裝 opencv，略過）")
    return found


def check(label, img, decs):
    ok = True
    for name, fn in decs:
        res = fn(img)
        good = bool(res) and all(t == URL for t, _ in res)
        ec = ",".join(str(e) for _, e in res) or "-"
        print(f"  {'OK ' if good else 'FAIL'} {label:<38} {name:<9} ec={ec:<4} {res[0][0] if res else '(無法解碼)'}")
        ok &= good
    return ok


def verify(svg_png=None):
    from PIL import Image, ImageFilter
    decs = decoders()
    if not decs:
        sys.exit("沒有可用的解碼器，請安裝 zxing-cpp 或 opencv-python-headless")
    ok = True
    png = Image.open(PNG)
    print(f"start-qr.png 尺寸 {png.size}")
    ok &= png.size[0] >= MIN_PNG and png.size[1] >= MIN_PNG
    ok &= check("start-qr.png", png, decs)
    ok &= check("start-qr.png 縮小到 160px", png.resize((160, 160), Image.LANCZOS), decs)
    if svg_png:
        ok &= check("start-qr.svg（Chromium 繪製）", Image.open(svg_png), decs)
    slide = Image.open(SLIDE)
    print(f"slide-qr.png 尺寸 {slide.size}")
    ok &= slide.size == (1920, 1080)
    ok &= check("slide-qr.png", slide, decs)
    ok &= check("slide-qr.png 縮小到 640×360", slide.resize((640, 360), Image.LANCZOS), decs)
    blurred = slide.resize((960, 540), Image.LANCZOS).filter(ImageFilter.GaussianBlur(2))
    ok &= check("slide-qr.png 960×540＋模糊（模擬投影）", blurred, decs)
    print("全部通過" if ok else "有項目失敗")
    return ok


if __name__ == "__main__":
    args = sys.argv[1:]
    svg_png = None
    if "--svg-png" in args:
        svg_png = args[args.index("--svg-png") + 1]
    if "--verify" not in args:
        qr = make_qr()
        modules, scale = write_png_svg(qr)
        s, n = write_slide(qr)
        print(f"QR 版本 {qr.version}、容錯 {qr.error}、{n}×{n} 模組（含留白 {modules}）")
        print(f"start-qr.png 每模組 {scale}px；slide-qr.png 每模組 {s}px")
    sys.exit(0 if verify(svg_png) else 1)
