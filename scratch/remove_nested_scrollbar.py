# Update assets/meenu-luxury.css and meenu-label-shopify-theme/assets/meenu-luxury.css
target_block = '''  .product-info-scrollable,
  .pdp-info-col {
    max-height: calc(100vh - 105px) !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    padding-right: 14px !important;
    scrollbar-width: thin;
    scrollbar-color: #D1C7BD transparent;
  }
  .product-info-scrollable::-webkit-scrollbar,
  .pdp-info-col::-webkit-scrollbar {
    width: 4px;
  }
  .product-info-scrollable::-webkit-scrollbar-track,
  .pdp-info-col::-webkit-scrollbar-track {
    background: transparent;
  }
  .product-info-scrollable::-webkit-scrollbar-thumb,
  .pdp-info-col::-webkit-scrollbar-thumb {
    background: #D1C7BD;
    border-radius: 4px;
  }'''

replacement_block = '''  .product-info-scrollable {
    max-height: calc(100vh - 105px) !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    padding-right: 14px !important;
    scrollbar-width: thin;
    scrollbar-color: #D1C7BD transparent;
  }
  .product-info-scrollable::-webkit-scrollbar {
    width: 4px;
  }
  .product-info-scrollable::-webkit-scrollbar-track {
    background: transparent;
  }
  .product-info-scrollable::-webkit-scrollbar-thumb {
    background: #D1C7BD;
    border-radius: 4px;
  }

  /* Natural Luxury Flow: Remove nested scrollbar & fill vertical space cleanly */
  .pdp-info-col {
    height: auto !important;
    max-height: none !important;
    overflow: visible !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 18px !important;
    padding-right: 0 !important;
  }'''

for path in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_block in content:
        content = content.replace(target_block, replacement_block)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path} successfully!")
    else:
        print(f"Target block not found in {path}")
