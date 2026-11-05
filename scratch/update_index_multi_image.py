with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update PDP wrap in index.html
old_pdp_wrap = '''          <div class="pdp-main-image-wrap">
            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">DROP 01 STAR</span>
              <span class="pdp-badge-pill pdp-badge-gold">STRICTLY 3 PIECES CRAFTED</span>
            </div>
            <button class="pdp-wishlist-toggle" id="pdpWishlistBtn" onclick="togglePdpWishlist()" title="Save to Wishlist" aria-label="Save to Wishlist">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </button>
            <img id="pdpMainImg" src="" alt="Silhouette" class="pdp-main-image">
          </div>'''

new_pdp_wrap = '''          <div class="pdp-main-image-wrap">
            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">DROP 01 STAR</span>
              <span class="pdp-badge-pill pdp-badge-gold" id="pdpCounterPill">STRICTLY 3 PIECES CRAFTED</span>
            </div>
            <button class="pdp-wishlist-toggle" id="pdpWishlistBtn" onclick="togglePdpWishlist()" title="Save to Wishlist" aria-label="Save to Wishlist">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </button>
            <img id="pdpMainImg" src="" alt="Silhouette" class="pdp-main-image">
            <button type="button" class="shopify-gallery-arrow shopify-gallery-prev" onclick="changePreviewGalleryImage(-1)" aria-label="Previous photo" style="display:none;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px;"><polyline points="15 18 9 12 15 6"></polyline></svg>
            </button>
            <button type="button" class="shopify-gallery-arrow shopify-gallery-next" onclick="changePreviewGalleryImage(1)" aria-label="Next photo" style="display:none;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px;"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
          </div>
          <!-- Multi-Image Thumbnails Rail -->
          <div class="shopify-pdp-thumbnails" id="pdpThumbnailsRail" style="display: none; gap: 8px; margin-top: 12px; overflow-x: auto; padding-bottom: 4px;">
          </div>'''

assert old_pdp_wrap in html, "old_pdp_wrap not found in index.html"
html = html.replace(old_pdp_wrap, new_pdp_wrap)

# 2. Add helper functions in JS
js_marker = "var activePdpProductId = null;"
js_gallery_helpers = '''var activePdpProductId = null;
    var previewPdpImages = [];
    var currentPreviewImgIndex = 0;

    function setPreviewGalleryImages(images) {
      previewPdpImages = (images && images.length) ? images : [];
      currentPreviewImgIndex = 0;
      var rail = document.getElementById('pdpThumbnailsRail');
      var prevBtn = document.querySelector('.pdp-main-image-wrap .shopify-gallery-prev');
      var nextBtn = document.querySelector('.pdp-main-image-wrap .shopify-gallery-next');
      var counter = document.getElementById('pdpCounterPill');

      if (rail) {
        if (previewPdpImages.length > 1) {
          rail.style.display = 'flex';
          rail.innerHTML = previewPdpImages.map(function(src, idx) {
            return '<button type="button" class="shopify-thumb-btn ' + (idx === 0 ? 'active' : '') + '" onclick="selectPreviewImage(' + idx + ')" style="flex:0 0 68px; width:68px; aspect-ratio:4/5; border-radius:6px; overflow:hidden; border:2px solid ' + (idx === 0 ? '#6E1A24' : 'transparent') + '; padding:0; background:#FAF5ED; cursor:pointer;"><img src="' + src + '" style="width:100%; height:100%; object-fit:cover; display:block;"></button>';
          }).join('');
          if (prevBtn) prevBtn.style.display = 'flex';
          if (nextBtn) nextBtn.style.display = 'flex';
          if (counter) counter.textContent = '1 / ' + previewPdpImages.length;
        } else {
          rail.style.display = 'none';
          rail.innerHTML = '';
          if (prevBtn) prevBtn.style.display = 'none';
          if (nextBtn) nextBtn.style.display = 'none';
          if (counter) counter.textContent = 'STRICTLY 3 PIECES CRAFTED';
        }
      }
    }

    function selectPreviewImage(idx) {
      if (!previewPdpImages || idx < 0 || idx >= previewPdpImages.length) return;
      currentPreviewImgIndex = idx;
      var mainImg = document.getElementById('pdpMainImg');
      if (mainImg) {
        mainImg.style.opacity = '0.35';
        setTimeout(function() {
          mainImg.src = previewPdpImages[idx];
          mainImg.style.opacity = '1';
        }, 100);
      }
      var btns = document.querySelectorAll('#pdpThumbnailsRail .shopify-thumb-btn');
      btns.forEach(function(b, i) {
        b.classList.toggle('active', i === idx);
        b.style.borderColor = (i === idx ? '#6E1A24' : 'transparent');
      });
      var counter = document.getElementById('pdpCounterPill');
      if (counter && previewPdpImages.length > 1) {
        counter.textContent = (idx + 1) + ' / ' + previewPdpImages.length;
      }
    }

    function changePreviewGalleryImage(dir) {
      if (!previewPdpImages || previewPdpImages.length <= 1) return;
      var nextIdx = currentPreviewImgIndex + dir;
      if (nextIdx < 0) nextIdx = previewPdpImages.length - 1;
      if (nextIdx >= previewPdpImages.length) nextIdx = 0;
      selectPreviewImage(nextIdx);
    }'''

assert js_marker in html, "js_marker not found in index.html"
html = html.replace(js_marker, js_gallery_helpers, 1)

# 3. Inside openProductPage(prodId), call setPreviewGalleryImages
img_set_marker = '''      var mainImg = document.getElementById('pdpMainImg');
      if (mainImg) {
        mainImg.src = p.b64;
        mainImg.alt = p.name;
      }'''

new_img_set = '''      var mainImg = document.getElementById('pdpMainImg');
      if (mainImg) {
        mainImg.src = p.b64;
        mainImg.alt = p.name;
      }
      // Populate multiple gallery images if present, or single image fallback
      var pImages = p.images || [p.b64];
      setPreviewGalleryImages(pImages);'''

assert img_set_marker in html, "img_set_marker not found in index.html"
html = html.replace(img_set_marker, new_img_set, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with multiple image gallery preview successfully!")
