with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'([^{}]*hamburger[^{}]*\{[^{}]*\})', text)
for m in matches:
    print(m)
    print('---')

matches2 = re.findall(r'([^{}]*header-left[^{}]*\{[^{}]*\})', text)
for m in matches2:
    print(m)
    print('---')
