import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# -------------------------------------------------------------
# Test 1: PDP with Sold-Out Size XL Selected (Direct WhatsApp Concierge)
# -------------------------------------------------------------
script_pdp = """
<script>
window.addEventListener('load', function() {
  openProductPage('JAB26ST05010');
  setTimeout(function() {
    var pills = document.querySelectorAll('.pdp-size-btn');
    pills.forEach(function(pill) {
      if (pill.textContent.includes('XL')) {
        pill.click();
      }
    });
    var actions = document.querySelector('.pdp-actions-row');
    if (actions) {
      actions.scrollIntoView({ behavior: 'instant', block: 'center' });
    }
  }, 400);
});
</script>
"""
html_pdp = base_html.replace("</body>", script_pdp + "</body>")
temp_pdp_html = os.path.join(scratch_dir, "temp_option_a_pdp.html")
with open(temp_pdp_html, "w", encoding="utf-8") as f:
    f.write(html_pdp)

shot_pdp = os.path.join(artifacts_dir, "verified_option_a_pdp_whatsapp.png")
cmd_pdp = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_opt_pdp')}",
    "--window-size=1400,950",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_pdp}",
    f"file:///{temp_pdp_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_pdp, check=True)
print("Saved Option A PDP Shot:", shot_pdp)

# -------------------------------------------------------------
# Test 2: Quick Size popup showing NOTIFY ON WHATSAPP row
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
temp_qs_html = os.path.join(scratch_dir, "temp_option_a_qs.html")
with open(temp_qs_html, "w", encoding="utf-8") as f:
    f.write(html_qs)

shot_qs = os.path.join(artifacts_dir, "verified_option_a_quick_size_whatsapp.png")
cmd_qs = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_opt_qs')}",
    "--window-size=1400,950",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_qs}",
    f"file:///{temp_qs_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_qs, check=True)
print("Saved Option A Quick Size Shot:", shot_qs)

# -------------------------------------------------------------
# Test 3: Mobile Viewport (412x915) PDP with WhatsApp Restock Button
# -------------------------------------------------------------
shot_mob = os.path.join(artifacts_dir, "verified_option_a_mobile_pdp.png")
cmd_mob = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_opt_mob')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_mob}",
    f"file:///{temp_pdp_html.replace(os.sep, '/')}"
]
subprocess.run(cmd_mob, check=True)
print("Saved Option A Mobile PDP Shot:", shot_mob)

print("ALL OPTION A VERIFICATION SHOTS GENERATED!")
