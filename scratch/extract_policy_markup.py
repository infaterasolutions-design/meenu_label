with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m_backdrop = re.search(r'(<div[^>]*id="policyModalBackdrop"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', html)
if m_backdrop:
    print("Found policyModalBackdrop markup:")
    print(m_backdrop.group(1).encode('ascii', 'replace').decode('ascii'))
else:
    # search lines
    lines = [l for l in html.splitlines() if 'policyModalBackdrop' in l]
    print("policyModalBackdrop lines:")
    for l in lines:
        print(l.encode('ascii', 'replace').decode('ascii'))
