from PIL import Image
import os

images = {
    'scratch/craft_chanderi_lux.jpg': r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\craftsmanship_chanderi_silk_1792783505808.jpg',
    'scratch/craft_crepe_lux.jpg': r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\craftsmanship_crepe_coords_1792783526091.jpg',
    'scratch/craft_organza_lux.jpg': r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\craftsmanship_organza_gota_1792783562904.jpg',
}

for out_path, in_path in images.items():
    img = Image.open(in_path)
    # Resize to width 800 (keeping 3:4 aspect ratio ~ 800x1067)
    w, h = img.size
    new_w = 800
    new_h = int(h * (800 / w))
    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    img_resized.save(out_path, 'JPEG', quality=88, optimize=True)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Saved {out_path}: {new_w}x{new_h}, {size_kb:.1f} KB")
