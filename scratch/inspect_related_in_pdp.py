with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('pdp-related-grid')
if idx != -1:
    print(text[idx:idx+1200].encode('ascii', errors='replace').decode('ascii'))
