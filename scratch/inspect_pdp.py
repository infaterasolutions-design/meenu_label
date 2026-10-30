with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\main-product.liquid', 'r', encoding='utf-8') as f:
    pdp = f.read()

print("=== main-product.liquid length ===", len(pdp))
print(pdp[:2500].encode('ascii', 'replace').decode('ascii'))
