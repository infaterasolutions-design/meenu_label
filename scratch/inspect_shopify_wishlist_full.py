with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/* 2. WISHLIST MANAGEMENT')
if idx == -1:
    idx = text.find('WISHLIST MANAGEMENT')
print(text[idx:idx+2500].encode('ascii', errors='replace').decode('ascii'))
