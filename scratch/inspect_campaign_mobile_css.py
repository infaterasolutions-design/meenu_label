with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
# Find media queries with campaign-hero
m = re.findall(r'(@media[^{]*\{[^{]*\{[^}]*\}[^}]*campaign-hero[^}]*\})', css)
print("Found media query matches:", len(m))

# Search for campaign-hero-content and campaign-hero-card
lines = css.splitlines()
for i, l in enumerate(lines):
    if 'campaign-hero-content' in l or 'campaign-badge' in l or 'campaign-hero-card' in l:
        print(f"Line {i+1}: {l}")
