with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('pdp-accordion')
if idx != -1:
    print(html[idx:idx+2500])
