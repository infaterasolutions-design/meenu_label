import subprocess
import os
from PIL import Image

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the previous right-side scrollable CSS with the proper STICKY IMAGE on left + NATURAL PAGE SCROLL on right!
old_css_rule = """.pdp-info-col {
        max-height: calc(100vh - 105px);
        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 14px;
        scrollbar-width: thin;
        scrollbar-color: #D1C7BD transparent;
      }"""

new_sticky_css = """
  /* Desktop Sticky Left Gallery & Natural Full Page Scroll */
  @media (min-width: 993px) {
    html, body {
      overflow-x: visible !important;
    }
    .pdp-section {
      overflow: visible !important;
    }
    .pdp-grid {
      display: grid !important;
      grid-template-columns: 1.05fr 1fr !important;
      gap: 48px !important;
      align-items: start !important;
      overflow: visible !important;
    }
    .pdp-gallery-col {
      position: -webkit-sticky !important;
      position: sticky !important;
      top: 110px !important;
      align-self: start !important;
      height: fit-content !important;
      z-index: 20 !important;
    }
    .pdp-info-col {
      max-height: none !important;
      overflow: visible !important;
      padding-right: 0 !important;
    }
  }
"""

test_html = html.replace("</head>", f"<style>{new_sticky_css}</style></head>")

# 1. State at top (Y=0)
inject_top = """
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
  window.scrollTo(0, 0);
});
"""
path_top = os.path.join(workspace, 'scratch', 'sticky_test_top.html')
with open(path_top, 'w', encoding='utf-8') as f:
    f.write(test_html.replace("</body>", f"<script>{inject_top}</script></body>"))

# 2. State scrolled down Y=500
inject_scrolled = """
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
  setTimeout(function() {
    window.scrollTo(0, 480);
  }, 100);
});
"""
path_scrolled = os.path.join(workspace, 'scratch', 'sticky_test_scrolled.html')
with open(path_scrolled, 'w', encoding='utf-8') as f:
    f.write(test_html.replace("</body>", f"<script>{inject_scrolled}</script></body>"))

def snap(html_file, out_png, width=1280, height=880):
    file_url = f"file:///{os.path.abspath(html_file).replace(os.sep, '/')}"
    cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--screenshot={out_png}',
        f'--window-size={width},{height}',
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    print(f"Captured {os.path.basename(out_png)}: exit {res.returncode}")

shot_top = os.path.join(artifacts_dir, 'sticky_image_pdp_top.png')
shot_scrolled = os.path.join(artifacts_dir, 'sticky_image_pdp_scrolled.png')

print("Snapping top...")
snap(path_top, shot_top)
print("Snapping scrolled...")
snap(path_scrolled, shot_scrolled)

print("Finished sticky image test renders!")
