with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("meenu-theme.js length:", len(js))
lines = [l for l in js.splitlines() if 'function ' in l]
print("Functions defined in meenu-theme.js:")
for l in lines:
    print(" -", l.strip())
