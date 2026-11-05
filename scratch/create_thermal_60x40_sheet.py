import os, base64

rot_sticker_path = r'C:\Users\sande\Downloads\Meenu_Label_60x40mm_Rotated_For_Print.png'
with open(rot_sticker_path, 'rb') as f:
    rot_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Meenu Label - 60x40mm Thermal Roll Print (Rotated 90°)</title>
  <style>
    @page {{
      size: 60mm 40mm;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f172a;
      color: #f8fafc;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .no-print {{
      background: #1e293b;
      max-width: 600px;
      width: 100%;
      margin-bottom: 24px;
      padding: 24px;
      border-radius: 12px;
      border: 1px solid #334155;
    }}
    .no-print h1 {{
      font-size: 20px;
      font-weight: 700;
      margin-bottom: 8px;
      color: #38bdf8;
    }}
    .no-print p {{
      color: #94a3b8;
      font-size: 14px;
      line-height: 1.5;
      margin-bottom: 16px;
    }}
    .btn-print {{
      background: #2563eb;
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
      background: #1d4ed8;
    }}
    
    /* 60mm x 40mm Single Label Container */
    .thermal-label {{
      width: 60mm;
      height: 40mm;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      border-radius: 2mm;
      overflow: hidden;
    }}
    .thermal-label img {{
      width: 100%;
      height: 100%;
      object-fit: fill;
    }}
    
    @media print {{
      body {{
        background: none;
        padding: 0;
        display: block;
      }}
      .no-print {{
        display: none !important;
      }}
      .thermal-label {{
        box-shadow: none;
        border-radius: 0;
        width: 60mm;
        height: 40mm;
        margin: 0;
        padding: 0;
        page-break-after: always;
      }}
    }}
  </style>
</head>
<body>

  <div class="no-print">
    <h1>🏷️ 60 × 40 mm Thermal Label Print (Rotated 90°)</h1>
    <p>This layout is rotated 90° sideways so it prints onto standard <strong>60 mm (W) × 40 mm (H) Amazon thermal barcode rolls</strong>.<br>
    Once printed, peel and stick it <strong>vertically</strong> on your 2" × 3.5" Meenu Label hang tag.<br>
    Width becomes 40 mm (no overhang!) and height fits into the blank card area.</p>
    <button class="btn-print" onclick="window.print()">🖨️ Print 60×40 Thermal Label</button>
  </div>

  <div class="thermal-label">
    <img src="{rot_b64}" alt="Meenu Label Rotated 90">
  </div>

</body>
</html>
"""

out_html = r"C:\Users\sande\Downloads\Meenu_60x40mm_Thermal_Print.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

brain_html = os.path.join(r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66", "Meenu_60x40mm_Thermal_Print.html")
with open(brain_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created 60x40 thermal print HTML:", out_html)
