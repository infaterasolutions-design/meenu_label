import os, base64

sticker_path = r'C:\Users\sande\Downloads\Meenu_Label_Real_Sticker_45x52mm.png'
with open(sticker_path, 'rb') as f:
    sticker_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Meenu Label - 45x52mm Hang Tag Sticker Sheet (A4)</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 8mm;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #f1f5f9;
      color: #0f172a;
      padding: 20px;
    }}
    .no-print {{
      background: #ffffff;
      max-width: 900px;
      margin: 0 auto 20px auto;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }}
    .no-print h1 {{
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .no-print p {{
      color: #475569;
      font-size: 14px;
      line-height: 1.5;
      margin-bottom: 16px;
    }}
    .btn-print {{
      background: #0f172a;
      color: #ffffff;
      padding: 12px 24px;
      font-size: 15px;
      font-weight: 600;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-print:hover {{
      background: #2563eb;
    }}
    
    /* A4 Grid Layout: 4 columns x 5 rows = 20 labels per A4 sheet */
    .sheet {{
      width: 210mm;
      min-height: 297mm;
      margin: 0 auto;
      background: #ffffff;
      padding: 8mm;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      display: grid;
      grid-template-columns: repeat(4, 45mm);
      grid-template-rows: repeat(5, 52mm);
      gap: 3mm;
      justify-content: center;
    }}
    
    .label-cell {{
      width: 45mm;
      height: 52mm;
      border: 1px dashed #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: #ffffff;
    }}
    
    .label-cell img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}
    
    @media print {{
      body {{
        background: none;
        padding: 0;
      }}
      .no-print {{
        display: none !important;
      }}
      .sheet {{
        box-shadow: none;
        margin: 0;
        padding: 0;
        gap: 0;
        width: 100%;
        min-height: auto;
      }}
      .label-cell {{
        border: 0.2pt solid #e2e8f0;
      }}
    }}
  </style>
</head>
<body>

  <div class="no-print">
    <h1>🏷️ Meenu Label — 45 × 52 mm Custom Fit Sticker Sheet (20 Labels per A4)</h1>
    <p>Calibrated specifically for your physical <strong>2.0" × 3.5" Meenu Label Hang Tag</strong>.<br>
    Fits into the blank middle area right between the string hole and the pre-printed wash care icons.<br>
    Press <strong>Ctrl + P</strong> to print on any A4 sticker sheet or label paper.</p>
    <button class="btn-print" onclick="window.print()">🖨️ Print 20 Labels on A4 Sheet</button>
  </div>

  <div class="sheet">
    <!-- 20 Labels Grid -->
""" + "\n".join([f'    <div class="label-cell"><img src="{sticker_b64}" alt="Meenu Label Sticker"></div>' for _ in range(20)]) + """
  </div>

</body>
</html>
"""

downloads_dir = r"C:\Users\sande\Downloads"
out_html = os.path.join(downloads_dir, "Meenu_Real_HangTag_Print_Sheet.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

brain_html = os.path.join(r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66", "Meenu_Real_HangTag_Print_Sheet.html")
with open(brain_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created 20-label A4 printable sheet:", out_html)
