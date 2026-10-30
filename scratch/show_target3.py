import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_cart = text.find('&#10024; Unlocked: FREE Express Shipping Across India')
snippet = text[pos_cart-120:pos_cart+250]
sys.stdout.buffer.write(snippet.encode('utf-8'))
