with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'class="card-body"', text))
print("Found", len(matches), "card-body in index.html")
if matches:
    idx0 = matches[0].start()
    print(text[idx0:idx0+600].encode('ascii', errors='replace').decode('ascii'))
