with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_header = text.find('<header>')
pos_home = text.find('id="storefrontHomeView"')
pos_pdp = text.find('id="productDetailView"')
print('header pos:', pos_header)
print('storefrontHomeView pos:', pos_home)
print('productDetailView pos:', pos_pdp)

# Check inside openProductPage
pos_fn = text.find('function openProductPage')
print('openProductPage pos:', pos_fn)
if pos_fn != -1:
    print(text[pos_fn:pos_fn+1200])
