with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'4\s*/\s*5', text))
print("Found", len(matches), "occurrences in meenu-luxury.css")
for m in matches:
    idx = m.start()
    print(text[max(0, idx - 50):min(len(text), idx + 80)])
    print('-'*30)
