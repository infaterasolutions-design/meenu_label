import os
import re
import zipfile

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
main_prod = os.path.join(theme_dir, 'sections', 'main-product.liquid')

with open(main_prod, 'r', encoding='utf-8') as f:
    text = f.read()

target_img = '<img src="{{ product.featured_image | image_url: width: 1000 }}" alt="{{ product.title }}" style="width: 100%; height: auto; display: block;">'
repl_img = '<img src="{{ product.featured_image | image_url: width: 1000 }}" alt="{{ product.title }}" style="width: 100%; aspect-ratio: 4 / 5; object-fit: cover; object-position: top center; display: block;">'

if target_img in text:
    text = text.replace(target_img, repl_img, 1)
    with open(main_prod, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated main-product.liquid img style to 4/5 portrait!")

# Re-zip
zip_target = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
with zipfile.ZipFile(zip_target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Theme re-packaged into {zip_target}")
