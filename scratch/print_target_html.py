import sys
with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('id="pdpAddToCartBtn"')
idx2 = c.find('</a>', idx1)
sys.stdout.buffer.write(repr(c[idx1-20:idx2+4]).encode('utf-8'))
