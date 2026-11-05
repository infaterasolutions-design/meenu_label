import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

script_qs = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger[data-product-id="JAB26ST05010"]');
    if (plusBtn) {
      plusBtn.click();
    }
  }, 300);
});
</script>
"""
html_qs = base_html.replace("</body>", script_qs + "</body>")
temp_qs = os.path.join(scratch_dir, "temp_qs_click.html")
with open(temp_qs, "w", encoding="utf-8") as f:
    f.write(html_qs)

shot_qs = os.path.join(artifacts_dir, "verified_option_a_quick_size_whatsapp.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_qs_click')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_qs}",
    f"file:///{temp_qs.replace(os.sep, '/')}"
], check=True)
print("Saved Option A Quick Size Shot:", shot_qs)
