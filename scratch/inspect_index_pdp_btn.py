with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('pdpAddToCartBtn')
print(c[idx-100:idx+800])
