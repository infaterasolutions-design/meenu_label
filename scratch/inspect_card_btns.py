import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<button[^>]*class="[^"]*(?:add|cart)[^"]*"[^>]*>[^<]*</button>', html, re.IGNORECASE)
for m in matches[:10]:
    print("CARD BTN:", m)

p = html.find('openQuickSizeSelector')
while p != -1:
    print("Found openQuickSizeSelector call around:", html[p-100:p+150])
    p = html.find('openQuickSizeSelector', p+1)
