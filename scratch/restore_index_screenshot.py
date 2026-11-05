with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore original pdp-grid in index.html
old_grid = '''.pdp-grid {
      display: grid;
      grid-template-columns: 440px 1fr;
      gap: 44px;
      align-items: flex-start;
      max-width: 1080px;
      margin: 0 auto;
    }'''

original_grid = '''.pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 56px;
      align-items: flex-start;
    }'''

if old_grid in html:
    html = html.replace(old_grid, original_grid)
    print("Restored original pdp-grid in index.html")

# Restore original pdp-main-image-wrap in index.html
old_wrap = '''.pdp-main-image-wrap {
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

original_wrap = '''.pdp-main-image-wrap {
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
      transition: transform 0.4s ease, opacity 0.2s ease;
    }'''

if old_wrap in html:
    html = html.replace(old_wrap, original_wrap)
    print("Restored original pdp-main-image-wrap in index.html")

# Badges in index.html
old_badge = '''            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">DROP 01 STAR</span>
              <span class="pdp-badge-pill pdp-badge-gold" id="pdpCounterPill">STRICTLY 3 PIECES CRAFTED</span>
            </div>'''

screen_badge = '''            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">FLAGSHIP HERO</span>
              <span class="pdp-badge-pill pdp-badge-gold" id="pdpCounterPill">STRICTLY 3 PIECES CRAFTED</span>
            </div>'''

if old_badge in html:
    html = html.replace(old_badge, screen_badge)
    print("Updated badges in index.html to match screenshot")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")
