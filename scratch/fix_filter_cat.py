with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("function filterCategory(cat, btn) {\n      closeProductPage();{", "function filterCategory(cat, btn) {{\n      closeProductPage();")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed filterCategory function in build_snitch_storefront.py")
