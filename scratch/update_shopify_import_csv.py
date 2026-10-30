import csv, os, re

with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'products = (\[[\s\S]*?\n\])', text)
prods = eval(m.group(1))

invoice_costs = {
    'JAB26SS05740': 1245,
    'JAB26ST05754': 1165,
    'JAB25ST02661': 1085,
    'JAB26ST05010': 925,
    'TXC26KB04820': 685,
    'SET916': 675,
    'JAC25ST03063': 655,
    'JAA26DR04449': 645,
    'JAA26DR03942': 595,
    'JAB24ST00932': 595,
    'JNE4046': 575,
    'SET974': 555,
    'JAC25CD03428': 555,
    'TXC26TP04108': 395,
    'ZAC26TP04826': 345,
    'TXC26TP04098': 295
}

fieldnames = [
    'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type', 'Tags',
    'Published', 'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value',
    'Option3 Name', 'Option3 Value', 'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker',
    'Variant Inventory Qty', 'Variant Inventory Policy', 'Variant Fulfillment Service',
    'Variant Price', 'Variant Compare At Price', 'Variant Requires Shipping', 'Variant Taxable',
    'Variant Barcode', 'Image Src', 'Image Position', 'Image Alt Text', 'Gift Card',
    'SEO Title', 'SEO Description', 'Google Shopping / Google Product Category',
    'Google Shopping / Gender', 'Google Shopping / Age Group', 'Google Shopping / MPN',
    'Google Shopping / Condition', 'Google Shopping / Custom Product',
    'Google Shopping / Custom Label 0', 'Google Shopping / Custom Label 1',
    'Google Shopping / Custom Label 2', 'Google Shopping / Custom Label 3',
    'Google Shopping / Custom Label 4', 'Variant Image', 'Variant Weight Unit',
    'Variant Tax Code', 'Cost per item', 'Price / International', 'Compare At Price / International', 'Status'
]

rows = []
for p in prods:
    code = p['code']
    handle = p['name'].lower().replace('&', 'and').replace(' ', '-').replace('/', '-').replace('---', '-').replace('--', '-')
    handle = re.sub(r'[^a-z0-9\-]', '', handle)
    cost = invoice_costs.get(code, 600)
    selling = p['price']
    mrp = p['mrp']
    cat = p.get('cat_label', 'Ethnic Wear')
    fabric = p.get('fabric', 'Handcrafted Silk')
    desc = f"<p><strong>{p['name']}</strong> by Meenu Label.</p><p>Crafted in Chandigarh atelier from premium {fabric}. Designed for effortless modern luxury and comfort drape.</p>"
    
    # 3 sizes: M, L, XL
    sizes = ['M', 'L', 'XL']
    for idx, s in enumerate(sizes):
        is_first = (idx == 0)
        # Check out of stock for JAB26ST05010-XL
        if code == 'JAB26ST05010' and s == 'XL':
            qty = 0
        else:
            qty = 1
            
        row = {
            'Handle': handle,
            'Title': p['name'] if is_first else '',
            'Body (HTML)': desc if is_first else '',
            'Vendor': 'Meenu Label',
            'Product Category': 'Apparel & Accessories > Clothing > Traditional & Ceremonial Clothing',
            'Type': cat,
            'Tags': f"chandigarh-atelier, debut-drop, {p['category']}, {fabric.split()[0].lower()}",
            'Published': 'TRUE',
            'Option1 Name': 'Size',
            'Option1 Value': s,
            'Option2 Name': '',
            'Option2 Value': '',
            'Option3 Name': '',
            'Option3 Value': '',
            'Variant SKU': f"{code}-{s}",
            'Variant Grams': '450',
            'Variant Inventory Tracker': 'shopify',
            'Variant Inventory Qty': str(qty),
            'Variant Inventory Policy': 'deny',
            'Variant Fulfillment Service': 'manual',
            'Variant Price': str(selling),
            'Variant Compare At Price': str(mrp),
            'Variant Requires Shipping': 'TRUE',
            'Variant Taxable': 'TRUE',
            'Variant Barcode': '',
            'Image Src': '',
            'Image Position': '',
            'Image Alt Text': '',
            'Gift Card': 'FALSE',
            'SEO Title': f"{p['name']} | Meenu Label Chandigarh" if is_first else '',
            'SEO Description': f"Buy {p['name']} online. Handcrafted in pure {fabric} with 24-hr express Tricity dispatch." if is_first else '',
            'Google Shopping / Google Product Category': '1604',
            'Google Shopping / Gender': 'Female',
            'Google Shopping / Age Group': 'Adult',
            'Google Shopping / MPN': f"{code}-{s}",
            'Google Shopping / Condition': 'new',
            'Google Shopping / Custom Product': 'FALSE',
            'Google Shopping / Custom Label 0': 'Drop 01',
            'Google Shopping / Custom Label 1': cat,
            'Google Shopping / Custom Label 2': 'Chandigarh Atelier',
            'Google Shopping / Custom Label 3': '',
            'Google Shopping / Custom Label 4': '',
            'Variant Image': '',
            'Variant Weight Unit': 'g',
            'Variant Tax Code': 'GST5',
            'Cost per item': str(cost),
            'Price / International': '',
            'Compare At Price / International': '',
            'Status': 'active'
        }
        rows.append(row)

out_csv = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv'
with open(out_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated complete Shopify Import CSV: {len(rows)} variant rows across {len(prods)} products!")

brain_csv = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\Meenu_Label_Shopify_Products_Import.csv'
import shutil
shutil.copyfile(out_csv, brain_csv)
print(f"Copied to {brain_csv}")
