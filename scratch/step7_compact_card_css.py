import sys
sys.stdout.reconfigure(encoding='utf-8')

for p in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css', 'index.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('padding: 18px 16px;\n  margin-top: 18px;', 'padding: 12px 14px;\n  margin-top: 12px;')
    c = c.replace('padding-bottom: 12px;\n  margin-bottom: 14px;', 'padding-bottom: 8px;\n  margin-bottom: 10px;')
    c = c.replace('gap: 16px;\n  position: relative;\n  padding-left: 24px;\n  margin: 16px 0;', 'gap: 9px;\n  position: relative;\n  padding-left: 24px;\n  margin: 10px 0;')
    c = c.replace('margin-top: 14px;\n  transition: all 0.2s ease;', 'margin-top: 10px;\n  transition: all 0.2s ease;')
    c = c.replace('padding: 12px 16px;\n  background: #25D366;', 'padding: 10px 14px;\n  background: #25D366;')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Compact shipment card styles applied to {p}")
