import os

target_pills = """        <div class="pdp-size-pills" id="shopifySizeGrid">
          {% for variant in product.variants %}
            <button type="button" 
                    class="pdp-size-btn {% if forloop.first %}selected{% endif %}" 
                    id="pdpSizeBtn_{{ variant.title }}" 
                    data-variant-id="{{ variant.id }}" 
                    data-size-title="{{ variant.title }}" 
                    {% if variant.featured_image %}data-variant-image="{{ variant.featured_image | image_url: width: 1200 }}"{% elsif variant.image %}data-variant-image="{{ variant.image | image_url: width: 1200 }}"{% endif %}
                    onclick="selectShopifyPdpSize('{{ variant.id }}', '{{ variant.title }}', this)">
              <span class="pdp-size-name">{{ variant.title }}{% if variant.title == 'M' %} (38){% elsif variant.title == 'L' %} (40){% elsif variant.title == 'XL' %} (42){% endif %}</span>
              <span class="pdp-size-sub">{% if variant.title contains 'M' %}Bust 38" | Waist 34"{% elsif variant.title contains 'L' %}Bust 40" | Waist 36"{% elsif variant.title contains 'XL' %}Bust 42" | Waist 38"{% else %}Standard Pret Fit{% endif %}</span>
              <span class="pdp-size-stock">Only 1 Left</span>
            </button>
          {% endfor %}
        </div>"""

replacement_pills = """        <div class="pdp-size-pills" id="shopifySizeGrid">
          {% for variant in product.variants %}
            <button type="button" 
                    class="pdp-size-btn {% if forloop.first and variant.available %}selected{% endif %} {% unless variant.available %}sold-out{% endunless %}" 
                    id="pdpSizeBtn_{{ variant.title }}" 
                    data-variant-id="{{ variant.id }}" 
                    data-size-title="{{ variant.title }}" 
                    data-available="{{ variant.available }}"
                    {% if variant.featured_image %}data-variant-image="{{ variant.featured_image | image_url: width: 1200 }}"{% elsif variant.image %}data-variant-image="{{ variant.image | image_url: width: 1200 }}"{% endif %}
                    onclick="selectShopifyPdpSize('{{ variant.id }}', '{{ variant.title }}', this, {{ variant.available }})">
              <span class="pdp-size-name">{{ variant.title }}{% if variant.title == 'M' %} (38){% elsif variant.title == 'L' %} (40){% elsif variant.title == 'XL' %} (42){% endif %}</span>
              <span class="pdp-size-sub">{% if variant.title contains 'M' %}Bust 38" | Waist 34"{% elsif variant.title contains 'L' %}Bust 40" | Waist 36"{% elsif variant.title contains 'XL' %}Bust 42" | Waist 38"{% else %}Standard Pret Fit{% endif %}</span>
              <span class="pdp-size-stock">{% if variant.available %}Only 1 Left{% else %}Sold Out{% endif %}</span>
            </button>
          {% endfor %}
        </div>"""

target_actions = """        <div class="pdp-actions-row">
          <button type="submit" id="pdpAddToCartBtn" class="pdp-btn-primary">ADD TO SHOPPING BAG</button>
          <button type="button" class="pdp-btn-buy" onclick="buyShopifyProductNow()">BUY IT NOW &rarr;</button>
          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001." target="_blank">"""

replacement_actions = """        <div class="pdp-actions-row">
          <button type="submit" id="pdpAddToCartBtn" class="pdp-btn-primary" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>ADD TO SHOPPING BAG</button>
          <button type="button" id="pdpBuyNowBtn" class="pdp-btn-buy" onclick="buyShopifyProductNow()" {% unless product.selected_or_first_available_variant.available %}style="display:none;"{% endunless %}>BUY IT NOW &rarr;</button>
          <button type="button" id="pdpNotifyBtn" class="pdp-btn-notify" onclick="openNotifyMeModal('{{ product.id }}', currentSelectedSizeTitle || 'M', '{{ product.title | escape }}', '{{ product.featured_image | default: product.images.first | image_url: width: 400 }}', '{{ product.price | money | escape }}')" {% if product.selected_or_first_available_variant.available %}style="display:none;"{% endif %}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            SOLD OUT &bull; NOTIFY ME WHEN AVAILABLE
          </button>
          <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}%20from%20Drop%2001." target="_blank">"""

target_func = """  function selectShopifyPdpSize(variantId, sizeTitle, btn) {
    currentSelectedVariantId = variantId;
    currentSelectedSizeTitle = sizeTitle;
    var inp = document.getElementById('selectedVariantId');
    if (inp) inp.value = variantId;

    var tiles = document.querySelectorAll('.pdp-size-btn');
    tiles.forEach(function(t) { t.classList.remove('selected'); });
    if (btn) btn.classList.add('selected');

    // Switch image if variant has assigned image
    if (btn) {
      var varImg = btn.getAttribute('data-variant-image');
      if (varImg) {
        var matchThumb = document.querySelector('.pdp-thumb-item[data-src="' + varImg + '"]');
        if (matchThumb) {
          matchThumb.click();
        }
      }
    }

    var notice = document.getElementById('shopifySizeRequiredNotice');
    if (notice) notice.style.display = 'none';

    var sec = document.getElementById('shopifySizeGrid');
    if (sec) sec.classList.remove('size-error-shake');

    var waBtn = document.getElementById('pdpWhatsAppBtn');
    if (waBtn) {
      var prodTitle = {{ product.title | json }};
      var text = encodeURIComponent('Hi Meenu Label! I would like to order "' + prodTitle + '" in Size ' + sizeTitle + ' from Drop 01. Please confirm piece reservation.');
      waBtn.href = 'https://wa.me/{{ settings.whatsapp_number | default: "919988898845" }}?text=' + text;
    }
  }"""

replacement_func = """  function selectShopifyPdpSize(variantId, sizeTitle, btn, isAvailable) {
    currentSelectedVariantId = variantId;
    currentSelectedSizeTitle = sizeTitle;
    var inp = document.getElementById('selectedVariantId');
    if (inp) inp.value = variantId;

    var tiles = document.querySelectorAll('.pdp-size-btn');
    tiles.forEach(function(t) { t.classList.remove('selected'); });
    if (btn) btn.classList.add('selected');

    var addBtn = document.getElementById('pdpAddToCartBtn');
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
    }

    // Switch image if variant has assigned image
    if (btn) {
      var varImg = btn.getAttribute('data-variant-image');
      if (varImg) {
        var matchThumb = document.querySelector('.pdp-thumb-item[data-src="' + varImg + '"]');
        if (matchThumb) {
          matchThumb.click();
        }
      }
    }

    var notice = document.getElementById('shopifySizeRequiredNotice');
    if (notice) notice.style.display = 'none';

    var sec = document.getElementById('shopifySizeGrid');
    if (sec) sec.classList.remove('size-error-shake');

    var waBtn = document.getElementById('pdpWhatsAppBtn');
    if (waBtn) {
      var prodTitle = {{ product.title | json }};
      var text = isAvailable === false
        ? encodeURIComponent('Hi Meenu Label! Please notify me when "' + prodTitle + '" in Size ' + sizeTitle + ' is back in stock.')
        : encodeURIComponent('Hi Meenu Label! I would like to order "' + prodTitle + '" in Size ' + sizeTitle + ' from Drop 01. Please confirm piece reservation.');
      waBtn.href = 'https://wa.me/{{ settings.whatsapp_number | default: "919988898845" }}?text=' + text;
    }
  }"""

for path in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    pills_ok = target_pills in content
    actions_ok = target_actions in content
    func_ok = target_func in content

    print(f'{path}: pills={pills_ok}, actions={actions_ok}, func={func_ok}')

    if pills_ok:
        content = content.replace(target_pills, replacement_pills, 1)
    if actions_ok:
        content = content.replace(target_actions, replacement_actions, 1)
    if func_ok:
        content = content.replace(target_func, replacement_func, 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
