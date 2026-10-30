import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_backdrop = text.find('id="cartBackdrop"')
pos_drawer = text.find('id="cartDrawer"')
print("Backdrop pos:", pos_backdrop)
print("Drawer pos:", pos_drawer)

# find end of cart drawer
# let's see what is after cartDrawer
pos_wishlist = text.find('id="wishlistDrawer"')
print("Wishlist drawer pos:", pos_wishlist)
if pos_backdrop != -1 and pos_wishlist != -1:
    snippet = text[pos_backdrop:pos_wishlist]
    print("Length of drawer HTML to remove:", len(snippet))
    sys.stdout.buffer.write(snippet[:300].encode('utf-8'))
    print("\n...\n")
    sys.stdout.buffer.write(snippet[-300:].encode('utf-8'))
