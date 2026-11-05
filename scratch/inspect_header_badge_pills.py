with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.finditer(r'<span class="header-badge-pill"[^>]*>', html)
print("=== index.html header-badge-pill elements ===")
for m in matches:
    print(m.group(0))

with open('sections/header.liquid', 'r', encoding='utf-8') as f:
    liquid = f.read()

matches2 = re.finditer(r'<span class="header-badge-pill"[^>]*>', liquid)
print("=== sections/header.liquid header-badge-pill elements ===")
for m in matches2:
    print(m.group(0))
