with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
print(re.findall(r'[a-zA-Z0-9_]*Account[a-zA-Z0-9_]*', c)[:10])
print(re.findall(r'[a-zA-Z0-9_]*Login[a-zA-Z0-9_]*', c)[:10])
print(re.findall(r'[a-zA-Z0-9_]*Otp[a-zA-Z0-9_]*', c)[:10])
