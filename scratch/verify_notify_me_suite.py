import subprocess
import os
import time

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"
os.makedirs(artifacts_dir, exist_ok=True)

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# -------------------------------------------------------------
# Test 1: Grid showing SOLD OUT card (JAB25ST02661) scrolled into view
# -------------------------------------------------------------
script_grid = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var card = document.querySelector('[data-id="JAB25ST02661"]');
    if (card) {
      card.scrollIntoView({ behavior: 'instant', block: 'center' });
    }
  }, 300);
});
</script>
"""
html_grid = base_html.replace("</body>", script_grid + "</body>")
temp_grid_html = os.path.join(scratch_dir, "temp_test_grid.html")
with open(temp_grid_html, "w", encoding="utf-8") as f:
    f.write(html_grid)

shot_grid = os.path.join(artifacts_dir, "verified_sold_out_card_grid.png")
cmd_grid = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_grid')}",
    "--window-size=1400,900",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_grid}",
    f"file:///{temp_grid_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_grid, check=True)
print("Saved Test 1: verified_sold_out_card_grid.png")

# -------------------------------------------------------------
# Test 2: Quick Size popup on JAB26ST05010 with XL marked SOLD OUT
# -------------------------------------------------------------
script_qs = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger[data-product-id="JAB26ST05010"]');
    if (plusBtn) {
      openQuickSizePopup(plusBtn);
    }
  }, 400);
});
</script>
"""
html_qs = base_html.replace("</body>", script_qs + "</body>")
temp_qs_html = os.path.join(scratch_dir, "temp_test_qs.html")
with open(temp_qs_html, "w", encoding="utf-8") as f:
    f.write(html_qs)

shot_qs = os.path.join(artifacts_dir, "verified_quick_size_sold_out_row.png")
cmd_qs = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_qs')}",
    "--window-size=1400,900",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_qs}",
    f"file:///{temp_qs_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_qs, check=True)
print("Saved Test 2: verified_quick_size_sold_out_row.png")

# -------------------------------------------------------------
# Test 3: Luxury Notify Me Restock Modal Open (Desktop)
# -------------------------------------------------------------
script_notify = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openNotifyMeModal(
      'JAB26ST05010',
      'XL',
      'The Heer Gulabi Raw Silk Ensemble',
      'data:image/jpeg;base64,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',
      '₹3,299'
    );
    // Fill sample phone number for alert
    var phoneInput = document.getElementById('notifyPhoneInput');
    if (phoneInput) {
      phoneInput.value = '9876543210';
    }
  }, 400);
});
</script>
"""
html_notify = base_html.replace("</body>", script_notify + "</body>")
temp_notify_html = os.path.join(scratch_dir, "temp_test_notify.html")
with open(temp_notify_html, "w", encoding="utf-8") as f:
    f.write(html_notify)

shot_notify = os.path.join(artifacts_dir, "verified_notify_modal_desktop.png")
cmd_notify = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_notify')}",
    "--window-size=1400,900",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_notify}",
    f"file:///{temp_notify_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_notify, check=True)
print("Saved Test 3: verified_notify_modal_desktop.png")

# -------------------------------------------------------------
# Test 4: PDP Page with Sold-Out Size XL Selected (Dynamic Action Button)
# -------------------------------------------------------------
script_pdp = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openProductPage('JAB26ST05010');
    setTimeout(function() {
      // Find size pill for XL and click it
      var pills = document.querySelectorAll('.pdp-size-btn');
      pills.forEach(function(pill) {
        if (pill.textContent.includes('XL')) {
          pill.click();
        }
      });
      // Scroll to PDP actions block
      var actions = document.querySelector('.pdp-actions-row');
      if (actions) {
        actions.scrollIntoView({ behavior: 'instant', block: 'center' });
      }
    }, 400);
  }, 400);
});
</script>
"""
html_pdp = base_html.replace("</body>", script_pdp + "</body>")
temp_pdp_html = os.path.join(scratch_dir, "temp_test_pdp.html")
with open(temp_pdp_html, "w", encoding="utf-8") as f:
    f.write(html_pdp)

shot_pdp = os.path.join(artifacts_dir, "verified_pdp_notify_button.png")
cmd_pdp = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_pdp')}",
    "--window-size=1400,900",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_pdp}",
    f"file:///{temp_pdp_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_pdp, check=True)
print("Saved Test 4: verified_pdp_notify_button.png")

# -------------------------------------------------------------
# Test 5: Mobile Viewport (412x915) Notify Me Modal
# -------------------------------------------------------------
shot_mob = os.path.join(artifacts_dir, "verified_notify_modal_mobile.png")
cmd_mob = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_mob')}",
    "--window-size=412,915",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_mob}",
    f"file:///{temp_notify_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_mob, check=True)
print("Saved Test 5: verified_notify_modal_mobile.png")

print("ALL HEADLESS CHROME VERIFICATION SUITE TESTS COMPLETED!")
