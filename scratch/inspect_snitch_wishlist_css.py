with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'\.snitch-size-wishlist-btn\b[^{]*\{[^}]*\}', text)
for m in matches:
    print(m.group(0))
