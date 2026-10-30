with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
m = re.findall(r'(\.sticky-catalog-header[^{]*)', css)
print("sticky-catalog-header in CSS:", m)

m2 = re.findall(r'(\.section-header[^{]*)', css)
print("section-header in CSS:", m2)

m3 = re.findall(r'(\.filter-tabs[^{]*)', css)
print("filter-tabs in CSS:", m3)

m4 = re.findall(r'(\.filter-tab[^{]*)', css)
print("filter-tab in CSS:", m4)
