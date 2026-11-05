with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update pdp-grid
old_pdp_grid = '''.pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 56px;
      align-items: flex-start;
    }'''

new_pdp_grid = '''.pdp-grid {
      display: grid;
      grid-template-columns: 440px 1fr;
      gap: 44px;
      align-items: flex-start;
      max-width: 1080px;
      margin: 0 auto;
    }'''

assert old_pdp_grid in html, "old_pdp_grid not found"
html = html.replace(old_pdp_grid, new_pdp_grid)

# Update pdp-main-image-wrap and pdp-main-image
old_wrap = '''.pdp-main-image-wrap {
      position: relative;
      width: 100%;
      border-radius: 12px;
      overflow: hidden;
      background: #F4EFEB;
      border: 1px solid var(--border-color);
      box-shadow: 0 12px 30px rgba(0,0,0,0.04);
    }
    .pdp-main-image {
      width: 100%;
      aspect-ratio: 4 / 5;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.4s ease;
    }'''

new_wrap = '''.pdp-main-image-wrap {
      position: relative;
      width: 100%;
      height: 460px;
      max-height: 68vh;
      border-radius: 10px;
      overflow: hidden;
      background: #FAF7F2;
      border: 1px solid var(--border-color);
      box-shadow: 0 4px 18px rgba(0,0,0,0.04);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .pdp-main-image {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      display: block;
      margin: 0 auto;
      transition: transform 0.3s ease, opacity 0.2s ease;
    }'''

assert old_wrap in html, "old_wrap not found"
html = html.replace(old_wrap, new_wrap)

# Price row nowrap in index.html
old_price_row = '''.pdp-price-row {
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin-bottom: 8px;
    }'''

new_price_row = '''.pdp-price-row {
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 8px;
      white-space: nowrap;
      flex-wrap: nowrap;
    }
    .pdp-price-main, .pdp-price-mrp, .pdp-price-discount {
      white-space: nowrap;
    }'''

if old_price_row in html:
    html = html.replace(old_price_row, new_price_row)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
