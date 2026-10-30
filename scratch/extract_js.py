import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

scripts = re.findall(r"<script[^>]*>(.*?)</script>", text, flags=re.DOTALL | re.IGNORECASE)
with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "w", encoding="utf-8") as f:
    f.write(scripts[0])

print("Extracted JS to scratch/extracted.js")
