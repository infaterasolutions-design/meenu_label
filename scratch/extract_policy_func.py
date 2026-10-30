with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.findall(r'(function openPolicyModal[\s\S]*?)(?=function|\Z)', html)
if m:
    print(m[0][:3000].encode('ascii', 'replace').decode('ascii'))
