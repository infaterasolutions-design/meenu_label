import os, csv, shutil

downloads_dir = r"C:\Users\sande\Downloads"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
csv_path = os.path.join(downloads_dir, "Meenu_Label_Shopify_Products_Import.csv")
csv_path_v16 = os.path.join(downloads_dir, "Meenu_Label_Shopify_Products_Import_16_Designs.csv")
artifact_csv = os.path.join(artifacts_dir, "Meenu_Label_Shopify_Products_Import.csv")

# 16 items: code, title, cat, fabric, wholesale_rate, retail_price, mrp, desc
items = [
    ("JAB26ST05010", "Jaipur Chanderi Silk Festive Suit", "Festive Suits", "Chanderi Silk & Zari with Organza Dupatta", 925, 2299, 3699,
     "An iconic 3-piece festive ensemble featuring a straight-cut Chanderi kurta with delicate zari V-neck piping, tailored cigarette trousers, and a lightweight printed organza dupatta that drapes effortlessly for celebratory occasions."),
    ("SET974", "Mustard Crepe Angrakha Co-ord Set", "Co-ord Sets", "Fluid Crepe Silk", 555, 1699, 2799,
     "A contemporary royal wrap silhouette. Tailored in fluid crepe silk with an overlapping Angrakha neckline trimmed in gold gota patti and playful side latkan tassels. Paired with matching silk trousers."),
    ("TXC26KB04820", "Lime Silk V-Neck Tunic Co-ord", "Co-ord Sets", "Silk Blend", 685, 1749, 2899,
     "Clean-lined minimalism. Featuring a modern V-neck tunic top in lustrous lime silk blend paired with relaxed ankle-length cigarette pants. Ideal for elevated brunches or festive workwear."),
    ("JAC25ST03063", "The Gulabi Organza Festive Suit", "Festive Suits", "Cotton Silk Blend & Sheer Organza", 655, 2199, 3499,
     "Subtle luxury in powder pink. Straight-cut kurta with delicate neckline zari border, matching tailored trousers, and a rich heritage floral-printed organza dupatta with golden tassels."),
    ("JAB24ST00932", "Midnight Botanical 3-Piece Fusion Set", "Festive Suits", "Fine Georgette & Crepe", 595, 1899, 2999,
     "A standout evening fusion set. Includes a cropped inner bodice, straight comfort trousers, and an ethereal printed floor-length overlay cape shrug for effortless movement."),
    ("SET916", "Lime Halter Dobby Palazzo Set", "Co-ord Sets", "Dobby Chiffon & Cotton Lining", 675, 1649, 2699,
     "Breezy and modern. Flattering halter-style high-neck top in textured dobby chiffon paired with fluid wide-leg palazzo pants. Lightweight, breathable, and head-turning."),
    ("JAC25CD03428", "Porcelain Ivory Embroidered Co-ord", "Co-ord Sets", "Premium Cotton Blend", 555, 1549, 2499,
     "The ultimate boardroom-to-brunch ensemble. Ivory longline tunic with minimal collar embroidery and matching tapered trousers tailored for all-day comfort."),
    ("JAA26DR04449", "Navy Botanical Georgette Midi Dress", "Dresses", "Flowing Georgette with Voile Lining", 645, 1699, 2799,
     "Graceful garden silhouette. Full balloon sleeves, elasticated waist cinching, and tiered ruffled midi hem in deep navy blooming print. A dream for outdoor sundowners."),
    ("JNE4046", "White Porcelain Floral Wrap Dress", "Dresses", "Airy Crepe Georgette", 575, 1599, 2599,
     "Resort elegance. Pure white wrap dress with Mediterranean cobalt floral motifs, 3/4 sleeves, and a matching fabric belt with circular buckle."),
    ("JAA26DR03942", "The Retro Polka Dot Wrap Dress", "Dresses", "100% Breathable Pure Cotton", 595, 1499, 2499,
     "Timeless 1950s chic reimagined. Wrap silhouette with adjustable waist sash, flared A-line skirt, and breathable pure cotton weave. Featured on our debut Instagram campaign."),
    ("TXC26TP04108", "Artisanal Abstract V-Neck Blouse", "Tops & Blouses", "Chiffon Crepe", 395, 999, 1799,
     "Statement daytime blouse featuring an abstract artisanal brushstroke print, elegant V-neckline, and relaxed fluid drape that tucks easily into palazzos or trousers."),
    ("TXC26TP04098", "Monochrome Foliage V-Neck Top", "Tops & Blouses", "Fine Silk Crepe", 295, 899, 1499,
     "Effortless casual elegance. Lightweight crepe top with subtle botanical leaf sketches, perfect paired with cigarette trousers or high-rise denims for daily meetings."),
    ("ZAC26TP04826", "Contemporary Floral Everyday Blouse", "Tops & Blouses", "Poly-Crepe Comfort Weave", 345, 949, 1599,
     "Minimalist everyday blouse featuring mandarin collar detailing, half placket buttons, and wrinkle-resistant easy-care fabric for modern working women."),
    # 3 New Designs added by User:
    ("JAB26SS05740", "Roohani Chanderi Sharara Festive Set", "Festive Suits", "Lustrous Chanderi Silk with Zari & Organza Dupatta", 995, 2399, 3799,
     "A regal festive ensemble. Crafted in lustrous Chanderi silk with intricate neck zari embroidery, paired with voluminous tiered Sharara pants and a scalloped golden-lace organza dupatta."),
    ("JAB25ST02661", "Noor Chanderi Silk Straight Kurta Suit", "Festive Suits", "Pure Chanderi Silk Blend with Hand Zari Detailing", 845, 2199, 3499,
     "Graceful poise in pure Chanderi silk. Tailored straight kurta accented with delicate hand-piped neckline zari, paired with coordinating cigarette trousers and a lightweight sheer dupatta for timeless festive charm."),
    ("JAB26ST05754", "Shahi Chanderi Royal Festive Ensemble", "Festive Suits", "Royal Chanderi Silk & Zari with Golden Border Dupatta", 995, 2299, 3699,
     "Exquisite craftsmanship from Surat's heritage looms. Straight-cut royal Chanderi kurta featuring heritage bootis and zari threadwork, paired with ankle-cut trousers and an opulent woven border dupatta.")
]

sizes = ["M (38)", "L (40)", "XL (42)"]

headers = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags",
    "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value",
    "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy",
    "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", "Variant Requires Shipping", "Variant Taxable",
    "Variant Barcode", "Image Src", "Image Position", "Image Alt Text", "Gift Card", "SEO Title", "SEO Description",
    "Cost per item", "Status"
]

rows = []
for code, title, cat, fabric, wholesale, price, mrp, desc in items:
    handle = title.lower().replace(" ", "-").replace("&", "and").replace(",", "").replace("(", "").replace(")", "")
    body_html = f"<p><strong>{title}</strong></p><p>{desc}</p><p><strong>Fabric:</strong> {fabric}</p><p><strong>Care:</strong> Gentle Hand Wash / Dry Clean. Made in India.</p>"
    tags = f"Drop 01, {cat}, Surat Wholesale, Meenu Label, Chandigarh, Breathable"

    for idx, sz in enumerate(sizes):
        sku = f"{code}-{sz.split()[0]}"
        row = [
            handle,
            title if idx == 0 else "",
            body_html if idx == 0 else "",
            "Meenu Label" if idx == 0 else "",
            "Apparel & Accessories > Clothing" if idx == 0 else "",
            cat if idx == 0 else "",
            tags if idx == 0 else "",
            "TRUE" if idx == 0 else "",
            "Size",
            sz,
            "", "", "", "",
            sku,
            "450",          # Variant Grams
            "shopify",      # Variant Inventory Tracker
            "1",            # Variant Inventory Qty (1 pc per size = 48 total)
            "deny",         # Variant Inventory Policy
            "manual",       # Variant Fulfillment Service
            str(price),     # Variant Price
            str(mrp),       # Variant Compare At Price
            "TRUE",         # Variant Requires Shipping
            "TRUE",         # Variant Taxable
            "",             # Variant Barcode
            "",             # Image Src
            "1" if idx == 0 else "",
            title if idx == 0 else "",
            "FALSE",
            f"{title} | Meenu Label Drop 01",
            desc[:150],
            str(wholesale), # Cost per item (dealer wholesale price)
            "active"
        ]
        rows.append(row)

# 1. Write to Artifacts
with open(artifact_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
print(f"Written artifact CSV: {artifact_csv}")

# 2. Write to v16 file in Downloads
with open(csv_path_v16, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
print(f"Written {csv_path_v16}")

# 3. Attempt to overwrite standard CSV in Downloads if not locked
try:
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Overwritten standard CSV: {csv_path}")
except Exception as e:
    print(f"Standard CSV is currently open in Excel: {e}")

print(f"SUCCESS: Generated Shopify Product Import CSV with {len(rows)} variants (16 designs x 3 sizes = 48 pieces total).")
