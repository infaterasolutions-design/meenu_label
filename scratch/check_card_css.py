with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
selectors = re.findall(r'(\.product-card[^{]*)', css)
print("Product card selectors in CSS:")
for s in selectors[:15]:
    print(" -", s.strip())

selectors_card = re.findall(r'(\.card-[^{]*)', css)
print("\nCard selectors in CSS:")
for s in selectors_card[:15]:
    print(" -", s.strip())
