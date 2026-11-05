from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

# 1. Desktop crop
d_path = os.path.join(artifacts_dir, "verified_snitch_drawer_desktop.png")
if os.path.exists(d_path):
    im_d = Image.open(d_path)
    # Drawer is bottom-center, max-width 540
    # Let's crop from y ~ 450 to 950, x from 430 to 1010
    crop_d = im_d.crop((440, 480, 1000, 950))
    crop_d.save(os.path.join(artifacts_dir, "verified_snitch_drawer_desktop_crop.png"))
    print("Saved verified_snitch_drawer_desktop_crop.png")

# 2. Mobile crop
m_path = os.path.join(artifacts_dir, "verified_snitch_drawer_mobile.png")
if os.path.exists(m_path):
    im_m = Image.open(m_path)
    crop_m = im_m.crop((0, 450, 412, 915))
    crop_m.save(os.path.join(artifacts_dir, "verified_snitch_drawer_mobile_crop.png"))
    print("Saved verified_snitch_drawer_mobile_crop.png")
