with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the broken lines in build_snitch_storefront.py
# In build_snitch_storefront.py, the lines were:
# html += '<button onclick="quickAddCart(\'' + p.id + '\', \'M\'); toggleWishlistProduct(\'' + p.id + '\');" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';
# html += '<button onclick="toggleWishlistProduct(\'' + p.id + '\')" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';

# We replace with clean data-pid attribute:
old_btn1 = """html += '<button onclick="quickAddCart(\\'' + p.id + '\\', \\'M\\'); toggleWishlistProduct(\\'' + p.id + '\\');" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';"""
new_btn1 = """html += '<button data-pid="' + p.id + '" onclick="moveWishlistToCart(this.dataset.pid)" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';"""

old_btn2 = """html += '<button onclick="toggleWishlistProduct(\\'' + p.id + '\\')" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';"""
new_btn2 = """html += '<button data-pid="' + p.id + '" onclick="toggleWishlistProduct(this.dataset.pid)" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';"""

print("old_btn1 in code:", old_btn1 in code)
print("old_btn2 in code:", old_btn2 in code)

if old_btn1 in code:
    code = code.replace(old_btn1, new_btn1)
else:
    # Substring search
    pos = code.find('quickAddCart')
    while pos != -1:
        chunk = code[pos-30:pos+250]
        if 'MOVE TO BAG' in chunk:
            print("Found MOVE TO BAG chunk:", chunk)
            code = code[:pos-30] + new_btn1 + code[pos+chunk.find(';</button>')+10:]
            break
        pos = code.find('quickAddCart', pos+200)

if old_btn2 in code:
    code = code.replace(old_btn2, new_btn2)
else:
    pos = code.find('toggleWishlistProduct')
    while pos != -1:
        chunk = code[pos-30:pos+200]
        if 'Remove</button>' in chunk:
            print("Found Remove button chunk:", chunk)
            line_start = code.rfind('html +=', 0, pos)
            line_end = code.find(';', pos) + 1
            code = code[:line_start] + new_btn2 + code[line_end:]
            break
        pos = code.find('toggleWishlistProduct', pos+200)

# Add moveWishlistToCart helper function
if 'function moveWishlistToCart' not in code:
    helper = """
    function moveWishlistToCart(pid) {{
      quickAddCart(pid, 'M');
      toggleWishlistProduct(pid);
    }}
"""
    ins_pos = code.find('function updateWishlistUI()')
    if ins_pos != -1:
        code = code[:ins_pos] + helper + "\n    " + code[ins_pos:]
        print("Added moveWishlistToCart function")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_snitch_storefront.py successfully.")
