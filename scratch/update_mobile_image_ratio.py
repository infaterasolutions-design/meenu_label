target_old = '''    .pdp-main-image-wrap {
      width: 100% !important;
      max-width: 100% !important;
      border-radius: 12px !important;
      overflow: hidden !important;
      box-sizing: border-box !important;
      position: relative !important;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06) !important;
    }
    .pdp-main-image {
      width: 100% !important;
      max-width: 100% !important;
      height: auto !important;
      aspect-ratio: 4 / 5 !important;
      max-height: 52vh !important;
      object-fit: cover !important;
      object-position: top center !important;
      display: block !important;
    }'''

target_new = '''    .pdp-main-image-wrap {
      width: 100% !important;
      max-width: 100% !important;
      aspect-ratio: 4 / 5 !important;
      border-radius: 12px !important;
      overflow: hidden !important;
      box-sizing: border-box !important;
      position: relative !important;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06) !important;
      background: #F4EFEB !important;
    }
    .pdp-main-image {
      width: 100% !important;
      height: 100% !important;
      aspect-ratio: 4 / 5 !important;
      object-fit: cover !important;
      object-position: top center !important;
      display: block !important;
    }'''

files_to_update = [
    'sections/main-product.liquid',
    'meenu-label-shopify-theme/sections/main-product.liquid',
    'assets/meenu-luxury.css',
    'meenu-label-shopify-theme/assets/meenu-luxury.css',
    'index.html'
]

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_old in content:
        content = content.replace(target_old, target_new)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path} successfully!")
    else:
        print(f"Target not found in {file_path}")
