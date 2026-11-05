with open('snippets/snitch-login-modal.liquid', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<script>')
if idx != -1:
    print(c[idx:idx+1500])
else:
    print("No script tag in snitch-login-modal.liquid")
