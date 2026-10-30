import sys

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r"@media[^{]+\{[^}]*announcement-bar[^}]*\}", text, flags=re.DOTALL)
for m in matches:
    print("Found media query:")
    sys.stdout.buffer.write(m.encode('utf-8'))
    print("\n---")
