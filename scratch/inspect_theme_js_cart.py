with open('assets/meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect updateCartUI and snitchAddSizeToCart in meenu-theme.js
idx = js.find('function updateCartUI')
print("Current updateCartUI in meenu-theme.js:")
print(js[idx:idx+500].encode('ascii', errors='replace').decode('ascii'))
