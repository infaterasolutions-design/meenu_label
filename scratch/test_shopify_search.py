import subprocess, os

css_path = os.path.abspath(r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\meenu-luxury.css').replace('\\', '/')

html_content = f"""<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="file:///{css_path}">
<style>
/* Test candidate fix */
.search-close-action {{
  z-index: 290 !important;
  position: absolute !important;
  top: 0 !important;
  right: 0 !important;
  cursor: pointer !important;
  pointer-events: auto !important;
}}
</style>
</head>
<body>
  <div class="search-overlay-bar open" id="searchOverlayBar">
    <div class="search-overlay-inner">
      <button type="button" class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>
      <form action="/search" method="get" class="search-input-box" role="search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
        <input type="search" name="q" id="searchInput" placeholder="Search by silhouette, style code, fabric, color..." autocomplete="off">
      </form>
      <div class="search-quick-tags">
        <span class="quick-tag-label">Popular Searches:</span>
        <a href="#" class="quick-tag">Festive Suits</a>
      </div>
    </div>
  </div>

<script>
window.addEventListener('load', () => {{
    const btn = document.querySelector('.search-close-action');
    const btnRect = btn.getBoundingClientRect();
    const cx = btnRect.left + btnRect.width / 2;
    const cy = btnRect.top + btnRect.height / 2;
    const elAtPoint = document.elementFromPoint(cx, cy);
    console.log('TEST CANDIDATE FIX:');
    console.log('BTN RECT:', JSON.stringify(btnRect));
    console.log('ELEMENT AT BTN CENTER:', elAtPoint ? (elAtPoint.tagName + '.' + elAtPoint.className + '#' + elAtPoint.id) : 'NONE');
    console.log('BTN z-index:', window.getComputedStyle(btn).zIndex);
    const box = document.querySelector('.search-input-box');
    console.log('BOX z-index:', window.getComputedStyle(box).zIndex);
}});
</script>
</body>
</html>
"""

temp_file = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\test_shopify_search_btn.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
temp_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\chrome_temp_test2'
res = subprocess.run([
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    f'--user-data-dir={temp_dir}',
    '--window-size=1280,800',
    '--virtual-time-budget=2000',
    '--enable-logging=stderr',
    f'file:///{temp_file}'
], capture_output=True, text=True)

for l in res.stderr.splitlines():
    if 'ELEMENT AT' in l or 'BTN' in l or 'BOX' in l or 'TEST CANDIDATE' in l:
        print(l)
