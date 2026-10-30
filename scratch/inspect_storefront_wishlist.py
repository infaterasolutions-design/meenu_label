with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
lines = [l for l in html.splitlines() if 'wishlist' in l.lower()]
print(f"Total wishlist lines in storefront: {len(lines)}")
for l in lines[:15]:
    print(" ", l.encode('ascii', 'replace').decode('ascii'))
