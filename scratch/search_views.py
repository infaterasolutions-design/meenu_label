import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

for term in ['id="storefrontHomeView"', 'id="productDetailView"', 'header-icon-btn']:
    pos = text.find(term)
    print(f"Term '{term}':", pos)
