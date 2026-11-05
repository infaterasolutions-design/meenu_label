with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function snitchAddSizeToCart')
print(js[idx:idx+900].encode('ascii', errors='replace').decode('ascii'))
