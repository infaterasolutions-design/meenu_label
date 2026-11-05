with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = list(re.finditer(r'wishlist', html, re.IGNORECASE))
print(f"Found {len(matches)} occurrences of wishlist in index.html")

for m in matches:
    idx = m.start()
    line_start = html.rfind('\n', 0, idx)
    line_end = html.find('\n', idx)
    print(html[line_start:line_end].strip())
