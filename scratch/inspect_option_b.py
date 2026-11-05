import os, re

# Define Option B Pricing Master
# (Code, Name, Price, MRP, WSP, Category)
option_b_pricing = {
    'SET974': {
        'price': 2399,
        'mrp': 3799,
        'name': 'The Gulzar Angrakha Crepe Silk Set',
        'color': 'Mustard Marigold & Ochre',
        'fabric': 'Artisanal Crepe Silk & Chiffon Dupatta'
    },
    'TXC26KB04820': {
        'price': 2499,
        'mrp': 3999,
        'name': 'The Mehr Lime Silk Blend Tunic Set',
        'color': 'Zesty Lime & Chartreuse',
        'fabric': 'Pure Silk Blend with Intricate Zari V-Neck'
    },
    'JAC25ST03063': {
        'price': 2499,
        'mrp': 3999,
        'name': 'The Gulabi Organza Festive Suit',
        'color': 'Gulabi Rose Pink',
        'fabric': 'Airy Cotton-Silk Blend with Embroidered Organza'
    },
    'JAB24ST00932': {
        'price': 2399,
        'mrp': 3799,
        'name': 'The Midnight Botanical Fusion Set',
        'color': 'Midnight Navy & Indigo',
        'fabric': 'Fluid Crepe Silk with Botanical Print'
    },
    'SET916': {
        'price': 2499,
        'mrp': 3999,
        'name': 'The Sitara Lime Dobby Palazzo Set',
        'color': 'Pistachio & Lime Green',
        'fabric': 'Textured Dobby Chiffon & Flared Palazzo'
    },
    'JAC25CD03428': {
        'price': 2399,
        'mrp': 3799,
        'name': 'The Porcelain Ivory Resort Co-ord',
        'color': 'Ivory Porcelain & Soft Sage',
        'fabric': 'Breathable Cotton Blend Comfort Weave'
    },
    'JAA26DR04449': {
        'price': 2499,
        'mrp': 3999,
        'name': 'The Neelam Botanical Georgette Midi',
        'color': 'Royal Navy & Floral Azure',
        'fabric': 'Featherlight Flowing Georgette'
    },
    'JNE4046': {
        'price': 2399,
        'mrp': 3799,
        'name': 'The White Porcelain Floral Wrap Dress',
        'color': 'Porcelain White & Coral Blossom',
        'fabric': 'Lined Premium Georgette Wrap'
    },
    'JAA26DR03942': {
        'price': 2399,
        'mrp': 3799,
        'name': 'The Retro Polka Dot Cotton Midi Dress',
        'color': 'Monochrome Noir & Polka White',
        'fabric': '100% Breathable Crisp Fine Cotton'
    },
    'TXC26TP04108': {
        'price': 1899,
        'mrp': 2999,
        'name': 'The Artisanal Abstract V-Neck Blouse',
        'color': 'Multicolor Terracotta & Amber',
        'fabric': 'Semi-Sheer Flowing Fine Chiffon'
    },
    'TXC26TP04098': {
        'price': 1799,
        'mrp': 2899,
        'name': 'The Monochrome Foliage V-Neck Top',
        'color': 'Ebony & Chalk White',
        'fabric': 'Smooth Poly-Crepe Fluid Drape'
    },
    'ZAC26TP04826': {
        'price': 1899,
        'mrp': 2999,
        'name': 'The Contemporary Floral Everyday Blouse',
        'color': 'Midnight Floral & Subtle Slate',
        'fabric': 'Wrinkle-Resistant Poly-Crepe Comfort Weave'
    },
    'JAB26ST05010': {
        'price': 2799,
        'mrp': 4499,
        'name': 'The Royal Wine Chanderi Festive Suit',
        'color': 'Deep Festive Wine / Maroon',
        'fabric': 'Pure Handloom Chanderi Silk with Intricate Zari'
    },
    'JAB26SS05740': {
        'price': 3199,
        'mrp': 4999,
        'name': 'The Roohani Champagne Sharara Set',
        'color': 'Almond Champagne Gold',
        'fabric': 'Lustrous Silk Blend with Gold Zari & Scalloped Dupatta'
    },
    'JAB25ST02661': {
        'price': 2999,
        'mrp': 4799,
        'name': 'The Noor Petrol Teal Chanderi Suit',
        'color': 'Petrol Teal Blue',
        'fabric': 'Pure Chanderi Silk with Intricate Floral Zari'
    },
    'JAB26ST05754': {
        'price': 2999,
        'mrp': 4799,
        'name': 'The Shahi Lilac Flared Festive Ensemble',
        'color': 'Royal Lilac / Lavender',
        'fabric': 'Lustrous Silk Blend Front-Slit Kurta with Zari'
    }
}

print("Loaded Option B configuration for 16 products.")
for k, v in option_b_pricing.items():
    print(f"{k:12} -> Price: Rs {v['price']:4} | MRP: Rs {v['mrp']:4} | {v['name']}")
