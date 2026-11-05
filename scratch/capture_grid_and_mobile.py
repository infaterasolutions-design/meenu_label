import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# 1. Grid shot: immediate scroll to JAB25ST02661
script_grid = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  var card = document.querySelector('[data-id="JAB25ST02661"]');
  if (card) {
    card.scrollIntoView({ block: 'center' });
  }
});
window.addEventListener('load', function() {
  var card = document.querySelector('[data-id="JAB25ST02661"]');
  if (card) {
    card.scrollIntoView({ block: 'center' });
  }
});
</script>
"""
html_grid = base_html.replace("</body>", script_grid + "</body>")
temp_grid = os.path.join(scratch_dir, "temp_grid_imm.html")
with open(temp_grid, "w", encoding="utf-8") as f:
    f.write(html_grid)

shot_grid = os.path.join(artifacts_dir, "verified_sold_out_card_grid.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_grid_imm')}",
    "--window-size=1400,950",
    "--virtual-time-budget=6000",
    f"--screenshot={shot_grid}",
    f"file:///{temp_grid.replace(os.sep, '/')}"
], check=True)
print("Saved Test 1: verified_sold_out_card_grid.png")

# 2. Mobile modal shot: immediate openNotifyMeModal
script_mob = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  openNotifyMeModal(
    'JAB25ST02661',
    'XL',
    'The Noor Petrol Teal Chanderi Suit',
    '',
    '₹2,999'
  );
  var phoneInput = document.getElementById('notifyPhoneInput');
  if (phoneInput) {
    phoneInput.value = '9988898845';
  }
});
window.addEventListener('load', function() {
  openNotifyMeModal(
    'JAB25ST02661',
    'XL',
    'The Noor Petrol Teal Chanderi Suit',
    '',
    '₹2,999'
  );
  var phoneInput = document.getElementById('notifyPhoneInput');
  if (phoneInput) {
    phoneInput.value = '9988898845';
  }
});
</script>
"""
html_mob = base_html.replace("</body>", script_mob + "</body>")
temp_mob = os.path.join(scratch_dir, "temp_mob_imm.html")
with open(temp_mob, "w", encoding="utf-8") as f:
    f.write(html_mob)

shot_mob = os.path.join(artifacts_dir, "verified_notify_modal_mobile.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_mob_imm')}",
    "--window-size=412,915",
    "--virtual-time-budget=6000",
    f"--screenshot={shot_mob}",
    f"file:///{temp_mob.replace(os.sep, '/')}"
], check=True)
print("Saved Test 5: verified_notify_modal_mobile.png")
