products = [
  {'sku': 'JAB26ST05010', 'name': 'Jaipur Chanderi Silk Festive Suit', 'cat': 'Festive Suits', 'cogs': 925, 'price': 2299, 'mrp': 3699, 'pcs': 2},
  {'sku': 'JAA26DR03942', 'name': 'The Retro Polka Dot Wrap Dress', 'cat': 'Dresses', 'cogs': 595, 'price': 1499, 'mrp': 2499, 'pcs': 3},
  {'sku': 'SET916', 'name': 'Lime Halter Dobby Palazzo Set', 'cat': 'Co-ord Sets', 'cogs': 675, 'price': 1649, 'mrp': 2699, 'pcs': 3},
  {'sku': 'JAC25ST03063', 'name': 'The Gulabi Organza Festive Suit', 'cat': 'Festive Suits', 'cogs': 655, 'price': 2199, 'mrp': 3499, 'pcs': 3},
  {'sku': 'SET974', 'name': 'Mustard Crepe Angrakha Co-ord Set', 'cat': 'Co-ord Sets', 'cogs': 555, 'price': 1699, 'mrp': 2799, 'pcs': 3},
  {'sku': 'JAA26DR04449', 'name': 'Navy Botanical Georgette Midi Dress', 'cat': 'Dresses', 'cogs': 645, 'price': 1699, 'mrp': 2799, 'pcs': 3},
  {'sku': 'TXC26KB04820', 'name': 'Lime Silk V-Neck Tunic Co-ord', 'cat': 'Co-ord Sets', 'cogs': 685, 'price': 1749, 'mrp': 2899, 'pcs': 3},
  {'sku': 'JAC25CD03428', 'name': 'Porcelain Ivory Embroidered Co-ord', 'cat': 'Co-ord Sets', 'cogs': 555, 'price': 1549, 'mrp': 2499, 'pcs': 3},
  {'sku': 'JNE4046', 'name': 'White Porcelain Floral Wrap Dress', 'cat': 'Dresses', 'cogs': 575, 'price': 1599, 'mrp': 2599, 'pcs': 3},
  {'sku': 'JAB24ST00932', 'name': 'Midnight Botanical 3-Piece Fusion Set', 'cat': 'Festive Suits', 'cogs': 595, 'price': 1899, 'mrp': 2999, 'pcs': 3},
  {'sku': 'TXC26TP04108', 'name': 'Artisanal Abstract V-Neck Blouse', 'cat': 'Tops & Blouses', 'cogs': 395, 'price': 999, 'mrp': 1799, 'pcs': 3},
  {'sku': 'TXC26TP04098', 'name': 'Monochrome Foliage V-Neck Top', 'cat': 'Tops & Blouses', 'cogs': 295, 'price': 899, 'mrp': 1499, 'pcs': 3},
  {'sku': 'ZAC26TP04826', 'name': 'Contemporary Floral Everyday Blouse', 'cat': 'Tops & Blouses', 'cogs': 345, 'price': 949, 'mrp': 1599, 'pcs': 3},
  {'sku': 'JAB26SS05740', 'name': 'Roohani Chanderi Sharara Festive Set', 'cat': 'Festive Suits', 'cogs': 1245, 'price': 2399, 'mrp': 3799, 'pcs': 3},
  {'sku': 'JAB25ST02661', 'name': 'Noor Chanderi Silk Straight Kurta Suit', 'cat': 'Festive Suits', 'cogs': 1085, 'price': 2199, 'mrp': 3499, 'pcs': 3},
  {'sku': 'JAB26ST05754', 'name': 'Shahi Chanderi Royal Festive Ensemble', 'cat': 'Festive Suits', 'cogs': 1165, 'price': 2299, 'mrp': 3699, 'pcs': 3},
]

# Fixed expenses per unit model from step 69:
# Revenue: 2000
# COGS: 550
# Shipping & Packaging: 110
# Payment/COD: 40
# RTO/Return Buffer: 100
# Taxes to Govt: 100
# Meta Ads Cost: 500
# Net Profit: 600
# Fixed Non-Product Ops Cost = 110 + 40 + 100 + 100 = 350
# Ad Cost = 500
# Total Expenses beyond COGS = 850

print(f"{'SKU':14} | {'Product Name':35} | {'COGS':5} | {'Current':7} | {'Net Margin':10} | {'Status':16} | {'Min Price for >=600'}")
print("-" * 115)

for p in products:
    net = p['price'] - p['cogs'] - 850
    target_price = p['cogs'] + 850 + 600 # COGS + 1450
    status = "PASS (>=600)" if net >= 600 else f"SHORT (-Rs.{600-net})"
    print(f"{p['sku']:14} | {p['name'][:35]:35} | Rs.{p['cogs']:<3} | Rs.{p['price']:<5} | Rs.{net:<8} | {status:16} | Rs.{target_price}")
