import subprocess
import os
import shutil

storefront_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'

with open(storefront_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Prepare HTML that opens PDP and scrolls to size section
inject_unselected = """
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
  var s = document.querySelector('.pdp-size-section');
  if (s) s.scrollIntoView({ block: 'center' });
});
"""
path_unselected = os.path.join(workspace, 'scratch', 'snap_pdp_unselected.html')
with open(path_unselected, 'w', encoding='utf-8') as f:
    f.write(text.replace("</body>", f"<script>{inject_unselected}</script></body>"))

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_profile = os.path.join(workspace, 'scratch', 'temp_chrome_iso')
if os.path.exists(temp_profile):
    shutil.rmtree(temp_profile, ignore_errors=True)
os.makedirs(temp_profile, exist_ok=True)

out_mobile = os.path.join(artifacts_dir, 'pdp_mobile_unselected.png')
file_url = f"file:///{os.path.abspath(path_unselected).replace(os.sep, '/')}"

cmd = [
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-extensions',
    f'--user-data-dir={temp_profile}',
    f'--screenshot={out_mobile}',
    '--window-size=412,1000',
    file_url
]

print("Launching isolated headless chrome...")
p = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("Exit code:", p.returncode)
print("Exists:", os.path.exists(out_mobile), "Size:", os.path.getsize(out_mobile) if os.path.exists(out_mobile) else 0)
