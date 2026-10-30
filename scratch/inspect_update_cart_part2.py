import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('// Append Gift Card to Cart Items')
snippet = text[idx:idx+2500]
sys.stdout.buffer.write(snippet.encode('utf-8'))
