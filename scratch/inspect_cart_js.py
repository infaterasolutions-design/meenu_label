with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
m = re.findall(r'(function toggleCartDrawer[\s\S]*?\{[\s\S]*?\})', js)
if m:
    print(m[0])
else:
    print("toggleCartDrawer not found as standard function, search occurrence:")
    lines = [l for l in js.splitlines() if 'toggleCartDrawer' in l or 'CartDrawer' in l or 'CartBackdrop' in l]
    print("\n".join(lines[:10]))
