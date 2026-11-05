import subprocess
import os
import time
from PIL import Image

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_23")
os.makedirs(temp_dir, exist_ok=True)

url = "file:///C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html#product-JAB26ST05010"

# 1. Desktop Screenshot (1440x950)
desktop_shot = os.path.join(artifacts_dir, "verified_pdp_desktop_23_frame.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_desk",
    "--window-size=1440,950",
    "--virtual-time-budget=3000",
    f"--screenshot={desktop_shot}",
    url
]
subprocess.run(cmd_desk, check=True)
print("Saved desktop screenshot:", desktop_shot)

# 2. Mobile Screenshot (412x1200)
mobile_shot = os.path.join(artifacts_dir, "verified_pdp_mobile_23_frame.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_mob",
    "--window-size=412,1200",
    "--virtual-time-budget=3000",
    f"--screenshot={mobile_shot}",
    url
]
subprocess.run(cmd_mobile, check=True)
print("Saved mobile screenshot:", mobile_shot)

# Let's crop gallery regions to inspect closely
im_d = Image.open(desktop_shot)
crop_d = im_d.crop((30, 80, 820, 920))
crop_d.save(os.path.join(artifacts_dir, "verified_desktop_gallery_23_cropped.png"))

im_m = Image.open(mobile_shot)
crop_m = im_m.crop((10, 60, 402, 720))
crop_m.save(os.path.join(artifacts_dir, "verified_mobile_gallery_23_cropped.png"))
print("Cropped galleries saved successfully!")
