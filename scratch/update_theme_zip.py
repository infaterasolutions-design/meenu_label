import os
import zipfile
import shutil

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
zip_dest = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
backup_dest = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.backup_size.zip'

if os.path.exists(zip_dest):
    shutil.copy2(zip_dest, backup_dest)
    print("Backed up zip to:", backup_dest)

# Create new zip
with zipfile.ZipFile(zip_dest, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Successfully packaged {zip_dest} ({os.path.getsize(zip_dest)} bytes)")
