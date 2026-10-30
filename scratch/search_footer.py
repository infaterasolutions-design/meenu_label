import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

pos_pdp = text.find('id="productDetailView"')
# find next section or footer
pos_footer = text.find('<footer>', pos_pdp)
print("pos_pdp:", pos_pdp)
print("pos_footer after pdp:", pos_footer)
if pos_footer != -1:
    snippet = text[pos_footer-400:pos_footer+200]
    sys.stdout.buffer.write(snippet.encode('utf-8'))
