theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/sections/main-product.liquid"
with open(p, 'r', encoding='utf-8') as f:
    pdp = f.read()

import re
forms = re.findall(r'<form[\s\S]*?<\/form>', pdp)
print(f"Forms in PDP: {len(forms)}")
for f in forms:
    print(f[:400])

scripts = re.findall(r'<script[\s\S]*?<\/script>', pdp)
print(f"\nScripts in PDP: {len(scripts)}")
for s in scripts:
    print(s[:500])
