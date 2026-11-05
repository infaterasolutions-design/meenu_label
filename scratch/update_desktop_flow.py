desktop_flow_css = '''
  /* Ensure Natural Desktop Flow & No Blank Bottom Space */
  @media (min-width: 901px) {
    .pdp-info-col {
      height: auto !important;
      max-height: none !important;
      overflow: visible !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 18px !important;
      padding-right: 0 !important;
    }
    .pdp-gallery-col {
      position: -webkit-sticky !important;
      position: sticky !important;
      top: 105px !important;
      align-self: start !important;
      height: fit-content !important;
    }
  }
'''

for path in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '</style>' in content and 'Ensure Natural Desktop Flow & No Blank Bottom Space' not in content:
        content = content.replace('</style>', desktop_flow_css + '\n</style>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Already updated or </style> not found in {path}")
