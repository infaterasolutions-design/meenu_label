import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# -------------------------------------------------------------
# Test 1: Grid showing SOLD OUT card (JAB25ST02661)
# -------------------------------------------------------------
script_grid = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var card = document.querySelector('[data-id="JAB25ST02661"]');
    if (card) {
      var rect = card.getBoundingClientRect();
      window.scrollTo(0, window.pageYOffset + rect.top - 120);
    }
  }, 500);
});
</script>
"""
html_grid = base_html.replace("</body>", script_grid + "</body>")
temp_grid_html = os.path.join(scratch_dir, "temp_test_grid2.html")
with open(temp_grid_html, "w", encoding="utf-8") as f:
    f.write(html_grid)

shot_grid = os.path.join(artifacts_dir, "verified_sold_out_card_grid.png")
cmd_grid = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_grid2')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_grid}",
    f"file:///{temp_grid_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_grid, check=True)
print("Saved Test 1: verified_sold_out_card_grid.png")

# -------------------------------------------------------------
# Test 3: Luxury Notify Me Modal Open (Desktop)
# -------------------------------------------------------------
script_notify = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
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
  }, 500);
});
</script>
"""
html_notify = base_html.replace("</body>", script_notify + "</body>")
temp_notify_html = os.path.join(scratch_dir, "temp_test_notify2.html")
with open(temp_notify_html, "w", encoding="utf-8") as f:
    f.write(html_notify)

shot_notify = os.path.join(artifacts_dir, "verified_notify_modal_desktop.png")
cmd_notify = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_notify2')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_notify}",
    f"file:///{temp_notify_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_notify, check=True)
print("Saved Test 3: verified_notify_modal_desktop.png")

# -------------------------------------------------------------
# Test 5: Mobile Viewport (412x915) Notify Me Modal
# -------------------------------------------------------------
shot_mob = os.path.join(artifacts_dir, "verified_notify_modal_mobile.png")
cmd_mob = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_mob2')}",
    "--window-size=412,915",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_mob}",
    f"file:///{temp_notify_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_mob, check=True)
print("Saved Test 5: verified_notify_modal_mobile.png")
