with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'images\s*:', text)
for m in matches:
    idx = m.start()
    print(text[max(0, idx - 50):min(len(text), idx + 200)])
    print('-'*40)
