with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'cart\.push', text)
for m in matches:
    idx = m.start()
    print(text[idx-50:idx+400].encode('ascii', errors='replace').decode('ascii'))
    print('='*40)
