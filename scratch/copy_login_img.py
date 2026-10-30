import shutil
import os

theme_assets = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'
src = os.path.join(theme_assets, 'hero_slide_2.jpg')
dst = os.path.join(theme_assets, 'hero_2_gulabi.jpg')

shutil.copyfile(src, dst)
print(f"Copied {src} to {dst} ({os.path.getsize(dst)} bytes)")
