with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's inspect the lines in build_snitch_storefront.py around updateWishlistUI
pos = code.find('function updateWishlistUI()')
if pos != -1:
    print(code[pos:pos+1500].encode('ascii', errors='replace').decode('ascii'))
