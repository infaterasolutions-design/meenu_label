import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

script_debug = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var card = document.querySelector('[data-id="JAB25ST02661"]');
    var data = {
      cardExists: !!card,
      cardRect: card ? card.getBoundingClientRect() : null,
      bodyHeight: document.body.scrollHeight,
      cardDisplay: card ? getComputedStyle(card).display : null,
      cardVisibility: card ? getComputedStyle(card).visibility : null
    };
    var pre = document.createElement('pre');
    pre.id = 'debug_info';
    pre.style = 'position:fixed; top:10px; left:10px; z-index:999999; background:black; color:lime; font-size:16px; padding:10px;';
    pre.textContent = JSON.stringify(data, null, 2);
    document.body.appendChild(pre);
  }, 500);
});
</script>
"""
html_debug = base_html.replace("</body>", script_debug + "</body>")
temp_path = os.path.join(scratch_dir, "temp_debug.html")
with open(temp_path, "w", encoding="utf-8") as f:
    f.write(html_debug)

shot_path = os.path.join(scratch_dir, "debug_card_rect.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_dbg')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_path}",
    f"file:///{temp_path.replace(os.sep, '/')}"
], check=True)

