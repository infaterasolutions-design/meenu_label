theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/snippets/nav-drawer.liquid"
with open(p, 'r', encoding='utf-8') as f:
    nd = f.read()

print("nav-drawer.liquid:")
print(nd)
