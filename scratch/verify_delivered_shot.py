import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

script_delivered = """
<script>
window.addEventListener('load', function() {
  openAccountModal('track');
  fillAndTrackDemo('#ML-1035');
});
</script>
"""
html_deliv = base_html.replace("</body>", script_delivered + "</body>")
temp_deliv_html = os.path.join(scratch_dir, "temp_tracking_delivered.html")
with open(temp_deliv_html, "w", encoding="utf-8") as f:
    f.write(html_deliv)

shot_deliv = os.path.join(artifacts_dir, "verified_tracking_delivered_desktop.png")
cmd_deliv = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_tracking_deliv')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_deliv}",
    temp_deliv_html
]
subprocess.run(cmd_deliv, check=True)
print("Captured delivered screenshot:", shot_deliv)
