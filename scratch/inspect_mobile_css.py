# Let's inspect the exact CSS rules in assets/meenu-luxury.css around line 4270
with open('assets/meenu-luxury.css', 'r', encoding='utf-8') as f:
    text = f.read()

target = "/* PDP on Mobile */"
idx = text.find(target)
if idx != -1:
    print(text[idx:idx+800])
else:
    print("Not found")
