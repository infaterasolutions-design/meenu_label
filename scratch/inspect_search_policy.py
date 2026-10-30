import os

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'

with open(os.path.join(theme_dir, 'assets', 'meenu-theme.js'), 'r', encoding='utf-8') as f:
    js = f.read()

print("openPolicyModal in JS:", "openPolicyModal" in js)
print("toggleSearchBar in JS:", "toggleSearchBar" in js)

# Let's inspect toggleSearchBar in js
lines = [l for l in js.splitlines() if 'toggleSearchBar' in l or 'searchOverlayBar' in l]
print("toggleSearchBar lines:")
for l in lines:
    print(" ", l)
