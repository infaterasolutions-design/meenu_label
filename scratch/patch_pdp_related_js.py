with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the related items generation block in build_snitch_storefront.py
old_block = """      related.forEach(function(r) {{
        var discount = Math.round(((r.mrp - r.price) / r.mrp) * 100);
        html += '<div class="product-card" onclick="openProductPage(\\'' + r.id + '\\')">';
        html += '<div class="card-thumb">';
        html += '<span class="card-badge ' + r.badge_class + '">' + r.badge + '</span>';
        html += '<button class="card-wishlist-btn" onclick="event.stopPropagation(); toggleWishlistProduct(\\'' + r.id + '\\')" title="Save to Wishlist">';
        html += '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        html += '</button>';
        html += '<img src="' + r.b64 + '" alt="' + r.name + '" loading="lazy">';
        html += '<div class="card-quick-actions">';
        html += '<button class="btn-quick-view" onclick="event.stopPropagation(); openQuickView(\\'' + r.id + '\\')">QUICK VIEW</button>';
        html += '</div>';
        html += '</div>';"""

new_block = """      related.forEach(function(r) {{
        var discount = Math.round(((r.mrp - r.price) / r.mrp) * 100);
        html += '<div class="product-card" data-pid="' + r.id + '" onclick="openProductPage(this.dataset.pid)">';
        html += '<div class="card-thumb">';
        html += '<span class="card-badge ' + r.badge_class + '">' + r.badge + '</span>';
        html += '<button class="card-wishlist-btn" data-pid="' + r.id + '" onclick="event.stopPropagation(); toggleWishlistProduct(this.dataset.pid)" title="Save to Wishlist">';
        html += '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        html += '</button>';
        html += '<img src="' + r.b64 + '" alt="' + r.name + '" loading="lazy">';
        html += '<div class="card-quick-actions">';
        html += '<button class="btn-quick-view" data-pid="' + r.id + '" onclick="event.stopPropagation(); openQuickView(this.dataset.pid)">QUICK VIEW</button>';
        html += '</div>';
        html += '</div>';"""

if old_block in text:
    text = text.replace(old_block, new_block)
    print("Replaced related items block successfully!")
else:
    print("Could not find exact old_block, searching substring...")
    pos = text.find('function populatePdpRelated')
    if pos != -1:
        end_pos = text.find('container.innerHTML = html;', pos)
        print("Function found, chunk:", text[pos:pos+400])
        # Replace inside this function
        chunk = text[pos:end_pos]
        chunk = chunk.replace("onclick=\"openProductPage(\\'\' + r.id + \'\\')\"", "data-pid=\"' + r.id + '\" onclick=\"openProductPage(this.dataset.pid)\"")
        chunk = chunk.replace("onclick=\"event.stopPropagation(); toggleWishlistProduct(\\'\' + r.id + \'\\')\"", "data-pid=\"' + r.id + '\" onclick=\"event.stopPropagation(); toggleWishlistProduct(this.dataset.pid)\"")
        chunk = chunk.replace("onclick=\"event.stopPropagation(); openQuickView(\\'\' + r.id + \'\\')\"", "data-pid=\"' + r.id + '\" onclick=\"event.stopPropagation(); openQuickView(this.dataset.pid)\"")
        text = text[:pos] + chunk + text[end_pos:]
        print("Replaced using substring inside populatePdpRelated")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved scratch/build_snitch_storefront.py")
