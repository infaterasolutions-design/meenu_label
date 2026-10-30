import os
import zipfile
import shutil

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
css_file = os.path.join(theme_dir, 'assets', 'meenu-luxury.css')

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add Snitch-style desktop sticky and scrollable CSS to meenu-luxury.css
snitch_theme_css = """
/* ========================================================
   SNITCH-STYLE DESKTOP PRODUCT PAGE (STICKY MEDIA & SCROLLABLE INFO)
   ======================================================== */
@media (min-width: 993px) {
  .product-main-grid,
  .pdp-grid {
    display: grid !important;
    grid-template-columns: 1.05fr 1fr !important;
    gap: 48px !important;
    align-items: start !important;
  }
  .product-gallery-sticky,
  .pdp-gallery-col {
    position: sticky !important;
    top: 85px !important;
    align-self: start !important;
  }
  .product-info-scrollable,
  .pdp-info-col {
    max-height: calc(100vh - 105px) !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    padding-right: 14px !important;
    scrollbar-width: thin;
    scrollbar-color: #D1C7BD transparent;
  }
  .product-info-scrollable::-webkit-scrollbar,
  .pdp-info-col::-webkit-scrollbar {
    width: 4px;
  }
  .product-info-scrollable::-webkit-scrollbar-track,
  .pdp-info-col::-webkit-scrollbar-track {
    background: transparent;
  }
  .product-info-scrollable::-webkit-scrollbar-thumb,
  .pdp-info-col::-webkit-scrollbar-thumb {
    background: #D1C7BD;
    border-radius: 4px;
  }
}
"""

if 'SNITCH-STYLE DESKTOP PRODUCT PAGE' not in css_content:
    css_content += '\n' + snitch_theme_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated meenu-luxury.css")
else:
    print("meenu-luxury.css already has Snitch styles")

# Package into zip
zip_dest = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
with zipfile.ZipFile(zip_dest, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Successfully packaged {zip_dest} ({os.path.getsize(zip_dest)} bytes)")
