with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\hero-editorial.liquid', 'r', encoding='utf-8') as f:
    hero = f.read()

print("=== hero-editorial.liquid ===")
print(hero.encode('ascii', 'replace').decode('ascii'))
