with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

for term in ['header-icon-action', 'brand-logo-img', 'hamburger-btn', 'shopify-size']:
    print(f"{term} in CSS:", term in css)
