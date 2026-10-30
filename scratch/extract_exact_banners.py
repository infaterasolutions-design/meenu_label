import base64
import os
import re

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

slides = re.findall(r'<div class="snitch-slide" style="background-image: url\(\'data:image\/[^;]+;base64,([^\']+)\'\);"', html)
theme_assets = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'

for i, b64_str in enumerate(slides):
    out_name = f"hero_slide_{i+1}.jpg"
    out_path = os.path.join(theme_assets, out_name)
    with open(out_path, 'wb') as img_f:
        img_f.write(base64.b64decode(b64_str))
    print(f"Saved {out_name}: {os.path.getsize(out_path)} bytes")

# Also let's check size of existing banner files
for b in ['banner_1_polka.jpg', 'banner_2_chanderi.jpg', 'banner_3_coord.jpg', 'banner_4_gulabi.jpg', 'banner_3_gulabi.jpg']:
    p = os.path.join(theme_assets, b)
    if os.path.exists(p):
        print(f"Existing {b}: {os.path.getsize(p)} bytes")
