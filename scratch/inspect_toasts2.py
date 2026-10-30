import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

p = html.find('function showToast')
if p != -1:
    print("=== showToast snippet ===")
    print(html[p:p+600])

p2 = html.find('function quickAddCart(')
if p2 != -1:
    print("=== quickAddCart snippet ===")
    print(html[p2:p2+600])

p3 = html.find('function openQuickSizeSelector')
if p3 != -1:
    print("=== openQuickSizeSelector snippet ===")
    print(html[p3:p3+600])
