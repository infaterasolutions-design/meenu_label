exact_target_html = """<button type="submit" id="pdpAddToCartBtn" class="pdp-btn-primary" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>ADD TO SHOPPING BAG</button>
          <button type="button" id="pdpBuyNowBtn" class="pdp-btn-buy" onclick="buyShopifyProductNow()" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>BUY IT NOW &rarr;</button>
          <button type="button" id="pdpNotifyBtn" class="pdp-btn-notify" onclick="openNotifyMeModal('{{ product.id }}', currentSelectedSizeTitle || 'M', '{{ product.title | escape }}', '{{ product.featured_image | default: product.images.first | image_url: width: 400 }}', '{{ product.price | money | escape }}')" {% if product.selected_or_first_available_variant.available %}style="display:none;"{% endif %}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            SOLD OUT &bull; NOTIFY ME WHEN AVAILABLE
          </button>
          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001." target="_blank">
            <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
          </a>"""

replacement_html = """<button type="submit" id="pdpAddToCartBtn" class="pdp-btn-primary" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>ADD TO SHOPPING BAG</button>
          <button type="button" id="pdpBuyNowBtn" class="pdp-btn-buy" onclick="buyShopifyProductNow()" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>BUY IT NOW &rarr;</button>

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

          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001." target="_blank" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>
            <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
          </a>"""

target_js = """    var addBtn = document.getElementById('pdpAddToCartBtn');
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

replacement_js = """    var addBtn = document.getElementById('pdpAddToCartBtn');
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
        regularWaBtn.href = "https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=" + encodeURIComponent("Hi Meenu Label! I would like to order '{{ product.title | escape }}' in Size " + sizeTitle + " from Drop 01.");
      }
      if (waNotifyBtn) waNotifyBtn.style.display = 'none';
      if (waitlistBtn) waitlistBtn.style.display = 'none';
    }"""

for p in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if exact_target_html in content and target_js in content:
        content = content.replace(exact_target_html, replacement_html, 1)
        content = content.replace(target_js, replacement_js, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated PDP in:", p)
    else:
        print("Target missing in:", p)
