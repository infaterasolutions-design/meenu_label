import os
import re

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
css_path = os.path.join(theme_dir, 'assets', 'meenu-luxury.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Check sections
sections_dir = os.path.join(theme_dir, 'sections')
print("=== AUDIT OF SECTIONS ===")
for fname in sorted(os.listdir(sections_dir)):
    p = os.path.join(sections_dir, fname)
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    raw_classes = re.findall(r'class=["\']([^"\']+)["\']', content)
    classes = set()
    for rc in raw_classes:
        for c in rc.split():
            if not c.startswith('{%') and not c.startswith('{{') and not '}' in c:
                classes.add(c)
    
    missing = [c for c in sorted(classes) if f".{c}" not in css]
    print(f"\n{fname}: {len(classes)} classes")
    if missing:
        print("  Missing in CSS:", missing)
    else:
        print("  ALL MATCH CSS!")
