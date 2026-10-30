with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\snippets\nav-drawer.liquid', 'r', encoding='utf-8') as f:
    nd = f.read()

print("=== snippets/nav-drawer.liquid ===")
print(nd.encode('ascii', 'replace').decode('ascii'))
