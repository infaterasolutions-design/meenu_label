with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\hero-editorial.liquid', 'r', encoding='utf-8') as f:
    hero = f.read()

import re
pills = re.findall(r'<div class="[^"]*pill[^"]*"[\s\S]*?<\/div>', hero)
print(f"Found {len(pills)} pill elements in hero-editorial.liquid:")
for p in pills:
    print("---", p[:100].encode('ascii', 'replace').decode('ascii'))
