with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('product-card')
while pos != -1:
    print(text[pos-40:pos+250].encode('ascii', errors='replace').decode('ascii'))
    print('---')
    pos = text.find('product-card', pos+200)
