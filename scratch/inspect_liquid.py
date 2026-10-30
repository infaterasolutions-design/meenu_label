import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\main-product.liquid', 'r', encoding='utf-8') as f:
    content = f.read()

print("main-product.liquid length:", len(content))
for line in content.split('\n'):
    if 'size' in line.lower() or 'variant' in line.lower() or 'selected' in line.lower():
        print(line[:120])
