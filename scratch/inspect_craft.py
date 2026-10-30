with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\craftsmanship-spotlight.liquid', 'r', encoding='utf-8') as f:
    craft = f.read()

print("=== craftsmanship-spotlight.liquid ===")
print(craft.encode('ascii', 'replace').decode('ascii'))
