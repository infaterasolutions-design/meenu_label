import os, subprocess
from PIL import Image

artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_verify_banner'
index_file = r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html'
file_url = 'file:///' + index_file.replace('\\', '/')

# 1. Desktop 1280x800
shot_desktop = os.path.join(artifacts_dir, 'verified_hero_banner1_desktop.png')
res1 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_desk',
    '--window-size=1280,800',
    '--virtual-time-budget=2500',
    f'--screenshot={shot_desktop}',
    file_url
], capture_output=True, text=True)

# 2. Mobile 375x812
shot_mobile = os.path.join(artifacts_dir, 'verified_hero_banner1_mobile.png')
res2 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_mob',
    '--window-size=375,812',
    '--virtual-time-budget=2500',
    f'--screenshot={shot_mobile}',
    file_url
], capture_output=True, text=True)

print("Desktop shot:", os.path.exists(shot_desktop))
if os.path.exists(shot_desktop):
    im_d = Image.open(shot_desktop)
    print("Desktop size:", im_d.size, f"({os.path.getsize(shot_desktop)/1024:.1f} KB)")
    # Crop hero slider area (y: 60 to 660)
    im_d.crop((0, 60, 1280, 660)).save(os.path.join(artifacts_dir, 'verified_hero_banner1_desktop_crop.png'))
    print("Saved verified_hero_banner1_desktop_crop.png")

print("Mobile shot:", os.path.exists(shot_mobile))
if os.path.exists(shot_mobile):
    im_m = Image.open(shot_mobile)
    print("Mobile size:", im_m.size, f"({os.path.getsize(shot_mobile)/1024:.1f} KB)")
    # Crop hero slider area (y: 50 to 550)
    im_m.crop((0, 50, 375, 550)).save(os.path.join(artifacts_dir, 'verified_hero_banner1_mobile_crop.png'))
    print("Saved verified_hero_banner1_mobile_crop.png")
