import os, zipfile

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
zip_dest1 = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
zip_dest2 = r'c:\Users\sande\Documents\antigravity\splendid-nobel\Meenu_Label_Shopify_Theme.zip'

valid_dirs = {'assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates'}

for zip_out in [zip_dest1, zip_dest2]:
    with zipfile.ZipFile(zip_out, 'w', zipfile.ZIP_DEFLATED) as z:
        for d in sorted(valid_dirs):
            dp = os.path.join(theme_dir, d)
            if not os.path.exists(dp):
                continue
            for root, dirs, files in os.walk(dp):
                for f in sorted(files):
                    if f.startswith('.') or f.endswith('.py') or f.endswith('.log'):
                        continue
                    full_path = os.path.join(root, f)
                    arcname = os.path.relpath(full_path, theme_dir)
                    z.write(full_path, arcname)

    size_mb = os.path.getsize(zip_out) / (1024 * 1024)
    print(f"Created {zip_out} ({size_mb:.2f} MB)")
