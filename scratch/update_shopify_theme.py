import os
import re
import shutil
import zipfile

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
main_prod = os.path.join(theme_dir, 'sections', 'main-product.liquid')
luxury_css = os.path.join(theme_dir, 'assets', 'meenu-luxury.css')

# 1. Update main-product.liquid
with open(main_prod, 'r', encoding='utf-8') as f:
    liq = f.read()

liq = re.sub(
    r'<section\s+style="[^"]*grid-template-columns:\s*1fr\s+1fr[^"]*"',
    r'<section style="max-width: 1200px; margin: 40px auto; padding: 0 40px; display: grid; grid-template-columns: 1.05fr 1fr; gap: 50px; align-items: start;"',
    liq
)

liq = re.sub(
    r'<div\s+style="border-radius:\s*12px;\s*overflow:\s*hidden;\s*border:\s*1px\s+solid\s+var\(--border-color\);\s*background:\s*#F4EFEB;"',
    r'<div style="position: -webkit-sticky; position: sticky; top: 115px; align-self: start; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color); background: #F4EFEB; z-index: 20;"',
    liq
)

with open(main_prod, 'w', encoding='utf-8') as f:
    f.write(liq)
print("Updated main-product.liquid successfully!")

# 2. Update meenu-luxury.css
with open(luxury_css, 'r', encoding='utf-8') as f:
    css = f.read()

target_gallery = """    /* Left Gallery */
    .pdp-gallery-col {
      position: sticky;
      top: 100px;
    }"""

repl_gallery = """    /* Left Gallery: Sticky in Viewport on Desktop */
    .pdp-gallery-col {
      position: -webkit-sticky;
      position: sticky;
      top: 115px;
      align-self: start;
      height: fit-content;
      z-index: 20;
    }"""

if target_gallery in css:
    css = css.replace(target_gallery, repl_gallery, 1)
    with open(luxury_css, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated meenu-luxury.css gallery sticky rule!")
else:
    print("target_gallery not matched in css")

# 3. Re-package Meenu_Label_Shopify_Theme.zip
zip_target = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
with zipfile.ZipFile(zip_target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Theme successfully re-packaged into {zip_target}")
