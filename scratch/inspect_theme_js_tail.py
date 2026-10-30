with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect last 100 lines of meenu-theme.js
lines = js.splitlines()
print(f"Total lines: {len(lines)}")
for l in lines[-80:]:
    print(l)
