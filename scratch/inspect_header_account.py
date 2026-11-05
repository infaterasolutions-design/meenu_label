with open('sections/header.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('openAccountModal')
if idx != -1:
    print(c[idx-100:idx+300])
else:
    print("Not found in header.liquid")
