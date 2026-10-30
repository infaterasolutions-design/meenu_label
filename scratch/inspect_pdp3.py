with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('var activePdpProductId = null;')
print(html[idx:idx+3500])
