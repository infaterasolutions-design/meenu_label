import os, base64

scratch_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch"
highres_dir = os.path.join(scratch_dir, "highres_products")
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
downloads_dir = r"C:\Users\sande\Downloads"

def get_b64(fname):
    p = os.path.join(highres_dir, fname)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

b64_polka = get_b64('JAA26DR03942.jpg')
b64_gulabi = get_b64('JAC25ST03063.jpg')
b64_chanderi = get_b64('JAB26ST05010.jpg')
b64_angrakha = get_b64('SET974.jpg')
b64_halter = get_b64('SET916.jpg')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meenu Label • Drop 01 Storefront Design</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #FAF8F5;
      --card-bg: #FFFFFF;
      --text-main: #1E1C19;
      --text-muted: #82786C;
      --border: #E8E2D8;
      --accent: #9A7B4F;
      --btn-dark: #1E1C19;
      --green-tag: #2E7D46;
      --red-tag: #C53030;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #EFECE6;
      color: var(--text-main);
      display: flex;
      justify-content: center;
      padding: 24px 12px;
    }}
    .phone-container {{
      width: 100%;
      max-width: 430px;
      background: var(--bg);
      border-radius: 44px;
      box-shadow: 0 25px 60px rgba(0,0,0,0.22);
      overflow: hidden;
      border: 10px solid #1C1917;
      display: flex;
      flex-direction: column;
      min-height: 880px;
      position: relative;
    }}
    .top-bar {{
      background: #1E1C19;
      color: #FAF8F5;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-align: center;
      padding: 8px 12px;
    }}
    header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      background: var(--bg);
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .brand-logo {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      letter-spacing: 0.2em;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--text-main);
    }}
    .icon-btn {{
      background: none;
      border: none;
      cursor: pointer;
      font-size: 18px;
    }}
    .hero {{
      position: relative;
      height: 340px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 24px 20px;
      background: #000;
    }}
    .hero img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.88;
    }}
    .hero-content {{
      position: relative;
      z-index: 10;
      color: #FFF;
    }}
    .hero-eyebrow {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #E6D5B8;
      margin-bottom: 4px;
    }}
    .hero-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 30px;
      line-height: 1.15;
      font-weight: 600;
      margin-bottom: 12px;
    }}
    .hero-btn {{
      display: inline-block;
      background: #FAF8F5;
      color: #1E1C19;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 10px 18px;
      border-radius: 6px;
      text-decoration: none;
    }}
    .filter-bar {{
      display: flex;
      gap: 8px;
      padding: 14px 16px;
      overflow-x: auto;
      border-bottom: 1px solid var(--border);
    }}
    .filter-bar::-webkit-scrollbar {{ display: none; }}
    .pill {{
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      border: 1px solid var(--border);
      background: #F2EFE9;
      color: var(--text-main);
    }}
    .pill.active {{
      background: #1E1C19;
      color: #FAF8F5;
      border-color: #1E1C19;
    }}
    .grid-container {{
      padding: 16px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }}
    .product-card {{
      background: #FFF;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
      cursor: pointer;
      transition: transform 0.15s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
    }}
    .card-img-wrap {{
      position: relative;
      height: 220px;
      background: #F4F1EB;
    }}
    .card-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .badge-scarcity {{
      position: absolute;
      top: 8px;
      left: 8px;
      background: var(--red-tag);
      color: #FFF;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.06em;
      padding: 3px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }}
    .badge-festive {{
      position: absolute;
      top: 8px;
      left: 8px;
      background: var(--green-tag);
      color: #FFF;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.06em;
      padding: 3px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }}
    .card-info {{
      padding: 10px;
    }}
    .card-title {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .card-sub {{
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}
    .price-row {{
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin-bottom: 6px;
    }}
    .price-cur {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .price-mrp {{
      font-size: 11px;
      text-decoration: line-through;
      color: #A39A8E;
    }}
    .sizes-tag {{
      font-size: 10px;
      font-weight: 600;
      color: var(--accent);
      background: #FAF6EE;
      padding: 2px 4px;
      border-radius: 3px;
      display: inline-block;
    }}
    .trust-strip {{
      margin: 10px 16px 20px;
      background: #F4EFEB;
      border-radius: 8px;
      padding: 12px 14px;
      border: 1px solid #E5DFD4;
      font-size: 11px;
      line-height: 1.5;
    }}
    .trust-strip strong {{
      color: #1E1C19;
      display: block;
      margin-bottom: 2px;
    }}
    .tab-bar {{
      display: flex;
      justify-content: space-around;
      padding: 14px 0;
      border-top: 1px solid var(--border);
      background: #FAF8F5;
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
    }}
    .tab-bar .active {{
      color: #1E1C19;
      font-weight: 700;
    }}
  </style>
</head>
<body>

  <div class="phone-container">
    <div class="top-bar">
      ✨ DROP 01 LIVE • FREE TRICITY DELIVERY • MEENULABEL.COM
    </div>

    <header>
      <button class="icon-btn">☰</button>
      <div class="brand-logo">MEENU LABEL</div>
      <button class="icon-btn">🛍️ <span style="font-size: 12px; font-weight:700;">(0)</span></button>
    </header>

    <div class="hero">
      <img src="{b64_chanderi}" alt="Debut Collection">
      <div class="hero-content">
        <div class="hero-eyebrow">The Debut Collection</div>
        <div class="hero-title">Effortless Everyday<br>Luxury Silhouettes</div>
        <a href="#collection" class="hero-btn">Shop Drop 01 →</a>
      </div>
    </div>

    <div class="filter-bar" id="collection">
      <div class="pill active">All (13)</div>
      <div class="pill">Co-ords</div>
      <div class="pill">Festive Suits</div>
      <div class="pill">Dresses</div>
      <div class="pill">Tops</div>
    </div>

    <div class="grid-container">
      <div class="product-card">
        <div class="card-img-wrap">
          <img src="{b64_polka}" alt="Polka Dress">
          <div class="badge-scarcity">Only 3 Left</div>
        </div>
        <div class="card-info">
          <div class="card-title">Retro Polka Wrap Dress</div>
          <div class="card-sub">Pure Breathable Cotton</div>
          <div class="price-row">
            <span class="price-cur">₹1,499</span>
            <span class="price-mrp">₹2,499</span>
          </div>
          <div class="sizes-tag">Sizes: M • L • XL</div>
        </div>
      </div>

      <div class="product-card">
        <div class="card-img-wrap">
          <img src="{b64_gulabi}" alt="Gulabi Festive Suit">
          <div class="badge-festive">Limited Run</div>
        </div>
        <div class="card-info">
          <div class="card-title">Gulabi Organza Suit</div>
          <div class="card-sub">Cotton Silk 3-Pc Set</div>
          <div class="price-row">
            <span class="price-cur">₹2,199</span>
            <span class="price-mrp">₹3,499</span>
          </div>
          <div class="sizes-tag">Sizes: M • L • XL</div>
        </div>
      </div>

      <div class="product-card">
        <div class="card-img-wrap">
          <img src="{b64_angrakha}" alt="Angrakha Co-ord">
          <div class="badge-scarcity">Selling Fast</div>
        </div>
        <div class="card-info">
          <div class="card-title">Mustard Angrakha Set</div>
          <div class="card-sub">Crepe Silk Wrap 2-Pc</div>
          <div class="price-row">
            <span class="price-cur">₹1,699</span>
            <span class="price-mrp">₹2,799</span>
          </div>
          <div class="sizes-tag">Sizes: M • L • XL</div>
        </div>
      </div>

      <div class="product-card">
        <div class="card-img-wrap">
          <img src="{b64_halter}" alt="Halter Co-ord">
          <div class="badge-festive">New Arrival</div>
        </div>
        <div class="card-info">
          <div class="card-title">Lime Halter Palazzo</div>
          <div class="card-sub">Dobby Chiffon 2-Pc</div>
          <div class="price-row">
            <span class="price-cur">₹1,599</span>
            <span class="price-mrp">₹2,599</span>
          </div>
          <div class="sizes-tag">Sizes: M • L • XL</div>
        </div>
      </div>
    </div>

    <div class="trust-strip">
      <strong>⚡ Priority 24-Hr Delivery in Tricity</strong>
      Chandigarh, Mohali & Panchkula same-day dispatch. 7-Day easy size exchange guarantee.
    </div>

    <div class="tab-bar">
      <div class="active">Home</div>
      <div>Shop</div>
      <div>Search</div>
      <div>Bag (0)</div>
    </div>
  </div>

</body>
</html>
"""

with open(os.path.join(artifacts_dir, "Meenu_Label_Storefront_Interactive.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

with open(os.path.join(downloads_dir, "Meenu_Label_Storefront_Interactive.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated Meenu_Label_Storefront_Interactive.html successfully!")
