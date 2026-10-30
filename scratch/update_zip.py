import shutil
import os

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
zip_dest = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme'

# Create zip archive
shutil.make_archive(zip_dest, 'zip', theme_dir)
print(f"Zip created at: {zip_dest}.zip ({os.path.getsize(zip_dest + '.zip')} bytes)")
