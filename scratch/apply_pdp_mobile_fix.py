mobile_css = '''
  /* ========================================================
     MOBILE RESPONSIVENESS & OVERFLOW ELIMINATION (NO SIDE CUTOFF)
     ======================================================== */
  @media (max-width: 900px) {
    .pdp-section {
      padding: 16px 14px 60px !important;
      max-width: 100vw !important;
      width: 100% !important;
      overflow-x: hidden !important;
      box-sizing: border-box !important;
    }
    .pdp-grid {
      display: flex !important;
      flex-direction: column !important;
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      gap: 20px !important;
      box-sizing: border-box !important;
    }
    .pdp-gallery-col {
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      position: static !important;
      box-sizing: border-box !important;
      height: auto !important;
    }
    .pdp-main-image-wrap {
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
    }
    .pdp-thumbnails-rail {
      display: flex !important;
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
      gap: 8px !important;
      margin-top: 10px !important;
      padding-bottom: 4px !important;
    }
    .pdp-thumb-item {
      flex: 0 0 54px !important;
      width: 54px !important;
      aspect-ratio: 4 / 5 !important;
      border-radius: 6px !important;
      box-sizing: border-box !important;
    }
    .pdp-trust-pills {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 8px !important;
      margin-top: 12px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .pdp-trust-pill {
      padding: 8px 4px !important;
      font-size: 10px !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
    }
    .pdp-trust-pill-icon {
      font-size: 15px !important;
    }
    .pdp-info-col {
      width: 100% !important;
      max-width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
      gap: 14px !important;
    }
    .pdp-top-bar {
      margin-bottom: 14px !important;
      padding-bottom: 12px !important;
      gap: 10px !important;
      width: 100% !important;
      box-sizing: border-box !important;
      flex-direction: column !important;
      align-items: flex-start !important;
    }
    .pdp-breadcrumb {
      font-size: 10.5px !important;
      line-height: 1.4 !important;
      word-break: break-word !important;
      width: 100% !important;
    }
    .pdp-title {
      font-size: 24px !important;
      line-height: 1.22 !important;
      word-break: break-word !important;
      margin: 2px 0 4px !important;
    }
    .pdp-price-row {
      flex-wrap: wrap !important;
      gap: 8px 12px !important;
      padding-bottom: 8px !important;
    }
    .pdp-price-main {
      font-size: 22px !important;
    }
    .pdp-price-mrp {
      font-size: 15px !important;
    }
    .pdp-meta-grid {
      grid-template-columns: 1fr 1fr !important;
      gap: 8px !important;
      padding: 10px 12px !important;
      font-size: 12px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .pdp-size-pills {
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 6px !important;
      width: 100% !important;
      box-sizing: border-box !important;
    }
    .pdp-size-btn {
      padding: 8px 4px !important;
      min-height: 48px !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
    }
    .pdp-size-name {
      font-size: 13px !important;
    }
    .pdp-size-sub {
      font-size: 9px !important;
    }
    .pdp-size-stock {
      font-size: 9px !important;
    }
  }
'''

# 1. Update sections/main-product.liquid
for path in ['sections/main-product.liquid', 'meenu-label-shopify-theme/sections/main-product.liquid']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert mobile_css before </style>
    if '</style>' in content and 'MOBILE RESPONSIVENESS & OVERFLOW ELIMINATION' not in content:
        content = content.replace('</style>', mobile_css + '\n</style>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path} with mobile responsiveness CSS")
    else:
        print(f"Already updated or </style> not found in {path}")
