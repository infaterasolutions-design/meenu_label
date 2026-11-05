with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
print(re.findall(r'class="snitch-plus-trigger"[^>]*', c)[:5])
