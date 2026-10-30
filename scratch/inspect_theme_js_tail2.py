theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'
js_path = f"{theme_dir}/assets/meenu-theme.js"
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

print("meenu-theme.js total length:", len(js))
lines = js.splitlines()
for l in lines[-40:]:
    print(l)
