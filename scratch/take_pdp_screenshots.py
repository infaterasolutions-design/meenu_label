import subprocess
import os
import time
from PIL import Image

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_pdp")
os.makedirs(temp_dir, exist_ok=True)

url = "file:///C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html#product-JAB26ST05010"

# 1. Mobile Screenshot (412x1200)
mobile_shot = os.path.join(artifacts_dir, "verified_pdp_mobile_full.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--window-size=412,1200",
    "--virtual-time-budget=4000",
    f"--screenshot={mobile_shot}",
    url
]
print("Capturing mobile screenshot...")
subprocess.run(cmd_mobile, check=True)
print("Saved mobile full screenshot:", mobile_shot)

# Crop mobile size area
if os.path.exists(mobile_shot):
    im = Image.open(mobile_shot)
    # PDP size selection is around y: 550 - 950 on 412px mobile
    print(f"Mobile image size: {im.size}")
    crop_mobile = os.path.join(artifacts_dir, "verified_pdp_mobile_size_unselected.png")
    # let's crop around 400 to 1000
    im_crop = im.crop((0, min(450, im.height - 400), im.width, min(950, im.height)))
    im_crop.save(crop_mobile)
    print("Saved mobile cropped size pills:", crop_mobile)

# 2. Desktop Screenshot (1440x900)
desktop_shot = os.path.join(artifacts_dir, "verified_pdp_desktop_full.png")
cmd_desktop = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_desk",
    "--window-size=1440,900",
    "--virtual-time-budget=4000",
    f"--screenshot={desktop_shot}",
    url
]
print("Capturing desktop screenshot...")
subprocess.run(cmd_desktop, check=True)
print("Saved desktop full screenshot:", desktop_shot)

if os.path.exists(desktop_shot):
    im_d = Image.open(desktop_shot)
    print(f"Desktop image size: {im_d.size}")
    crop_desktop = os.path.join(artifacts_dir, "verified_pdp_desktop_size_unselected.png")
    # on desktop, right column is from x=700 to 1400, y=200 to 800
    im_d_crop = im_d.crop((650, 200, 1400, 750))
    im_d_crop.save(crop_desktop)
    print("Saved desktop cropped size pills:", crop_desktop)
