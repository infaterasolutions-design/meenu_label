import sys
sys.stdout.reconfigure(encoding='utf-8')

# -------------------------------------------------------------
# 1. Update index.html
# -------------------------------------------------------------
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

# A. Remove 'selected' from size M button in HTML
old_m_btn = '<button type="button" class="pdp-size-btn selected" id="pdpSizeBtn_M" onclick="selectPdpSize(\'M\', this)">'
new_m_btn = '<button type="button" class="pdp-size-btn" id="pdpSizeBtn_M" onclick="selectPdpSize(\'M\', this)">'

if old_m_btn in h:
    h = h.replace(old_m_btn, new_m_btn)
    print("Removed hardcoded 'selected' from pdpSizeBtn_M in index.html")
else:
    print("Hardcoded selected not found on pdpSizeBtn_M")

# B. Add pdpSizeNotice banner inside pdp-size-section
old_pills_end = """              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
          </div>"""

new_pills_end = """              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
            <div id="pdpSizeNotice" style="display:none; color:#B91C1C; background:#FEF2F2; border:1px solid #FCA5A5; border-radius:6px; padding:10px 14px; font-size:12px; font-weight:600; text-align:center; margin-top:8px;">
              &#9888;&#65039; Please select your size (M, L, or XL) before adding to bag
            </div>
          </div>"""

if old_pills_end in h:
    h = h.replace(old_pills_end, new_pills_end)
    print("Added pdpSizeNotice to index.html")
else:
    print("old_pills_end not found in index.html")

# C. Update PDP JavaScript logic in index.html
old_pdp_js_start = "    var activePdpProductId = null;\n    var pdpSelectedSize = 'M';"
new_pdp_js_start = "    var activePdpProductId = null;\n    var pdpSelectedSize = null;\n    var savedHomeScrollY = 0;"

if old_pdp_js_start in h:
    h = h.replace(old_pdp_js_start, new_pdp_js_start)
    print("Updated activePdpProductId and pdpSelectedSize in index.html")
else:
    print("old_pdp_js_start not found in index.html")

# In openProductPage: save scroll and don't default select size M
old_open_pdp = """    function openProductPage(prodId) {
      var p = productsData.find(function(item) { return item.id === prodId; });
      if (!p) return;

      activePdpProductId = prodId;
      pdpSelectedSize = 'M';"""

new_open_pdp = """    function openProductPage(prodId) {
      var p = productsData.find(function(item) { return item.id === prodId; });
      if (!p) return;

      // Save exact scroll position before switching views
      savedHomeScrollY = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
      try {
        sessionStorage.setItem('meenu_home_scroll', savedHomeScrollY);
      } catch(e) {}

      activePdpProductId = prodId;
      pdpSelectedSize = null;"""

if old_open_pdp in h:
    h = h.replace(old_open_pdp, new_open_pdp)
    print("Updated openProductPage start in index.html")
else:
    print("old_open_pdp not found in index.html")

# Remove default size selection at end of openProductPage
old_default_size = """      // Size buttons default selection (pick first available or M)
      var defaultSize = (p.sold_out_sizes && p.sold_out_sizes.indexOf('M') !== -1 && !p.sold_out) ? 'L' : 'M';
      selectPdpSize(defaultSize, document.getElementById('pdpSizeBtn_' + defaultSize));

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, 'M');"""

new_default_size = """      // Reset size pills: no size selected by default
      ['M', 'L', 'XL'].forEach(function(s) {
        var sBtn = document.getElementById('pdpSizeBtn_' + s);
        if (sBtn) sBtn.classList.remove('selected');
      });

      var sizeNotice = document.getElementById('pdpSizeNotice');
      if (sizeNotice) sizeNotice.style.display = 'none';

      // Default action buttons state
      var addBtn = document.getElementById('pdpAddToCartBtn');
      var buyBtn = document.getElementById('pdpBuyNowBtn');
      var waNotifyBtn = document.getElementById('pdpNotifyWhatsAppBtn');
      var waitlistBtn = document.getElementById('pdpNotifyWaitlistBtn');
      var regularWaBtn = document.getElementById('pdpWhatsAppBtn');

      if (p.sold_out) {
        if (addBtn) addBtn.style.display = 'none';
        if (buyBtn) buyBtn.style.display = 'none';
        if (regularWaBtn) regularWaBtn.style.display = 'none';
        if (waNotifyBtn) waNotifyBtn.style.display = 'flex';
        if (waitlistBtn) waitlistBtn.style.display = 'flex';
      } else {
        if (addBtn) addBtn.style.display = 'block';
        if (buyBtn) buyBtn.style.display = 'block';
        if (regularWaBtn) regularWaBtn.style.display = 'flex';
        if (waNotifyBtn) waNotifyBtn.style.display = 'none';
        if (waitlistBtn) waitlistBtn.style.display = 'none';
      }

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, null);"""

if old_default_size in h:
    h = h.replace(old_default_size, new_default_size)
    print("Removed default size selection in openProductPage in index.html")
else:
    print("old_default_size not found in index.html")

# Replace closeProductPage to restore exact scroll position
old_close_pdp = """    function closeProductPage() {
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (homeView) homeView.style.display = 'block';
      if (pdpView) pdpView.style.display = 'none';

      try {
        window.location.hash = '#catalog';
      } catch(e) {}

      if (activePdpProductId) {
        var card = document.querySelector('.product-card[data-id="' + activePdpProductId + '"]');
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    }"""

new_close_pdp = """    function closeProductPage() {
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (pdpView) pdpView.style.display = 'none';
      if (homeView) homeView.style.display = 'block';

      try {
        if (window.location.hash.startsWith('#product-')) {
          history.replaceState(null, null, window.location.pathname + window.location.search);
        }
      } catch(e) {}

      var targetScroll = savedHomeScrollY;
      try {
        var stored = sessionStorage.getItem('meenu_home_scroll');
        if (stored !== null) targetScroll = parseInt(stored, 10);
      } catch(e) {}

      // Immediately restore exact scroll position where user was standing
      window.scrollTo(0, targetScroll);
      requestAnimationFrame(function() {
        window.scrollTo(0, targetScroll);
      });
      setTimeout(function() {
        window.scrollTo(0, targetScroll);
      }, 40);
    }

    // Hardware / Browser Back button support on mobile & desktop
    window.addEventListener('popstate', function() {
      var pdpView = document.getElementById('productDetailView');
      if (pdpView && pdpView.style.display === 'block') {
        closeProductPage();
      }
    });"""

if old_close_pdp in h:
    h = h.replace(old_close_pdp, new_close_pdp)
    print("Updated closeProductPage to restore exact scroll in index.html")
else:
    print("old_close_pdp not found in index.html")

# Update selectPdpSize to hide notice
old_select_pdp = """    function selectPdpSize(size, btn) {
      pdpSelectedSize = size;
      document.querySelectorAll('.pdp-size-btn').forEach(function(b) {
        b.classList.remove('selected');
      });
      if (btn) {
        btn.classList.add('selected');
      } else {
        var autoBtn = document.getElementById('pdpSizeBtn_' + size);
        if (autoBtn) autoBtn.classList.add('selected');
      }
      var p = productsData.find(function(item) { return item.id === activePdpProductId; });"""

new_select_pdp = """    function selectPdpSize(size, btn) {
      pdpSelectedSize = size;
      document.querySelectorAll('.pdp-size-btn').forEach(function(b) {
        b.classList.remove('selected');
      });
      if (btn) {
        btn.classList.add('selected');
      } else {
        var autoBtn = document.getElementById('pdpSizeBtn_' + size);
        if (autoBtn) autoBtn.classList.add('selected');
      }
      var notice = document.getElementById('pdpSizeNotice');
      if (notice) notice.style.display = 'none';

      var p = productsData.find(function(item) { return item.id === activePdpProductId; });"""

if old_select_pdp in h:
    h = h.replace(old_select_pdp, new_select_pdp)
    print("Updated selectPdpSize in index.html")
else:
    print("old_select_pdp not found in index.html")

# Update addPdpProductToCart and buyPdpProductNow to require size selection
old_cart_actions = """    function addPdpProductToCart() {
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }

    function buyPdpProductNow() {
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }"""

new_cart_actions = """    function showPdpSizeRequired() {
      var notice = document.getElementById('pdpSizeNotice');
      if (notice) notice.style.display = 'block';
      var pills = document.querySelector('.pdp-size-pills');
      if (pills) {
        pills.classList.remove('size-error-shake');
        void pills.offsetWidth;
        pills.classList.add('size-error-shake');
        pills.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      if (typeof showToast === 'function') {
        showToast('⚠️ Please select a size (M, L, or XL) first.');
      }
    }

    function addPdpProductToCart() {
      if (!activePdpProductId) return;
      if (!pdpSelectedSize) {
        showPdpSizeRequired();
        return;
      }
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }

    function buyPdpProductNow() {
      if (!activePdpProductId) return;
      if (!pdpSelectedSize) {
        showPdpSizeRequired();
        return;
      }
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }"""

if old_cart_actions in h:
    h = h.replace(old_cart_actions, new_cart_actions)
    print("Updated addPdpProductToCart & buyPdpProductNow to require size in index.html")
else:
    print("old_cart_actions not found in index.html")

# Update updatePdpWhatsAppLink to handle null size
old_wa_link = """    function updatePdpWhatsAppLink(product, size) {
      var text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/918511616133?text=' + text;
    }"""

new_wa_link = """    function updatePdpWhatsAppLink(product, size) {
      var text;
      if (size) {
        text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      } else {
        text = encodeURIComponent('Hi Meenu Label Atelier! I am inquiring about "' + product.name + '" (Style #' + product.code + ') from Drop 01. Please share sizing recommendations and express delivery details.');
      }
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/918511616133?text=' + text;
    }"""

if old_wa_link in h:
    h = h.replace(old_wa_link, new_wa_link)
    print("Updated updatePdpWhatsAppLink in index.html")
else:
    print("old_wa_link not found in index.html")

# Also update Quick View modal in index.html to not default select size M
old_modal_open = """      activeModalProduct = p;
      selectedSize = 'M';"""

new_modal_open = """      activeModalProduct = p;
      selectedSize = null;"""

if old_modal_open in h:
    h = h.replace(old_modal_open, new_modal_open)
    print("Updated openProductModal selectedSize to null in index.html")

old_modal_btns = """      var btns = document.querySelectorAll('.modal-size-btn');
      btns.forEach(function(b, idx) {
        if (idx === 0) b.classList.add('selected');
        else b.classList.remove('selected');
      });"""

new_modal_btns = """      var btns = document.querySelectorAll('.modal-size-btn');
      btns.forEach(function(b) {
        b.classList.remove('selected');
      });"""

if old_modal_btns in h:
    h = h.replace(old_modal_btns, new_modal_btns)
    print("Removed default selected from modal size buttons in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

print("Updated index.html successfully!")

# -------------------------------------------------------------
# 2. Update sections/main-product.liquid & mirror
# -------------------------------------------------------------
pdp_liquid_files = [
    'sections/main-product.liquid',
    'meenu-label-shopify-theme/sections/main-product.liquid'
]

for p in pdp_liquid_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # A. Remove selected on forloop.first
    old_btn_tag = 'class="pdp-size-btn {% if forloop.first and variant.available %}selected{% endif %} {% unless variant.available %}sold-out{% endunless %}"'
    new_btn_tag = 'class="pdp-size-btn {% unless variant.available %}sold-out{% endunless %}"'
    if old_btn_tag in c:
        c = c.replace(old_btn_tag, new_btn_tag)
        print(f"Removed default selected from {p}")
    else:
        print(f"old_btn_tag not found in {p}")

    # B. Hidden input empty initial value
    old_hidden = '<input type="hidden" name="id" id="selectedVariantId" value="{{ product.selected_or_first_available_variant.id }}">'
    new_hidden = '<input type="hidden" name="id" id="selectedVariantId" value="">'
    if old_hidden in c:
        c = c.replace(old_hidden, new_hidden)
        print(f"Set selectedVariantId value to empty in {p}")
    else:
        print(f"old_hidden not found in {p}")

    # C. JS initial values null
    old_js_init = """  var currentSelectedVariantId = {{ product.selected_or_first_available_variant.id | json }};
  var currentSelectedSizeTitle = {{ product.selected_or_first_available_variant.title | json }};"""
    new_js_init = """  var currentSelectedVariantId = null;
  var currentSelectedSizeTitle = null;"""
    if old_js_init in c:
        c = c.replace(old_js_init, new_js_init)
        print(f"Set JS variant init to null in {p}")
    else:
        print(f"old_js_init not found in {p}")

    # D. Update back button to use history.back()
    old_back_btn = '<a class="pdp-back-btn" href="{{ collection.url | default: \'/collections/all\' }}">'
    new_back_btn = '<a class="pdp-back-btn" href="javascript:void(0)" onclick="if(window.history.length > 1){window.history.back();}else{window.location.href=\'{{ collection.url | default: \"/collections/all\" }}\';}" aria-label="Back to Collection">'
    if old_back_btn in c:
        c = c.replace(old_back_btn, new_back_btn)
        print(f"Updated pdp-back-btn in {p} to use history.back()")
    else:
        print(f"old_back_btn not found in {p}")

    # E. validateShopifyForm ensure size selection is enforced
    old_val = """  function validateShopifyForm(e) {
    if (!currentSelectedVariantId) {
      if (e) e.preventDefault();
      var notice = document.getElementById('shopifySizeRequiredNotice');
      if (notice) notice.style.display = 'block';

      var sec = document.getElementById('shopifySizeGrid');
      if (sec) {
        sec.classList.remove('size-error-shake');
        void sec.offsetWidth;
        sec.classList.add('size-error-shake');
        sec.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      return false;
    }
    return true;
  }"""

    new_val = """  function validateShopifyForm(e) {
    if (!currentSelectedVariantId || !currentSelectedSizeTitle) {
      if (e) e.preventDefault();
      var notice = document.getElementById('shopifySizeRequiredNotice');
      if (notice) notice.style.display = 'block';

      var sec = document.getElementById('shopifySizeGrid');
      if (sec) {
        sec.classList.remove('size-error-shake');
        void sec.offsetWidth;
        sec.classList.add('size-error-shake');
        sec.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      if (typeof showMeenuToast === 'function') {
        showMeenuToast('⚠️ Please select your size (M, L, or XL) first');
      }
      return false;
    }
    return true;
  }"""
    if old_val in c:
        c = c.replace(old_val, new_val)
        print(f"Updated validateShopifyForm in {p}")

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

# -------------------------------------------------------------
# 3. Update assets/meenu-theme.js & mirror
# -------------------------------------------------------------
theme_js_files = [
    'assets/meenu-theme.js',
    'meenu-label-shopify-theme/assets/meenu-theme.js'
]

scroll_preservation_js = """
/* =========================================================================
   SCROLL POSITION PRESERVATION ON NAVIGATION
   ========================================================================= */
document.addEventListener('click', function(e) {
  var productLink = e.target.closest('a[href*="/products/"]');
  if (productLink) {
    var curScroll = window.pageYOffset || document.documentElement.scrollTop || 0;
    try {
      sessionStorage.setItem('meenu_catalog_scroll_' + window.location.pathname, curScroll);
    } catch(err) {}
  }
});

window.addEventListener('pageshow', function(e) {
  try {
    var key = 'meenu_catalog_scroll_' + window.location.pathname;
    var saved = sessionStorage.getItem(key);
    if (saved !== null && (e.persisted || (window.performance && window.performance.navigation && window.performance.navigation.type === 2) || (window.performance && window.performance.getEntriesByType && window.performance.getEntriesByType('navigation')[0] && window.performance.getEntriesByType('navigation')[0].type === 'back_forward'))) {
      var scrollY = parseInt(saved, 10);
      window.scrollTo(0, scrollY);
      setTimeout(function() { window.scrollTo(0, scrollY); }, 50);
    }
  } catch(err) {}
});
"""

for p in theme_js_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'SCROLL POSITION PRESERVATION ON NAVIGATION' not in c:
        c = c + "\n" + scroll_preservation_js
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added scroll preservation JS to {p}")
    else:
        print(f"Scroll preservation JS already in {p}")

# -------------------------------------------------------------
# 4. Update assets/meenu-luxury.css & mirror for size shake
# -------------------------------------------------------------
shake_css = """
@keyframes sizeShake {
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-6px); }
  40%, 80% { transform: translateX(6px); }
}
.size-error-shake {
  animation: sizeShake 0.4s ease;
}
"""

for p in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'size-error-shake' not in c:
        c = c + "\n" + shake_css
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added size-error-shake CSS to {p}")
    else:
        print(f"size-error-shake already present in {p}")

# Also add shake_css to index.html style if not present
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()
if 'size-error-shake' not in h:
    pos = h.find('</style>')
    if pos != -1:
        h = h[:pos] + "\n" + shake_css + "\n" + h[pos:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(h)
        print("Added size-error-shake to index.html style")

print("All updates in step 9 applied!")
