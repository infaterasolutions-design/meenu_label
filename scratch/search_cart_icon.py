import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('toggleCart()')
print("toggleCart() found at:", pos)
if pos != -1:
    snippet = text[pos-200:pos+250]
    sys.stdout.buffer.write(snippet.encode('utf-8'))
