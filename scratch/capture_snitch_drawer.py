import subprocess
import os
import time

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_snitch")
os.makedirs(temp_dir, exist_ok=True)

with open("C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html", "r", encoding="utf-8") as f:
    html = f.read()

auto_trigger = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var btn = document.querySelector('.snitch-plus-trigger');
    if (btn) {
      openQuickSizePopup(btn);
    }
  }, 400);
});
</script>
"""

html_test = html.replace("</body>", auto_trigger + "</body>")
temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_snitch_test.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_test)

url = f"file:///{temp_html_path.replace(os.sep, '/')}"

# 1. Desktop Screenshot (1440x950)
desktop_shot = os.path.join(artifacts_dir, "verified_snitch_drawer_desktop.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_desk",
    "--window-size=1440,950",
    "--virtual-time-budget=4000",
    f"--screenshot={desktop_shot}",
    url
]
subprocess.run(cmd_desk, check=True)
print("Saved desktop snitch drawer screenshot:", desktop_shot)

# 2. Mobile Screenshot (412x915)
mobile_shot = os.path.join(artifacts_dir, "verified_snitch_drawer_mobile.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_mob",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={mobile_shot}",
    url
]
subprocess.run(cmd_mobile, check=True)
print("Saved mobile snitch drawer screenshot:", mobile_shot)
