with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'(\.pdp-[^{]+{[^}]+})', css)
print(f"Total .pdp- rules: {len(matches)}")
for m in matches[:25]:
    # print selector
    lines = m.split('\n')
    print(lines[0])
