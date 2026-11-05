with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'aspect-ratio:\s*4\s*/\s*5', text))
print("Found", len(matches), "occurrences of aspect-ratio: 4 / 5 in index.html")
for m in matches:
    idx = m.start()
    print(text[max(0, idx - 40):min(len(text), idx + 60)])
    print('-'*30)
