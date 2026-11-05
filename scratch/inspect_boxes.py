from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

desk_path = os.path.join(artifacts_dir, "verified_pdp_desktop_full.png")
im_desk = Image.open(desk_path)
print("Desktop total size:", im_desk.size)

mob_path = os.path.join(artifacts_dir, "verified_pdp_mobile_full.png")
im_mob = Image.open(mob_path)
print("Mobile total size:", im_mob.size)
