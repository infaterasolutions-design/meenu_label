import re

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for header and top promo in html
m = re.findall(r'<body[^>]*>([\s\S]{1,4000})', html)
if m:
    # remove base64
    clean = re.sub(r'data:image\/[^;]+;base64,[a-zA-Z0-9+/=]+', '...', m[0])
    print("BODY START:")
    print(clean[:2000])
