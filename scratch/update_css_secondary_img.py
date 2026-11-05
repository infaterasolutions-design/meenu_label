css_add = '''
    .card-thumb .card-img-secondary {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      opacity: 0;
      transition: opacity 0.4s ease, transform 0.4s ease;
      pointer-events: none;
    }
    .product-card:hover .card-thumb .card-img-secondary {
      opacity: 1;
      transform: scale(1.05);
    }
'''

for path in ['assets/meenu-luxury.css', 'meenu-label-shopify-theme/assets/meenu-luxury.css']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = ".product-card:hover .card-thumb img {"
    if target in content and ".card-thumb .card-img-secondary" not in content:
        content = content.replace(target, css_add + "\n    " + target, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Skipped {path}")
