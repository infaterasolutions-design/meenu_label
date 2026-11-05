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
# Test 1: Track My Order Desktop (with #ML-1042 timeline)
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
temp_track_html = os.path.join(scratch_dir, "temp_tracking_desktop.html")
with open(temp_track_html, "w", encoding="utf-8") as f:
    f.write(html_track)

shot_track = os.path.join(artifacts_dir, "verified_tracking_tab_desktop.png")
cmd_track = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_tracking_1')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_track}",
    temp_track_html
]
print("Running Test 1 (Desktop Tracking)...")
subprocess.run(cmd_track, check=True)
print("Captured:", shot_track, os.path.exists(shot_track), os.path.getsize(shot_track))

# -------------------------------------------------------------
# Test 2: VIP Login & Recent Orders Dashboard
# -------------------------------------------------------------
script_vip = """
<script>
window.addEventListener('load', function() {
  localStorage.setItem('meenu_vip_user', JSON.stringify({
    phone: '+91 85116 16133',
    loggedInAt: new Date().toISOString(),
    tier: 'Atelier Privé VIP'
  }));
  openAccountModal('login');
});
</script>
"""
html_vip = base_html.replace("</body>", script_vip + "</body>")
temp_vip_html = os.path.join(scratch_dir, "temp_vip_desktop.html")
with open(temp_vip_html, "w", encoding="utf-8") as f:
    f.write(html_vip)

shot_vip = os.path.join(artifacts_dir, "verified_vip_login_desktop.png")
cmd_vip = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_tracking_2')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_vip}",
    temp_vip_html
]
print("Running Test 2 (VIP Dashboard)...")
subprocess.run(cmd_vip, check=True)
print("Captured:", shot_vip, os.path.exists(shot_vip), os.path.getsize(shot_vip))

# -------------------------------------------------------------
# Test 3: Track My Order Mobile (412x915)
# -------------------------------------------------------------
shot_mobile = os.path.join(artifacts_dir, "verified_tracking_modal_mobile.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_temp_tracking_3')}",
    "--window-size=412,915",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_mobile}",
    temp_track_html
]
print("Running Test 3 (Mobile Tracking)...")
subprocess.run(cmd_mobile, check=True)
print("Captured:", shot_mobile, os.path.exists(shot_mobile), os.path.getsize(shot_mobile))

print("All screenshots captured successfully!")
