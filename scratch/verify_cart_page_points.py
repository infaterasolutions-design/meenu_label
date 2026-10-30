import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Check locations where we need to plug in:
# 1. Header icon action for cart:
pos_header_cart = text.find('onclick="toggleCart()" title="Shopping Bag"')
print("pos_header_cart:", pos_header_cart)

# 2. Before footer:
pos_footer = text.find('<!-- Footer -->')
print("pos_footer:", pos_footer)

# 3. CSS insertion:
pos_css = text.find('/* Cart Progress Bar */')
print("pos_css:", pos_css)
