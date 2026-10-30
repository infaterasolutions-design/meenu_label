with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m_policy = re.findall(r'(<div[^>]*id="policyModal"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', html)
if m_policy:
    print("Found policyModal HTML, length:", len(m_policy[0]))
    print(m_policy[0][:1500].encode('ascii', 'replace').decode('ascii'))
else:
    # search for openPolicyModal definition
    m_func = re.findall(r'(function openPolicyModal[\s\S]*?\{[\s\S]*?\n\})', html)
    if m_func:
        print("Found openPolicyModal function:\n", m_func[0])
    
    # search for policy modal id
    idx = html.find('id="policyModal"')
    if idx != -1:
        print("policyModal snippet:\n", html[idx-50:idx+1500].encode('ascii', 'replace').decode('ascii'))
    else:
        print("id policyModal not found, search 'policy':")
        lines = [l for l in html.splitlines() if 'openPolicyModal' in l]
        for l in lines[:10]:
            print(l.encode('ascii', 'replace').decode('ascii'))
