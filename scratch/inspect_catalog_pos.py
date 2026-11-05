with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="catalog"')
print(c[idx:idx+600])
