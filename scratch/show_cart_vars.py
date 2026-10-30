import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_js = text.find('var discountPercent = 0;')
if pos_js == -1:
    pos_js = text.find('discountPercent')
snippet = text[pos_js-50:pos_js+600]
sys.stdout.buffer.write(snippet.encode('utf-8'))
