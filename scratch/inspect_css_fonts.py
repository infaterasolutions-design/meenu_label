html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect font-family declarations in CSS
import re
css_fonts = re.findall(r"([^{}]*\{[^{}]*font-family:[^{}]*\})", text[:30000])
for cf in css_fonts[:10]:
    print("---", cf.strip()[:150])
