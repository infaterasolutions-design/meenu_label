import subprocess
import os
from PIL import Image

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_user_img")
os.makedirs(temp_dir, exist_ok=True)

# Create a temporary HTML file that opens JAB26ST05010 with image 1 selected
with open("C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html", "r", encoding="utf-8") as f:
    html = f.read()

# Auto-select index 1 on load
html_mod = html.replace(
    "setPreviewGalleryImages(pImages);",
    "setPreviewGalleryImages(pImages); setTimeout(function(){ selectPreviewImage(1); }, 200);"
)

temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_pdp_img2.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_mod)

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = f"file:///{temp_html_path.replace(os.sep, '/')}#product-JAB26ST05010"

# Desktop
shot_d = os.path.join(artifacts_dir, "verified_user_image_desktop.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_d",
    "--window-size=1440,950",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_d}",
    url
], check=True)

# Mobile
shot_m = os.path.join(artifacts_dir, "verified_user_image_mobile.png")
subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_m",
    "--window-size=412,1200",
    "--virtual-time-budget=3500",
    f"--screenshot={shot_m}",
    url
], check=True)

# Crop gallery area for crisp visual comparison
im_d = Image.open(shot_d)
crop_d = im_d.crop((30, 80, 820, 920))
crop_d.save(os.path.join(artifacts_dir, "verified_user_image_desktop_crop.png"))

im_m = Image.open(shot_m)
crop_m = im_m.crop((10, 60, 402, 720))
crop_m.save(os.path.join(artifacts_dir, "verified_user_image_mobile_crop.png"))

print("Captured user photo in 2:3 frame on both Desktop and Mobile successfully!")
