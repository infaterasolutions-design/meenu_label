theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/sections/main-product.liquid"
with open(p, 'r', encoding='utf-8') as f:
    pdp = f.read()

idx = pdp.find('<script>')
print(pdp[idx:].encode('ascii', 'replace').decode('ascii'))
