with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('function updateCartUI')
print("=== updateCartUI ===")
print(text[idx1:idx1+800].encode('ascii', errors='replace').decode('ascii'))

idx2 = text.find('function updateWishlistUI')
print("=== updateWishlistUI ===")
print(text[idx2:idx2+600].encode('ascii', errors='replace').decode('ascii'))
