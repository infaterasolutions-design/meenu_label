from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

# Desktop
desk_path = os.path.join(artifacts_dir, "verified_pdp_desktop_full.png")
if os.path.exists(desk_path):
    im_desk = Image.open(desk_path)
    # The gallery is on the left side
    crop_desk = im_desk.crop((30, 80, 800, 850))
    crop_desk.save(os.path.join(artifacts_dir, "current_desktop_pdp_gallery.png"))
    print("Saved current_desktop_pdp_gallery.png")

# Mobile
mob_path = os.path.join(artifacts_dir, "verified_pdp_mobile_full.png")
if os.path.exists(mob_path):
    im_mob = Image.open(mob_path)
    crop_mob = im_mob.crop((10, 60, 402, 600))
    crop_mob.save(os.path.join(artifacts_dir, "current_mobile_pdp_gallery.png"))
    print("Saved current_mobile_pdp_gallery.png")
