theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/sections/header.liquid"
with open(p, 'r', encoding='utf-8') as f:
    hdr = f.read()

idx = hdr.find('header-account-btn')
print(hdr[idx-50:idx+400])
