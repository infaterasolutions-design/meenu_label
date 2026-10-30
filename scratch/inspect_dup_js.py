with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Let's inspect where duplicates start
idx = js.find('// --- Navigation & Search Bar Controls ---')
print("Position of Navigation & Search Bar Controls:", idx)
print("Before it:\n", js[idx-200:idx])
