import os

theme_script = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_shopify_theme.py"
with open(theme_script, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    ("13 Exclusive Designs", "16 Exclusive Designs"),
    ("39 Pieces Total (M, L, XL)", "48 Pieces Total (M, L, XL)"),
    ("The Debut 13 Silhouettes", "The Debut 16 Silhouettes"),
    ('"default": 13', '"default": 16'),
]

for old, new in replacements:
    c = text.count(old)
    text = text.replace(old, new)
    print(f"Theme script: replaced '{old}' -> '{new}' ({c} times)")

with open(theme_script, "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: Updated build_shopify_theme.py")
