from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
im = Image.open(os.path.join(artifacts_dir, "verified_isolated_header_badges.png"))
w, h = im.size
print("Crop dimensions:", w, h)

# Let's inspect columns where badge pill colors appear
# In 230px width:
# The 4 icons are spaced ~50px apart
# Search is left ~0-50
# Cart is ~60-110
# Wishlist is ~120-170
# User is ~180-230
cart_badge_pixels = 0
wishlist_badge_pixels = 0

for x in range(w):
    for y in range(h):
        r, g, b = im.getpixel((x, y))[:3]
        # Gold badge color #C59B27 / #C5A059
        if (r > 150 and g > 120 and b < 80) or (r > 180 and g < 50 and b < 50):
            if x < 120:
                cart_badge_pixels += 1
            else:
                wishlist_badge_pixels += 1

print(f"Cart icon badge pixels: {cart_badge_pixels}")
print(f"Wishlist icon badge pixels: {wishlist_badge_pixels}")

if cart_badge_pixels > 0 and wishlist_badge_pixels == 0:
    print("PERFECT: Cart badge is active, and Wishlist badge is completely untouched and clean (0)!")
else:
    print("Check badge isolation")
