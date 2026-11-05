with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

s_start = text.find('<style>')
s_end = text.find('</style>')
print(text[s_start:s_start + 1200])
