import os

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

print("HTML size:", len(html))
print("product-card count:", html.count('class="product-card"'))
for code in ["JAB26SS05740", "JAB25ST02661", "JAB26ST05754", "JAB26ST05010"]:
    print(f"{code} in HTML: {code in html}")

for count_str in ["All (16)", "Festive Suits (6)", "48 Pieces Total", "16 Silhouettes"]:
    print(f"'{count_str}' in HTML: {count_str in html}")
