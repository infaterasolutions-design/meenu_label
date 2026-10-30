with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\featured-collection.liquid', 'r', encoding='utf-8') as f:
    fc = f.read()

print("=== featured-collection.liquid ===")
print(fc.encode('ascii', 'replace').decode('ascii'))
