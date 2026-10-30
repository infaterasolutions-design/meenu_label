import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="productModalBackdrop"')
if idx != -1:
    print("=== productModalBackdrop snippet ===")
    print(html[idx:idx+2500])
