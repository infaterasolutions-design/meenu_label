files = ['sections/main-product.liquid', 'assets/meenu-luxury.css', 'index.html']
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    import re
    m_45 = list(re.finditer(r'aspect-ratio:\s*4\s*/\s*5', text))
    m_23 = list(re.finditer(r'aspect-ratio:\s*2\s*/\s*3', text))
    print(f"{fname}:")
    print(f"  aspect-ratio 4/5: {len(m_45)}")
    print(f"  aspect-ratio 2/3: {len(m_23)}")
