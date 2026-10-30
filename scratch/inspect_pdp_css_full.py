with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('/* ========================================================\n       PRODUCT DETAIL PAGE (PDP) - LUXURY ATELIER VIEW')
if idx == -1:
    idx = html.find('PRODUCT DETAIL PAGE')
print(html[idx:idx+2500])
