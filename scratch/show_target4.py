import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_cart_footer = text.find('<div class="cart-footer">')
snippet = text[pos_cart_footer:pos_cart_footer+800]
sys.stdout.buffer.write(snippet.encode('utf-8'))
