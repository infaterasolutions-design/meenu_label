with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('.snitch-login-dialog')
if idx != -1:
    print(c[idx:idx+800])
else:
    print("snitch-login-dialog not found in css")
