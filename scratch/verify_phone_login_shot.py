import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch"
brain_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

script_phone = """
<script>
window.addEventListener('load', function() {
  localStorage.removeItem('meenu_vip_user');
  openAccountModal('login');
});
</script>
"""
html_phone = base_html.replace("</body>", script_phone + "</body>")
temp_phone_html = os.path.join(artifacts_dir, "temp_login_phone.html")
with open(temp_phone_html, "w", encoding="utf-8") as f:
    f.write(html_phone)

shot_phone = os.path.join(brain_dir, "verified_login_step_phone.png")
cmd_phone = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(artifacts_dir, 'chrome_temp_login_phone')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_phone}",
    temp_phone_html
]
subprocess.run(cmd_phone, check=True)
print("Captured phone login step screenshot:", shot_phone)
