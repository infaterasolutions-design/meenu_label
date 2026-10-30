import subprocess
import os
from PIL import Image

storefront_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(storefront_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Page at top
inject_top = """
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
});
"""
path_top = os.path.join(workspace, 'scratch', 'temp_snitch_top.html')
with open(path_top, 'w', encoding='utf-8') as f:
    f.write(text.replace("</body>", f"<script>{inject_top}</script></body>"))

# 2. Page with right side scrolled to accordions
inject_scrolled = """
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
  setTimeout(function() {
    var infoCol = document.querySelector('.pdp-info-col');
    if (infoCol) {
      infoCol.scrollTop = 550; // scroll right side down to accordions
    }
  }, 100);
});
"""
path_scrolled = os.path.join(workspace, 'scratch', 'temp_snitch_scrolled.html')
with open(path_scrolled, 'w', encoding='utf-8') as f:
    f.write(text.replace("</body>", f"<script>{inject_scrolled}</script></body>"))

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

shot_top = os.path.join(artifacts_dir, 'verified_snitch_pdp_desktop_top.png')
shot_scrolled = os.path.join(artifacts_dir, 'verified_snitch_pdp_desktop_scrolled.png')

print("Taking top screenshot...")
snap(path_top, shot_top)

print("Taking scrolled screenshot...")
snap(path_scrolled, shot_scrolled)

print("All captures finished!")
