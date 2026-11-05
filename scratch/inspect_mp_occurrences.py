with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Check all occurrences of 4 / 5 or 4/5
matches = list(re.finditer(r'4\s*/\s*5', text))
print("Found", len(matches), "occurrences in main-product.liquid")
for m in matches:
    idx = m.start()
    print(text[max(0, idx - 50):min(len(text), idx + 80)])
    print('-'*30)
