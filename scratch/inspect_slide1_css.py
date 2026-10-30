with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'(\.slide-1-cta-box[^{]*\{[^}]+\})', css)
print("slide-1-cta-box rules:")
for rule in m:
    print(rule.encode('ascii', 'replace').decode('ascii'))
    print("---")
