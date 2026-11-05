from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

im_d = Image.open(os.path.join(artifacts_dir, "verified_snitch_drawer_desktop_crop.png"))
print("Desktop crop size:", im_d.size)

im_m = Image.open(os.path.join(artifacts_dir, "verified_snitch_drawer_mobile_crop.png"))
print("Mobile crop size:", im_m.size)
