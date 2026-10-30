import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Find occurrences of 'Cormorant Garamond' in CSS and inline styles
matches = re.findall(r"[^{;]*Cormorant Garamond[^;}]*", text)
print(f"Found {len(matches)} occurrences of Cormorant Garamond:")
for m in matches[:15]:
    print("---", m.strip())

# Specifically find cart page title
title_match = re.search(r'<h1[^>]*Shopping Bag.*?</h1>', text, re.I | re.DOTALL)
if title_match:
    print("\nCart Page H1 found:")
    print(title_match.group(0))
