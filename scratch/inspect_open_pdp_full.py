with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function openProductPage')
print(text[pos:pos+1500])
