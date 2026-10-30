with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('collection_liquid')
if pos != -1:
    print(text[pos:pos+900].encode('ascii', errors='replace').decode('ascii'))
