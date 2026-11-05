import os, base64

sticker_path = r'C:\Users\sande\Downloads\Meenu_Label_45x65mm_Sticker.png'
with open(sticker_path, 'rb') as f:
    sticker_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Meenu Label - 45x65mm Hang Tag Sticker Print Sheet</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 10mm;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #f0f2f5;
      color: #1a1a1a;
      padding: 20px;
    }}
    .no-print {{
      background: #ffffff;
      max-width: 900px;
      margin: 0 auto 20px auto;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }}
    .no-print h1 {{
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .no-print p {{
      color: #666;
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
    
    /* A4 Grid Layout for 16 stickers */
    .sheet {{
      width: 210mm;
      min-height: 297mm;
      margin: 0 auto;
      background: #ffffff;
      padding: 10mm;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
      display: grid;
      grid-template-columns: repeat(4, 45mm);
      grid-template-rows: repeat(4, 65mm);
      gap: 3mm;
      justify-content: center;
    }}
    
    .label-cell {{
      width: 45mm;
      height: 65mm;
      border: 1px dashed #d1d5db;
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
        border: 0.25pt solid #eee;
      }}
    }}
  </style>
</head>
<body>

  <div class="no-print">
    <h1>🏷️ Meenu Label — 45 × 65 mm Hang Tag Price Label Sheet</h1>
    <p>This sheet is calibrated for printing directly onto A4 pre-cut sticker paper (or full A4 sticker sheets) for your <strong>2.0" × 3.5" Meenu Label Hang Tags</strong>.<br>
    Click the button below or press <strong>Ctrl + P</strong>. Ensure <em>Margins: None</em> and <em>Scale: 100%</em> in the print dialog.</p>
    <button class="btn-print" onclick="window.print()">🖨️ Print 16 Labels on A4 Sheet</button>
  </div>

  <div class="sheet">
    <!-- 16 Labels Grid -->
""" + "\n".join([f'    <div class="label-cell"><img src="{sticker_b64}" alt="Meenu Label Sticker"></div>' for _ in range(16)]) + """
  </div>

</body>
</html>
"""

downloads_dir = r"C:\Users\sande\Downloads"
out_html = os.path.join(downloads_dir, "Meenu_HangTag_Print_Sheet.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

brain_html = os.path.join(r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66", "Meenu_HangTag_Print_Sheet.html")
with open(brain_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created printable HTML sheet: {out_html}")
