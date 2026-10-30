import re

with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'products = (\[[\s\S]*?\n\])', text)
prods = eval(m.group(1))

prod_by_code = {p['code']: p for p in prods}

invoice_rates = {
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

shipping_per_pc = 755.0 / 47.0

print(f"{'SKU':15} | {'Product Name':32} | {'Cost':7} | {'Landed':7} | {'Retail':7} | {'MRP':6} | {'Margin %':8} | {'Stock Qty'}")
print("-" * 105)

total_retail_val = 0
total_landed_val = 0

for code, cost in invoice_rates.items():
    p = prod_by_code[code]
    landed = cost * 1.05 + shipping_per_pc
    selling = p['price']
    mrp = p['mrp']
    margin_pct = ((selling - landed) / selling) * 100
    qty = 2 if code == 'JAB26ST05010' else 3
    total_retail_val += selling * qty
    total_landed_val += landed * qty
    print(f"{code:15} | {p['name'][:32]:32} | Rs.{cost:5.0f} | Rs.{landed:5.0f} | Rs.{selling:5.0f} | Rs.{mrp:5.0f} | {margin_pct:6.1f}% | {qty} pcs")

print("-" * 105)
print(f"Total Ordered Stock: 47 pieces across 16 silhouettes")
print(f"Total Purchase Cost (Base): Rs. 32,045.00")
print(f"GST 5%: Rs. 1,602.25")
print(f"DTDC Express Shipping: Rs. 755.00")
print(f"TOTAL INVOICE AMOUNT PAYABLE: Rs. 34,402.25")
print(f"Total Potential Retail Gross Revenue: Rs. {total_retail_val:,.2f}")
print(f"Total Gross Profit Potential: Rs. {total_retail_val - 34402.25:,.2f}")
print(f"Overall Portfolio Gross Margin: {((total_retail_val - 34402.25) / total_retail_val)*100:.1f}%")
print(f"Inventory Value Markup Multiplier: {total_retail_val / 34402.25:.2f}x")
