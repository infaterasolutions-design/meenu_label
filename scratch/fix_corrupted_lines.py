import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix any corrupted "subif (totalEl) totalEl" occurrences
corrupted_pattern = r"if\s*\(subtotalEl\)\s*if\s*\(subtotalEl\)\s*subif\s*\(totalEl\)\s*totalEl\.textContent\s*=\s*'₹'\s*\+\s*subtotal\.toLocaleString\('en-IN'\);"
matches = re.findall(corrupted_pattern, text)
print("Found corrupted pattern matches:", len(matches))

fixed_line = "if (subtotalEl) subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');"
text = re.sub(corrupted_pattern, fixed_line, text)

# Also check for any other "subif" or malformed text
bad_tokens = re.findall(r"\w*subif\w*", text)
print("Bad tokens found:", bad_tokens)
for b in set(bad_tokens):
    text = text.replace(b, "subtotalEl")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: Cleaned up corrupted lines!")
