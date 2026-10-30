import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

for var in ['selectedSize', 'pdpSelectedSize']:
    print(f"=== {var} ===")
    for m in re.finditer(r'\b' + re.escape(var) + r'\b', html):
        idx = m.start()
        print(html[max(0, idx-40):min(len(html), idx+80)].replace('\n', ' '))
