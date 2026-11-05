import os, base64
from PIL import Image

src_png = r'C:\Users\sande\Downloads\Grace in Every Drape.png'
im = Image.open(src_png)
print(f"Loaded Grace in Every Drape: {im.size}, mode: {im.mode}")

dest_dirs = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'
]

# Ensure RGB mode for JPEG saving
if im.mode in ('RGBA', 'P'):
    im_rgb = im.convert('RGB')
else:
    im_rgb = im

# Save to scratch optimized jpg
scratch_jpg = r'scratch\banner_grace_opt.jpg'
im_rgb.save(scratch_jpg, 'JPEG', quality=92, optimize=True)
print(f"Scratch optimized JPG size: {os.path.getsize(scratch_jpg)} bytes")

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    # 1. banner_grace_in_every_drape.png
    im.save(os.path.join(d, 'banner_grace_in_every_drape.png'), 'PNG')
    # 2. banner_grace_in_every_drape.jpg
    im_rgb.save(os.path.join(d, 'banner_grace_in_every_drape.jpg'), 'JPEG', quality=92, optimize=True)
    # 3. hero_slide_2.jpg (legacy fallback)
    im_rgb.save(os.path.join(d, 'hero_slide_2.jpg'), 'JPEG', quality=92, optimize=True)

print("Saved assets in both root and meenu-label-shopify-theme!")
for d in dest_dirs:
    for f in ['banner_grace_in_every_drape.png', 'banner_grace_in_every_drape.jpg', 'hero_slide_2.jpg']:
        p = os.path.join(d, f)
        print(f"  {p}: {os.path.getsize(p)} bytes")
