with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\value-props.liquid', 'r', encoding='utf-8') as f:
    val = f.read()

print("=== value-props.liquid ===")
print(val.encode('ascii', 'replace').decode('ascii'))
