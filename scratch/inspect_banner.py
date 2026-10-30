import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

print("File read successfully, total characters:", len(text))

# Search for announcement bar CSS and HTML
matches = re.findall(r".{0,100}announcement-bar.{0,200}", text, flags=re.IGNORECASE)
for m in matches[:5]:
    print("MATCH:", m.strip())
