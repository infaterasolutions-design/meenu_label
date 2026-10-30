import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_drawer = text.find('class="cart-drawer" id="cartDrawer"')
pos_drawer_end = text.find('</div>\n  </div>', pos_drawer)
if pos_drawer_end == -1:
    pos_drawer_end = text.find('</div>\r\n  </div>', pos_drawer)

snippet = text[pos_drawer:pos_drawer+4000]
sys.stdout.buffer.write(snippet.encode('utf-8'))
