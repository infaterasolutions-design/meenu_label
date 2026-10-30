with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    ('Jaipur Chanderi Silk Festive Suit', 'The Royal Wine Chanderi Festive Suit'),
    ('Warm Mustard & Fuchsia', 'Royal Wine & Antique Gold'),
    ('Drop 01 Star', 'Flagship Hero'),
    ('Flagship Marigold Courtyard Elegance (JAB26ST05010)', 'Flagship Royal Wine Courtyard Elegance (JAB26ST05010)'),
    ('delicate zari V-neck piping, tailored cigarette trousers, and a lightweight printed organza dupatta that drapes effortlessly', 'intricate antique gold zari neckline embroidery, tailored cigarette trousers, and a sheer fluid organza dupatta that drapes with regal grace')
]

for old, new in replacements:
    count = text.count(old)
    text = text.replace(old, new)
    print(f'Replaced {old[:35]} ({count} times)')

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('build_snitch_storefront.py successfully updated.')
