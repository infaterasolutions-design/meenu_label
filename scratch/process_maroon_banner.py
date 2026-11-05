import os
from PIL import Image

src_png = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(src_png)
print(f"Loaded: {im.size}, mode: {im.mode}")

# We will save to:
# 1. root assets/
# 2. subfolder meenu-label-shopify-theme/assets/

dest_dirs = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'
]

# Ensure RGB mode for JPEG saving
if im.mode in ('RGBA', 'P'):
    im_rgb = im.convert('RGB')
else:
    im_rgb = im

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    # Save as banner_festive_maroon.png
    im.save(os.path.join(d, 'banner_festive_maroon.png'), 'PNG')
    
    # Save high-quality web JPEG (1983x793) at quality=95
    im_rgb.save(os.path.join(d, 'banner_festive_maroon.jpg'), 'JPEG', quality=95, optimize=True)
    
    # Also overwrite hero_slide_1.jpg so any existing references get the new maroon banner
    im_rgb.save(os.path.join(d, 'hero_slide_1.jpg'), 'JPEG', quality=95, optimize=True)

print("Saved banner_festive_maroon.png, banner_festive_maroon.jpg, and hero_slide_1.jpg in both directories!")

for d in dest_dirs:
    for f in ['banner_festive_maroon.png', 'banner_festive_maroon.jpg', 'hero_slide_1.jpg']:
        p = os.path.join(d, f)
        print(f"{p}: {os.path.getsize(p)} bytes")
