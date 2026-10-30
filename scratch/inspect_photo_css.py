with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.snitch-campaign-photo[^{]*\{[^}]+\})', css)
for m in matches:
    print(m)
    print("---")
