with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'class="product-card"', text))
print("Found", len(matches), "cards in index.html")
# Print the price row of the first card
idx0 = matches[0].start()
print(text[idx0:idx0+700].encode('ascii', errors='replace').decode('ascii'))
