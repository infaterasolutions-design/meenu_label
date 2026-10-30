import zipfile
import os
import shutil

zip_path = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
extract_dir = r"C:\Users\sande\Documents\antigravity\splendid-nobel\scratch\theme_extracted"

if os.path.exists(extract_dir):
    shutil.rmtree(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_dir)

cart_snippet_path = os.path.join(extract_dir, "snippets", "cart-drawer.liquid")
with open(cart_snippet_path, "r", encoding="utf-8") as f:
    print(f.read())
