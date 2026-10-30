import os

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
for root, dirs, files in os.walk(theme_dir):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), theme_dir)
        print(rel)
