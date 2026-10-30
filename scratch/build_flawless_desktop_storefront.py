import os, base64, json

highres_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66\scratch\highres_products"
downloads_dir = r"C:\Users\sande\Downloads"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"

def get_b64(fname):
    p = os.path.join(highres_dir, fname)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

products = [
    {
        "id": "JAB26ST05010",
        "code": "JAB26ST05010",
        "name": "Jaipur Chanderi Silk Festive Suit",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Chanderi Silk & Zari with Organza Dupatta",
        "color": "Warm Mustard & Fuchsia",
        "price": 2299,
        "mrp": 3699,
        "badge": "Drop 01 Star",
        "badge_class": "badge-exclusive",
        "desc": "An iconic 3-piece festive ensemble featuring a straight-cut Chanderi kurta with delicate zari V-neck piping, tailored cigarette trousers, and a lightweight printed organza dupatta that drapes effortlessly for celebratory occasions.",
        "img_file": "JAB26ST05010.jpg"
    },
    {
        "id": "JAA26DR03942",
        "code": "JAA26DR03942",
        "name": "The Retro Polka Dot Wrap Dress",
        "category": "dress",
        "cat_label": "Dresses",
        "fabric": "100% Breathable Pure Cotton",
        "color": "Monochrome Polka Dot",
        "price": 1499,
        "mrp": 2499,
        "badge": "Only 3 Left",
        "badge_class": "badge-scarcity",
        "desc": "Timeless 1950s chic reimagined. Wrap silhouette with adjustable waist sash, flared A-line skirt, and breathable pure cotton weave. Featured on our debut Instagram campaign.",
        "img_file": "JAA26DR03942.jpg"
    },
    {
        "id": "JAC25ST03063",
        "code": "JAC25ST03063",
        "name": "The Gulabi Organza Festive Suit",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Cotton Silk Blend & Sheer Organza",
        "color": "Powder Pink (Gulabi)",
        "price": 2199,
        "mrp": 3499,
        "badge": "Limited Edition",
        "badge_class": "badge-exclusive",
        "desc": "Subtle luxury in powder pink. Straight-cut kurta with delicate neckline zari border, matching tailored trousers, and a rich heritage floral-printed organza dupatta with golden tassels.",
        "img_file": "JAC25ST03063.jpg"
    },
    {
        "id": "SET974",
        "code": "SET974",
        "name": "Mustard Crepe Angrakha Co-ord Set",
        "category": "coord",
        "cat_label": "Co-ord Sets",
        "fabric": "Fluid Crepe Silk",
        "color": "Rich Mustard Gold",
        "price": 1699,
        "mrp": 2799,
        "badge": "Only 3 Left",
        "badge_class": "badge-scarcity",
        "desc": "A contemporary royal wrap silhouette. Tailored in fluid crepe silk with an overlapping Angrakha neckline trimmed in gold gota patti and playful side latkan tassels. Paired with matching silk trousers.",
        "img_file": "SET974.jpg"
    },
    {
        "id": "SET916",
        "code": "SET916",
        "name": "Lime Halter Dobby Palazzo Set",
        "category": "coord",
        "cat_label": "Co-ord Sets",
        "fabric": "Dobby Chiffon & Cotton Lining",
        "color": "Chartreuse Lime",
        "price": 1649,
        "mrp": 2699,
        "badge": "Trending",
        "badge_class": "badge-trending",
        "desc": "Breezy and modern. Flattering halter-style high-neck top in textured dobby chiffon paired with fluid wide-leg palazzo pants. Lightweight, breathable, and head-turning.",
        "img_file": "SET916.jpg"
    },
    {
        "id": "JAA26DR04449",
        "code": "JAA26DR04449",
        "name": "Navy Botanical Georgette Midi Dress",
        "category": "dress",
        "cat_label": "Dresses",
        "fabric": "Flowing Georgette with Voile Lining",
        "color": "Deep Navy Multi-Floral",
        "price": 1699,
        "mrp": 2799,
        "badge": "Bestseller",
        "badge_class": "badge-trending",
        "desc": "Graceful garden silhouette. Full balloon sleeves, elasticated waist cinching, and tiered ruffled midi hem in deep navy blooming print. A dream for outdoor sundowners.",
        "img_file": "JAA26DR04449.jpg"
    },
    {
        "id": "TXC26KB04820",
        "code": "TXC26KB04820",
        "name": "Lime Silk V-Neck Tunic Co-ord",
        "category": "coord",
        "cat_label": "Co-ord Sets",
        "fabric": "Silk Blend",
        "color": "Citrus Lime",
        "price": 1749,
        "mrp": 2899,
        "badge": "Selling Fast",
        "badge_class": "badge-scarcity",
        "desc": "Clean-lined minimalism. Featuring a modern V-neck tunic top in lustrous lime silk blend paired with relaxed ankle-length cigarette pants. Ideal for elevated brunches or festive workwear.",
        "img_file": "TXC26KB04820.jpg"
    },
    {
        "id": "JAC25CD03428",
        "code": "JAC25CD03428",
        "name": "Porcelain Ivory Embroidered Co-ord",
        "category": "coord",
        "cat_label": "Co-ord Sets",
        "fabric": "Premium Cotton Blend",
        "color": "Porcelain Ivory & Tan",
        "price": 1549,
        "mrp": 2499,
        "badge": "Workwear Luxe",
        "badge_class": "badge-exclusive",
        "desc": "The ultimate boardroom-to-brunch ensemble. Ivory longline tunic with minimal collar embroidery and matching tapered trousers tailored for all-day comfort.",
        "img_file": "JAC25CD03428.jpg"
    },
    {
        "id": "JNE4046",
        "code": "JNE4046",
        "name": "White Porcelain Floral Wrap Dress",
        "category": "dress",
        "cat_label": "Dresses",
        "fabric": "Airy Crepe Georgette",
        "color": "Crisp White & Cobalt Florals",
        "price": 1599,
        "mrp": 2599,
        "badge": "Only 3 Left",
        "badge_class": "badge-scarcity",
        "desc": "Resort elegance. Pure white wrap dress with Mediterranean cobalt floral motifs, 3/4 sleeves, and a matching fabric belt with circular buckle.",
        "img_file": "JNE4046.jpg"
    },
    {
        "id": "JAB24ST00932",
        "code": "JAB24ST00932",
        "name": "Midnight Botanical 3-Piece Fusion Set",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Fine Georgette & Crepe",
        "color": "Midnight Black & Florals",
        "price": 1899,
        "mrp": 2999,
        "badge": "Fusion Edit",
        "badge_class": "badge-trending",
        "desc": "A standout evening fusion set. Includes a cropped inner bodice, straight comfort trousers, and an ethereal printed floor-length overlay cape shrug for effortless movement.",
        "img_file": "JAB24ST00932.jpg"
    },
    {
        "id": "TXC26TP04108",
        "code": "TXC26TP04108",
        "name": "Artisanal Abstract V-Neck Blouse",
        "category": "top",
        "cat_label": "Tops & Blouses",
        "fabric": "Chiffon Crepe",
        "color": "Multi-Color Earth Print",
        "price": 999,
        "mrp": 1799,
        "badge": "Under ₹1000",
        "badge_class": "badge-trending",
        "desc": "Statement daytime blouse featuring an abstract artisanal brushstroke print, elegant V-neckline, and relaxed fluid drape that tucks easily into palazzos or trousers.",
        "img_file": "TXC26TP04108.jpg"
    },
    {
        "id": "TXC26TP04098",
        "code": "TXC26TP04098",
        "name": "Monochrome Foliage V-Neck Top",
        "category": "top",
        "cat_label": "Tops & Blouses",
        "fabric": "Fine Silk Crepe",
        "color": "Ivory & Botanical Ink",
        "price": 899,
        "mrp": 1499,
        "badge": "Under ₹1000",
        "badge_class": "badge-trending",
        "desc": "Effortless casual elegance. Lightweight crepe top with subtle botanical leaf sketches, perfect paired with cigarette trousers or high-rise denims for daily meetings.",
        "img_file": "TXC26TP04098.jpg"
    },
    {
        "id": "ZAC26TP04826",
        "code": "ZAC26TP04826",
        "name": "Contemporary Floral Everyday Blouse",
        "category": "top",
        "cat_label": "Tops & Blouses",
        "fabric": "Poly-Crepe Comfort Weave",
        "color": "Black & White Botanical",
        "price": 949,
        "mrp": 1599,
        "badge": "Everyday Essential",
        "badge_class": "badge-exclusive",
        "desc": "Minimalist everyday blouse featuring mandarin collar detailing, half placket buttons, and wrinkle-resistant easy-care fabric for modern working women.",
        "img_file": "ZAC26TP04826.jpg"
    }
]

print("Loading base64 images for all 13 products...")
for p in products:
    p["b64"] = get_b64(p["img_file"])

hero_b64 = products[0]["b64"] # Jaipur Chanderi Silk Suit

# Generate pre-rendered product cards HTML
cards_html = ""
for p in products:
    discount = round(((p["mrp"] - p["price"]) / p["mrp"]) * 100)
    cards_html += f"""
    <div class="product-card" data-category="{p['category']}" data-id="{p['id']}">
      <div class="card-thumb" onclick="openProductModal('{p['id']}')">
        <span class="card-badge {p['badge_class']}">{p['badge']}</span>
        <img src="{p['b64']}" alt="{p['name']}" loading="lazy">
        <div class="card-quick-actions">
          <button class="btn-quick-view" onclick="event.stopPropagation(); openProductModal('{p['id']}')">QUICK VIEW 👁️</button>
        </div>
      </div>
      <div class="card-body">
        <span class="card-cat">{p['cat_label']}</span>
        <h3 class="card-title" onclick="openProductModal('{p['id']}')">{p['name']}</h3>
        <div class="card-fabric">{p['fabric']}</div>
        <div class="card-price-row">
          <span class="price-main">₹{p['price']:,}</span>
          <span class="price-mrp">₹{p['mrp']:,}</span>
          <span class="price-discount">{discount}% OFF</span>
        </div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'M')">M (38)</span>
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'L')">L (40)</span>
            <span class="size-chip" onclick="quickAddCart('{p['id']}', 'XL')">XL (42)</span>
          </div>
          <span class="stock-chip">Only 3 Left</span>
        </div>
      </div>
    </div>
    """

# Minimal sanitized products data for JavaScript (id, name, code, price, mrp, desc, fabric, badge, badge_class, b64)
js_products_data = json.dumps([{
    "id": p["id"],
    "code": p["code"],
    "name": p["name"],
    "price": p["price"],
    "mrp": p["mrp"],
    "desc": p["desc"],
    "fabric": p["fabric"],
    "badge": p["badge"],
    "badge_class": p["badge_class"],
    "b64": p["b64"]
} for p in products])

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meenu Label • Contemporary Ethnic & Fusion Wear | meenulabel.com</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-primary: #FAF8F5;
      --bg-card: #FFFFFF;
      --bg-surface: #F3EFE8;
      --text-main: #1E1C19;
      --text-muted: #7A7267;
      --text-light: #9B9387;
      --border-color: #E6E0D6;
      --accent-gold: #9E7D47;
      --accent-rose: #B83A3A;
      --accent-green: #2B6E44;
      --btn-dark: #1E1C19;
      --btn-hover: #332F2A;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    /* Top Marquee */
    .announcement-bar {
      background: var(--text-main);
      color: #FAF8F5;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 9px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .announcement-bar a { color: #E8D3B9; text-decoration: none; margin-left: 14px; }

    /* Main Header Structure: 2 Distinct Clean Rows (Never Overlap!) */
    header {
      background: rgba(250, 248, 245, 0.98);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 34px;
      z-index: 90;
    }
    .header-top-row {
      max-width: 1400px;
      margin: 0 auto;
      padding: 18px 40px 10px;
      text-align: center;
    }
    .brand-logo {
      font-family: 'Cormorant Garamond', serif;
      font-size: 42px;
      font-weight: 600;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: var(--text-main);
      text-decoration: none;
      display: inline-block;
    }
    .brand-sub {
      font-size: 10px;
      letter-spacing: 0.25em;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-top: -4px;
      display: block;
    }

    /* Second Row: Navigation and Actions */
    .header-nav-row {
      max-width: 1400px;
      margin: 0 auto;
      padding: 10px 40px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(230, 224, 214, 0.5);
    }
    .nav-links {
      display: flex;
      gap: 30px;
      list-style: none;
    }
    .nav-links a {
      color: var(--text-main);
      text-decoration: none;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      transition: color 0.15s;
      position: relative;
    }
    .nav-links a:hover, .nav-links a.active {
      color: var(--accent-gold);
    }
    .nav-links a.active::after {
      content: '';
      position: absolute;
      bottom: -6px;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--text-main);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .search-box {
      display: flex;
      align-items: center;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 13px;
    }
    .search-box input {
      border: none;
      outline: none;
      background: transparent;
      margin-left: 8px;
      width: 150px;
      font-size: 13px;
    }
    .header-btn {
      background: none;
      border: none;
      cursor: pointer;
      font-size: 14px;
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 6px;
    }
    .header-btn:hover { background: var(--bg-surface); }
    .cart-badge {
      background: var(--text-main);
      color: #FAF8F5;
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 10px;
      font-weight: 700;
    }

    /* Hero Editorial Section */
    .hero-section {
      max-width: 1400px;
      margin: 30px auto;
      padding: 0 40px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: center;
    }
    .hero-card {
      background: #FAF5ED;
      border-radius: 16px;
      padding: 55px 45px;
      border: 1px solid var(--border-color);
    }
    .hero-tag {
      display: inline-block;
      background: #EFE4D2;
      color: var(--accent-gold);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 20px;
    }
    .hero-heading {
      font-family: 'Cormorant Garamond', serif;
      font-size: 50px;
      line-height: 1.12;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 18px;
    }
    .hero-desc {
      font-size: 16px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 30px;
      max-width: 500px;
    }
    .hero-cta-group {
      display: flex;
      gap: 16px;
      align-items: center;
    }
    .btn-primary {
      background: var(--btn-dark);
      color: #FAF8F5;
      padding: 14px 28px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: inline-block;
      border: none;
      cursor: pointer;
      transition: background 0.15s, transform 0.1s;
    }
    .btn-primary:hover { background: var(--btn-hover); transform: translateY(-1px); }
    .btn-secondary {
      background: transparent;
      color: var(--text-main);
      padding: 13px 24px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.05em;
      border: 1px solid var(--border-color);
      cursor: pointer;
    }
    .btn-secondary:hover { background: #FFFFFF; }

    .hero-media-wrap {
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      height: 540px;
      box-shadow: 0 15px 35px rgba(0,0,0,0.08);
      border: 1px solid var(--border-color);
      background: #F4EFEB;
    }
    .hero-media-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 20%;
      display: block;
    }
    .hero-overlay-pill {
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(8px);
      padding: 12px 20px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }
    .hero-overlay-pill .name { font-weight: 700; font-size: 14px; color: var(--text-main); }
    .hero-overlay-pill .meta { font-size: 12px; color: var(--text-muted); }

    /* Catalog Section */
    .catalog-section {
      max-width: 1400px;
      margin: 60px auto 40px;
      padding: 0 40px;
    }
    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 28px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 16px;
    }
    .section-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 38px;
      font-weight: 600;
      color: var(--text-main);
    }
    .section-sub {
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .filter-tabs {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    .filter-tab {
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      padding: 8px 18px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.15s;
    }
    .filter-tab:hover { border-color: var(--text-main); }
    .filter-tab.active {
      background: var(--text-main);
      color: #FAF8F5;
      border-color: var(--text-main);
    }

    /* 4-Column Product Grid */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 28px;
      margin-top: 30px;
    }
    .product-card {
      background: var(--bg-card);
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .product-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(0,0,0,0.06);
    }
    .card-thumb {
      position: relative;
      height: 380px;
      background: #F4EFEB;
      overflow: hidden;
      cursor: pointer;
    }
    .card-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }
    .product-card:hover .card-thumb img {
      transform: scale(1.03);
    }

    /* Badges */
    .card-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      z-index: 2;
    }
    .badge-scarcity { background: var(--accent-rose); color: #FFF; }
    .badge-exclusive { background: var(--accent-green); color: #FFF; }
    .badge-trending { background: var(--accent-gold); color: #FFF; }

    .card-quick-actions {
      position: absolute;
      bottom: 12px;
      left: 12px;
      right: 12px;
      display: flex;
      gap: 8px;
      opacity: 0;
      transform: translateY(8px);
      transition: all 0.2s ease;
      z-index: 5;
    }
    .product-card:hover .card-quick-actions {
      opacity: 1;
      transform: translateY(0);
    }
    .btn-quick-view {
      flex: 1;
      background: rgba(255, 255, 255, 0.95);
      color: var(--text-main);
      border: 1px solid var(--border-color);
      padding: 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.05em;
      cursor: pointer;
      text-align: center;
    }
    .btn-quick-view:hover { background: #FFFFFF; border-color: var(--text-main); }

    .card-body {
      padding: 16px 18px 20px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .card-cat {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }
    .card-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 20px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 4px;
      line-height: 1.25;
      cursor: pointer;
    }
    .card-fabric {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 12px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .card-price-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-bottom: 14px;
    }
    .price-main {
      font-size: 18px;
      font-weight: 700;
      color: var(--text-main);
    }
    .price-mrp {
      font-size: 13px;
      text-decoration: line-through;
      color: var(--text-light);
    }
    .price-discount {
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-green);
      background: #EBF7EE;
      padding: 2px 6px;
      border-radius: 4px;
    }

    .card-sizes-row {
      display: flex;
      gap: 6px;
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid #F0EAE1;
      align-items: center;
      justify-content: space-between;
    }
    .size-pills { display: flex; gap: 4px; }
    .size-chip {
      font-size: 11px;
      font-weight: 600;
      padding: 4px 8px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      background: #FAF8F5;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.1s;
    }
    .size-chip:hover { border-color: var(--text-main); background: #FFF; }
    .stock-chip { font-size: 10px; font-weight: 700; color: var(--accent-rose); }

    /* Value Proposition Strip */
    .value-strip {
      background: #F4EFEB;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      margin: 80px 0 60px;
      padding: 40px 0;
    }
    .value-inner {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 40px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 30px;
    }
    .value-item { display: flex; gap: 16px; align-items: flex-start; }
    .value-icon { font-size: 28px; line-height: 1; }
    .value-title { font-weight: 700; font-size: 15px; color: var(--text-main); margin-bottom: 4px; }
    .value-desc { font-size: 13px; color: var(--text-muted); line-height: 1.4; }

    /* Founder Note */
    .founder-section {
      max-width: 1200px;
      margin: 60px auto 80px;
      padding: 60px;
      background: #FFFFFF;
      border-radius: 16px;
      border: 1px solid var(--border-color);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .founder-content .tag {
      font-size: 11px;
      letter-spacing: 0.15em;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 12px;
      display: block;
    }
    .founder-content h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 40px;
      line-height: 1.2;
      color: var(--text-main);
      margin-bottom: 20px;
    }
    .founder-content p {
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.7;
      margin-bottom: 16px;
    }
    .founder-sig {
      font-family: 'Cormorant Garamond', serif;
      font-size: 26px;
      font-style: italic;
      color: var(--text-main);
      margin-top: 24px;
    }
    .founder-role {
      font-size: 12px;
      color: var(--text-light);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }
    .founder-stat-box {
      background: #FAF8F5;
      padding: 30px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
    }
    .stat-row {
      display: flex;
      justify-content: space-between;
      padding: 14px 0;
      border-bottom: 1px solid var(--border-color);
    }
    .stat-row:last-child { border-bottom: none; }
    .stat-label { font-size: 13px; color: var(--text-muted); }
    .stat-val { font-size: 13px; font-weight: 700; color: var(--text-main); }

    /* Footer */
    footer {
      background: #1E1C19;
      color: #FAF8F5;
      padding: 70px 40px 30px;
    }
    .footer-inner {
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.5fr;
      gap: 50px;
      padding-bottom: 50px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .footer-col h4 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      letter-spacing: 0.1em;
      margin-bottom: 18px;
      color: #FAF8F5;
    }
    .footer-col p {
      font-size: 13px;
      color: #A8A095;
      line-height: 1.6;
      margin-bottom: 16px;
    }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 10px; }
    .footer-col ul li a {
      color: #C0B7AB;
      text-decoration: none;
      font-size: 13px;
      transition: color 0.15s;
    }
    .footer-col ul li a:hover { color: #FAF8F5; }
    .footer-bottom {
      max-width: 1400px;
      margin: 30px auto 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: #8C8479;
    }

    /* Modal Backdrop & Container */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 14, 12, 0.7);
      backdrop-filter: blur(5px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .modal-backdrop.open { display: flex; }
    .product-modal {
      background: var(--bg-primary);
      border-radius: 16px;
      max-width: 980px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      border: 1px solid var(--border-color);
      box-shadow: 0 30px 70px rgba(0,0,0,0.3);
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      position: relative;
    }
    .modal-close {
      position: absolute;
      top: 18px;
      right: 18px;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      z-index: 10;
    }
    .modal-media {
      background: #F4EFEB;
      height: 100%;
      min-height: 520px;
      position: relative;
    }
    .modal-media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .modal-info {
      padding: 40px;
      display: flex;
      flex-direction: column;
    }
    .modal-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 10px;
      align-self: flex-start;
    }
    .modal-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.2;
      margin-bottom: 6px;
    }
    .modal-code {
      font-size: 12px;
      color: var(--text-light);
      margin-bottom: 16px;
    }
    .modal-price-wrap {
      display: flex;
      align-items: baseline;
      gap: 12px;
      padding: 12px 0;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 20px;
    }
    .modal-price-cur { font-size: 26px; font-weight: 700; color: var(--text-main); }
    .modal-price-mrp { font-size: 16px; text-decoration: line-through; color: var(--text-light); }
    .modal-price-off { font-size: 12px; font-weight: 700; color: var(--accent-green); background: #EBF7EE; padding: 3px 8px; border-radius: 4px; }

    .modal-sizes-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 20px;
    }
    .modal-size-btn {
      background: #FFFFFF;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s;
    }
    .modal-size-btn:hover { border-color: var(--text-main); }
    .modal-size-btn.selected {
      border-color: var(--text-main);
      background: #FAF5ED;
      box-shadow: inset 0 0 0 1px var(--text-main);
    }
    .modal-size-btn .sz-label { font-size: 13px; font-weight: 700; color: var(--text-main); display: block; }
    .modal-size-btn .sz-stock { font-size: 10px; font-weight: 600; color: var(--accent-rose); margin-top: 2px; display: block; }

    .pincode-card {
      background: #FAF8F5;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 24px;
    }
    .pincode-row { display: flex; gap: 8px; margin-top: 8px; }
    .pincode-input {
      flex: 1;
      padding: 8px 12px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      font-size: 13px;
      outline: none;
    }
    .pincode-check-btn {
      background: var(--text-main);
      color: #FFF;
      border: none;
      padding: 8px 14px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
    }
    .pincode-result { font-size: 12px; margin-top: 6px; font-weight: 500; }
    .pincode-result.success { color: var(--accent-green); }

    .modal-actions { display: flex; flex-direction: column; gap: 10px; margin-top: auto; }
    .btn-add-bag {
      width: 100%;
      background: var(--text-main);
      color: #FAF8F5;
      border: none;
      padding: 15px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      transition: background 0.15s;
    }
    .btn-add-bag:hover { background: var(--btn-hover); }

    .btn-upi-instant {
      width: 100%;
      background: #E8CA97;
      color: #1E1C19;
      border: 1px solid #D8B77E;
      padding: 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }
    .btn-upi-instant:hover { background: #DFC08A; }

    .btn-whatsapp-order {
      width: 100%;
      background: #E8F5E9;
      color: #1B5E20;
      border: 1px solid #C8E6C9;
      padding: 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }
    .btn-whatsapp-order:hover { background: #DCEDC8; }

    /* Cart Drawer */
    .cart-drawer-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 14, 12, 0.5);
      z-index: 300;
      display: none;
    }
    .cart-drawer-backdrop.open { display: block; }
    .cart-drawer {
      position: fixed;
      top: 0; right: -480px; bottom: 0;
      width: 100%;
      max-width: 450px;
      background: var(--bg-primary);
      z-index: 310;
      box-shadow: -10px 0 35px rgba(0,0,0,0.15);
      display: flex;
      flex-direction: column;
      transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .cart-drawer.open { right: 0; }
    .cart-header {
      padding: 20px 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .cart-header h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 26px;
      font-weight: 600;
    }
    .cart-close-btn { background: none; border: none; font-size: 20px; cursor: pointer; }
    .free-shipping-bar {
      background: #F4EFEB;
      padding: 12px 24px;
      font-size: 12px;
      font-weight: 600;
      border-bottom: 1px solid var(--border-color);
      color: var(--accent-green);
    }
    .cart-items-list {
      flex: 1;
      overflow-y: auto;
      padding: 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .cart-item {
      display: flex;
      gap: 14px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }
    .cart-item img {
      width: 75px;
      height: 95px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border-color);
    }
    .cart-item-details { flex: 1; }
    .cart-item-title { font-size: 14px; font-weight: 700; color: var(--text-main); margin-bottom: 2px; }
    .cart-item-meta { font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }
    .cart-item-price { font-size: 14px; font-weight: 700; color: var(--text-main); }
    .cart-item-remove { background: none; border: none; color: var(--accent-rose); font-size: 11px; cursor: pointer; text-decoration: underline; }

    .cart-footer { padding: 24px; border-top: 1px solid var(--border-color); background: #FFFFFF; }
    .cart-summary-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px; color: var(--text-muted); }
    .cart-summary-row.total {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      border-top: 1px solid var(--border-color);
      padding-top: 12px;
      margin-top: 8px;
    }
    .coupon-box { display: flex; gap: 6px; margin: 14px 0; }
    .coupon-input {
      flex: 1;
      padding: 8px 12px;
      border: 1px solid var(--border-color);
      border-radius: 4px;
      font-size: 12px;
      text-transform: uppercase;
    }
    .coupon-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 8px 14px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
    }
    .btn-checkout {
      width: 100%;
      background: var(--text-main);
      color: #FFF;
      border: none;
      padding: 15px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
    }

    .guide-table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 13px; }
    .guide-table th, .guide-table td { border: 1px solid var(--border-color); padding: 10px 14px; text-align: center; }
    .guide-table th { background: #FAF5ED; font-weight: 700; }

    .toast-note {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--text-main);
      color: #FAF8F5;
      padding: 14px 22px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      display: none;
      z-index: 400;
    }

    @media (max-width: 1024px) {
      .product-grid { grid-template-columns: repeat(2, 1fr); }
      .hero-section { grid-template-columns: 1fr; }
      .founder-section { grid-template-columns: 1fr; padding: 30px; }
      .value-inner { grid-template-columns: repeat(2, 1fr); }
      .footer-inner { grid-template-columns: 1fr 1fr; }
      .product-modal { grid-template-columns: 1fr; }
      .header-nav-row { flex-direction: column; gap: 14px; }
    }
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="announcement-bar">
    <div>📍 CHANDIGARH • PANCHKULA • MOHALI</div>
    <div>✨ DROP 01 DEBUT LIVE • FREE EXPRESS SHIPPING IN TRICITY • LIMITED 3 PIECES PER SIZE</div>
    <div>
      <span>CODE: <strong>DEBUT10</strong> (10% OFF)</span>
      <a href="javascript:void(0)" onclick="openSizeGuide()">SIZE GUIDE</a>
    </div>
  </div>

  <!-- Header with 2 Distinct Rows (Zero Text Collisions) -->
  <header>
    <div class="header-top-row">
      <a href="#" class="brand-logo">MEENU LABEL</a>
      <span class="brand-sub">CHANDIGARH • ESTD 2026</span>
    </div>

    <div class="header-nav-row">
      <nav>
        <ul class="nav-links">
          <li><a href="javascript:void(0)" class="active" onclick="filterCategory('all', this)">All Silhouettes (13)</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('coord', this)">Co-ord Sets (4)</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('festive', this)">Festive Suits (3)</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('dress', this)">Dresses (3)</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('top', this)">Tops & Blouses (3)</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <div class="search-box">
          <span>🔍</span>
          <input type="text" id="searchInput" placeholder="Search silhouettes..." onkeyup="searchProducts()">
        </div>
        <button class="header-btn" onclick="openSizeGuide()">📏 Guide</button>
        <button class="header-btn" onclick="toggleCart()">
          🛍️ Bag <span class="cart-badge" id="headerCartCount">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section with Pre-Loaded Image -->
  <section class="hero-section">
    <div class="hero-card">
      <span class="hero-tag">Debut Collection • Drop 01</span>
      <h1 class="hero-heading">Effortless Everyday Luxury Silhouettes</h1>
      <p class="hero-desc">
        Crafted in pure breathable cottons, fluid chanderi silks, and textured dobby chiffons. 
        Mindfully tailored in Chandigarh for the modern woman who refuses to compromise between all-day comfort and royal elegance.
      </p>
      <div class="hero-cta-group">
        <a href="#catalog" class="btn-primary">EXPLORE 13 DESIGNS ↓</a>
        <a href="#founder" class="btn-secondary">OUR STORY</a>
      </div>
    </div>

    <div class="hero-media-wrap">
      <img id="heroImage" src="HERO_IMAGE_PLACEHOLDER" alt="Meenu Label Drop 01">
      <div class="hero-overlay-pill">
        <div class="name">The Jaipur Chanderi Silk Suit</div>
        <div class="meta">Pure Chanderi Kurta + Silk Trousers + Organza Dupatta • ₹2,299</div>
      </div>
    </div>
  </section>

  <!-- Catalog Section with Pre-Rendered Cards -->
  <section class="catalog-section" id="catalog">
    <div class="section-header">
      <div>
        <h2 class="section-title">The Debut 13 Silhouettes</h2>
        <p class="section-sub">Authentic catalog pieces ordered from Surat. Strictly 3 exclusive pieces per design (1 each in M, L, XL).</p>
      </div>

      <div class="filter-tabs">
        <button class="filter-tab active" onclick="filterCategory('all', this)">All (13)</button>
        <button class="filter-tab" onclick="filterCategory('coord', this)">Co-ord Sets (4)</button>
        <button class="filter-tab" onclick="filterCategory('festive', this)">Festive Suits (3)</button>
        <button class="filter-tab" onclick="filterCategory('dress', this)">Dresses (3)</button>
        <button class="filter-tab" onclick="filterCategory('top', this)">Tops & Blouses (3)</button>
      </div>
    </div>

    <div class="product-grid" id="productGrid">
      CARDS_PLACEHOLDER
    </div>
  </section>

  <!-- Value Props -->
  <div class="value-strip">
    <div class="value-inner">
      <div class="value-item">
        <div class="value-icon">⚡</div>
        <div>
          <div class="value-title">Tricity 24-Hr Express Dispatch</div>
          <div class="value-desc">Priority same-day packing and next-day delivery in Chandigarh, Mohali, and Panchkula.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">🌿</div>
        <div>
          <div class="value-title">100% Breathable Fabrics</div>
          <div class="value-desc">Pure cottons, chanderi silks, and soft chiffons tested for long working days and Indian summers.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">📏</div>
        <div>
          <div class="value-title">True-to-Size M, L, XL Fits</div>
          <div class="value-desc">Standard Indian bust measurements (38", 40", 42") tailored to flatter your natural posture.</div>
        </div>
      </div>
      <div class="value-item">
        <div class="value-icon">🔄</div>
        <div>
          <div class="value-title">7-Day Easy Size Exchange</div>
          <div class="value-desc">Hassle-free door-to-door size exchange. Kept pristine in our reusable EVA zipper bags.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Founder Story Section -->
  <section class="founder-section" id="founder">
    <div class="founder-content">
      <span class="tag">Behind The Label</span>
      <h3>Crafted for the woman who values mindful elegance.</h3>
      <p>
        Meenu Label was born from a very personal realization: contemporary Indian ethnic wear was either too synthetic and mass-produced, or absurdly overpriced at high-street boutiques.
      </p>
      <p>
        Operating proudly out of Chandigarh under <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong>, we set out to bridge this gap. Every design in our Debut Drop is hand-shortlisted directly from master textile weavers in Surat, tailored in small, mindful batches of just 3 pieces per size.
      </p>
      <div class="founder-sig">Meenu</div>
      <div class="founder-role">Founder, Meenu Label</div>
    </div>

    <div class="founder-stat-box">
      <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; margin-bottom: 16px;">Drop 01 Transparency</h4>
      <div class="stat-row">
        <span class="stat-label">Total Curated Designs</span>
        <span class="stat-val">13 Silhouettes</span>
      </div>
      <div class="stat-row">
        <span class="stat-label">Inventory Production</span>
        <span class="stat-val">39 Pieces Total (Strict Scarcity)</span>
      </div>
      <div class="stat-row">
        <span class="stat-label">Sizes Produced</span>
        <span class="stat-val">M (38"), L (40"), XL (42")</span>
      </div>
      <div class="stat-row">
        <span class="stat-label">Official Registered Store</span>
        <span class="stat-val">meenulabel.com</span>
      </div>
      <div class="stat-row">
        <span class="stat-label">Operating Entity</span>
        <span class="stat-val">Infatera Software Solutions OPC Pvt. Ltd.</span>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div class="footer-col">
        <h4 style="font-size: 28px; letter-spacing: 0.15em;">MEENU LABEL</h4>
        <p>Contemporary Indian ethnic wear and modern fusion silhouettes. Handcrafted elegance for everyday grace.</p>
        <p style="font-size: 11px; color: #82786D;">
          Operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong><br>
          Chandigarh, India • Official Domain: <strong>meenulabel.com</strong>
        </p>
      </div>
      <div class="footer-col">
        <h4>Collection</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="filterCategory('all')">All Drop 01 Items</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('coord')">Co-ord Sets</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('festive')">Festive Suits</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('dress')">Day Dresses</a></li>
          <li><a href="javascript:void(0)" onclick="filterCategory('top')">Casual Tops</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Client Care</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="openSizeGuide()">Size & Fit Guide</a></li>
          <li><a href="javascript:void(0)">7-Day Exchange Policy</a></li>
          <li><a href="javascript:void(0)">Tricity 24-Hr Dispatch</a></li>
          <li><a href="mailto:meenulabel24@gmail.com">meenulabel24@gmail.com</a></li>
          <li><a href="https://wa.me/919876543210" target="_blank">WhatsApp Concierge</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Newsletter</h4>
        <p>Receive exclusive early access to Drop 02 and private founder trunk shows.</p>
        <div style="display: flex; gap: 8px; margin-top: 12px;">
          <input type="email" placeholder="Enter your email..." style="padding: 10px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.08); color: #FFF; font-size: 13px; flex: 1;">
          <button class="btn-primary" style="padding: 10px 18px;" onclick="showToast('Thank you for subscribing!')">JOIN</button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Meenu Label (Infatera Software Solutions OPC Pvt. Ltd.). All rights reserved.</div>
      <div>🔒 256-Bit SSL Encrypted • Powered by Shopify Online Store 2.0 • 100% Secure UPI & Card Checkout</div>
    </div>
  </footer>

  <!-- Product Detail Modal -->
  <div class="modal-backdrop" id="productModalBackdrop" onclick="closeModalOnBackdrop(event)">
    <div class="product-modal" id="productModal">
      <button class="modal-close" onclick="closeModal()">✕</button>
      <div class="modal-media">
        <img id="modalImg" src="" alt="">
      </div>
      <div class="modal-info">
        <span class="modal-badge badge-scarcity" id="modalBadge">ONLY 1 LEFT IN SIZE M</span>
        <h2 class="modal-title" id="modalTitle">Product Title</h2>
        <div class="modal-code" id="modalCode">Product Code</div>
        <div class="modal-price-wrap">
          <span class="modal-price-cur" id="modalPrice">₹1,499</span>
          <span class="modal-price-mrp" id="modalMrp">₹2,499</span>
          <span class="modal-price-off" id="modalOff">40% OFF</span>
        </div>
        <p id="modalDesc" style="font-size: 14px; color: var(--text-muted); line-height: 1.6; margin-bottom: 20px;">
          Product description.
        </p>

        <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 12px; font-weight: 700;">
          <span>SELECT SIZE (INDIAN BUST MEASUREMENTS)</span>
          <button onclick="openSizeGuide()" style="background:none; border:none; color:var(--accent-gold); font-size:12px; cursor:pointer; text-decoration:underline;">📏 Size Chart</button>
        </div>
        <div class="modal-sizes-grid">
          <div class="modal-size-btn selected" onclick="selectModalSize('M', this)">
            <span class="sz-label">M (38")</span>
            <span class="sz-stock">🔥 Only 1 left</span>
          </div>
          <div class="modal-size-btn" onclick="selectModalSize('L', this)">
            <span class="sz-label">L (40")</span>
            <span class="sz-stock">Only 1 left</span>
          </div>
          <div class="modal-size-btn" onclick="selectModalSize('XL', this)">
            <span class="sz-label">XL (42")</span>
            <span class="sz-stock">Only 1 left</span>
          </div>
        </div>

        <div class="pincode-card">
          <div style="font-size: 12px; font-weight: 700; color: var(--text-main);">📍 Check Estimated Delivery</div>
          <div class="pincode-row">
            <input type="text" class="pincode-input" id="pincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6">
            <button class="pincode-check-btn" onclick="checkPincode()">Check</button>
          </div>
          <div class="pincode-result" id="pincodeResult"></div>
        </div>

        <div class="modal-actions">
          <button class="btn-add-bag" onclick="addCurrentProductToCart()">ADD TO BAG 🛍️</button>
          <button class="btn-upi-instant" onclick="triggerUpiCheckout()">⚡ BUY NOW WITH UPI / GPAY</button>
          <a href="#" class="btn-whatsapp-order" id="modalWhatsAppBtn" target="_blank">
            💬 Order Directly via WhatsApp
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Cart Drawer -->
  <div class="cart-drawer-backdrop" id="cartBackdrop" onclick="toggleCart()"></div>
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-header">
      <h3>Your Shopping Bag (<span id="cartCount">0</span>)</h3>
      <button class="cart-close-btn" onclick="toggleCart()">✕</button>
    </div>
    <div class="free-shipping-bar">
      🚚 You have unlocked <strong>FREE Express Shipping</strong>!
    </div>
    <div class="cart-items-list" id="cartItemsList"></div>
    <div class="cart-footer">
      <div class="coupon-box">
        <input type="text" class="coupon-input" id="couponCode" placeholder="Promo code (e.g. DEBUT10)">
        <button class="coupon-btn" onclick="applyCoupon()">Apply</button>
      </div>
      <div class="cart-summary-row">
        <span>Subtotal</span>
        <span id="cartSubtotal">₹0</span>
      </div>
      <div class="cart-summary-row">
        <span>Discount</span>
        <span id="cartDiscount" style="color: var(--accent-green);">-₹0</span>
      </div>
      <div class="cart-summary-row">
        <span>Estimated GST (5% included)</span>
        <span id="cartGst">₹0</span>
      </div>
      <div class="cart-summary-row">
        <span>Express Shipping</span>
        <span style="color: var(--accent-green); font-weight:700;">FREE</span>
      </div>
      <div class="cart-summary-row total">
        <span>Total Amount</span>
        <span id="cartTotal">₹0</span>
      </div>
      <button class="btn-checkout" onclick="proceedToCheckout()">PROCEED TO CHECKOUT 🔒</button>
    </div>
  </div>

  <!-- Size Guide Modal -->
  <div class="modal-backdrop" id="sizeGuideBackdrop" onclick="closeSizeGuide(event)">
    <div style="background: #FFF; border-radius: 12px; padding: 36px; max-width: 600px; width: 100%; position: relative;">
      <button class="modal-close" onclick="closeSizeGuideDirect()">✕</button>
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; margin-bottom: 8px;">Meenu Label Standard Size Chart</h3>
      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">
        All measurements are in inches. Our silhouettes are true-to-size with comfortable ease for breathing and movement.
      </p>
      <table class="guide-table">
        <thead>
          <tr>
            <th>Size</th>
            <th>Bust (Inches)</th>
            <th>Waist (Inches)</th>
            <th>Hip (Inches)</th>
            <th>Ideal Body Bust</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>M (38)</strong></td><td>38"</td><td>32" - 34"</td><td>40" - 42"</td><td>36" - 37"</td></tr>
          <tr><td><strong>L (40)</strong></td><td>40"</td><td>34" - 36"</td><td>42" - 44"</td><td>38" - 39"</td></tr>
          <tr><td><strong>XL (42)</strong></td><td>42"</td><td>36" - 38"</td><td>44" - 46"</td><td>40" - 41"</td></tr>
        </tbody>
      </table>
      <div style="background: #FAF8F5; padding: 14px; border-radius: 6px; font-size: 12px; color: var(--text-muted);">
        💡 <strong>Fit Tip:</strong> If you prefer a relaxed comfort drape, we suggest choosing your true size. For wrap dresses, the tie-belt allows customized waist cinching.
      </div>
    </div>
  </div>

  <div class="toast-note" id="toastNote"></div>

  <!-- Pure, Error-Free JavaScript -->
  <script>
    var productsData = JS_DATA_PLACEHOLDER;
    var cart = [];
    var activeModalProduct = null;
    var selectedSize = 'M';
    var discountPercent = 0;

    function filterCategory(cat, btn) {
      if (btn) {
        var tabs = document.querySelectorAll('.filter-tab');
        for (var i = 0; i < tabs.length; i++) tabs[i].classList.remove('active');
        btn.classList.add('active');

        var navs = document.querySelectorAll('.nav-links a');
        for (var j = 0; j < navs.length; j++) navs[j].classList.remove('active');
      }

      var cards = document.querySelectorAll('.product-card');
      for (var k = 0; k < cards.length; k++) {
        var cardCat = cards[k].getAttribute('data-category');
        if (cat === 'all' || cardCat === cat) {
          cards[k].style.display = 'flex';
        } else {
          cards[k].style.display = 'none';
        }
      }

      if (btn && window.scrollY > 400) {
        document.getElementById('catalog').scrollIntoView({ behavior: 'smooth' });
      }
    }

    function searchProducts() {
      var q = document.getElementById('searchInput').value.toLowerCase().trim();
      var cards = document.querySelectorAll('.product-card');
      for (var i = 0; i < cards.length; i++) {
        var text = cards[i].innerText.toLowerCase();
        if (!q || text.indexOf(q) !== -1) {
          cards[i].style.display = 'flex';
        } else {
          cards[i].style.display = 'none';
        }
      }
    }

    function openProductModal(id) {
      var p = null;
      for (var i = 0; i < productsData.length; i++) {
        if (productsData[i].id === id) { p = productsData[i]; break; }
      }
      if (!p) return;
      activeModalProduct = p;
      selectedSize = 'M';

      document.getElementById('modalImg').src = p.b64;
      document.getElementById('modalBadge').textContent = p.badge.toUpperCase();
      document.getElementById('modalBadge').className = 'modal-badge ' + p.badge_class;
      document.getElementById('modalTitle').textContent = p.name;
      document.getElementById('modalCode').textContent = 'Product Code: ' + p.code + '  •  Fabric: ' + p.fabric;
      document.getElementById('modalPrice').textContent = '₹' + p.price.toLocaleString('en-IN');
      document.getElementById('modalMrp').textContent = '₹' + p.mrp.toLocaleString('en-IN');
      var off = Math.round(((p.mrp - p.price) / p.mrp) * 100);
      document.getElementById('modalOff').textContent = off + '% OFF';
      document.getElementById('modalDesc').textContent = p.desc;
      document.getElementById('pincodeResult').textContent = '';

      var sizeBtns = document.querySelectorAll('.modal-size-btn');
      for (var j = 0; j < sizeBtns.length; j++) {
        sizeBtns[j].classList.remove('selected');
        if (j === 0) sizeBtns[j].classList.add('selected');
      }

      updateWhatsAppLink(p, 'M');
      document.getElementById('productModalBackdrop').classList.add('open');
    }

    function closeModal() {
      document.getElementById('productModalBackdrop').classList.remove('open');
    }

    function closeModalOnBackdrop(e) {
      if (e.target.id === 'productModalBackdrop') closeModal();
    }

    function selectModalSize(size, el) {
      selectedSize = size;
      var btns = document.querySelectorAll('.modal-size-btn');
      for (var i = 0; i < btns.length; i++) btns[i].classList.remove('selected');
      el.classList.add('selected');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }

    function updateWhatsAppLink(product, size) {
      var text = encodeURIComponent('Hi Meenu Label! I would like to order "' + product.name + '" (Code: ' + product.code + ') in Size ' + size + ' for ₹' + product.price + '. Please confirm delivery details.');
      document.getElementById('modalWhatsAppBtn').href = 'https://wa.me/919876543210?text=' + text;
    }

    function checkPincode() {
      var pin = document.getElementById('pincodeInput').value.trim();
      var res = document.getElementById('pincodeResult');
      if (pin.length !== 6 || isNaN(pin)) {
        res.textContent = '❌ Please enter a valid 6-digit Indian pincode.';
        res.style.color = '#B83A3A';
        return;
      }
      if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {
        res.textContent = '⚡ Tricity Priority! Arrives Tomorrow by 2 PM via Express Courier.';
        res.style.color = '#2B6E44';
      } else {
        res.textContent = '✓ Available! Estimated delivery within 2-3 business days.';
        res.style.color = '#2B6E44';
      }
    }

    function quickAddCart(id, size) {
      var p = null;
      for (var i = 0; i < productsData.length; i++) {
        if (productsData[i].id === id) { p = productsData[i]; break; }
      }
      if (!p) return;
      addToCart(p, size);
    }

    function addCurrentProductToCart() {
      if (!activeModalProduct) return;
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }

    function addToCart(product, size) {
      var existing = null;
      for (var i = 0; i < cart.length; i++) {
        if (cart[i].id === product.id && cart[i].size === size) {
          existing = cart[i];
          break;
        }
      }
      if (existing) {
        existing.qty += 1;
      } else {
        cart.push({
          id: product.id,
          name: product.name,
          price: product.price,
          size: size,
          img: product.b64,
          qty: 1
        });
      }
      updateCartUI();
      openCart();
      showToast('Added ' + product.name + ' (' + size + ') to Bag!');
    }

    function removeFromCart(id, size) {
      cart = cart.filter(function(item) {
        return !(item.id === id && item.size === size);
      });
      updateCartUI();
    }

    function updateCartUI() {
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;
      document.getElementById('cartCount').textContent = totalItems;
      document.getElementById('headerCartCount').textContent = totalItems;

      var listEl = document.getElementById('cartItemsList');
      var subtotalEl = document.getElementById('cartSubtotal');
      var discountEl = document.getElementById('cartDiscount');
      var gstEl = document.getElementById('cartGst');
      var totalEl = document.getElementById('cartTotal');

      if (cart.length === 0) {
        listEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 40px; margin-bottom: 12px;">🛍️</div><div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Your bag is empty</div><div style="font-size: 13px;">Explore our debut 13 silhouettes and find your fit.</div></div>';
        subtotalEl.textContent = '₹0';
        discountEl.textContent = '-₹0';
        gstEl.textContent = '₹0';
        totalEl.textContent = '₹0';
        return;
      }

      var subtotal = 0;
      var html = '';
      for (var j = 0; j < cart.length; j++) {
        var it = cart[j];
        subtotal += it.price * it.qty;
        html += '<div class="cart-item"><img src="' + it.img + '" alt="' + it.name + '"><div class="cart-item-details"><div class="cart-item-title">' + it.name + '</div><div class="cart-item-meta">Size: <strong>' + it.size + '</strong> • Qty: ' + it.qty + '</div><div style="display:flex; justify-content:space-between; align-items:center;"><span class="cart-item-price">₹' + (it.price * it.qty).toLocaleString('en-IN') + '</span><button class="cart-item-remove" onclick="removeFromCart(\\'' + it.id + '\\', \\'' + it.size + '\\')">Remove</button></div></div></div>';
      }
      listEl.innerHTML = html;

      var discountAmt = Math.round(subtotal * discountPercent);
      var finalTotal = subtotal - discountAmt;
      var gstAmt = Math.round(finalTotal * 0.05);

      subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
      discountEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');
      gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');
      totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');
    }

    function toggleCart() {
      document.getElementById('cartDrawer').classList.toggle('open');
      document.getElementById('cartBackdrop').classList.toggle('open');
    }
    function openCart() {
      document.getElementById('cartDrawer').classList.add('open');
      document.getElementById('cartBackdrop').classList.add('open');
    }

    function applyCoupon() {
      var code = document.getElementById('couponCode').value.trim().toUpperCase();
      if (code === 'DEBUT10') {
        discountPercent = 0.10;
        updateCartUI();
        showToast('🎉 Promo code DEBUT10 applied! 10% discount added.');
      } else {
        showToast('❌ Invalid code. Try "DEBUT10" for 10% off.');
      }
    }

    function triggerUpiCheckout() {
      showToast('⚡ Launching Instant UPI / GPay checkout...');
      setTimeout(function() {
        alert('Meenu Label Instant UPI Checkout\\n\\nProduct: ' + activeModalProduct.name + '\\nSize: ' + selectedSize + '\\nAmount: ₹' + activeModalProduct.price + '\\n\\nIn live production, this seamlessly launches Google Pay / PhonePe / Paytm UPI app.');
      }, 300);
    }

    function proceedToCheckout() {
      if (cart.length === 0) {
        alert('Your bag is empty!');
        return;
      }
      alert('🔒 Redirecting to Shopify 1-Click Secure Razorpay / Cashfree Gateway for meenulabel.com...');
    }

    function openSizeGuide() {
      document.getElementById('sizeGuideBackdrop').classList.add('open');
    }
    function closeSizeGuideDirect() {
      document.getElementById('sizeGuideBackdrop').classList.remove('open');
    }
    function closeSizeGuide(e) {
      if (e.target.id === 'sizeGuideBackdrop') closeSizeGuideDirect();
    }

    function showToast(msg) {
      var t = document.getElementById('toastNote');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(function() { t.style.display = 'none'; }, 3200);
    }
  </script>
</body>
</html>
"""

# Replace placeholders safely
html_final = html_content.replace("HERO_IMAGE_PLACEHOLDER", hero_b64)
html_final = html_final.replace("CARDS_PLACEHOLDER", cards_html)
html_final = html_final.replace("JS_DATA_PLACEHOLDER", js_products_data)

out_file_downloads = os.path.join(downloads_dir, "Meenu_Label_Desktop_Storefront.html")
with open(out_file_downloads, "w", encoding="utf-8") as f:
    f.write(html_final)

out_file_artifacts = os.path.join(artifacts_dir, "Meenu_Label_Desktop_Storefront.html")
with open(out_file_artifacts, "w", encoding="utf-8") as f:
    f.write(html_final)

print("SUCCESS: Generated 100% pre-rendered, error-free desktop storefront HTML!")
