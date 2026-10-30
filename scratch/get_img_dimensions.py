from PIL import Image
import base64
import io
import re
import json

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const productsData\s*=\s*(\[.*?\]);', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    for i, prod in enumerate(data[:3]):
        b64_str = prod['b64']
        if ',' in b64_str:
            b64_str = b64_str.split(',', 1)[1]
        raw = base64.b64decode(b64_str)
        img = Image.open(io.BytesIO(raw))
        print(f"Product {i} ({prod['id']}): {img.size[0]} x {img.size[1]} px, aspect ratio: {img.size[0] / img.size[1]:.3f} (H/W: {img.size[1]/img.size[0]:.3f})")
else:
    print("productsData not found")
