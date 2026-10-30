import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for cart drawer and pdp buy button
for term in ['cart-drawer', 'pdp-modal', 'buy-now', 'checkout']:
    idx = text.find(term)
    print(f"Term '{term}' found at:", idx)
    if idx != -1:
        snippet = text[idx:idx+400]
        print(snippet[:200])
        print("---")
