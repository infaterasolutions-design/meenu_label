with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="productModalBackdrop"')
if pos != -1:
    print(text[pos-50:pos+1200].encode('ascii', errors='replace').decode('ascii'))
