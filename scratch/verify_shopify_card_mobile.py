import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

# HTML specifically simulating the user's two cards from their screenshot:
# Card 1: The Artisanal Abstract V-Neck Top, Rs. 1,899.00, Rs. 2,999.00
# Card 2: The Contemporary Floral Embroidered Top, Rs. 1,899.00, Rs. 2,999.00

with open("assets/meenu-luxury.css", "r", encoding="utf-8") as f:
    css = f.read()

test_page = f"""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
{css}
body {{
  background: #FAF8F5;
  margin: 0;
  padding: 16px 0;
  font-family: 'Plus Jakarta Sans', sans-serif;
}}
.demo-header {{
  padding: 0 14px 12px;
  font-size: 14px;
  font-weight: 700;
  color: #1A1A1A;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}}
</style>
</head>
<body>
<div class="demo-header">Drop 01 Silhouettes (Mobile 2-Col View)</div>
<div class="product-grid">
  <!-- Card 1 -->
  <div class="product-card">
    <div class="card-thumb">
      <img src="file:///c:/Users/sande/Documents/antigravity/splendid-nobel/assets/JAA26DR03942_1.jpg" class="card-img-primary" alt="The Artisanal Abstract V-Neck Top">
      <button type="button" class="card-wishlist-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
      </button>
    </div>
    <div class="card-body">
      <h3 class="card-title">The Artisanal Abstract V-Neck Top</h3>
      <div class="card-price-row">
        <div class="card-price-left">
          <span class="price-main">Rs. 1,899.00</span>
          <div class="card-price-compare-wrap">
            <span class="price-mrp">Rs. 2,999.00</span>
            <span class="price-discount">37% OFF</span>
          </div>
        </div>
        <button type="button" class="snitch-plus-trigger">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="3" x2="12" y2="15"></line><line x1="6" y1="9" x2="18" y2="9"></line><line x1="4" y1="19" x2="20" y2="19"></line></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Card 2 -->
  <div class="product-card">
    <div class="card-thumb">
      <img src="file:///c:/Users/sande/Documents/antigravity/splendid-nobel/assets/TXC26TP04098_1.jpg" class="card-img-primary" alt="The Contemporary Floral Embroidered Top">
      <button type="button" class="card-wishlist-btn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
      </button>
    </div>
    <div class="card-body">
      <h3 class="card-title">The Contemporary Floral Embroidered Top</h3>
      <div class="card-price-row">
        <div class="card-price-left">
          <span class="price-main">Rs. 1,899.00</span>
          <div class="card-price-compare-wrap">
            <span class="price-mrp">Rs. 2,999.00</span>
            <span class="price-discount">37% OFF</span>
          </div>
        </div>
        <button type="button" class="snitch-plus-trigger">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="3" x2="12" y2="15"></line><line x1="6" y1="9" x2="18" y2="9"></line><line x1="4" y1="19" x2="20" y2="19"></line></svg>
        </button>
      </div>
    </div>
  </div>
</div>
</body>
</html>"""

demo_path = os.path.join(scratch_dir, "temp_demo_shopify_cards.html")
with open(demo_path, "w", encoding="utf-8") as f:
    f.write(test_page)

shot_shopify_mob = os.path.join(artifacts_dir, "verified_shopify_cards_mobile.png")
cmd = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_shopify_cards')}",
    "--window-size=390,750",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_shopify_mob}",
    demo_path
]

print("Running exact Shopify Cards Mobile Screenshot Test (390x750)...")
subprocess.run(cmd, check=True)
print("Captured:", shot_shopify_mob)
