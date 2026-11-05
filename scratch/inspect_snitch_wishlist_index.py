with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function toggleSnitchSizeWishlist')
print(text[idx:idx+900].encode('ascii', errors='replace').decode('ascii'))
