import json, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS to index.html style block
with open('scratch/add_notify_css.py', 'r', encoding='utf-8') as f:
    py_text = f.read()

# Extract css_to_add from scratch/add_notify_css.py
css_match = re.search(r'css_to_add = """(.*?)"""', py_text, re.DOTALL)
if css_match:
    css_code = css_match.group(1).strip()
    if 'MEENU LABEL - SOLD OUT & LUXURY NOTIFY ME' not in content:
        # insert before </style>
        content = content.replace('</style>', css_code + '\n</style>', 1)
        print('1. Added CSS to index.html')
    else:
        print('1. CSS already present in index.html')

# 2. Add #meenuNotifyBackdrop HTML markup right before <div class="snitch-size-backdrop" id="snitchSizeModalBackdrop"
with open('snippets/notify-me-modal.liquid', 'r', encoding='utf-8') as f:
    modal_html = f.read().strip()

if 'id="meenuNotifyBackdrop"' not in content:
    target_modal = '<div class="snitch-size-backdrop" id="snitchSizeModalBackdrop"'
    content = content.replace(target_modal, modal_html + '\n\n' + target_modal, 1)
    print('2. Added Notify Me Modal HTML to index.html')
else:
    print('2. Notify Me Modal HTML already present in index.html')

# 3. Update productsData in index.html
# Update JAB26ST05010 to have "sold_out_sizes": ["XL"]
# Update JAB25ST02661 to have "sold_out": true, "sold_out_sizes": ["XS", "S", "M", "L", "XL", "XXL"]
m_pdata = re.search(r'var productsData = (\[.*?\]);', content)
if m_pdata:
    pdata = json.loads(m_pdata.group(1))
    for p in pdata:
        if p['id'] == 'JAB26ST05010':
            p['sold_out_sizes'] = ['XL']
        if p['id'] == 'JAB25ST02661':
            p['sold_out'] = True
            p['sold_out_sizes'] = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    
    new_pdata_str = 'var productsData = ' + json.dumps(pdata) + ';'
    content = content.replace(m_pdata.group(0), new_pdata_str, 1)
    print('3. Updated productsData with sold out properties in index.html')

# 4. Update product card in index.html for JAB25ST02661
old_card_target = """    <div class="product-card" data-category="festive" data-id="JAB25ST02661" onclick="openProductPage('JAB25ST02661')">
      <div class="card-thumb">
        <span class="card-badge badge-scarcity">Only 3 Left</span>"""

new_card_target = """    <div class="product-card is-sold-out" data-category="festive" data-id="JAB25ST02661" onclick="openProductPage('JAB25ST02661')">
      <div class="card-thumb">
        <span class="card-badge badge-sold-out">SOLD OUT</span>"""

if old_card_target in content:
    content = content.replace(old_card_target, new_card_target, 1)
    print('4a. Updated card badge to SOLD OUT for JAB25ST02661')

old_btn_target = """          <button type="button" class="snitch-plus-trigger" data-product-id="JAB25ST02661" onclick="event.preventDefault(); event.stopPropagation(); openQuickSizePopup(this)" title="Select Size &amp; Add to Bag" aria-label="Select Size &amp; Add to Bag">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="3" x2="12" y2="15"></line>
              <line x1="6" y1="9" x2="18" y2="9"></line>
              <line x1="4" y1="19" x2="20" y2="19"></line>
            </svg>
          </button>"""

new_btn_target = """          <button type="button" class="snitch-notify-trigger" data-product-id="JAB25ST02661" onclick="event.preventDefault(); event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'M', 'The Noor Petrol Teal Chanderi Suit', '', '₹2,599')" title="Sold Out - Notify Me When Available" aria-label="Notify Me When Available">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span class="notify-btn-text">NOTIFY ME</span>
          </button>"""

if old_btn_target in content:
    content = content.replace(old_btn_target, new_btn_target, 1)
    print('4b. Updated card button to NOTIFY ME for JAB25ST02661')

# 5. Update PDP Actions row in index.html
old_pdp_actions = """          <!-- Actions -->
          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>"""

new_pdp_actions = """          <!-- Actions -->
          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" id="pdpAddToCartBtn" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" id="pdpBuyNowBtn" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>
            <button class="pdp-btn-notify" id="pdpNotifyBtn" style="display:none;" onclick="triggerPdpNotifyMe()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              SOLD OUT &bull; NOTIFY ME WHEN AVAILABLE
            </button>"""

if old_pdp_actions in content:
    content = content.replace(old_pdp_actions, new_pdp_actions, 1)
    print('5. Updated PDP actions row in index.html')

# 6. Update openProductPage & selectPdpSize in index.html
old_select_pdp_size = """    function selectPdpSize(size, btn) {
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
    }"""

new_select_pdp_size = """    function selectPdpSize(size, btn) {
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
      if (p) {
        updatePdpWhatsAppLink(p, size);

        var isSoldOut = false;
        if (p.sold_out) isSoldOut = true;
        else if (p.sold_out_sizes && p.sold_out_sizes.indexOf(size) !== -1) isSoldOut = true;

        var addBtn = document.getElementById('pdpAddToCartBtn');
        var buyBtn = document.getElementById('pdpBuyNowBtn');
        var notifyBtn = document.getElementById('pdpNotifyBtn');

        if (isSoldOut) {
          if (addBtn) addBtn.style.display = 'none';
          if (buyBtn) buyBtn.style.display = 'none';
          if (notifyBtn) notifyBtn.style.display = 'flex';
        } else {
          if (addBtn) addBtn.style.display = 'block';
          if (buyBtn) buyBtn.style.display = 'block';
          if (notifyBtn) notifyBtn.style.display = 'none';
        }
      }
    }

    function triggerPdpNotifyMe() {
      if (!activePdpProductId) return;
      var p = productsData.find(function(item) { return item.id === activePdpProductId; });
      if (!p) return;
      openNotifyMeModal(p.id, pdpSelectedSize || 'M', p.name, p.b64, '₹' + p.price.toLocaleString('en-IN'));
    }"""

if old_select_pdp_size in content:
    content = content.replace(old_select_pdp_size, new_select_pdp_size, 1)
    print('6a. Updated selectPdpSize in index.html')

# Also in openProductPage: update size pills labels and classes
old_pdp_open_end = """      // Size buttons
      selectPdpSize('M', document.getElementById('pdpSizeBtn_M'));"""

new_pdp_open_end = """      // Update size pills for availability
      ['M', 'L', 'XL'].forEach(function(s) {
        var sBtn = document.getElementById('pdpSizeBtn_' + s);
        if (sBtn) {
          var isAvail = true;
          if (p.sold_out) isAvail = false;
          else if (p.sold_out_sizes && p.sold_out_sizes.indexOf(s) !== -1) isAvail = false;

          sBtn.classList.toggle('sold-out', !isAvail);
          var stockLabel = sBtn.querySelector('.pdp-size-stock');
          if (stockLabel) {
            stockLabel.textContent = isAvail ? 'Only 1 Left' : 'Sold Out';
          }
        }
      });

      // Size buttons default selection (pick first available or M)
      var defaultSize = (p.sold_out_sizes && p.sold_out_sizes.indexOf('M') !== -1 && !p.sold_out) ? 'L' : 'M';
      selectPdpSize(defaultSize, document.getElementById('pdpSizeBtn_' + defaultSize));"""

if old_pdp_open_end in content:
    content = content.replace(old_pdp_open_end, new_pdp_open_end, 1)
    print('6b. Updated openProductPage in index.html')

# 7. Update Quick Size rows creation in index.html
old_snitch_sizes = """      standardSizes.forEach(function(sName) {
        createSnitchSizeRow(sizeListEl, sName, productId + '_' + sName, true);
      });"""

new_snitch_sizes = """      var pObj = (typeof productsData !== 'undefined') ? productsData.find(function(p) { return p.id === productId || p.code === productId; }) : null;
      standardSizes.forEach(function(sName) {
        var isAvail = true;
        if (pObj) {
          if (pObj.sold_out) isAvail = false;
          else if (pObj.sold_out_sizes && pObj.sold_out_sizes.indexOf(sName) !== -1) isAvail = false;
        }
        createSnitchSizeRow(sizeListEl, sName, productId + '_' + sName, isAvail);
      });"""

if old_snitch_sizes in content:
    content = content.replace(old_snitch_sizes, new_snitch_sizes, 1)
    print('7a. Updated standardSizes in index.html')

old_create_row_index = """function createSnitchSizeRow(container, sizeName, variantId, isAvailable) {
  var row = document.createElement('button');
  row.type = 'button';
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status';
  if (!isAvailable) {
    statusSpan.textContent = 'OUT OF STOCK';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  }

  container.appendChild(row);
}"""

new_create_row_index = """function createSnitchSizeRow(container, sizeName, variantId, isAvailable) {
  var row = document.createElement('button');
  row.type = 'button';
  row.className = 'snitch-size-row' + (!isAvailable ? ' disabled sold-out' : '');
  
  var nameSpan = document.createElement('span');
  nameSpan.className = 'snitch-size-name';
  nameSpan.textContent = sizeName;
  row.appendChild(nameSpan);

  var statusSpan = document.createElement('span');
  statusSpan.className = 'snitch-size-status' + (!isAvailable ? ' sold-out-status' : '');
  if (!isAvailable) {
    statusSpan.textContent = 'SOLD OUT • NOTIFY ME';
  }
  row.appendChild(statusSpan);

  if (isAvailable) {
    row.onclick = function() {
      snitchAddSizeToCart(row, variantId, sizeName);
    };
  } else {
    row.onclick = function() {
      closeSnitchSizePopup();
      openNotifyMeModal(
        activeSnitchProduct.id,
        sizeName,
        activeSnitchProduct.title,
        activeSnitchProduct.image,
        activeSnitchProduct.price
      );
    };
  }

  container.appendChild(row);
}"""

if old_create_row_index in content:
    content = content.replace(old_create_row_index, new_create_row_index, 1)
    print('7b. Updated createSnitchSizeRow in index.html')

# 8. Append Notify Me JS code if not present
with open('scratch/patch_theme_js_notify.py', 'r', encoding='utf-8') as f:
    js_py_text = f.read()

js_match = re.search(r'code_to_add = """(.*?)"""', js_py_text, re.DOTALL)
if js_match:
    js_code = js_match.group(1).strip()
    if 'activeNotifyProduct' not in content:
        content = content.replace('</script>\n</body>', js_code + '\n</script>\n</body>', 1)
        print('8. Appended Notify Me JS to index.html')
    else:
        print('8. activeNotifyProduct already in index.html')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully saved updated index.html!')
