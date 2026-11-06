import os, sys, base64
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

b3_src = r"C:\Users\sande\Downloads\Everyday Dresses New Collection.png"
b4_src = r"C:\Users\sande\Downloads\Chic Yellow Co-Ord Collection.png"

im3 = Image.open(b3_src)
im4 = Image.open(b4_src)

print(f"Loaded b3: {im3.size}, mode={im3.mode}")
print(f"Loaded b4: {im4.size}, mode={im4.mode}")

# Convert to RGB if needed
im3_rgb = im3.convert('RGB') if im3.mode in ('RGBA', 'P') else im3
im4_rgb = im4.convert('RGB') if im4.mode in ('RGBA', 'P') else im4

# Scale to standard 1920 width maintaining exact aspect ratio for crispness
w3_std, h3_std = 1920, int(1920 * im3.height / im3.width) # 1920 x 960
w4_std, h4_std = 1920, int(1920 * im4.height / im4.width) # 1920 x 960

im3_std = im3_rgb.resize((w3_std, h3_std), Image.Resampling.LANCZOS)
im4_std = im4_rgb.resize((w4_std, h4_std), Image.Resampling.LANCZOS)

dest_dirs = [
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\assets',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'
]

# Save optimized JPEGs
b3_opt_jpg = r'scratch\banner_everyday_dresses_opt.jpg'
b4_opt_jpg = r'scratch\banner_chic_yellow_coord_opt.jpg'

im3_std.save(b3_opt_jpg, 'JPEG', quality=92, optimize=True, progressive=True)
im4_std.save(b4_opt_jpg, 'JPEG', quality=92, optimize=True, progressive=True)

print(f"Optimized B3 JPG size: {os.path.getsize(b3_opt_jpg):,} bytes")
print(f"Optimized B4 JPG size: {os.path.getsize(b4_opt_jpg):,} bytes")

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    # B3
    im3.save(os.path.join(d, 'banner_everyday_dresses.png'), 'PNG')
    im3_std.save(os.path.join(d, 'banner_everyday_dresses.jpg'), 'JPEG', quality=92, optimize=True, progressive=True)
    im3_std.save(os.path.join(d, 'hero_slide_3.jpg'), 'JPEG', quality=92, optimize=True, progressive=True)
    # B4
    im4.save(os.path.join(d, 'banner_chic_yellow_coord.png'), 'PNG')
    im4_std.save(os.path.join(d, 'banner_chic_yellow_coord.jpg'), 'JPEG', quality=92, optimize=True, progressive=True)
    im4_std.save(os.path.join(d, 'hero_slide_4.jpg'), 'JPEG', quality=92, optimize=True, progressive=True)

print("Saved all banner assets into both assets/ and meenu-label-shopify-theme/assets/ successfully!")
