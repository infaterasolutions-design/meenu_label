theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/snippets/snitch-login-modal.liquid"
with open(p, 'r', encoding='utf-8') as f:
    login = f.read()

print("snitch-login-modal.liquid length:", len(login))
print(login[:2000])
