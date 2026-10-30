import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('function updateCart')
if idx == -1:
    idx = text.find('function renderCart')
if idx == -1:
    idx = text.find('cartSubtotal')

if idx != -1:
    snippet = text[idx:idx+1500]
    sys.stdout.buffer.write(snippet.encode('utf-8'))
else:
    print("Not found")
