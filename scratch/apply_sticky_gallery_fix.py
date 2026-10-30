import sys
import shutil
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
backup_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.backup_sticky_gallery.html'

shutil.copy2(file_path, backup_path)
print("Backup created at:", backup_path)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update line 25 body overflow
target_body_css = """body {
      font-family: 'Montserrat', sans-serif;
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }"""

replacement_body_css = """body {
      font-family: 'Montserrat', sans-serif;
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }
    @media (max-width: 992px) {
      body {
        overflow-x: hidden;
      }
    }"""

if target_body_css in content:
    content = content.replace(target_body_css, replacement_body_css, 1)
    print("Updated body base CSS")
else:
    print("target_body_css not matched, checking alternate")

# 2. Update PDP Grid & Gallery CSS
target_pdp_css = """    /* 2-Column Luxury PDP Layout (Snitch-Style Sticky Media & Scrollable Right Side) */
    .pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 48px;
      align-items: start;
    }
    @media (max-width: 992px) {
      .pdp-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    /* Left Gallery: Sticky on Desktop so image remains constantly in view */
    .pdp-gallery-col {
      position: sticky;
      top: 85px;
      align-self: start;
    }

    /* Right Column: Scrollable on Desktop like Snitch */
    @media (min-width: 993px) {
      .pdp-grid {
        align-items: start;
      }
      .pdp-gallery-col {
        position: sticky;
        top: 85px;
        align-self: start;
      }
      .pdp-info-col {
        max-height: calc(100vh - 105px);
        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 14px;
        scrollbar-width: thin;
        scrollbar-color: #D1C7BD transparent;
      }
      .pdp-info-col::-webkit-scrollbar {
        width: 4px;
      }
      .pdp-info-col::-webkit-scrollbar-track {
        background: transparent;
      }
      .pdp-info-col::-webkit-scrollbar-thumb {
        background: #D1C7BD;
        border-radius: 4px;
      }
      .pdp-info-col::-webkit-scrollbar-thumb:hover {
        background: var(--text-main);
      }
    }"""

replacement_pdp_css = """    /* 2-Column Luxury PDP Layout (Sticky Image on Left + Natural Page Scroll on Right) */
    .pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 48px;
      align-items: start;
    }
    @media (max-width: 992px) {
      .pdp-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    /* Left Gallery: Sticky on Desktop so image remains constantly in view */
    .pdp-gallery-col {
      position: -webkit-sticky;
      position: sticky;
      top: 115px;
      align-self: start;
      height: fit-content;
      z-index: 20;
    }

    /* Desktop Full Flow: Left image is sticky, Right details flow naturally without cut-off */
    @media (min-width: 993px) {
      html, body {
        overflow-x: visible !important;
      }
      .pdp-section,
      .pdp-grid {
        overflow: visible !important;
      }
      .pdp-grid {
        align-items: start !important;
      }
      .pdp-gallery-col {
        position: -webkit-sticky !important;
        position: sticky !important;
        top: 115px !important;
        align-self: start !important;
        height: fit-content !important;
        z-index: 20 !important;
      }
      .pdp-main-image-wrap {
        max-height: calc(100vh - 220px);
        display: flex;
        align-items: center;
        justify-content: center;
        background: #F4EFEB;
      }
      .pdp-main-image {
        max-height: calc(100vh - 220px);
        object-fit: cover;
      }
      .pdp-info-col {
        max-height: none !important;
        overflow: visible !important;
        padding-right: 0 !important;
      }
    }"""
assert target_pdp_css in content, "target_pdp_css not found"
content = content.replace(target_pdp_css, replacement_pdp_css, 1)

# 3. Check mobile overflow at bottom
target_mobile_overflow = """html, body {
      width: 100% !important;
      max-width: 100% !important;
      overflow-x: clip !important;
      position: relative !important;
      margin: 0 !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }"""

replacement_mobile_overflow = """@media (max-width: 992px) {
      html, body {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
        position: relative !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
      }
    }
    @media (min-width: 993px) {
      html, body {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: visible !important;
        position: relative !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
      }
    }"""
assert target_mobile_overflow in content, "target_mobile_overflow not found"
content = content.replace(target_mobile_overflow, replacement_mobile_overflow, 1)

# 4. Check div balance
open_divs = len(re.findall(r'<div\b', content, re.IGNORECASE))
close_divs = len(re.findall(r'</div>', content, re.IGNORECASE))
print(f"Div balance: Open={open_divs}, Close={close_divs}, Diff={open_divs - close_divs}")
assert open_divs == close_divs, "Div tags are not balanced!"

# 5. Check JS syntax
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', content, re.DOTALL)
for i, s in enumerate(scripts):
    res = subprocess.run(['node', '--check', '-'], input=s, text=True, capture_output=True, encoding='utf-8', errors='ignore')
    assert res.returncode == 0, f"Script #{i} error: {res.stderr}"
print("All JS scripts verified valid!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html updated with perfectly balanced sticky image and natural full flow!")
