import subprocess, os, json
from PIL import Image

artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_verify_suite'
index_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    orig_html = f.read()

# 1. Desktop Test: Capture Search Open and Search Closed
desktop_test_js = """
<script>
window.addEventListener('load', () => {
    console.log('--- SUITE: DESKTOP TEST START ---');
    const searchTrigger = document.querySelector('.header-search-btn') || document.querySelector('.header-left .header-icon-action');
    const bar = document.getElementById('searchOverlayBar');
    const closeBtn = document.getElementById('searchCloseBtn');
    
    // Step 1: Open search
    if (searchTrigger) searchTrigger.click();
    else toggleSearchBar();
    
    console.log('DESKTOP OPEN CLASS:', bar.classList.contains('open'));
    
    // Check elementFromPoint
    const rect = closeBtn.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const el = document.elementFromPoint(cx, cy);
    console.log('DESKTOP ELEMENT AT CLOSE BTN:', el ? (el.tagName + '.' + el.className + '#' + el.id) : 'NONE');
    console.log('--- SUITE: DESKTOP TEST OPEN READY ---');
});
</script>
"""

desktop_open_html = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\temp_desktop_open.html'
with open(desktop_open_html, 'w', encoding='utf-8') as f:
    f.write(orig_html.replace('</body>', desktop_test_js + '</body>'))

shot_desktop_open = os.path.join(artifacts_dir, 'verified_search_open_desktop.png')
res = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_1',
    '--window-size=1280,800',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_desktop_open}',
    f'file:///{desktop_open_html}'
], capture_output=True, text=True)

for l in res.stderr.splitlines():
    if 'SUITE:' in l or 'DESKTOP' in l:
        print(l)

# Desktop Closed Test (simulate click on close button)
desktop_close_test_js = """
<script>
window.addEventListener('load', () => {
    console.log('--- SUITE: DESKTOP CLOSE TEST START ---');
    const searchTrigger = document.querySelector('.header-search-btn') || document.querySelector('.header-left .header-icon-action');
    const bar = document.getElementById('searchOverlayBar');
    const closeBtn = document.getElementById('searchCloseBtn');
    
    if (searchTrigger) searchTrigger.click();
    else toggleSearchBar();
    
    // Click close button
    closeBtn.click();
    console.log('DESKTOP AFTER CLOSE CLICK OPEN CLASS:', bar.classList.contains('open'));
    console.log('--- SUITE: DESKTOP CLOSE TEST FINISHED ---');
});
</script>
"""

desktop_closed_html = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\temp_desktop_closed.html'
with open(desktop_closed_html, 'w', encoding='utf-8') as f:
    f.write(orig_html.replace('</body>', desktop_close_test_js + '</body>'))

shot_desktop_closed = os.path.join(artifacts_dir, 'verified_search_closed_desktop.png')
res2 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_2',
    '--window-size=1280,800',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_desktop_closed}',
    f'file:///{desktop_closed_html}'
], capture_output=True, text=True)

for l in res2.stderr.splitlines():
    if 'SUITE:' in l or 'DESKTOP' in l:
        print(l)

# 2. Mobile Test (375x812): Search Open and Close
mobile_test_js = """
<script>
window.addEventListener('load', () => {
    console.log('--- SUITE: MOBILE TEST START ---');
    const bar = document.getElementById('searchOverlayBar');
    const closeBtn = document.getElementById('searchCloseBtn');
    
    toggleSearchBar();
    console.log('MOBILE OPEN CLASS:', bar.classList.contains('open'));
    
    const rect = closeBtn.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const el = document.elementFromPoint(cx, cy);
    console.log('MOBILE ELEMENT AT CLOSE BTN:', el ? (el.tagName + '.' + el.className + '#' + el.id) : 'NONE');
    console.log('--- SUITE: MOBILE TEST OPEN READY ---');
});
</script>
"""

mobile_open_html = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\temp_mobile_open.html'
with open(mobile_open_html, 'w', encoding='utf-8') as f:
    f.write(orig_html.replace('</body>', mobile_test_js + '</body>'))

shot_mobile_open = os.path.join(artifacts_dir, 'verified_search_open_mobile.png')
res3 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_3',
    '--window-size=375,812',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_mobile_open}',
    f'file:///{mobile_open_html}'
], capture_output=True, text=True)

for l in res3.stderr.splitlines():
    if 'SUITE:' in l or 'MOBILE' in l:
        print(l)

# 3. Mobile Close Test
mobile_close_test_js = """
<script>
window.addEventListener('load', () => {
    console.log('--- SUITE: MOBILE CLOSE TEST START ---');
    const bar = document.getElementById('searchOverlayBar');
    const closeBtn = document.getElementById('searchCloseBtn');
    
    toggleSearchBar();
    closeBtn.click();
    console.log('MOBILE AFTER CLOSE CLICK OPEN CLASS:', bar.classList.contains('open'));
    console.log('--- SUITE: MOBILE CLOSE TEST FINISHED ---');
});
</script>
"""

mobile_closed_html = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\temp_mobile_closed.html'
with open(mobile_closed_html, 'w', encoding='utf-8') as f:
    f.write(orig_html.replace('</body>', mobile_close_test_js + '</body>'))

shot_mobile_closed = os.path.join(artifacts_dir, 'verified_search_closed_mobile.png')
res4 = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}_4',
    '--window-size=375,812',
    '--virtual-time-budget=2500',
    '--enable-logging=stderr',
    f'--screenshot={shot_mobile_closed}',
    f'file:///{mobile_closed_html}'
], capture_output=True, text=True)

for l in res4.stderr.splitlines():
    if 'SUITE:' in l or 'MOBILE' in l:
        print(l)

# Check screenshots
print("=== SCREENSHOT SUMMARY ===")
for shot in [shot_desktop_open, shot_desktop_closed, shot_mobile_open, shot_mobile_closed]:
    if os.path.exists(shot):
        im = Image.open(shot)
        print(f"Verified {os.path.basename(shot)}: {im.size} ({os.path.getsize(shot)/1024:.1f} KB)")
    else:
        print(f"FAILED: {shot} does not exist!")
