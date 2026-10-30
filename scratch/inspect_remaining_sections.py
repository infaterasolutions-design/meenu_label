import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections'

for name in ['featured-collection.liquid', 'value-props.liquid', 'founder-story.liquid', 'footer.liquid']:
    p = os.path.join(theme_dir, name)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"=== {name} (first 25 lines) ===")
        print("".join(lines[:25]))
