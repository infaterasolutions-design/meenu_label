html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('id="quickViewModal"')
if idx == -1:
    idx = text.find('class="modal"')
print("Quick view modal index:", idx)
if idx != -1:
    print(text[idx:idx+400])
