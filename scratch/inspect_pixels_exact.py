from PIL import Image
import os

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
im = Image.open(os.path.join(artifacts_dir, "verified_isolated_header_badges.png"))
w, h = im.size

# Let's print out what x, y coordinates had badge pixels
for y in range(h):
    for x in range(w):
        r, g, b = im.getpixel((x, y))[:3]
        if (r > 150 and g > 120 and b < 80) or (r > 180 and g < 50 and b < 50):
            print(f"Pixel at ({x}, {y}): RGB=({r}, {g}, {b})")
