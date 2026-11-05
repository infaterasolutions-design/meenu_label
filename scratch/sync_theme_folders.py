import os, shutil

root_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
sub_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'

folders = ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']

for folder in folders:
    src_folder = os.path.join(root_dir, folder)
    dst_folder = os.path.join(sub_dir, folder)
    os.makedirs(dst_folder, exist_ok=True)
    
    for f in os.listdir(src_folder):
        sf = os.path.join(src_folder, f)
        df = os.path.join(dst_folder, f)
        if os.path.isfile(sf):
            shutil.copy2(sf, df)

print("Synchronized all folders from root to meenu-label-shopify-theme successfully!")

# Verify hero-editorial.liquid in both locations
p1 = os.path.join(root_dir, 'sections', 'hero-editorial.liquid')
p2 = os.path.join(sub_dir, 'sections', 'hero-editorial.liquid')
with open(p1, 'r', encoding='utf-8') as f1, open(p2, 'r', encoding='utf-8') as f2:
    assert f1.read() == f2.read(), "hero-editorial.liquid must be identical!"
    print("Verified: hero-editorial.liquid is 100% identical in both root and subfolder!")

# Verify meenu-luxury.css in both locations
c1 = os.path.join(root_dir, 'assets', 'meenu-luxury.css')
c2 = os.path.join(sub_dir, 'assets', 'meenu-luxury.css')
with open(c1, 'r', encoding='utf-8') as f1, open(c2, 'r', encoding='utf-8') as f2:
    assert f1.read() == f2.read(), "meenu-luxury.css must be identical!"
    print("Verified: meenu-luxury.css is 100% identical in both root and subfolder!")
