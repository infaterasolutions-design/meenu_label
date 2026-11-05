import csv

path = r'c:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import_16_Designs.csv'
with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f'Rows in 16_Designs: {len(rows)}')
for r in rows[:5]:
    print(r['Handle'], 'Image Src:', r.get('Image Src', ''))
