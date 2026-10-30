import csv

with open(r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    seen = set()
    for row in reader:
        handle = row['Handle']
        if handle not in seen:
            seen.add(handle)
            print(f"{row['Type']:16} | {row['Variant SKU']:14} | {row['Title']}")
