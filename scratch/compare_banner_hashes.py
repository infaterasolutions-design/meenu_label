import os
import hashlib

theme_assets = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'

for fname in ['hero_slide_1.jpg', 'hero_slide_2.jpg', 'hero_slide_3.jpg', 'hero_slide_4.jpg', 'banner_1_polka.jpg', 'banner_2_chanderi.jpg', 'banner_3_coord.jpg', 'banner_4_gulabi.jpg', 'banner_3_gulabi.jpg']:
    p = os.path.join(theme_assets, fname)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            h = hashlib.md5(f.read()).hexdigest()
        print(f"{fname}: size={os.path.getsize(p)}, md5={h}")
