with open('sections/main-product.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('pdpNotifyBtn')
print(c[idx-100:idx+900])
