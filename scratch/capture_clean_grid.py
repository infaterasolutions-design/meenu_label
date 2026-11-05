import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Hide hero and campaign so catalog grid is directly visible at top, and scroll card into view
script_grid = """
<style>
.snitch-hero-section, .campaign-edit-section, .craftsmanship-section {
  display: none !important;
}
</style>
<script>
window.addEventListener('load', function() {
  var card = document.querySelector('[data-id="JAB25ST02661"]');
  if (card) {
    card.scrollIntoView({ behavior: 'instant', block: 'center' });
  }
});
</script>
"""
html_grid = base_html.replace("</head>", script_grid + "</head>")
temp_grid = os.path.join(scratch_dir, "temp_grid_clean2.html")
with open(temp_grid, "w", encoding="utf-8") as f:
    f.write(html_grid)

shot_grid = os.path.join(artifacts_dir, "verified_sold_out_card_grid.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_grid_clean2')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_grid}",
    f"file:///{temp_grid.replace(os.sep, '/')}"
], check=True)
print("Saved Test 1: verified_sold_out_card_grid.png")
