theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/templates/index.json"
with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

print(content)
