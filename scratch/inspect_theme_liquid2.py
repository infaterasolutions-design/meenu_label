theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/layout/theme.liquid"
with open(p, 'r', encoding='utf-8') as f:
    tl = f.read()

print(tl)
