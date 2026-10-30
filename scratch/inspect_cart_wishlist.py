theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/assets/meenu-theme.js"
with open(p, 'r', encoding='utf-8') as f:
    js = f.read()

import re
funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', js)
print("All functions in meenu-theme.js:")
for fn in funcs:
    print(" -", fn)

print("\nWishlist matches in JS:")
lines = [l for l in js.splitlines() if 'wish' in l.lower()]
print(f"Total wishlist lines: {len(lines)}")
for l in lines[:10]:
    print(" ", l)

print("\nCart matches in JS:")
cart_lines = [l for l in js.splitlines() if 'cart' in l.lower()]
print(f"Total cart lines: {len(cart_lines)}")
for l in cart_lines[:10]:
    print(" ", l)
