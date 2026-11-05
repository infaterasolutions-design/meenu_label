with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

import re
print(re.findall(r'{%\s*render\s+[^%]+%}', c))
