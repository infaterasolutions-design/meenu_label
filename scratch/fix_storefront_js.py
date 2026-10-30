with open('scratch/storefront_script_0.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the problematic line 163 and 164
target1 = """html += '<button onclick="quickAddCart(\'\' + p.id + \'\', \'M\'); toggleWishlistProduct(\'\' + p.id + \'\');" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';"""
rep1 = """html += '<button data-pid="' + p.id + '" onclick="quickAddCart(this.dataset.pid, \\'M\\'); toggleWishlistProduct(this.dataset.pid);" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';"""

target2 = """html += '<button onclick="toggleWishlistProduct(\'\' + p.id + \'\')" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';"""
rep2 = """html += '<button data-pid="' + p.id + '" onclick="toggleWishlistProduct(this.dataset.pid)" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';"""

print("target1 in js:", target1 in js)
print("target2 in js:", target2 in js)

if target1 in js:
    js = js.replace(target1, rep1)
if target2 in js:
    js = js.replace(target2, rep2)

with open('scratch/storefront_script_0_fixed.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Saved scratch/storefront_script_0_fixed.js")
