with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('.pdp-btn-whatsapp')
if idx != -1:
    print(c[idx:idx+600])
else:
    print('Not found')
