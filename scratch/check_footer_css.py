with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = ['footer-inner', 'footer-col', 'footer-bottom', 'modal-btn-primary']
for c in classes:
    print(f".{c}: {'FOUND' if f'.{c}' in css else 'MISSING'}")
