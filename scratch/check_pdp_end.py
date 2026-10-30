with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_pdp = text.find('id="productDetailView"')
pos_footer = text.find('<footer>')

print("PDP pos:", pos_pdp)
print("Footer pos:", pos_footer)
print("Content between PDP and footer (last 300 chars):")
print(text[pos_footer-300:pos_footer])
