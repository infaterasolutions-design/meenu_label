theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/sections/craftsmanship-spotlight.liquid"
with open(p, 'r', encoding='utf-8') as f:
    craft = f.read()

import re
badges = re.findall(r'<span class="[^"]*badge[^"]*"[^>]*>[\s\S]*?<\/span>', craft)
print(f"Found {len(badges)} badges in craftsmanship:")
for b in badges:
    print(" -", b)
