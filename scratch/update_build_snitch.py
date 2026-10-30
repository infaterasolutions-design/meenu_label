import os, shutil

script_path = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"

with open(script_path, "r", encoding="utf-8") as f:
    content = f.read()

new_products_code = """        "img_file": "ZAC26TP04826.jpg"
    },
    {
        "id": "JAB26SS05740",
        "code": "JAB26SS05740",
        "name": "Roohani Chanderi Sharara Festive Set",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Lustrous Chanderi Silk with Zari & Organza Dupatta",
        "color": "Royal Emerald & Gold",
        "price": 2399,
        "mrp": 3799,
        "badge": "New Arrival",
        "badge_class": "badge-exclusive",
        "desc": "A regal festive ensemble. Crafted in lustrous Chanderi silk with intricate neck zari embroidery, paired with voluminous tiered Sharara pants and a scalloped golden-lace organza dupatta.",
        "img_file": "JAB26SS05740.jpg"
    },
    {
        "id": "JAB25ST02661",
        "code": "JAB25ST02661",
        "name": "Noor Chanderi Silk Straight Kurta Suit",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Pure Chanderi Silk Blend with Hand Zari Detailing",
        "color": "Golden Honey & Teal",
        "price": 2199,
        "mrp": 3499,
        "badge": "Only 3 Left",
        "badge_class": "badge-scarcity",
        "desc": "Graceful poise in pure Chanderi silk. Tailored straight kurta accented with delicate hand-piped neckline zari, paired with coordinating cigarette trousers and a lightweight sheer dupatta for timeless festive charm.",
        "img_file": "JAB25ST02661.jpg"
    },
    {
        "id": "JAB26ST05754",
        "code": "JAB26ST05754",
        "name": "Shahi Chanderi Royal Festive Ensemble",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Royal Chanderi Silk & Zari with Golden Border Dupatta",
        "color": "Regal Mustard & Magenta",
        "price": 2299,
        "mrp": 3699,
        "badge": "Trending",
        "badge_class": "badge-trending",
        "desc": "Exquisite craftsmanship from Surat's heritage looms. Straight-cut royal Chanderi kurta featuring heritage bootis and zari threadwork, paired with ankle-cut trousers and an opulent woven border dupatta.",
        "img_file": "JAB26ST05754.jpg"
    }
]"""

# 1. Replace the products closing bracket
target_prod = """        "img_file": "ZAC26TP04826.jpg"\n    }\n]"""
assert target_prod in content, "Could not find products closing bracket!"
content = content.replace(target_prod, new_products_code, 1)

# 2. Update all count texts
replacements = [
    ("Strictly 39 Pieces Total", "Strictly 48 Pieces Total"),
    ("All Silhouettes (13)", "All Silhouettes (16)"),
    ("Festive Suits (3)", "Festive Suits (6)"),
    ("The Debut 13 Silhouettes", "The Debut 16 Silhouettes"),
    ("All (13)", "All (16)"),
    ("13 Silhouettes", "16 Silhouettes"),
    ("39 Pieces Total (Strict Scarcity)", "48 Pieces Total (Strict Scarcity)"),
    ("Curated Silhouettes: 13 designs", "Curated Silhouettes: 16 designs"),
    ("Production Cap: 39 pieces total", "Production Cap: 48 pieces total"),
]

for old, new in replacements:
    count = content.count(old)
    content = content.replace(old, new)
    print(f"Replaced '{old}' -> '{new}' ({count} times)")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Updated build_snitch_storefront.py with 16 products and updated scarcity metrics.")
