with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\snippets\cart-drawer.liquid', 'r', encoding='utf-8') as f:
    cd = f.read()

print("=== snippets/cart-drawer.liquid ===")
print(cd.encode('ascii', 'replace').decode('ascii'))
