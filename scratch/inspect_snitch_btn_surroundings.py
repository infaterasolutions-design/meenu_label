with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'class="snitch-plus-trigger"', text))
print("Found", len(matches), "snitch-plus-trigger in index.html")
if matches:
    idx = matches[0].start()
    print(text[max(0, idx-200):min(len(text), idx+300)].encode('ascii', errors='replace').decode('ascii'))
