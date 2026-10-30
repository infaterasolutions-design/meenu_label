import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('PROCEED TO CHECKOUT')
if idx != -1:
    snippet = text[idx-200:idx+300]
    sys.stdout.buffer.write(snippet.encode('utf-8'))
