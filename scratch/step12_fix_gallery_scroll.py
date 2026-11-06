import os

# =========================================================================
# STEP 12: FIX GALLERY NEXT/PREV BUTTON UNWANTED DOWNWARD SCREEN SCROLL
# =========================================================================

# 1. Update sections/main-product.liquid and meenu-label-shopify-theme/sections/main-product.liquid
pdp_liquid_files = [
    "sections/main-product.liquid",
    "meenu-label-shopify-theme/sections/main-product.liquid"
]

old_fn = """  function changeShopifyGalleryImage(dir) {
    if (!shopifyGalleryImages || shopifyGalleryImages.length <= 1) return;
    var nextIdx = currentShopifyGalleryIndex + dir;
    if (nextIdx < 0) nextIdx = shopifyGalleryImages.length - 1;
    if (nextIdx >= shopifyGalleryImages.length) nextIdx = 0;

    var thumbs = document.querySelectorAll('.pdp-thumb-item');
    if (thumbs[nextIdx]) {
      selectShopifyGalleryImage(thumbs[nextIdx], shopifyGalleryImages[nextIdx], nextIdx);
      thumbs[nextIdx].scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }
  }"""

new_fn = """  function changeShopifyGalleryImage(dir, e) {
    if (e && e.preventDefault) e.preventDefault();
    if (!shopifyGalleryImages || shopifyGalleryImages.length <= 1) return;
    var nextIdx = currentShopifyGalleryIndex + dir;
    if (nextIdx < 0) nextIdx = shopifyGalleryImages.length - 1;
    if (nextIdx >= shopifyGalleryImages.length) nextIdx = 0;

    var thumbs = document.querySelectorAll('.pdp-thumb-item');
    if (thumbs[nextIdx]) {
      selectShopifyGalleryImage(thumbs[nextIdx], shopifyGalleryImages[nextIdx], nextIdx);
      
      // Scroll ONLY the thumbnails rail horizontally without scrolling the main window/page
      var rail = document.getElementById('shopifyPdpThumbs');
      if (rail) {
        var thumb = thumbs[nextIdx];
        var scrollLeftTarget = thumb.offsetLeft - (rail.clientWidth / 2) + (thumb.clientWidth / 2);
        rail.scrollTo({ left: scrollLeftTarget, behavior: 'smooth' });
      }
    }
  }"""

old_btn_prev = '<button type="button" class="pdp-gallery-arrow pdp-gallery-prev" onclick="changeShopifyGalleryImage(-1)" aria-label="Previous photo">'
new_btn_prev = '<button type="button" class="pdp-gallery-arrow pdp-gallery-prev" onclick="event.preventDefault(); changeShopifyGalleryImage(-1, event)" aria-label="Previous photo">'

old_btn_next = '<button type="button" class="pdp-gallery-arrow pdp-gallery-next" onclick="changeShopifyGalleryImage(1)" aria-label="Next photo">'
new_btn_next = '<button type="button" class="pdp-gallery-arrow pdp-gallery-next" onclick="event.preventDefault(); changeShopifyGalleryImage(1, event)" aria-label="Next photo">'

for p_file in pdp_liquid_files:
    if os.path.exists(p_file):
        with open(p_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        if old_fn in content:
            content = content.replace(old_fn, new_fn, 1)
            print(f"Replaced changeShopifyGalleryImage in {p_file}")
        else:
            print(f"WARNING: old_fn not found in {p_file}")
            
        if old_btn_prev in content:
            content = content.replace(old_btn_prev, new_btn_prev, 1)
            print(f"Updated pdp-gallery-prev in {p_file}")
        if old_btn_next in content:
            content = content.replace(old_btn_next, new_btn_next, 1)
            print(f"Updated pdp-gallery-next in {p_file}")
            
        with open(p_file, "w", encoding="utf-8") as f:
            f.write(content)


# 2. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

old_idx_prev = '<button type="button" class="shopify-gallery-arrow shopify-gallery-prev" onclick="changePreviewGalleryImage(-1)"'
new_idx_prev = '<button type="button" class="shopify-gallery-arrow shopify-gallery-prev" onclick="event.preventDefault(); changePreviewGalleryImage(-1, event)"'

old_idx_next = '<button type="button" class="shopify-gallery-arrow shopify-gallery-next" onclick="changePreviewGalleryImage(1)"'
new_idx_next = '<button type="button" class="shopify-gallery-arrow shopify-gallery-next" onclick="event.preventDefault(); changePreviewGalleryImage(1, event)"'

if old_idx_prev in idx_content:
    idx_content = idx_content.replace(old_idx_prev, new_idx_prev, 1)
    print("Updated shopify-gallery-prev in index.html")
if old_idx_next in idx_content:
    idx_content = idx_content.replace(old_idx_next, new_idx_next, 1)
    print("Updated shopify-gallery-next in index.html")

# Update selectPreviewImage in index.html to also scroll rail safely
old_idx_sel = """      var counter = document.getElementById('pdpCounterPill');
      if (counter && previewPdpImages.length > 1) {
        counter.textContent = (idx + 1) + ' / ' + previewPdpImages.length;
      }
    }"""

new_idx_sel = """      var counter = document.getElementById('pdpCounterPill');
      if (counter && previewPdpImages.length > 1) {
        counter.textContent = (idx + 1) + ' / ' + previewPdpImages.length;
      }
      var rail = document.getElementById('pdpThumbnailsRail');
      if (rail && btns[idx]) {
        var scrollLeftTarget = btns[idx].offsetLeft - (rail.clientWidth / 2) + (btns[idx].clientWidth / 2);
        rail.scrollTo({ left: scrollLeftTarget, behavior: 'smooth' });
      }
    }"""

if old_idx_sel in idx_content:
    idx_content = idx_content.replace(old_idx_sel, new_idx_sel, 1)
    print("Updated selectPreviewImage in index.html with safe rail scrolling")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

print("\nStep 12 updates successfully completed!")
