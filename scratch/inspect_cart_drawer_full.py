theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/snippets/cart-drawer.liquid"
with open(p, 'r', encoding='utf-8') as f:
    cd = f.read()

print("cart-drawer.liquid:")
print(cd)
