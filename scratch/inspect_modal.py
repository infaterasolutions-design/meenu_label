import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

p = html.find('function openProductModal')
if p != -1:
    print("=== openProductModal snippet ===")
    print(html[p:p+1200])

p2 = html.find('function selectSize(')
if p2 != -1:
    print("=== selectSize snippet ===")
    print(html[p2:p2+800])
