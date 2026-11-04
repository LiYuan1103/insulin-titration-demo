# start.html 與 QR code 說明

## 檔案

| 檔案 | 內容 |
|---|---|
| `../start.html` | 聽眾入口頁（單一 HTML，無後端） |
| `start-qr.png` | QR code，1219×1219 px，黑白純色 |
| `start-qr.svg` | QR code 向量版（含 `viewBox`，可任意縮放） |
| `slide-qr.png` | 1920×1080 投影片圖：左 QR、右標題／講者／「掃描即可使用今天示範的工具」／網址 |
| `make_qr.py` | 產生以上三個圖檔並自動解碼驗證的程式 |
| `../.nojekyll` | 空檔，讓 GitHub Pages 原樣發佈、不經 Jekyll 處理 |

QR 內容：`https://liyuan1103.github.io/insulin-titration-demo/start.html`

## 驗證結果

用兩套獨立解碼器（zxing-cpp、OpenCV）解碼，全部讀出上面的網址，容錯等級回報為 H：

- `start-qr.png` 原尺寸，以及縮小到 160 px
- `start-qr.svg` 經 Chromium 繪製成 900 px（非整數倍縮放，確認 `viewBox` 有效）
- `slide-qr.png` 原尺寸、縮小到 640×360、縮小到 960×540 再加高斯模糊（模擬從會場後排拍投影幕）

## 講義連結怎麼補

打開 `start.html`，找到 `<script>` 第一行：

```js
const HANDOUT_URL = "";
```

把網址貼進引號裡即可，例如 `const HANDOUT_URL = "https://example.com/handout.pdf";`。
也可以填 repo 內的相對路徑（例如把 `handout.pdf` 放在根目錄，填 `"handout.pdf"`）。
填好後按鈕會從「講義連結即將補上」變成「開啟講義」，並在新分頁開啟；留空就維持原樣。

## 重新產生 QR code

```bash
sudo apt-get install -y fonts-noto-cjk
pip install segno pillow zxing-cpp opencv-python-headless
python3 qr/make_qr.py
```

只想驗證既有檔案：`python3 qr/make_qr.py --verify`。網址或投影片文字都寫在 `make_qr.py` 開頭與 `write_slide()` 裡。

## 我自行做的假設

1. **分支**：指定的工作分支原本停在只有 `index.html` 的舊 commit，`bayes.html` 只在 `main`。因此先把工作分支快轉到 `main`，再新增檔案，最後快轉合併回 `main`。
2. **網址大小寫**：GitHub Pages 的網域不分大小寫，但路徑分大小寫。QR 用全小寫網域 `liyuan1103.github.io`，路徑 `insulin-titration-demo` 與 repo 名稱一致。
3. **GitHub Pages 是否已開啟**：這個工作環境連不到 `github.io`，無法實際確認。若尚未開啟，請到 repo 的 Settings → Pages，來源選 `main` 分支、根目錄（`/ (root)`）。
4. **QR 規格**：版本 7（45×45 模組）、容錯 H（約可承受 30% 遮擋或汙損）、四周留白 4 模組（規格建議的最小值）。PNG 每模組 23 px，邊長 1219 px，超過要求的 1000 px；用整數倍放大，邊緣銳利不模糊。顏色用純黑純白，掃描相容性最好。
5. **投影片配色**：用淺色背景，與 `start.html` 淺色模式同一組顏色。理由是會場開燈時淺色投影對比較穩定，而且 QR 四周本來就需要淺色留白。
6. **投影片文字**：標題拆成兩行「控糖之巔」／「基礎胰島素 × AI 示範工具」，所以省略「｜」。需求只列標題、網址、一句說明；我另外加了「演講現場工具」小標、講者「郭力源 醫師」與一行免責聲明。不需要的話，把 `make_qr.py` 的 `write_slide()` 裡對應的 `d.text(...)` 刪掉後重跑即可。
7. **網頁標題**：寬螢幕一行完整顯示「控糖之巔｜基礎胰島素 × AI 示範工具」。手機寬度改成兩行並在視覺上隱藏「｜」，螢幕閱讀器仍會讀到完整標題。瀏覽器分頁標題用完整字串。
8. **卡片名稱**：計算器沿用 `index.html` 的標題「基礎胰島素滴定示範計算器」；模擬器依你的描述寫成「固定規則 vs 貝氏方法 教學模擬器」。每張卡片附一張小示意圖，分別是空腹血糖逐日降進目標綠帶，以及固定規則（藍）與貝氏方法（橘）兩條線。顏色沿用兩個工具頁本身的配色，方便聽眾和投影片上看到的畫面對上。
9. **各角色的一小步**：是我依演講主題（每 3 天依空腹血糖小步調整）擬的建議文字。藥師那一句用了低血糖 < 70 mg/dL、先吃 15 公克糖（15-15 原則）。請依你自己的衛教內容確認或修改，文字都在 `start.html` 的 `<dl class="roles">` 裡。
10. **不蒐集資料**：頁面沒有 Cookie、localStorage、分析程式、表單或任何資料傳送。唯一的外部請求是字型，和另外兩頁一樣經 Google Fonts 載入；標題「控糖之巔」的襯線字只下載這 4 個字。離線或被擋時會自動改用手機內建字型，版面不受影響。
11. **額外加的小功能**：頁面最下方有「把這一頁分享給同事」，顯示網址並附「複製網址」按鈕，方便聽眾轉傳到 LINE。需求沒有列，如不需要可整段刪除 `<section class="share">`。
12. **免責聲明**：依指定文字「教學示範與模擬工具，非臨床決策工具，實際劑量請依醫師指示」固定在畫面底部，樣式和 `index.html` 的底部橫幅相同（深底、琥珀色上框、警示三角形）。
13. **預覽成品**：Claude 成品預覽頁只放 `start.html` 本身，用來看版面與文字；兩張卡片用相對路徑連到 `index.html`、`bayes.html`，在 GitHub Pages 上才會開啟對應工具，在預覽頁裡點下去會找不到頁面。repo 裡這兩個檔案沒有任何修改。
