import os, re, csv

option_b = {
    'SET974': {
        'name': 'The Gulzar Angrakha Crepe Silk Set',
        'price': 2399,
        'mrp': 3799,
        'color': 'Mustard Marigold & Ochre',
        'fabric': 'Artisanal Crepe Silk & Chiffon Dupatta',
        'desc': 'Radiant mustard angrakha silhouette crafted in fluid crepe silk with intricate traditional neck detailing, paired with straight trousers and a sheer printed dupatta.'
    },
    'TXC26KB04820': {
        'name': 'The Mehr Lime Silk Blend Tunic Set',
        'price': 2499,
        'mrp': 3999,
        'color': 'Zesty Lime & Chartreuse',
        'fabric': 'Pure Silk Blend with Intricate Zari V-Neck',
        'desc': 'Modern regal tailoring in crisp silk blend. Features a delicate zari embroidered V-neckline, paired with matching ankle-cut trousers for festive daytime occasions.'
    },
    'JAC25ST03063': {
        'name': 'The Gulabi Organza Festive Suit',
        'price': 2499,
        'mrp': 3999,
        'color': 'Gulabi Rose Pink',
        'fabric': 'Airy Cotton-Silk Blend with Embroidered Organza',
        'desc': 'Soft romance in gulabi rose. A flared Anarkali silhouette in breathable cotton-silk blend, paired with coordinating bottoms and an ethereal organza dupatta.'
    },
    'JAB24ST00932': {
        'name': 'The Midnight Botanical Fusion Set',
        'price': 2399,
        'mrp': 3799,
        'color': 'Midnight Navy & Indigo',
        'fabric': 'Fluid Crepe Silk with Botanical Print',
        'desc': 'An artisanal 3-piece ensemble featuring rich midnight navy crepe with delicate floral vine motifs, straight cigarette pants, and a whisper-light dupatta.'
    },
    'SET916': {
        'name': 'The Sitara Lime Dobby Palazzo Set',
        'price': 2499,
        'mrp': 3999,
        'color': 'Pistachio & Lime Green',
        'fabric': 'Textured Dobby Chiffon & Flared Palazzo',
        'desc': 'Breezy celebratory elegance. Crafted from textured dobby chiffon featuring a halter-style neckline and voluminous flared palazzo pants for sunset gatherings.'
    },
    'JAC25CD03428': {
        'name': 'The Porcelain Ivory Resort Co-ord',
        'price': 2399,
        'mrp': 3799,
        'color': 'Ivory Porcelain & Soft Sage',
        'fabric': 'Breathable Cotton Blend Comfort Weave',
        'desc': 'Effortless luxury co-ord set. Relaxed tailored button-down shirt with botanical motifs paired with high-waisted wide-leg trousers for modern leisure.'
    },
    'JAA26DR04449': {
        'name': 'The Neelam Botanical Georgette Midi',
        'price': 2499,
        'mrp': 3999,
        'color': 'Royal Navy & Floral Azure',
        'fabric': 'Featherlight Flowing Georgette',
        'desc': 'Graceful movement in featherlight georgette. Tiered midi dress with cinched elasticated waist and subtle flutter sleeves, perfect for high-tea and celebrations.'
    },
    'JNE4046': {
        'name': 'The White Porcelain Floral Wrap Dress',
        'price': 2399,
        'mrp': 3799,
        'color': 'Porcelain White & Coral Blossom',
        'fabric': 'Lined Premium Georgette Wrap',
        'desc': 'Chic Parisian silhouette crafted in premium lined georgette. Feminine wrap bodice with adjustable side tie and fluttering hem.'
    },
    'JAA26DR03942': {
        'name': 'The Retro Polka Dot Cotton Midi Dress',
        'price': 2399,
        'mrp': 3799,
        'color': 'Monochrome Noir & Polka White',
        'fabric': '100% Breathable Crisp Fine Cotton',
        'desc': 'Timeless monochrome sophistication. Pure breathable fine cotton midi dress with iconic polka dots, contrast belt tie, and tailored A-line sweep.'
    },
    'TXC26TP04108': {
        'name': 'The Artisanal Abstract V-Neck Blouse',
        'price': 1899,
        'mrp': 2999,
        'color': 'Multicolor Terracotta & Amber',
        'fabric': 'Semi-Sheer Flowing Fine Chiffon',
        'desc': 'Expressive art in wearable luxury. Relaxed V-neck blouse in fluid fine chiffon with abstract brushstrokes, styled seamlessly with tailored trousers or skirts.'
    },
    'TXC26TP04098': {
        'name': 'The Monochrome Foliage V-Neck Top',
        'price': 1799,
        'mrp': 2899,
        'color': 'Ebony & Chalk White',
        'fabric': 'Smooth Poly-Crepe Fluid Drape',
        'desc': 'Modern work-to-evening essential. Tailored monochrome botanical print top with flattering V-neckline in wrinkle-resistant comfort drape.'
    },
    'ZAC26TP04826': {
        'name': 'The Contemporary Floral Everyday Blouse',
        'price': 1899,
        'mrp': 2999,
        'color': 'Midnight Floral & Subtle Slate',
        'fabric': 'Wrinkle-Resistant Poly-Crepe Comfort Weave',
        'desc': 'Minimalist everyday blouse featuring mandarin collar detailing, half placket buttons, and easy-care luxury poly-crepe fabric for modern professionals.'
    },
    'JAB26ST05010': {
        'name': 'The Jaipur Chanderi Silk Festive Suit',
        'price': 2799,
        'mrp': 4499,
        'color': 'Deep Festive Wine / Maroon',
        'fabric': 'Pure Handloom Chanderi Silk with Intricate Zari',
        'desc': 'The flagship debut hero ensemble. Crafted in deep festive wine Chanderi silk with intricate neck zari embroidery, tailored cigarette pants, and a lightweight organza dupatta.'
    },
    'JAB26SS05740': {
        'name': 'The Roohani Champagne Sharara Set',
        'price': 3199,
        'mrp': 4999,
        'color': 'Almond Champagne Gold',
        'fabric': 'Lustrous Silk Blend with Gold Zari & Scalloped Dupatta',
        'desc': 'An ethereal festive sharara ensemble. Crafted in lustrous almond champagne silk blend with fine gold zari detailing, paired with flared sharara pants and an intricately scalloped golden lace dupatta.'
    },
    'JAB25ST02661': {
        'name': 'The Noor Petrol Teal Chanderi Suit',
        'price': 2999,
        'mrp': 4799,
        'color': 'Petrol Teal Blue',
        'fabric': 'Pure Chanderi Silk with Intricate Floral Zari',
        'desc': 'Timeless elegance in pure Chanderi silk. Tailored straight-cut kurta in deep petrol teal accented with intricate floral zari threadwork on the neckline and sleeves, paired with classic trousers and a woven sheer dupatta.'
    },
    'JAB26ST05754': {
        'name': 'The Shahi Lilac Flared Festive Ensemble',
        'price': 2999,
        'mrp': 4799,
        'color': 'Royal Lilac / Lavender',
        'fabric': 'Lustrous Silk Blend Front-Slit Kurta with Zari',
        'desc': 'Exquisite craftsmanship in royal lavender silk blend. High front-slit flared silhouette embellished with golden threadwork along the placket and hem, paired with tailored trousers and a luminous coordinating dupatta.'
    }
}

# 1. Update scratch/build_snitch_storefront.py
b_path = r'scratch/build_snitch_storefront.py'
with open(b_path, 'r', encoding='utf-8') as f:
    code = f.read()

# We can reconstruct the `products = [...]` list in `build_snitch_storefront.py`
pattern = r'products\s*=\s*\[(.*?)\]\s*\n\s*print\("Loading base64'
match = re.search(pattern, code, re.DOTALL)
if not match:
    print("Error: Could not locate products list in build_snitch_storefront.py")
else:
    # Let's inspect each item and update its fields
    prod_block = match.group(1)
    # Parse individual dicts by splitting or regex
    item_pattern = r'\{\s*"id":\s*"([^"]+)".*?\}'
    items = re.findall(item_pattern, prod_block, re.DOTALL)
    print(f"Found {len(items)} products in build_snitch_storefront.py")

    # Rebuild products array cleanly
    new_prods = []
    # Let's read the existing products array safely via python exec in isolated dict
    sandbox = {}
    exec(match.group(0).split('print(')[0], sandbox)
    existing_prods = sandbox['products']

    for p in existing_prods:
        pid = p['id']
        if pid in option_b:
            opt = option_b[pid]
            p['name'] = opt['name']
            p['price'] = opt['price']
            p['mrp'] = opt['mrp']
            p['color'] = opt['color']
            p['fabric'] = opt['fabric']
            p['desc'] = opt['desc']
        new_prods.append(p)

    import json
    new_prods_str = "products = " + json.dumps(new_prods, indent=4) + "\n\n"
    
    code = code[:match.start()] + new_prods_str + code[match.end() - len('print("Loading base64'):]
    with open(b_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated build_snitch_storefront.py with Option B pricing!")

# 2. Update Shopify CSVs
csv_files = [
    r'Meenu_Label_Shopify_Products_Import.csv',
    r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Products_Import.csv'
]

for cf in csv_files:
    if not os.path.exists(cf):
        continue
    with open(cf, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    header = reader[0]
    handle_idx = header.index('Handle')
    title_idx = header.index('Title')
    body_idx = header.index('Body (HTML)')
    sku_idx = header.index('Variant SKU')
    price_idx = header.index('Variant Price')
    compare_idx = header.index('Variant Compare At Price')
    seo_title_idx = header.index('SEO Title')
    seo_desc_idx = header.index('SEO Description')

    for row in reader[1:]:
        sku = row[sku_idx]
        base_sku = sku.split('-')[0] if '-' in sku else sku
        if base_sku in option_b:
            opt = option_b[base_sku]
            row[price_idx] = str(opt['price'])
            row[compare_idx] = str(opt['mrp'])
            if row[title_idx]:
                row[title_idx] = opt['name']
                row[body_idx] = f"<p><strong>{opt['name']}</strong> by Meenu Label.</p><p>Crafted in Chandigarh atelier from premium {opt['fabric']}. Designed for effortless modern luxury and comfort drape.</p>"
                row[seo_title_idx] = f"{opt['name']} | Meenu Label Chandigarh"
                row[seo_desc_idx] = f"Buy {opt['name']} online. Handcrafted in pure {opt['fabric']} with 24-hr express Tricity dispatch."

    with open(cf, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(reader)
    print(f"Updated {cf} with Option B pricing!")
