import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

script_scroll = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    window.scrollTo(0, 4350);
  }, 400);
});
</script>
"""

html_mod = base_html.replace("</body>", script_scroll + "</body>")
temp_path = os.path.join(scratch_dir, "temp_grid_scroll_exact.html")
with open(temp_path, "w", encoding="utf-8") as f:
    f.write(html_mod)

shot_path = os.path.join(artifacts_dir, "verified_sold_out_card_grid.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_grid_exact')}",
    "--window-size=1400,950",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_path}",
    f"file:///{temp_path.replace(os.sep, '/')}"
], check=True)
print("Saved Test 1: verified_sold_out_card_grid.png")
