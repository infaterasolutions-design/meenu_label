with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.findall(r'(function toggleWishlist[\s\S]*?)(?=function|\Z)', html)
for match in m:
    print(match[:1200].encode('ascii', 'replace').decode('ascii'))
    print("----------------")

m_drawer = re.findall(r'(<div[^>]*id="wishlistDrawer"[\s\S]*?<\/div>\s*<\/div>)', html)
if m_drawer:
    print("\nWishlist Drawer Markup:")
    print(m_drawer[0].encode('ascii', 'replace').decode('ascii'))
