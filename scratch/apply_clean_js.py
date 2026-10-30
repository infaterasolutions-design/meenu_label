import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted.js", "r", encoding="utf-8") as f:
    clean_js = f.read()

# Replace the content of the script tag
script_match = re.search(r"<script[^>]*>(.*?)</script>", html, flags=re.DOTALL | re.IGNORECASE)
if script_match:
    start = script_match.start(1)
    end = script_match.end(1)
    new_html = html[:start] + clean_js + html[end:]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("SUCCESS: Storefront HTML script replaced with 100% valid JavaScript!")
else:
    print("ERROR: Could not find script tag in HTML")
