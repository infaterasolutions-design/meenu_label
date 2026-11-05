files = [
    'sections/main-product.liquid',
    'assets/meenu-luxury.css',
    'index.html',
    'meenu-label-shopify-theme/sections/main-product.liquid',
    'meenu-label-shopify-theme/assets/meenu-luxury.css'
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    if '!important !important' in c:
        c = c.replace('!important !important', '!important')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Cleaned duplicate !important in {fname}")
    else:
        print(f"No duplicates in {fname}")
