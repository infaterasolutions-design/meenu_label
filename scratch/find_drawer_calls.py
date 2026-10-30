import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Occurrences of openCart():")
for m in re.finditer(r"\bopenCart\s*\(", text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 60)
    print("---", text[start:end].replace('\n', ' '))

print("\nOccurrences of toggleCart():")
for m in re.finditer(r"\btoggleCart\s*\(", text):
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + 60)
    print("---", text[start:end].replace('\n', ' '))
