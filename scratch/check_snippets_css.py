import os
import re

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
css_path = os.path.join(theme_dir, 'assets', 'meenu-luxury.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

snippets_dir = os.path.join(theme_dir, 'snippets')
for fname in os.listdir(snippets_dir):
    fpath = os.path.join(snippets_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    classes = set(re.findall(r'class=["\']([^"\']+)["\']', content))
    flat_classes = set(c for line in classes for c in line.split() if not c.startswith('{%') and not c.startswith('{{'))
    missing = [c for c in flat_classes if f".{c}" not in css]
    print(f"=== {fname} ===")
    print(f"  Total classes: {len(flat_classes)}, Missing in CSS: {len(missing)}")
    if missing:
        print("  Missing:", missing)
