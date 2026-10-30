with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'Order Directly via WhatsApp\r\n    </a>'
if target not in text:
    target = 'Order Directly via WhatsApp\n    </a>'

box = """
    <div class="whatsapp-benefit-box">
      <span class="wa-icon">&#128172;</span>
      <div>
        <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
        Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
      </div>
    </div>"""

if target in text:
    text = text.replace(target, target + box, 1)
    with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added benefit box to build_shopify_theme.py!")
else:
    print("Target not found")
