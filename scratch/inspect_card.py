with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\snippets\product-card.liquid', 'r', encoding='utf-8') as f:
    pc = f.read()

print("=== snippets/product-card.liquid ===")
print(pc.encode('ascii', 'replace').decode('ascii'))
