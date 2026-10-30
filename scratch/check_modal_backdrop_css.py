with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'(\.modal-backdrop[^{]*\{[^}]+\})', css)
print("modal-backdrop rules:")
for rule in m:
    print(rule.encode('ascii', 'replace').decode('ascii'))
    print("---")
