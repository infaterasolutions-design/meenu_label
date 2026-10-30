import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r"function\s+[a-zA-Z0-9_]*cart[a-zA-Z0-9_]*\s*\(", text, flags=re.IGNORECASE)
print("Cart functions:", matches)
for line in text.splitlines():
    if 'addToCart' in line:
        print(line[:120])
