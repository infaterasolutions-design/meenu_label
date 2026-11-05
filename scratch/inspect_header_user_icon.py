with open('sections/header.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

import re
print(re.findall(r'<a[^>]*account[^>]*>.*?</a\s*>', c, re.IGNORECASE | re.DOTALL))
print(re.findall(r'<button[^>]*account[^>]*>.*?</button\s*>', c, re.IGNORECASE | re.DOTALL))
