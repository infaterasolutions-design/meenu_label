import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find PDP container
idx = html.find('id="productDetailView"')
if idx != -1:
    print("=== productDetailView HTML structure ===")
    print(html[idx:idx+3500])
