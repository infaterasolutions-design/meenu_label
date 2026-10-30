import zipfile
import os
import shutil

zip_path = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
extract_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch\theme_extracted"

if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

# 1. Update assets/meenu-luxury.css
css_path = os.path.join(extract_dir, "assets", "meenu-luxury.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

global_css_rule = """
/* Clean Modern Lining Numerals Globally */
html, body, *, *::before, *::after {
  font-variant-numeric: lining-nums proportional-nums !important;
  font-feature-settings: "lnum" 1, "pnum" 1 !important;
}

.modern-num-pill,
[class*="count"],
[class*="price"],
.qty-stepper {
  font-family: 'Plus Jakarta Sans', 'Montserrat', -apple-system, sans-serif !important;
  font-variant-numeric: lining-nums !important;
  font-feature-settings: "lnum" 1 !important;
}

.modern-num-pill {
  font-size: 0.75em !important;
  font-weight: 500 !important;
  color: var(--text-muted) !important;
  vertical-align: middle !important;
  margin-left: 4px !important;
}
"""
css = global_css_rule + "\n" + css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update sections/main-cart.liquid
cart_liquid_path = os.path.join(extract_dir, "sections", "main-cart.liquid")
with open(cart_liquid_path, "r", encoding="utf-8") as f:
    liquid = f.read()

old_h1_liquid = "Shopping Bag ({{ cart.item_count }})"
new_h1_liquid = 'Shopping Bag <span class="modern-num-pill">({{ cart.item_count }})</span>'

if old_h1_liquid in liquid:
    liquid = liquid.replace(old_h1_liquid, new_h1_liquid, 1)

with open(cart_liquid_path, "w", encoding="utf-8") as f:
    f.write(liquid)

# Repack zip
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, extract_dir)
            z.write(full_path, rel_path)

print("SUCCESS: Meenu_Label_Shopify_Theme.zip repacked with modern digit fonts!")
