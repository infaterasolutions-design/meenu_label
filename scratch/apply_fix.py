import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
backup_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.backup_size_fix.html'

shutil.copy2(file_path, backup_path)
print("Backup created at:", backup_path)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS update: add pdpSizeShake keyframes and pdp-size-error-shake
target_css = """    .pdp-size-btn.selected .pdp-size-stock {
      color: #FFD54F;
    }"""
replacement_css = """    .pdp-size-btn.selected .pdp-size-stock {
      color: #FFD54F;
    }
    @keyframes pdpSizeShake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-6px); }
      40%, 80% { transform: translateX(6px); }
    }
    .pdp-size-error-shake {
      animation: pdpSizeShake 0.4s ease-in-out;
      outline: 2px solid #E53935 !important;
      border-radius: 8px;
    }"""
assert target_css in content, "Target CSS not found"
content = content.replace(target_css, replacement_css, 1)

# 2. PDP Size HTML update
target_pdp_html = """          <!-- Size Selection -->
          <div class="pdp-size-section">
            <div class="pdp-size-header">
              <span class="pdp-size-label">Select Size (Standard Indian Pret)</span>
              <span class="pdp-size-chart-link" onclick="openSizeGuide()">&#128207; View Detailed Measurements</span>
            </div>
            <div class="pdp-size-pills">
              <button type="button" class="pdp-size-btn selected" id="pdpSizeBtn_M" onclick="selectPdpSize('M', this)">
                <span class="pdp-size-name">M (38)</span>
                <span class="pdp-size-sub">Bust 38" | Waist 34"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_L" onclick="selectPdpSize('L', this)">
                <span class="pdp-size-name">L (40)</span>
                <span class="pdp-size-sub">Bust 40" | Waist 36"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
          </div>"""

replacement_pdp_html = """          <!-- Size Selection -->
          <div class="pdp-size-section">
            <div class="pdp-size-header">
              <span class="pdp-size-label">Select Size (Standard Indian Pret) <span id="pdpSelectedSizeIndicator" style="display:none; color:var(--accent-burgundy,#6E1A24); font-weight:700; margin-left:6px; font-size:11px;"></span></span>
              <span class="pdp-size-chart-link" onclick="openSizeGuide()">&#128207; View Detailed Measurements</span>
            </div>
            <div class="pdp-size-pills">
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_M" onclick="selectPdpSize('M', this)">
                <span class="pdp-size-name">M (38)</span>
                <span class="pdp-size-sub">Bust 38" | Waist 34"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_L" onclick="selectPdpSize('L', this)">
                <span class="pdp-size-name">L (40)</span>
                <span class="pdp-size-sub">Bust 40" | Waist 36"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
            <div id="pdpSizeSelectPrompt" style="display:none; color:#B91C1C; background:#FEF2F2; border:1px solid #FCA5A5; border-radius:6px; padding:10px 14px; font-size:12px; font-weight:600; text-align:center; margin-top:8px;">
              &#9888; Please select your size (M, L, or XL) before adding to bag
            </div>
          </div>"""
assert target_pdp_html in content, "Target PDP HTML not found"
content = content.replace(target_pdp_html, replacement_pdp_html, 1)

# 3. Modal HTML update
target_modal_html = """          <div class="modal-sizes-group">
            <button class="modal-size-btn selected" onclick="selectModalSize('M', this)">M (38")</button>
            <button class="modal-size-btn" onclick="selectModalSize('L', this)">L (40")</button>
            <button class="modal-size-btn" onclick="selectModalSize('XL', this)">XL (42")</button>
          </div>"""

replacement_modal_html = """          <div class="modal-sizes-group">
            <button class="modal-size-btn" onclick="selectModalSize('M', this)">M (38")</button>
            <button class="modal-size-btn" onclick="selectModalSize('L', this)">L (40")</button>
            <button class="modal-size-btn" onclick="selectModalSize('XL', this)">XL (42")</button>
          </div>
          <div id="modalSizeSelectPrompt" style="display:none; color:#B91C1C; background:#FEF2F2; border:1px solid #FCA5A5; border-radius:6px; padding:8px 12px; font-size:11.5px; font-weight:600; text-align:center; margin-top:8px;">
            &#9888; Please select your size (M, L, or XL) before adding to bag
          </div>"""
assert target_modal_html in content, "Target Modal HTML not found"
content = content.replace(target_modal_html, replacement_modal_html, 1)

# 4. Modal JS variables & openProductModal
target_modal_js = """    var activeModalProduct = null;
    var selectedSize = 'M';"""
replacement_modal_js = """    var activeModalProduct = null;
    var selectedSize = null;"""
assert target_modal_js in content, "Target Modal JS var not found"
content = content.replace(target_modal_js, replacement_modal_js, 1)

target_modal_open = """      activeModalProduct = p;
      selectedSize = 'M';"""
replacement_modal_open = """      activeModalProduct = p;
      selectedSize = null;"""
assert target_modal_open in content, "Target Modal open var not found"
content = content.replace(target_modal_open, replacement_modal_open, 1)

target_modal_btns = """      var btns = document.querySelectorAll('.modal-size-btn');
      btns.forEach(function(b, idx) {
        if (idx === 0) b.classList.add('selected');
        else b.classList.remove('selected');
      });

      updateWhatsAppLink(p, 'M');"""
replacement_modal_btns = """      var btns = document.querySelectorAll('.modal-size-btn');
      btns.forEach(function(b) {
        b.classList.remove('selected');
      });
      var mPrompt = document.getElementById('modalSizeSelectPrompt');
      if (mPrompt) mPrompt.style.display = 'none';
      var mGroup = document.querySelector('.modal-sizes-group');
      if (mGroup) mGroup.classList.remove('pdp-size-error-shake');

      updateWhatsAppLink(p, null);"""
assert target_modal_btns in content, "Target Modal btns not found"
content = content.replace(target_modal_btns, replacement_modal_btns, 1)

# 5. Modal selectModalSize & updateWhatsAppLink & addCurrentProductToCart
target_modal_funcs = """    function selectModalSize(size, el) {
      selectedSize = size;
      document.querySelectorAll('.modal-size-btn').forEach(function(b) { b.classList.remove('selected'); });
      if (el) el.classList.add('selected');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }

    function updateWhatsAppLink(product, size) {
      var text = encodeURIComponent('Hi Meenu Label! I would like to order "' + product.name + '" (Code: ' + product.code + ') in Size ' + size + ' for ₹' + product.price + '. Please confirm delivery details.');
      document.getElementById('modalWhatsAppBtn').href = 'https://wa.me/918511616133?text=' + text;
    }"""

replacement_modal_funcs = """    function selectModalSize(size, el) {
      selectedSize = size;
      document.querySelectorAll('.modal-size-btn').forEach(function(b) { b.classList.remove('selected'); });
      if (el) el.classList.add('selected');
      var mPrompt = document.getElementById('modalSizeSelectPrompt');
      if (mPrompt) mPrompt.style.display = 'none';
      var mGroup = document.querySelector('.modal-sizes-group');
      if (mGroup) mGroup.classList.remove('pdp-size-error-shake');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }

    function updateWhatsAppLink(product, size) {
      var text;
      if (size) {
        text = encodeURIComponent('Hi Meenu Label! I would like to order "' + product.name + '" (Code: ' + product.code + ') in Size ' + size + ' for ₹' + product.price + '. Please confirm delivery details.');
      } else {
        text = encodeURIComponent('Hi Meenu Label! I would like to order / enquire about "' + product.name + '" (Code: ' + product.code + ') for ₹' + product.price + '. Please help me choose the right size and confirm delivery details.');
      }
      var btn = document.getElementById('modalWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/918511616133?text=' + text;
    }"""
assert target_modal_funcs in content, "Target Modal funcs not found"
content = content.replace(target_modal_funcs, replacement_modal_funcs, 1)

target_add_modal = """    function addCurrentProductToCart() {
      if (!activeModalProduct) return;
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }"""

replacement_add_modal = """    function addCurrentProductToCart() {
      if (!activeModalProduct) return;
      if (!selectedSize) {
        showToast('⚠️ Please select your size (M, L, or XL) first');
        var mPrompt = document.getElementById('modalSizeSelectPrompt');
        if (mPrompt) mPrompt.style.display = 'block';
        var mGroup = document.querySelector('.modal-sizes-group');
        if (mGroup) {
          mGroup.classList.remove('pdp-size-error-shake');
          void mGroup.offsetWidth;
          mGroup.classList.add('pdp-size-error-shake');
          setTimeout(function() { mGroup.classList.remove('pdp-size-error-shake'); }, 1200);
        }
        return;
      }
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }"""
assert target_add_modal in content, "Target addCurrentProductToCart not found"
content = content.replace(target_add_modal, replacement_add_modal, 1)

# 6. PDP JS variables & openProductPage
target_pdp_var = """    var activePdpProductId = null;
    var pdpSelectedSize = 'M';"""
replacement_pdp_var = """    var activePdpProductId = null;
    var pdpSelectedSize = null;"""
assert target_pdp_var in content, "Target PDP var not found"
content = content.replace(target_pdp_var, replacement_pdp_var, 1)

target_pdp_open_var = """      activePdpProductId = prodId;
      pdpSelectedSize = 'M';"""
replacement_pdp_open_var = """      activePdpProductId = prodId;
      pdpSelectedSize = null;"""
assert target_pdp_open_var in content, "Target PDP open var not found"
content = content.replace(target_pdp_open_var, replacement_pdp_open_var, 1)

target_pdp_open_reset = """      // Size buttons
      selectPdpSize('M', document.getElementById('pdpSizeBtn_M'));

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, 'M');"""

replacement_pdp_open_reset = """      // Size buttons: reset to unselected state (no default selection)
      document.querySelectorAll('.pdp-size-btn').forEach(function(b) {
        b.classList.remove('selected');
      });
      var sizePrompt = document.getElementById('pdpSizeSelectPrompt');
      if (sizePrompt) sizePrompt.style.display = 'none';
      var sizePills = document.querySelector('.pdp-size-pills');
      if (sizePills) sizePills.classList.remove('pdp-size-error-shake');
      var indicator = document.getElementById('pdpSelectedSizeIndicator');
      if (indicator) {
        indicator.textContent = '';
        indicator.style.display = 'none';
      }

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, null);"""
assert target_pdp_open_reset in content, "Target PDP open reset not found"
content = content.replace(target_pdp_open_reset, replacement_pdp_open_reset, 1)

# 7. PDP selectPdpSize, updatePdpWhatsAppLink, addPdpProductToCart, buyPdpProductNow
target_pdp_funcs = """    function selectPdpSize(size, btn) {
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
      var p = productsData.find(function(item) { return item.id === activePdpProductId; });
      if (p) updatePdpWhatsAppLink(p, size);
    }

    function updatePdpWhatsAppLink(product, size) {
      var text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/918511616133?text=' + text;
    }

    function addPdpProductToCart() {
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }

    function buyPdpProductNow() {
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }"""

replacement_pdp_funcs = """    function selectPdpSize(size, btn) {
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
      var sizePrompt = document.getElementById('pdpSizeSelectPrompt');
      if (sizePrompt) sizePrompt.style.display = 'none';
      var sizePills = document.querySelector('.pdp-size-pills');
      if (sizePills) sizePills.classList.remove('pdp-size-error-shake');
      var indicator = document.getElementById('pdpSelectedSizeIndicator');
      if (indicator) {
        indicator.textContent = '— Size ' + size + ' Selected';
        indicator.style.display = 'inline';
      }

      var p = productsData.find(function(item) { return item.id === activePdpProductId; });
      if (p) updatePdpWhatsAppLink(p, size);
    }

    function updatePdpWhatsAppLink(product, size) {
      var text;
      if (size) {
        text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      } else {
        text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order / enquire about "' + product.name + '" (Style #' + product.code + ') from Drop 01. Please help me choose the right size (M 38 / L 40 / XL 42) and confirm express Tricity delivery details.');
      }
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/918511616133?text=' + text;
    }

    function showPdpSizeRequiredAlert() {
      showToast('⚠️ Please select your size (M, L, or XL) first');
      var prompt = document.getElementById('pdpSizeSelectPrompt');
      if (prompt) prompt.style.display = 'block';
      var sizePills = document.querySelector('.pdp-size-pills');
      if (sizePills) {
        sizePills.classList.remove('pdp-size-error-shake');
        void sizePills.offsetWidth;
        sizePills.classList.add('pdp-size-error-shake');
        setTimeout(function() { sizePills.classList.remove('pdp-size-error-shake'); }, 1200);
        sizePills.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }

    function addPdpProductToCart() {
      if (!activePdpProductId) return;
      if (!pdpSelectedSize) {
        showPdpSizeRequiredAlert();
        return;
      }
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }

    function buyPdpProductNow() {
      if (!activePdpProductId) return;
      if (!pdpSelectedSize) {
        showPdpSizeRequiredAlert();
        return;
      }
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }"""
assert target_pdp_funcs in content, "Target PDP funcs not found"
content = content.replace(target_pdp_funcs, replacement_pdp_funcs, 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: All replacements applied accurately to Meenu_Label_Desktop_Storefront.html!")
