from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"

# 1. Desktop
im_desk = Image.open(os.path.join(artifacts_dir, "verified_popup_wishlist_active_desktop.png"))
print("Desktop image size:", im_desk.size)

# Find where the white drawer background is (RGB: 255, 255, 255)
# In vertical center x = 720 (center of 1440)
drawer_top = None
for y in range(im_desk.height):
    r, g, b, *a = im_desk.getpixel((720, y))
    if r > 250 and g > 250 and b > 250:
        # Check if 10 consecutive pixels are white
        if all(im_desk.getpixel((720, y+k))[0] > 250 for k in range(10)):
            drawer_top = y
            break

print("Detected drawer_top in desktop:", drawer_top)

# Crop drawer header: y from drawer_top to drawer_top + 65, x from 450 to 990
if drawer_top is not None:
    hdr_crop = im_desk.crop((445, drawer_top, 995, drawer_top + 65))
    hdr_crop.save(os.path.join(artifacts_dir, "verified_desktop_drawer_header_exact.png"))
    
    # Heart button is rightmost 60px of the header: x from 930 to 990
    heart_crop = im_desk.crop((925, drawer_top, 990, drawer_top + 65))
    heart_crop.save(os.path.join(artifacts_dir, "verified_desktop_heart_button_exact.png"))
    
    # Check red pixels in heart_crop
    red_count = 0
    for x in range(heart_crop.width):
        for y in range(heart_crop.height):
            r, g, b, *a = heart_crop.getpixel((x, y))
            if r > 180 and g < 75 and b < 75:
                red_count += 1
    print("Red pixels in exact heart crop:", red_count)

# 2. Mobile
im_mob = Image.open(os.path.join(artifacts_dir, "verified_popup_wishlist_active_mobile.png"))
print("Mobile image size:", im_mob.size)
mob_drawer_top = None
for y in range(im_mob.height):
    r, g, b, *a = im_mob.getpixel((206, y))
    if r > 250 and g > 250 and b > 250:
        if all(im_mob.getpixel((206, y+k))[0] > 250 for k in range(10)):
            mob_drawer_top = y
            break

print("Detected drawer_top in mobile:", mob_drawer_top)
if mob_drawer_top is not None:
    mob_hdr = im_mob.crop((0, mob_drawer_top, 412, mob_drawer_top + 65))
    mob_hdr.save(os.path.join(artifacts_dir, "verified_mobile_drawer_header_exact.png"))
    
    mob_heart = im_mob.crop((350, mob_drawer_top, 410, mob_drawer_top + 65))
    mob_heart.save(os.path.join(artifacts_dir, "verified_mobile_heart_button_exact.png"))
