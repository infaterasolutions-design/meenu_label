with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

for c in ['policy-modal-card', 'policy-modal-header', 'policy-modal-body']:
    print(f"{c} in CSS:", c in css)
