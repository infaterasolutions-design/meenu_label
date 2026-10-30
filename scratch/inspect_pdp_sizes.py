with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\main-product.liquid', 'r', encoding='utf-8') as f:
    pdp = f.read()

import re
m = re.findall(r'(<!-- Size Selector[\s\S]*?<\/form>)', pdp)
if m:
    print(m[0].encode('ascii', 'replace').decode('ascii'))
else:
    print("Size selector form snippet not found directly, let's print lines:")
    lines = [l for l in pdp.splitlines() if 'shopifySize' in l or 'shopify-size' in l or 'variant' in l]
    print("\n".join(lines[:20]))
