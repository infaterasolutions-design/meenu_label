import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# -------------------------------------------------------------
# Test 1: Frictionless Tracking Desktop
# -------------------------------------------------------------
script_track = """
<script>
window.addEventListener('load', function() {
  openAccountModal('track');
  fillAndTrackDemo('#ML-1042');
});
</script>
"""
html_track = base_html.replace("</body>", script_track + "</body>")
temp_track_html = os.path.join(scratch_dir, "temp_fric_track.html")
with open(temp_track_html, "w", encoding="utf-8") as f:
    f.write(html_track)

shot_track = os.path.join(artifacts_dir, "verified_frictionless_tracking.png")
cmd_track = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_fric_1')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_track}",
    temp_track_html
]
print("Running Test 1 (Frictionless Tracking)...")
subprocess.run(cmd_track, check=True)
print("Captured:", shot_track)

# -------------------------------------------------------------
# Test 2: Frictionless VIP Concierge Desktop
# -------------------------------------------------------------
script_concierge = """
<script>
window.addEventListener('load', function() {
  openAccountModal('concierge');
});
</script>
"""
html_concierge = base_html.replace("</body>", script_concierge + "</body>")
temp_concierge_html = os.path.join(scratch_dir, "temp_fric_concierge.html")
with open(temp_concierge_html, "w", encoding="utf-8") as f:
    f.write(html_concierge)

shot_concierge = os.path.join(artifacts_dir, "verified_frictionless_concierge.png")
cmd_concierge = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_fric_2')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_concierge}",
    temp_concierge_html
]
print("Running Test 2 (Frictionless VIP Concierge)...")
subprocess.run(cmd_concierge, check=True)
print("Captured:", shot_concierge)

# -------------------------------------------------------------
# Test 3: Frictionless Mobile (412x915)
# -------------------------------------------------------------
shot_mobile = os.path.join(artifacts_dir, "verified_frictionless_mobile.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_fric_3')}",
    "--window-size=412,915",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_mobile}",
    temp_track_html
]
print("Running Test 3 (Frictionless Mobile)...")
subprocess.run(cmd_mobile, check=True)
print("Captured:", shot_mobile)

print("All frictionless screenshots captured successfully!")
