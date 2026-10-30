html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for "Shopping Bag ("
idx = text.find("Shopping Bag (")
while idx != -1:
    print("Found 'Shopping Bag (' at:", idx)
    print(text[max(0, idx-50):min(len(text), idx+150)])
    print("---")
    idx = text.find("Shopping Bag (", idx+1)

# Let's search for wishlist title
idx_w = text.find("Wishlist (")
while idx_w != -1:
    print("Found 'Wishlist (' at:", idx_w)
    print(text[max(0, idx_w-50):min(len(text), idx_w+150)])
    print("---")
    idx_w = text.find("Wishlist (", idx_w+1)
