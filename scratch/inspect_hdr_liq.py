with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\header.liquid', 'r', encoding='utf-8') as f:
    hdr = f.read()

print("=== header.liquid ===")
print(hdr.encode('ascii', 'replace').decode('ascii'))
