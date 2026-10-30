with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = [
    'craftsmanship-section', 'craftsmanship-header', 'craftsmanship-eyebrow',
    'craftsmanship-title', 'craftsmanship-grid', 'craft-card', 'craft-card-img',
    'craft-card-overlay', 'craft-card-badge', 'craft-card-content',
    'craft-card-eyebrow', 'craft-card-title', 'craft-card-cta'
]

for c in classes:
    found = f".{c}" in css
    print(f".{c}: {'FOUND' if found else 'MISSING'}")
