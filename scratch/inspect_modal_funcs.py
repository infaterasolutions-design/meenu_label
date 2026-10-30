import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find("function selectModalSize(size, el)")
print(html[idx:idx+1200])

idx2 = html.find("function addCurrentProductToCart()")
print(html[idx2:idx2+400])
