import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<[^>]*class="[^"]*\bselected\b[^"]*"[^>]*>', html)
for m in matches:
    print(m)
