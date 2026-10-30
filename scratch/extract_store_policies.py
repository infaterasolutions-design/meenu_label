with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx_p = html.find('policyModalBackdrop')
if idx_p != -1:
    print("=== policyModalBackdrop HTML ===")
    print(html[idx_p-40:idx_p+1500].encode('ascii', 'replace').decode('ascii'))

idx_sp = html.find('const STORE_POLICIES')
if idx_sp == -1:
    idx_sp = html.find('var STORE_POLICIES')
if idx_sp != -1:
    print("=== STORE_POLICIES ===")
    print(html[idx_sp:idx_sp+3000].encode('ascii', 'replace').decode('ascii'))
