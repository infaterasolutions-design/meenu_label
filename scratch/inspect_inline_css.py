with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

style_start = text.find('<style>')
style_end = text.find('</style>')
if style_start != -1:
    print(text[style_start:style_end+8])
