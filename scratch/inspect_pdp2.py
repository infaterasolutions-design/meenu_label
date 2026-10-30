with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

for term in ['pdpSelectedSize', 'addPdpToCart', 'buyPdpNow', 'updatePdpWhatsAppLink']:
    print(f"=== Occurrences of {term} ===")
    for m in re.finditer(re.escape(term), html):
        idx = m.start()
        print(html[max(0, idx-50):min(len(html), idx+150)].replace('\n', ' '))
        print("-" * 40)
