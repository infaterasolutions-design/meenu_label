theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
p = f"{theme_dir}/assets/meenu-theme.js"
with open(p, 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function isSnitchLoggedIn')
print(js[idx:idx+1500])
