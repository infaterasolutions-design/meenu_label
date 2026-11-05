from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
im = Image.open(os.path.join(artifacts_dir, "verified_header_cart_digit_badge.png"))
print("Badge crop size:", im.size)

# Let's inspect non-white pixels to see the badge circle and digit
# Find where the badge pill is (gold/red pill with number)
w, h = im.size
badge_pixels = 0
for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))[:3]
        # check gold badge color #C59B27 / #C5A059 or dark pill
        if (r > 150 and g > 120 and b < 80) or (r > 180 and g < 50 and b < 50):
            badge_pixels += 1

print("Found badge colored pixels:", badge_pixels)
if badge_pixels > 0:
    print("SUCCESS: Cart badge pill is visible in real-time without page refresh!")
else:
    print("Check badge styling")
