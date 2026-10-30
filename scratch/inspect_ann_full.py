with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m = re.search(r'(<div class="announcement-bar"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', html)
if m:
    print(m.group(1).encode('ascii', 'replace').decode('ascii'))
else:
    idx = html.find('class="announcement-bar"')
    print(html[idx:idx+1200].encode('ascii', 'replace').decode('ascii'))
