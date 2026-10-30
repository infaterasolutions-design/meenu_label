with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Look for overflow in body, html, #productDetailView, .pdp-section, .pdp-grid
for sel in ['body', 'html', '#productDetailView', '.pdp-section', '.pdp-grid', '.pdp-gallery-col', '.pdp-info-col', '.storefront-wrap', '.main-content']:
    matches = re.findall(r'[^{}]*' + re.escape(sel) + r'[^{}]*\{[^}]*\}', html)
    for m in matches:
        if 'overflow' in m or 'height' in m or 'position' in m or 'sticky' in m:
            print(f"=== {sel} ===")
            print(m.strip())
