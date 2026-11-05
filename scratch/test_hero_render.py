import os, base64, subprocess

with open(r'scratch\banner_modern_ethnic_opt.jpg', 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')
b64_url = f"data:image/jpeg;base64,{b64_data}"

test_html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: sans-serif; background: #fff; }}
.snitch-hero-viewport {{
  width: 100%;
  height: 600px;
  position: relative;
  overflow: hidden;
}}
.snitch-slide {{
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  cursor: pointer;
}}
@media (max-width: 768px) {{
  .snitch-hero-viewport {{
    height: 72vh;
    min-height: 480px;
    max-height: 600px;
  }}
}}
</style>
</head>
<body>
  <div class="snitch-hero-viewport">
    <div class="snitch-slide" style="background-image: url('{b64_url}');"></div>
  </div>
</body>
</html>
"""

test_file = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\test_hero_banner.html'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(test_html_content)

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_hero'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
file_url = 'file:///' + test_file.replace('\\', '/')

# 1. Desktop 1280x800
shot_desktop = os.path.join(artifacts_dir, 'verified_modern_ethnic_banner_desktop.png')
res1 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_desk',
    '--window-size=1280,800',
    '--virtual-time-budget=2000',
    f'--screenshot={shot_desktop}',
    file_url
], capture_output=True, text=True)

# 2. Mobile 375x812
shot_mobile = os.path.join(artifacts_dir, 'verified_modern_ethnic_banner_mobile.png')
res2 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_mob',
    '--window-size=375,812',
    '--virtual-time-budget=2000',
    f'--screenshot={shot_mobile}',
    file_url
], capture_output=True, text=True)

print("Desktop shot:", os.path.exists(shot_desktop))
if os.path.exists(shot_desktop):
    print("Desktop size:", os.path.getsize(shot_desktop))
print("Mobile shot:", os.path.exists(shot_mobile))
if os.path.exists(shot_mobile):
    print("Mobile size:", os.path.getsize(shot_mobile))
