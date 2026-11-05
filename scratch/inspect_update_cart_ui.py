with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function updateCartUI')
print(text[idx:idx+800].encode('ascii', errors='replace').decode('ascii'))
