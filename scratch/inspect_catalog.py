import csv

path = r'c:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv'
with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f'Total rows: {len(rows)}')
products = {}
for r in rows:
    handle = r['Handle']
    if handle not in products:
        products[handle] = {
            'title': r['Title'],
            'type': r['Type'],
            'tags': r['Tags'],
            'price': r['Variant Price'],
            'compare_price': r.get('Variant Compare At Price', ''),
            'image': r.get('Image Src', ''),
            'variants': []
        }
    products[handle]['variants'].append(r['Option1 Value'])

print(f'Unique products: {len(products)}')
for h, p in products.items():
    print(f"- [{h}] {p['title']} | Type: {p['type']} | Tags: {p['tags']} | Price: Rs.{p['price']} | Sizes: {','.join(p['variants'])}")
