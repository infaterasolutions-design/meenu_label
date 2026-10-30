import re

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

m = re.findall(r'(<div[^>]*class="[^"]*cart[^"]*"[^>]*>[\s\S]{1,600})', html)
for match in m:
    print(match.encode('ascii', 'replace').decode('ascii'))
    print("---------------------------------")
