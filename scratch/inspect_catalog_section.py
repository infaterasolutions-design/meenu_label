with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="catalog"')
if pos != -1:
    print(text[pos-50:pos+1000].encode('ascii', errors='replace').decode('ascii'))
