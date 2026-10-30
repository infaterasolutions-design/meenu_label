theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
fc_path = f"{theme_dir}/sections/featured-collection.liquid"
with open(fc_path, 'r', encoding='utf-8') as f:
    fc = f.read()

print("featured-collection.liquid:")
print(fc)
