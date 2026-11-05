with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function selectPdpSize')
print(c[idx:idx+1200])
