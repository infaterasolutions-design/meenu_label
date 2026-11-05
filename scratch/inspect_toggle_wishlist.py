with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function toggleWishlist(param)')
print(text[idx:idx+1500].encode('ascii', errors='replace').decode('ascii'))
