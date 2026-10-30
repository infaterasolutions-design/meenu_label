with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx = html.find('var STORE_POLICIES = {')
if idx != -1:
    end_idx = html.find('function openPolicyModal', idx)
    print("STORE_POLICIES length:", end_idx - idx)
    with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_policies.js', 'w', encoding='utf-8') as out_f:
        out_f.write(html[idx:end_idx].strip())
    print("Saved extracted_policies.js successfully!")
