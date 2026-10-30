from PIL import Image
import base64
import io
import re

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'data:image/webp;base64,([^"\']+)', text)
if m:
    data = base64.b64decode(m.group(1))
    im = Image.open(io.BytesIO(data))
    print(f'Original image size: {im.size[0]} x {im.size[1]}, aspect: {im.size[0]/im.size[1]:.3f}')
