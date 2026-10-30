with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\assets\meenu-luxury.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.campaign-hero-card {\n        min-height: 480px;')
if idx == -1:
    idx = css.find('min-height: 480px')
print(css[idx-200:idx+400])
