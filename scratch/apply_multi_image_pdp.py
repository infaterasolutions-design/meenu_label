import re

liquid_content = '''<section class="shopify-product-layout">
  <!-- Left Column: Multi-Image Product Gallery -->
  <div class="shopify-pdp-gallery-col">
    <!-- Main Showcase Image Container -->
    <div class="shopify-pdp-main-image-wrap" id="shopifyPdpMainWrap">
      <div class="shopify-pdp-badges">
        <span class="pdp-atelier-badge">HANDCRAFTED PREVIEW</span>
        {% if product.images.size > 1 %}
          <span class="pdp-image-counter" id="shopifyImageCounter">1 / {{ product.images.size }}</span>
        {% endif %}
      </div>

      {% if product.images.size > 0 %}
        <img id="shopifyMainImg" 
             src="{{ product.featured_image | default: product.images.first | image_url: width: 1200 }}" 
             alt="{{ product.title | escape }}" 
             loading="eager"
             onclick="openShopifyLightbox(this.src)"
             title="Click to view high-resolution zoom">
      {% else %}
        <div class="shopify-img-placeholder">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          <span class="placeholder-title">{{ product.title }}</span>
          <span class="placeholder-sub">Handcrafted Edition &bull; Awaiting Photography</span>
        </div>
      {% endif %}

      {% if product.images.size > 1 %}
        <!-- Prev & Next Navigation Arrows -->
        <button type="button" class="shopify-gallery-arrow shopify-gallery-prev" onclick="changeShopifyGalleryImage(-1)" aria-label="Previous photo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <button type="button" class="shopify-gallery-arrow shopify-gallery-next" onclick="changeShopifyGalleryImage(1)" aria-label="Next photo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      {% endif %}
    </div>

    <!-- Multi-Image Interactive Thumbnails Rail -->
    {% if product.images.size > 1 %}
      <div class="shopify-pdp-thumbnails" id="shopifyPdpThumbs">
        {% for image in product.images %}
          <button type="button" 
                  class="shopify-thumb-btn {% if forloop.first %}active{% endif %}" 
                  data-index="{{ forloop.index0 }}"
                  data-src="{{ image | image_url: width: 1200 }}"
                  onclick="selectShopifyGalleryImage(this, '{{ image | image_url: width: 1200 }}', {{ forloop.index0 }})"
                  aria-label="View photo {{ forloop.index }} of {{ product.images.size }}">
            <img src="{{ image | image_url: width: 220, height: 275, crop: 'center' }}" 
                 alt="{{ image.alt | default: product.title | escape }}" 
                 loading="lazy">
          </button>
        {% endfor %}
      </div>
    {% endif %}

    <!-- Atelier Craftsmanship Guarantees -->
    <div class="shopify-pdp-trust-grid">
      <div class="trust-tile">
        <span class="trust-icon">&#10024;</span>
        <strong>Chandigarh Atelier</strong>
        <small>Handcrafted Precision</small>
      </div>
      <div class="trust-tile">
        <span class="trust-icon">&#128666;</span>
        <strong>Tricity 24-Hr</strong>
        <small>Complimentary Courier</small>
      </div>
      <div class="trust-tile">
        <span class="trust-icon">&#128207;</span>
        <strong>Custom Alterations</strong>
        <small>Bespoke Hem & Fitting</small>
      </div>
    </div>
  </div>

  <!-- Right Column: Product Details & Purchase Form -->
  <div class="shopify-pdp-info-col">
    <span style="font-size: 11px; font-weight: 700; color: var(--accent-rose, #C95D63); letter-spacing: 0.1em; text-transform: uppercase;">
      &#128293; ONLY 1 PIECE LEFT PER SIZE
    </span>
    <h1 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 38px; font-weight: 600; margin: 8px 0 4px; line-height: 1.2;">{{ product.title }}</h1>
    <div style="font-size: 12px; color: var(--text-muted, #7A7269); margin-bottom: 16px;">SKU: {{ product.selected_or_first_available_variant.sku | default: 'MEENU-DROP01' }}</div>

    <div style="display: flex; align-items: baseline; gap: 12px; padding: 14px 0; border-top: 1px solid var(--border-color, #E8E2D9); border-bottom: 1px solid var(--border-color, #E8E2D9); margin-bottom: 24px;">
      <span style="font-size: 26px; font-weight: 700; color: var(--text-main, #1A1A1A); font-variant-numeric: lining-nums;">{{ product.price | money }}</span>
      {% if product.compare_at_price > product.price %}
        <span style="font-size: 16px; text-decoration: line-through; color: var(--text-muted, #7A7269); font-variant-numeric: lining-nums;">{{ product.compare_at_price | money }}</span>
        <span style="font-size: 11px; font-weight: 700; color: var(--accent-green, #2E7D32); background: #EBF7EE; padding: 3px 8px; border-radius: 4px;">SAVINGS INCLUDED</span>
      {% endif %}
    </div>

    <!-- Size Selector (NO DEFAULT SELECTION) -->
    <div class="shopify-size-section" id="shopifySizeSection" style="margin-bottom: 20px;">
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 12px; font-weight: 700;">
        <span>SELECT SIZE (INDIAN BUST MEASUREMENTS) <span id="shopifySelectedSizeLabel" style="display:none; color:var(--accent-burgundy,#6E1A24); font-weight:700; margin-left:6px;"></span></span>
        <a href="javascript:void(0)" onclick="openSizeGuideModal()" style="color: var(--accent-gold, #C5A059); text-decoration: none;">&#128207; Size Chart</a>
      </div>
      <div id="shopifySizeGrid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
        {% for variant in product.variants %}
          <button type="button" 
                  class="shopify-size-tile" 
                  data-variant-id="{{ variant.id }}" 
                  data-size-title="{{ variant.title }}" 
                  {% if variant.featured_image %}data-variant-image="{{ variant.featured_image | image_url: width: 1200 }}"{% elsif variant.image %}data-variant-image="{{ variant.image | image_url: width: 1200 }}"{% endif %}
                  onclick="selectShopifyVariant('{{ variant.id }}', '{{ variant.title }}', this)" 
                  style="background: #FFFFFF; border: 1.5px solid var(--border-color, #E8E2D9); padding: 10px; border-radius: 6px; text-align: center; cursor: pointer; transition: all 0.2s ease;">
            <strong style="display:block; font-size: 14px;">{{ variant.title }}</strong>
            <span style="display:block; font-size: 10px; color: var(--accent-rose, #C95D63); font-weight:700; text-transform:uppercase;">Only 1 Left!</span>
          </button>
        {% endfor %}
      </div>
      <div id="shopifySizeRequiredNotice" style="display:none; color:#B91C1C; background:#FEF2F2; border:1px solid #FCA5A5; border-radius:6px; padding:10px 14px; font-size:12px; font-weight:600; text-align:center; margin-top:8px;">
        &#9888;&#65039; Please select your size (M, L, or XL) before adding to bag
      </div>
    </div>

    <!-- Pincode Checker -->
    <div style="background: #FAF5ED; padding: 14px; border-radius: 8px; margin-bottom: 24px; border: 1px solid var(--border-color, #E8E2D9);">
      <div style="font-size: 12px; font-weight: 700; margin-bottom: 6px;">&#128205; Check Tricity Express Delivery</div>
      <div style="display: flex; gap: 8px;">
        <input type="text" id="pdpPincode" placeholder="Enter 6-digit Pincode" maxlength="6" style="padding: 8px 12px; border: 1px solid var(--border-color, #E8E2D9); border-radius: 4px; flex: 1;">
        <button type="button" class="btn-primary" style="padding: 8px 14px; font-size: 12px;" onclick="checkTricityPincode(document.getElementById('pdpPincode').value)">Check</button>
      </div>
      <div id="PincodeResult" style="font-size: 12px; margin-top: 6px; font-weight: 600;"></div>
    </div>

    <!-- Shopify Product Form -->
    {% form 'product', product, id: 'shopifyProductForm', onsubmit: 'return validateShopifyForm(event)' %}
      <input type="hidden" name="id" id="selectedVariantId" value="">
      <button type="submit" id="pdpAddToCartBtn" class="btn-primary" style="width: 100%; padding: 16px; margin-bottom: 10px; cursor: pointer; font-size: 13px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">ADD TO BAG &#128717;&#65039;</button>
    {% endform %}

    <!-- Save to Wishlist Button -->
    <button type="button" id="pdpWishlistBtn" class="pdp-wishlist-toggle" 
      data-wishlist-id="{{ product.id | default: 'drop01_1' }}" 
      data-wishlist-title="{{ product.title | escape }}" 
      data-wishlist-price="{{ product.price | money | escape }}" 
      data-wishlist-image="{{ product.featured_image | default: product.images.first | image_url: width: 300 }}" 
      data-wishlist-url="{{ product.url }}" 
      onclick="toggleWishlist(this)" 
      style="width: 100%; background: #FFFFFF; border: 1.5px solid var(--border-color, #E8E2D9); padding: 12px; border-radius: 6px; font-weight: 700; font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 12px; transition: all 0.2s ease; color: var(--text-main, #1A1A1A);">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="width: 16px; height: 16px; pointer-events: none;">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="pdp-wishlist-txt">SAVE TO WISHLIST</span>
    </button>

    <!-- Direct WhatsApp Order -->
    <a id="shopifyWhatsAppBtn" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001.%20Please%20help%20me%20choose%20the%20right%20size." target="_blank" style="display: block; text-align: center; background: #E8F5E9; color: #1B5E20; border: 1px solid #C8E6C9; padding: 13px; border-radius: 6px; font-weight: 700; text-decoration: none; font-size: 13px;">
      &#128172; Order Directly via WhatsApp
    </a>
    <div class="whatsapp-benefit-box" style="margin-top: 12px; background: #FAF7F2; border: 1px solid var(--border-color, #E8E2D9); border-radius: 8px; padding: 12px; display: flex; gap: 10px; font-size: 11px; color: var(--text-muted, #7A7269); line-height: 1.5;">
      <span class="wa-icon" style="font-size: 16px;">&#128172;</span>
      <div>
        <strong style="color: var(--text-main, #1A1A1A); display: block; margin-bottom: 2px;">Shoppers with size doubts or customization questions:</strong>
        Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
      </div>
    </div>
  </div>
</section>

<!-- High-Resolution Lightbox Zoom Modal -->
<div id="shopifyLightboxModal" class="shopify-lightbox-modal" onclick="closeShopifyLightbox()">
  <button type="button" class="shopify-lightbox-close" onclick="closeShopifyLightbox()" aria-label="Close high-resolution zoom">&times;</button>
  <img id="shopifyLightboxImg" src="" alt="{{ product.title | escape }}" onclick="event.stopPropagation()">
</div>

<style>
  .shopify-product-layout {
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 40px;
    display: grid;
    grid-template-columns: 1.05fr 1fr;
    gap: 50px;
    align-items: start;
  }
  @media (max-width: 900px) {
    .shopify-product-layout {
      grid-template-columns: 1fr;
      gap: 32px;
      padding: 0 20px;
      margin: 20px auto;
    }
  }

  /* Gallery Column */
  .shopify-pdp-gallery-col {
    position: -webkit-sticky;
    position: sticky;
    top: 115px;
    align-self: start;
    z-index: 20;
  }
  @media (max-width: 900px) {
    .shopify-pdp-gallery-col {
      position: relative !important;
      top: 0 !important;
    }
  }

  /* Main Showcase Wrap */
  .shopify-pdp-main-image-wrap {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border-color, #E8E2D9);
    background: #F4EFEB;
    aspect-ratio: 4 / 5;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  }
  .shopify-pdp-main-image-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    display: block;
    cursor: zoom-in;
    transition: opacity 0.22s ease;
  }

  /* Badges */
  .shopify-pdp-badges {
    position: absolute;
    top: 14px;
    left: 14px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    z-index: 5;
    pointer-events: none;
  }
  .pdp-atelier-badge {
    background: rgba(26, 26, 26, 0.88);
    backdrop-filter: blur(8px);
    color: #FFFFFF;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 20px;
    width: fit-content;
  }
  .pdp-image-counter {
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(8px);
    color: #1A1A1A;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.08em;
    padding: 3px 8px;
    border-radius: 20px;
    width: fit-content;
    border: 1px solid rgba(0, 0, 0, 0.06);
  }

  /* Arrow Controls */
  .shopify-gallery-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(0, 0, 0, 0.08);
    color: #1A1A1A;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
  }
  .shopify-gallery-arrow:hover {
    background: #FFFFFF;
    color: var(--accent-burgundy, #6E1A24);
    transform: translateY(-50%) scale(1.08);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.14);
  }
  .shopify-gallery-arrow svg {
    width: 18px;
    height: 18px;
  }
  .shopify-gallery-prev {
    left: 14px;
  }
  .shopify-gallery-next {
    right: 14px;
  }

  /* Multi-Image Thumbnails Rail */
  .shopify-pdp-thumbnails {
    display: flex;
    gap: 10px;
    margin-top: 14px;
    overflow-x: auto;
    scrollbar-width: thin;
    padding-bottom: 4px;
    -webkit-overflow-scrolling: touch;
  }
  .shopify-pdp-thumbnails::-webkit-scrollbar {
    height: 4px;
  }
  .shopify-pdp-thumbnails::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.15);
    border-radius: 4px;
  }
  .shopify-thumb-btn {
    flex: 0 0 74px;
    width: 74px;
    aspect-ratio: 4 / 5;
    border-radius: 8px;
    overflow: hidden;
    border: 2px solid transparent;
    padding: 0;
    background: #F4EFEB;
    cursor: pointer;
    transition: all 0.2s ease;
    opacity: 0.6;
  }
  .shopify-thumb-btn:hover {
    opacity: 0.95;
    border-color: rgba(110, 26, 36, 0.3);
  }
  .shopify-thumb-btn.active {
    opacity: 1;
    border-color: var(--accent-burgundy, #6E1A24);
    box-shadow: 0 0 0 1px var(--accent-burgundy, #6E1A24);
    transform: translateY(-1px);
  }
  .shopify-thumb-btn img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    display: block;
  }

  /* Placeholder */
  .shopify-img-placeholder {
    width: 100%;
    height: 100%;
    min-height: 480px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #8C827A;
    background: #FAF5ED;
    padding: 30px;
    text-align: center;
  }
  .shopify-img-placeholder svg {
    width: 48px;
    height: 48px;
    margin-bottom: 12px;
    opacity: 0.5;
  }
  .shopify-img-placeholder .placeholder-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 22px;
    font-weight: 600;
    color: #1A1A1A;
    margin-bottom: 4px;
  }
  .shopify-img-placeholder .placeholder-sub {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  /* Trust Grid */
  .shopify-pdp-trust-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-top: 16px;
    text-align: center;
  }
  .shopify-pdp-trust-grid .trust-tile {
    background: #FAF7F2;
    border: 1px solid var(--border-color, #E8E2D9);
    padding: 10px 6px;
    border-radius: 8px;
  }
  .shopify-pdp-trust-grid .trust-icon {
    font-size: 16px;
    display: block;
    margin-bottom: 2px;
  }
  .shopify-pdp-trust-grid strong {
    font-size: 11px;
    display: block;
    color: var(--text-main, #1A1A1A);
  }
  .shopify-pdp-trust-grid small {
    font-size: 10px;
    color: var(--text-muted, #7A7269);
  }

  /* Lightbox Zoom Modal */
  .shopify-lightbox-modal {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(15, 14, 12, 0.94);
    backdrop-filter: blur(12px);
    z-index: 99999;
    align-items: center;
    justify-content: center;
    padding: 24px;
    cursor: zoom-out;
  }
  .shopify-lightbox-modal.open {
    display: flex;
  }
  .shopify-lightbox-modal img {
    max-width: 90vw;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    cursor: default;
    animation: shopifyZoomIn 0.22s ease-out;
  }
  .shopify-lightbox-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #FFFFFF;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    font-size: 26px;
    line-height: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s;
  }
  .shopify-lightbox-close:hover {
    background: rgba(255, 255, 255, 0.35);
    transform: scale(1.08);
  }
  @keyframes shopifyZoomIn {
    from { opacity: 0; transform: scale(0.93); }
    to { opacity: 1; transform: scale(1); }
  }

  /* Size Selector Styles */
  .shopify-size-tile.selected {
    background: var(--text-main, #1A1A1A) !important;
    border-color: var(--text-main, #1A1A1A) !important;
    color: #FFFFFF !important;
  }
  .shopify-size-tile.selected strong {
    color: #FFFFFF !important;
  }
  .shopify-size-tile.selected span {
    color: #FFD54F !important;
  }
  @keyframes sizeTileShake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-6px); }
    40%, 80% { transform: translateX(6px); }
  }
  .size-error-shake {
    animation: sizeTileShake 0.4s ease-in-out;
    outline: 2px solid #E53935 !important;
    border-radius: 8px;
  }
</style>

<script>
  var currentSelectedVariantId = null;
  var currentSelectedSizeTitle = null;

  var shopifyGalleryImages = [
    {% for image in product.images %}
      {{ image | image_url: width: 1200 | json }}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
  var currentShopifyGalleryIndex = 0;

  function selectShopifyGalleryImage(btn, src, index) {
    var mainImg = document.getElementById('shopifyMainImg');
    if (mainImg) {
      mainImg.style.opacity = '0.35';
      setTimeout(function() {
        mainImg.src = src;
        mainImg.style.opacity = '1';
      }, 100);
    }

    currentShopifyGalleryIndex = index;

    var allThumbs = document.querySelectorAll('.shopify-thumb-btn');
    allThumbs.forEach(function(t) { t.classList.remove('active'); });
    if (btn) btn.classList.add('active');

    var counter = document.getElementById('shopifyImageCounter');
    if (counter && shopifyGalleryImages.length > 1) {
      counter.textContent = (currentShopifyGalleryIndex + 1) + ' / ' + shopifyGalleryImages.length;
    }
  }

  function changeShopifyGalleryImage(dir) {
    if (!shopifyGalleryImages || shopifyGalleryImages.length <= 1) return;
    var nextIdx = currentShopifyGalleryIndex + dir;
    if (nextIdx < 0) nextIdx = shopifyGalleryImages.length - 1;
    if (nextIdx >= shopifyGalleryImages.length) nextIdx = 0;

    var thumbs = document.querySelectorAll('.shopify-thumb-btn');
    if (thumbs[nextIdx]) {
      selectShopifyGalleryImage(thumbs[nextIdx], shopifyGalleryImages[nextIdx], nextIdx);
      thumbs[nextIdx].scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    }
  }

  function openShopifyLightbox(src) {
    var modal = document.getElementById('shopifyLightboxModal');
    var img = document.getElementById('shopifyLightboxImg');
    if (modal && img) {
      img.src = src;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeShopifyLightbox() {
    var modal = document.getElementById('shopifyLightboxModal');
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  // Keyboard navigation for gallery & lightbox
  window.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      closeShopifyLightbox();
    } else if (e.key === 'ArrowLeft') {
      changeShopifyGalleryImage(-1);
    } else if (e.key === 'ArrowRight') {
      changeShopifyGalleryImage(1);
    }
  });

  // Touch Swipe on Main Image Container
  (function() {
    var wrap = document.getElementById('shopifyPdpMainWrap');
    if (!wrap) return;
    var touchStartX = 0;
    var touchEndX = 0;
    wrap.addEventListener('touchstart', function(e) {
      if (e.changedTouches && e.changedTouches.length > 0) {
        touchStartX = e.changedTouches[0].screenX;
      }
    }, { passive: true });
    wrap.addEventListener('touchend', function(e) {
      if (e.changedTouches && e.changedTouches.length > 0) {
        touchEndX = e.changedTouches[0].screenX;
        var diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 40) {
          if (diff > 0) {
            changeShopifyGalleryImage(1);
          } else {
            changeShopifyGalleryImage(-1);
          }
        }
      }
    }, { passive: true });
  })();

  function selectShopifyVariant(variantId, sizeTitle, btn) {
    currentSelectedVariantId = variantId;
    currentSelectedSizeTitle = sizeTitle;
    var inp = document.getElementById('selectedVariantId');
    if (inp) inp.value = variantId;

    var tiles = document.querySelectorAll('.shopify-size-tile');
    tiles.forEach(function(t) { t.classList.remove('selected'); });
    if (btn) btn.classList.add('selected');

    // If variant has assigned image, switch gallery to it
    if (btn) {
      var varImg = btn.getAttribute('data-variant-image');
      if (varImg) {
        var matchThumb = document.querySelector('.shopify-thumb-btn[data-src="' + varImg + '"]');
        if (matchThumb) {
          matchThumb.click();
        }
      }
    }

    var notice = document.getElementById('shopifySizeRequiredNotice');
    if (notice) notice.style.display = 'none';

    var sec = document.getElementById('shopifySizeGrid');
    if (sec) sec.classList.remove('size-error-shake');

    var lbl = document.getElementById('shopifySelectedSizeLabel');
    if (lbl) {
      lbl.textContent = '— Size ' + sizeTitle + ' Selected';
      lbl.style.display = 'inline';
    }

    var waBtn = document.getElementById('shopifyWhatsAppBtn');
    if (waBtn) {
      var prodTitle = {{ product.title | json }};
      var text = encodeURIComponent('Hi Meenu Label! I would like to order "' + prodTitle + '" in Size ' + sizeTitle + ' from Drop 01. Please confirm piece reservation.');
      waBtn.href = 'https://wa.me/{{ settings.whatsapp_number | default: "919988898845" }}?text=' + text;
    }
  }

  function validateShopifyForm(e) {
    if (!currentSelectedVariantId) {
      if (e) e.preventDefault();
      var notice = document.getElementById('shopifySizeRequiredNotice');
      if (notice) notice.style.display = 'block';

      var sec = document.getElementById('shopifySizeGrid');
      if (sec) {
        sec.classList.remove('size-error-shake');
        void sec.offsetWidth;
        sec.classList.add('size-error-shake');
        setTimeout(function() { sec.classList.remove('size-error-shake'); }, 1200);
        sec.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      return false;
    }

    if (e) e.preventDefault();
    var btn = document.getElementById('pdpAddToCartBtn');
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = 'ADDING TO BAG...';
    }

    fetch('/cart/add.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        items: [{
          id: currentSelectedVariantId,
          quantity: 1
        }]
      })
    })
    .then(function() {
      window.location.href = '/cart';
    })
    .catch(function(err) {
      console.warn('Cart add notice:', err);
      var form = document.getElementById('shopifyProductForm');
      if (form) {
        form.submit();
      } else {
        window.location.href = '/cart';
      }
    });

    return false;
  }
</script>

{% schema %}
{
  "name": "Product Main",
  "settings": []
}
{% endschema %}
'''

with open('sections/main-product.liquid', 'w', encoding='utf-8') as f:
    f.write(liquid_content)

with open('meenu-label-shopify-theme/sections/main-product.liquid', 'w', encoding='utf-8') as f:
    f.write(liquid_content)

print("Updated sections/main-product.liquid in both root and subfolder successfully!")
