import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Search for openProduct or modal
for term in ['openProduct', 'productModal', 'modal-body', 'function open']:
    idx = text.find(term)
    print(f"Term '{term}':", idx)
    if idx != -1:
        snippet = text[idx:idx+400]
        print(snippet[:200])
        print("---")
