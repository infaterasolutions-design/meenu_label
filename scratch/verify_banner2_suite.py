import os, subprocess
from PIL import Image

artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_verify_banner2'
index_file = r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html'

with open(index_file, 'r', encoding='utf-8') as f:
    orig_html = f.read()

# Test script to switch directly to Slide 2 on load
slide2_test_script = """
<script>
window.addEventListener('load', () => {
    console.log('--- SWITCHING HERO SLIDER TO SLIDE 2 ---');
    if (typeof goToSlide === 'function') {
        goToSlide(1);
    } else {
        const track = document.getElementById('sliderTrack');
        if (track) track.style.transform = 'translateX(-25%)';
    }
    console.log('--- SLIDE 2 READY FOR SCREENSHOT ---');
});
</script>
"""

test_html_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\temp_slide2_verify.html'
with open(test_html_path, 'w', encoding='utf-8') as f:
    f.write(orig_html.replace('</body>', slide2_test_script + '</body>'))

file_url = 'file:///' + test_html_path.replace('\\', '/')

# 1. Desktop 1280x800
shot_desktop = os.path.join(artifacts_dir, 'verified_hero_banner2_desktop.png')
res1 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_desk',
    '--window-size=1280,800',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_desktop}',
    file_url
], capture_output=True, text=True)

# 2. Mobile 375x812
shot_mobile = os.path.join(artifacts_dir, 'verified_hero_banner2_mobile.png')
res2 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_mob',
    '--window-size=375,812',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_mobile}',
    file_url
], capture_output=True, text=True)

for l in res1.stderr.splitlines():
    if 'SWITCHING' in l or 'SLIDE 2' in l:
        print("Desktop test log:", l)

for l in res2.stderr.splitlines():
    if 'SWITCHING' in l or 'SLIDE 2' in l:
        print("Mobile test log:", l)

print("Desktop shot:", os.path.exists(shot_desktop))
if os.path.exists(shot_desktop):
    im_d = Image.open(shot_desktop)
    print("Desktop size:", im_d.size, f"({os.path.getsize(shot_desktop)/1024:.1f} KB)")
    # Crop hero slider area (y: 60 to 660)
    im_d.crop((0, 60, 1280, 660)).save(os.path.join(artifacts_dir, 'verified_hero_banner2_desktop_crop.png'))
    print("Saved verified_hero_banner2_desktop_crop.png")

print("Mobile shot:", os.path.exists(shot_mobile))
if os.path.exists(shot_mobile):
    im_m = Image.open(shot_mobile)
    print("Mobile size:", im_m.size, f"({os.path.getsize(shot_mobile)/1024:.1f} KB)")
    # Crop hero slider area (y: 50 to 550)
    im_m.crop((0, 50, 375, 550)).save(os.path.join(artifacts_dir, 'verified_hero_banner2_mobile_crop.png'))
    print("Saved verified_hero_banner2_mobile_crop.png")
