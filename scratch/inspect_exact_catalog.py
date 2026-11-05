import csv, os

csv_path = r'c:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv'
if not os.path.exists(csv_path):
    csv_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\Meenu_Label_Shopify_Products_Import.csv'

with open(csv_path, 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"File: {csv_path}")
print(f"Total Rows: {len(rows)}")

products = {}
for r in rows:
    h = r.get('Handle')
    if h not in products:
        products[h] = {
            'title': r.get('Title'),
            'type': r.get('Type'),
            'tags': r.get('Tags'),
            'category': r.get('Product Category'),
            'variants': []
        }
    products[h]['variants'].append({
        'option': r.get('Option1 Value'),
        'price': r.get('Variant Price'),
        'mrp': r.get('Variant Compare At Price')
    })

print(f"Total Products: {len(products)}\n")
for i, (h, p) in enumerate(products.items(), 1):
    sizes = [v['option'] for v in p['variants'] if v['option']]
    price = p['variants'][0]['price'] if p['variants'] else ''
    mrp = p['variants'][0]['mrp'] if p['variants'] else ''
    print(f"{i:2d}. [{p['type']}] {p['title']}")
    print(f"    Handle: {h} | Price: Rs.{price} (MRP: Rs.{mrp}) | Sizes: {', '.join(sizes)}")
    print(f"    Tags: {p['tags']}")
