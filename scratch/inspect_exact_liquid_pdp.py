import sys
with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function selectShopifyPdpSize')
sys.stdout.buffer.write(c[idx:idx+800].encode('utf-8'))
