with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_pdp = text.find('id="productDetailView"')
pos_footer = text.find('<footer>')
pos_cart = text.find('id="cartDrawer"')
pos_wish = text.find('id="wishlistDrawer"')
pos_account = text.find('id="accountModalBackdrop"')

print("PDP start:", pos_pdp)
print("Footer start:", pos_footer)
print("CartDrawer pos:", pos_cart)
print("WishlistDrawer pos:", pos_wish)
print("AccountModal pos:", pos_account)
