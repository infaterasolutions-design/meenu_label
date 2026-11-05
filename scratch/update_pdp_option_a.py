# scratch/update_pdp_option_a.py

# 1. Update sections/main-product.liquid and meenu-label-shopify-theme
pdp_liquid_target = """          <button type="submit" name="add" id="pdpAddToCartBtn" class="pdp-btn-primary" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>ADD TO SHOPPING BAG</button>
          <button type="button" id="pdpBuyNowBtn" class="pdp-btn-buy" onclick="buyItNowPdp()" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>BUY IT NOW &rarr;</button>
          <button type="button" id="pdpNotifyBtn" class="pdp-btn-notify" onclick="openNotifyMeModal('{{ product.id }}', currentSelectedSizeTitle || 'M', '{{ product.title | escape }}', '{{ product.featured_image | default: product.images.first | image_url: width: 400 }}', '{{ product.price | money | escape }}')" {% if product.selected_or_first_available_variant.available %}style="display:none;"{% endif %}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            SOLD OUT &bull; NOTIFY ME WHEN AVAILABLE
          </button>
          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label%20Atelier!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001.%20Please%20confirm%20piece%20reservation." target="_blank">
            <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
          </a>"""

pdp_liquid_replacement = """          <button type="submit" name="add" id="pdpAddToCartBtn" class="pdp-btn-primary" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>ADD TO SHOPPING BAG</button>
          <button type="button" id="pdpBuyNowBtn" class="pdp-btn-buy" onclick="buyItNowPdp()" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>BUY IT NOW &rarr;</button>

          <!-- Direct WhatsApp Concierge Restock Button (Option A) -->
          <a id="pdpNotifyWhatsAppBtn" class="pdp-btn-notify-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text={{ 'Hi Meenu Label! Please notify me when \"' | append: product.title | append: '\" in Size ' | append: product.selected_or_first_available_variant.title | append: ' is back in stock. Please share restock timeline.' | url_encode }}" target="_blank" {% if product.selected_or_first_available_variant.available %}style="display:none;"{% endif %}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.953 1.18-.175.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.151-.176.201-.301.301-.502.101-.201.05-.376-.025-.527-.075-.15-.678-1.634-.929-2.237-.245-.588-.493-.508-.678-.518-.175-.01-.376-.01-.577-.01-.201 0-.527.075-.803.376s-1.054 1.029-1.054 2.511c0 1.482 1.079 2.913 1.23 3.114.15.201 2.122 3.24 5.14 4.544.718.31 1.279.496 1.716.635.722.23 1.379.197 1.9.119.58-.088 1.78-.727 2.03-1.43.251-.703.251-1.305.176-1.43-.075-.126-.276-.201-.577-.351z"/>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2.05 21.95l4.908-1.353C8.414 21.49 10.15 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18.2c-1.61 0-3.13-.45-4.43-1.23l-.317-.189-2.906.801.815-2.833-.207-.328A8.152 8.152 0 0 1 3.8 12c0-4.52 3.68-8.2 8.2-8.2 4.52 0 8.2 3.68 8.2 8.2 0 4.52-3.68 8.2-8.2 8.2z"/>
            </svg>
            <span>NOTIFY ME ON WHATSAPP WHEN RESTOCKED</span>
          </a>

          <!-- Secondary Waitlist Trigger Button on PDP -->
          <button type="button" id="pdpNotifyWaitlistBtn" class="pdp-btn-notify-waitlist" onclick="openNotifyMeModal('{{ product.id }}', currentSelectedSizeTitle || 'M', '{{ product.title | escape }}', '{{ product.featured_image | default: product.images.first | image_url: width: 400 }}', '{{ product.price | money | escape }}')" {% if product.selected_or_first_available_variant.available %}style="display:none;"{% endif %}>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
            <span>OR JOIN WAITLIST VIA EMAIL / SMS</span>
          </button>

          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label%20Atelier!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001.%20Please%20confirm%20piece%20reservation." target="_blank" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>
            <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
          </a>"""

js_liquid_target = """    var addBtn = document.getElementById('pdpAddToCartBtn');
    var buyBtn = document.getElementById('pdpBuyNowBtn');
    var notifyBtn = document.getElementById('pdpNotifyBtn');

    if (isAvailable === false) {
      if (addBtn) addBtn.style.display = 'none';
      if (buyBtn) buyBtn.style.display = 'none';
      if (notifyBtn) notifyBtn.style.display = 'flex';
    } else {
      if (addBtn) addBtn.style.display = 'block';
      if (buyBtn) buyBtn.style.display = 'block';
      if (notifyBtn) notifyBtn.style.display = 'none';
    }"""

js_liquid_replacement = """    var addBtn = document.getElementById('pdpAddToCartBtn');
    var buyBtn = document.getElementById('pdpBuyNowBtn');
    var waNotifyBtn = document.getElementById('pdpNotifyWhatsAppBtn');
    var waitlistBtn = document.getElementById('pdpNotifyWaitlistBtn');
    var regularWaBtn = document.getElementById('pdpWhatsAppBtn');

    if (isAvailable === false) {
      if (addBtn) addBtn.style.display = 'none';
      if (buyBtn) buyBtn.style.display = 'none';
      if (regularWaBtn) regularWaBtn.style.display = 'none';
      if (waNotifyBtn) {
        waNotifyBtn.style.display = 'flex';
        waNotifyBtn.href = "https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=" + encodeURIComponent("Hi Meenu Label! Please notify me when '{{ product.title | escape }}' in Size " + sizeTitle + " is back in stock. Please share restock timeline.");
      }
      if (waitlistBtn) waitlistBtn.style.display = 'flex';
    } else {
      if (addBtn) addBtn.style.display = 'block';
      if (buyBtn) buyBtn.style.display = 'block';
      if (regularWaBtn) {
        regularWaBtn.style.display = 'flex';
        regularWaBtn.href = "https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=" + encodeURIComponent("Hi Meenu Label Atelier! I would like to order '{{ product.title | escape }}' in Size " + sizeTitle + ". Please confirm availability and delivery.");
      }
      if (waNotifyBtn) waNotifyBtn.style.display = 'none';
      if (waitlistBtn) waitlistBtn.style.display = 'none';
    }"""

for p in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if pdp_liquid_target in content and js_liquid_target in content:
        content = content.replace(pdp_liquid_target, pdp_liquid_replacement, 1)
        content = content.replace(js_liquid_target, js_liquid_replacement, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated PDP in:", p)
    else:
        print("Targets missing in:", p)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

index_pdp_btn_target = """          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" id="pdpAddToCartBtn" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" id="pdpBuyNowBtn" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>
            <button class="pdp-btn-notify" id="pdpNotifyBtn" style="display:none;" onclick="triggerPdpNotifyMe()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              SOLD OUT &bull; NOTIFY ME WHEN AVAILABLE
            </button>
            <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="#" target="_blank">
              <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
            </a>"""

index_pdp_btn_replacement = """          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" id="pdpAddToCartBtn" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" id="pdpBuyNowBtn" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>

            <!-- Direct WhatsApp Concierge Button (Option A) -->
            <a id="pdpNotifyWhatsAppBtn" class="pdp-btn-notify-whatsapp" style="display:none;" href="#" target="_blank">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.953 1.18-.175.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.151-.176.201-.301.301-.502.101-.201.05-.376-.025-.527-.075-.15-.678-1.634-.929-2.237-.245-.588-.493-.508-.678-.518-.175-.01-.376-.01-.577-.01-.201 0-.527.075-.803.376s-1.054 1.029-1.054 2.511c0 1.482 1.079 2.913 1.23 3.114.15.201 2.122 3.24 5.14 4.544.718.31 1.279.496 1.716.635.722.23 1.379.197 1.9.119.58-.088 1.78-.727 2.03-1.43.251-.703.251-1.305.176-1.43-.075-.126-.276-.201-.577-.351z"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2.05 21.95l4.908-1.353C8.414 21.49 10.15 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18.2c-1.61 0-3.13-.45-4.43-1.23l-.317-.189-2.906.801.815-2.833-.207-.328A8.152 8.152 0 0 1 3.8 12c0-4.52 3.68-8.2 8.2-8.2 4.52 0 8.2 3.68 8.2 8.2 0 4.52-3.68 8.2-8.2 8.2z"/>
              </svg>
              <span>NOTIFY ME ON WHATSAPP WHEN RESTOCKED</span>
            </a>

            <!-- Secondary Waitlist Trigger -->
            <button type="button" class="pdp-btn-notify-waitlist" id="pdpNotifyWaitlistBtn" style="display:none;" onclick="triggerPdpNotifyMe()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
              <span>OR JOIN RESTOCK WAITLIST (EMAIL / SMS)</span>
            </button>

            <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="#" target="_blank">
              <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
            </a>"""

index_js_target = """        var addBtn = document.getElementById('pdpAddToCartBtn');
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
        }"""

index_js_replacement = """        var addBtn = document.getElementById('pdpAddToCartBtn');
        var buyBtn = document.getElementById('pdpBuyNowBtn');
        var waNotifyBtn = document.getElementById('pdpNotifyWhatsAppBtn');
        var waitlistBtn = document.getElementById('pdpNotifyWaitlistBtn');
        var regularWaBtn = document.getElementById('pdpWhatsAppBtn');

        if (isSoldOut) {
          if (addBtn) addBtn.style.display = 'none';
          if (buyBtn) buyBtn.style.display = 'none';
          if (regularWaBtn) regularWaBtn.style.display = 'none';
          if (waNotifyBtn) {
            waNotifyBtn.style.display = 'flex';
            var msg = 'Hi Meenu Label! Please notify me when "' + p.name + '" (Style #' + p.code + ') in Size ' + size + ' is back in stock. Please share restock timeline.';
            waNotifyBtn.href = 'https://wa.me/919988898845?text=' + encodeURIComponent(msg);
          }
          if (waitlistBtn) waitlistBtn.style.display = 'flex';
        } else {
          if (addBtn) addBtn.style.display = 'block';
          if (buyBtn) buyBtn.style.display = 'block';
          if (regularWaBtn) regularWaBtn.style.display = 'flex';
          if (waNotifyBtn) waNotifyBtn.style.display = 'none';
          if (waitlistBtn) waitlistBtn.style.display = 'none';
        }"""

if index_pdp_btn_target in idx_content and index_js_target in idx_content:
    idx_content = idx_content.replace(index_pdp_btn_target, index_pdp_btn_replacement, 1)
    idx_content = idx_content.replace(index_js_target, index_js_replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print("Updated index.html PDP with Option A WhatsApp Concierge!")
else:
    print("Targets not found in index.html")
