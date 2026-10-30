with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect all occurrences of @media for mobile campaign
import re
queries = re.findall(r'(@media[^{]*\{[\s\S]*?\.campaign-hero-card[\s\S]*?\})', css)
for q in queries:
    print(q[:800])
    print("---")
