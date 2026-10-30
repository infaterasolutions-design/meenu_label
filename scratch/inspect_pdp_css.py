import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'[^{}]*pdp-size[^{}]*\{[^}]*\}', html)
for m in matches[:15]:
    print(m.strip())
    print("-" * 30)
