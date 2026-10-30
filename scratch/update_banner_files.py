import shutil
import os

theme_assets = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets'

# Overwrite old banners with new ones
shutil.copyfile(os.path.join(theme_assets, 'hero_slide_1.jpg'), os.path.join(theme_assets, 'banner_2_chanderi.jpg'))
shutil.copyfile(os.path.join(theme_assets, 'hero_slide_2.jpg'), os.path.join(theme_assets, 'banner_3_gulabi.jpg'))
shutil.copyfile(os.path.join(theme_assets, 'hero_slide_2.jpg'), os.path.join(theme_assets, 'banner_4_gulabi.jpg'))
shutil.copyfile(os.path.join(theme_assets, 'hero_slide_3.jpg'), os.path.join(theme_assets, 'banner_1_polka.jpg'))
shutil.copyfile(os.path.join(theme_assets, 'hero_slide_4.jpg'), os.path.join(theme_assets, 'banner_3_coord.jpg'))

print("All banner assets updated with new authentic photography!")
