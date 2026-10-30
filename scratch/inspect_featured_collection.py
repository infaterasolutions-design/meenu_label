with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('featured-collection.liquid')
if pos != -1:
    print(text[pos:pos+1000].encode('ascii', errors='replace').decode('ascii'))
