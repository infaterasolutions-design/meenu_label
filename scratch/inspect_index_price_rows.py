with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("index.html length:", len(html))

# Let's inspect card-price-row in index.html
import re
price_rows = list(re.finditer(r'<div class="card-price-row">', html))
print(f"Found {len(price_rows)} card-price-row in index.html")

# Let's see what each card looks like
first_row = price_rows[0].start()
print(html[first_row-200:first_row+300].encode('ascii', errors='replace').decode('ascii'))
