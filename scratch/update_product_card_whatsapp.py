liquid_target = """      {% else %}
        <button type="button" class="snitch-notify-trigger" 
                data-product-id="{{ product.id }}"
                data-product-title="{{ product.title | escape }}"
                data-product-price="{{ product.price | money | escape }}"
                data-product-image="{{ product.featured_image | default: product.images.first | image_url: width: 400 }}"
                data-product-url="{{ product.url }}"
                onclick="event.preventDefault(); event.stopPropagation(); openNotifyMeModal('{{ product.id }}', 'M', '{{ product.title | escape }}', '{{ product.featured_image | default: product.images.first | image_url: width: 400 }}', '{{ product.price | money | escape }}')" 
                title="Sold Out - Notify Me When Available" 
                aria-label="Notify Me When Available">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
          <span class="notify-btn-text">NOTIFY ME</span>
        </button>
      {% endif %}"""

liquid_replacement = """      {% else %}
        <a class="snitch-notify-trigger whatsapp-notify-trigger" 
           href="https://wa.me/{{ settings.whatsapp_number | default: '919988898845' }}?text={{ 'Hi Meenu Label! Please notify me when \"' | append: product.title | append: '\" is back in stock. Please share restock timeline.' | url_encode }}"
           target="_blank"
           onclick="event.stopPropagation();" 
           title="Notify Me on WhatsApp When Restocked" 
           aria-label="Notify Me on WhatsApp When Restocked">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.953 1.18-.175.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.151-.176.201-.301.301-.502.101-.201.05-.376-.025-.527-.075-.15-.678-1.634-.929-2.237-.245-.588-.493-.508-.678-.518-.175-.01-.376-.01-.577-.01-.201 0-.527.075-.803.376s-1.054 1.029-1.054 2.511c0 1.482 1.079 2.913 1.23 3.114.15.201 2.122 3.24 5.14 4.544.718.31 1.279.496 1.716.635.722.23 1.379.197 1.9.119.58-.088 1.78-.727 2.03-1.43.251-.703.251-1.305.176-1.43-.075-.126-.276-.201-.577-.351z"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2.05 21.95l4.908-1.353C8.414 21.49 10.15 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18.2c-1.61 0-3.13-.45-4.43-1.23l-.317-.189-2.906.801.815-2.833-.207-.328A8.152 8.152 0 0 1 3.8 12c0-4.52 3.68-8.2 8.2-8.2 4.52 0 8.2 3.68 8.2 8.2 0 4.52-3.68 8.2-8.2 8.2z"/>
          </svg>
          <span class="notify-btn-text">NOTIFY ON WHATSAPP</span>
        </a>
      {% endif %}"""

for p in ['snippets/product-card.liquid', 'meenu-label-shopify-theme/snippets/product-card.liquid']:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if liquid_target in content:
        content = content.replace(liquid_target, liquid_replacement, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated:", p)
    else:
        print("Target not found in:", p)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

index_target = """          <button type="button" class="snitch-notify-trigger" data-product-id="JAB25ST02661" onclick="event.preventDefault(); event.stopPropagation(); openNotifyMeModal('JAB25ST02661', 'M', 'The Noor Petrol Teal Chanderi Suit', '', '&#8377;2,999')" title="Sold Out - Notify Me When Available" aria-label="Notify Me When Available">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
            </svg>
            <span class="notify-btn-text">NOTIFY ME</span>
          </button>"""

index_replacement = """          <a class="snitch-notify-trigger whatsapp-notify-trigger" data-product-id="JAB25ST02661" href="https://wa.me/919988898845?text=Hi%20Meenu%20Label!%20Please%20notify%20me%20when%20%22The%20Noor%20Petrol%20Teal%20Chanderi%20Suit%22%20is%20back%20in%20stock.%20Please%20share%20restock%20timeline." target="_blank" onclick="event.stopPropagation();" title="Notify Me on WhatsApp When Restocked" aria-label="Notify Me on WhatsApp When Restocked">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.1-.477-.15-.678.15-.2.301-.778.98-.953 1.18-.175.2-.351.226-.652.075-.301-.15-1.272-.469-2.423-1.496-.896-.799-1.501-1.786-1.677-2.087-.175-.301-.019-.464.132-.614.135-.135.301-.351.451-.527.151-.176.201-.301.301-.502.101-.201.05-.376-.025-.527-.075-.15-.678-1.634-.929-2.237-.245-.588-.493-.508-.678-.518-.175-.01-.376-.01-.577-.01-.201 0-.527.075-.803.376s-1.054 1.029-1.054 2.511c0 1.482 1.079 2.913 1.23 3.114.15.201 2.122 3.24 5.14 4.544.718.31 1.279.496 1.716.635.722.23 1.379.197 1.9.119.58-.088 1.78-.727 2.03-1.43.251-.703.251-1.305.176-1.43-.075-.126-.276-.201-.577-.351z"/>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2.05 21.95l4.908-1.353C8.414 21.49 10.15 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18.2c-1.61 0-3.13-.45-4.43-1.23l-.317-.189-2.906.801.815-2.833-.207-.328A8.152 8.152 0 0 1 3.8 12c0-4.52 3.68-8.2 8.2-8.2 4.52 0 8.2 3.68 8.2 8.2 0 4.52-3.68 8.2-8.2 8.2z"/>
            </svg>
            <span class="notify-btn-text">NOTIFY ON WHATSAPP</span>
          </a>"""

if index_target in idx_content:
    idx_content = idx_content.replace(index_target, index_replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print("Updated: index.html card JAB25ST02661")
else:
    print("index_target not found in index.html")
