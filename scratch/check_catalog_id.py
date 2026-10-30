with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

print('id="catalog" in code:', 'id="catalog"' in code)
pos = code.find('class="collection')
if pos != -1:
    print(code[pos-50:pos+250].encode('ascii', errors='replace').decode('ascii'))

# Let's search for id="..." around collection
import re
for m in re.finditer(r'<section[^>]*>', code):
    print(m.group(0).encode('ascii', errors='replace').decode('ascii'))
