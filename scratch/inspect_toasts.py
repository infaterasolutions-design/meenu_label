import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Toast / Alert functions in HTML:")
for m in re.finditer(r'function\s+([a-zA-Z0-9_]*(?:toast|Toast|alert|Alert|notify|Notify)[a-zA-Z0-9_]*)\s*\(', html):
    print(m.group(1))

# Also search for quickAddCart definition
p = html.find('function quickAddCart')
if p != -1:
    print("\n=== quickAddCart snippet ===")
    print(html[p:p+1200])
