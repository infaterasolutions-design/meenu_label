with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.splitlines()
for i, l in enumerate(lines[140:190]):
    print(f"{141+i}: {l}")
