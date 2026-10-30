import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Search for backdrops or modals with high z-index
matches = re.findall(r"\.[\w\-]*backdrop[^{]*\{[^}]*\}", text, flags=re.DOTALL | re.IGNORECASE)
for m in matches:
    print("BACKDROP CSS:", m.strip()[:200])

# 2. Check all <script> tags for basic syntax or unclosed blocks
scripts = re.findall(r"<script[^>]*>(.*?)</script>", text, flags=re.DOTALL | re.IGNORECASE)
print(f"Found {len(scripts)} script tags")
for i, s in enumerate(scripts):
    print(f"Script {i+1} length: {len(s)}")
