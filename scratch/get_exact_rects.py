import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger');
    openQuickSizePopup(plusBtn);

    setTimeout(function() {
      var wishBtn = document.getElementById('snitchSizeWishlistBtn');
      wishBtn.click(); // toggle active

      setTimeout(function() {
        var drawer = document.getElementById('snitchSizeDrawer');
        var dRect = drawer.getBoundingClientRect();
        var wRect = wishBtn.getBoundingClientRect();
        var hBadge = document.getElementById('headerWishlistCount');
        var hRect = hBadge.getBoundingClientRect();

        var d = document.createElement('div');
        d.id = 'rect-exact-dump';
        d.textContent = 'DRAWER:' + Math.round(dRect.x) + ',' + Math.round(dRect.y) + ',' + Math.round(dRect.width) + ',' + Math.round(dRect.height) + ' | WISH_BTN:' + Math.round(wRect.x) + ',' + Math.round(wRect.y) + ',' + Math.round(wRect.width) + ',' + Math.round(wRect.height) + ' | HEADER_BADGE:' + Math.round(hRect.x) + ',' + Math.round(hRect.y) + ',' + Math.round(hRect.width) + ',' + Math.round(hRect.height) + ' | WISH_ACTIVE:' + wishBtn.classList.contains('active') + ' | BADGE_TEXT:' + hBadge.textContent;
        document.body.appendChild(d);
      }, 300);
    }, 400);
  }, 400);
});
</script>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('</body>', test_script + '</body>')
temp_path = os.path.join(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch', 'temp_exact_rects.html')
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(text)

cmd = [
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    '--window-size=1440,950',
    '--virtual-time-budget=4000',
    '--dump-dom',
    f"file:///{temp_path.replace(os.sep, '/')}"
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.split('\n'):
    if 'rect-exact-dump' in l:
        print(l)
