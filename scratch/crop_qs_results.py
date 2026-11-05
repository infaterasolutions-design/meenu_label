from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

# 1. Desktop modal crop
d_path = os.path.join(artifacts_dir, "verified_quick_size_desktop.png")
if os.path.exists(d_path):
    im_d = Image.open(d_path)
    # The modal is centered (440px wide around x=500-940, y=200-750)
    crop_d = im_d.crop((460, 200, 980, 750))
    crop_d.save(os.path.join(artifacts_dir, "verified_quick_size_modal_desktop_crop.png"))
    print("Saved desktop modal crop")

# 2. Mobile bottom sheet crop
m_path = os.path.join(artifacts_dir, "verified_quick_size_mobile.png")
if os.path.exists(m_path):
    im_m = Image.open(m_path)
    # Mobile bottom sheet is at bottom (y from ~400 to 915)
    crop_m = im_m.crop((0, 420, 412, 915))
    crop_m.save(os.path.join(artifacts_dir, "verified_quick_size_sheet_mobile_crop.png"))
    print("Saved mobile bottom sheet crop")

# 3. Card plus button crop
g_path = os.path.join(artifacts_dir, "verified_product_card_plus_btn.png")
if os.path.exists(g_path):
    im_g = Image.open(g_path)
    # Scroll/crop first product card area
    # In full desktop (1440x950), collection grid is usually below hero
    # Let's see dimensions
    print("Grid full size:", im_g.size)
