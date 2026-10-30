with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
slides = re.findall(r'<div class="snitch-slide" style="background-image: url\(\'data:image\/([^;]+);base64,([^\']+)\'\);"', html)
print(f"Found {len(slides)} slides in storefront HTML:")
for i, (fmt, b64) in enumerate(slides):
    print(f"Slide {i+1}: format={fmt}, length={len(b64)}")
