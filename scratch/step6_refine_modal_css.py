import sys
sys.stdout.reconfigure(encoding='utf-8')

for p in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    c = c.replace('height: min(650px, 90vh);', 'height: min(720px, 92vh);')
    c = c.replace(
        '/* Right Form Column */\n    .snitch-login-content {\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      background: #000000;\n      padding: 32px 28px;\n      height: 100%;\n    }',
        '/* Right Form Column */\n    .snitch-login-content {\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      background: #000000;\n      padding: 20px 24px;\n      height: 100%;\n      overflow-y: auto;\n      scrollbar-width: thin;\n    }'
    )
    c = c.replace('padding: 42px 36px 34px;', 'padding: 28px 30px 24px; margin: auto 0;')
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Refined modal dimensions in {p}")

# Also update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('height: min(650px, 90vh);', 'height: min(720px, 92vh);')
c = c.replace(
    '/* Right Form Column */\n    .snitch-login-content {\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      background: #000000;\n      padding: 32px 28px;\n      height: 100%;\n    }',
    '/* Right Form Column */\n    .snitch-login-content {\n      display: flex;\n      align-items: center;\n      justify-content: center;\n      background: #000000;\n      padding: 20px 24px;\n      height: 100%;\n      overflow-y: auto;\n      scrollbar-width: thin;\n    }'
)
c = c.replace('padding: 42px 36px 34px;', 'padding: 28px 30px 24px; margin: auto 0;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Refined modal dimensions in index.html")
