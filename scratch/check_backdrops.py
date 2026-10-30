import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# Check for any element with class containing 'backdrop' and 'open'
matches = re.findall(r'<[^>]*class=[\'"][^\'"]*backdrop[^\'"]*open[^\'"]*[\'"][^>]*>', text)
print("Open backdrops found in HTML:", matches)

# Check for any unclosed divs or syntax
open_divs = len(re.findall(r'<div\b', text, re.I))
close_divs = len(re.findall(r'</div>', text, re.I))
print(f"Total <div: {open_divs}, Total </div: {close_divs}")
