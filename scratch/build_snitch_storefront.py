import os, base64, json, shutil

downloads_dir = r"C:\Users\sande\Downloads"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
scratch_dir = os.path.join(artifacts_dir, "scratch")
highres_dir = os.path.join(scratch_dir, "highres_products")
banners_dir = os.path.join(scratch_dir, "banners")

def get_b64(path):
    if os.path.exists(path):
        ext = os.path.splitext(path)[1].lower()
        mime = "image/png" if ext == ".png" else "image/jpeg"
        with open(path, 'rb') as f:
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ''

# 1. Load official logo
logo_b64 = get_b64(os.path.join(downloads_dir, "meenu_logo_official.png"))

# 2. Load 4 Full-Bleed 1500x708 Cinematic Editorial Banners
banner_1_b64 = get_b64(os.path.join(banners_dir, 'hero_1_marigold.jpg'))
banner_2_b64 = get_b64(os.path.join(banners_dir, 'hero_2_gulabi.jpg'))
banner_3_b64 = get_b64(os.path.join(banners_dir, 'hero_3_polka.jpg'))
banner_4_b64 = get_b64(os.path.join(banners_dir, 'hero_4_lime.jpg'))
login_campaign_b64 = get_b64(r'scratch/login_campaign_banner.jpg')
campaign_cafe_b64 = get_b64(r'scratch/campaign_cafe.jpg')
campaign_balcony_b64 = get_b64(r'scratch/campaign_balcony.jpg')
campaign_sukhna_b64 = get_b64(r'scratch/campaign_sukhna.jpg')
craft_chanderi_b64 = get_b64(r'scratch/craft_chanderi_lux.jpg')
craft_crepe_b64 = get_b64(r'scratch/craft_crepe_lux.jpg')
craft_organza_b64 = get_b64(r'scratch/craft_organza_lux.jpg')

# 3. Catalog Products
products = [
    {
        "id": "JAB26ST05010",
        "code": "JAB26ST05010",
        "name": "The Royal Wine Chanderi Festive Suit",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Chanderi Silk & Zari with Organza Dupatta",
        "color": "Royal Wine & Antique Gold",
        "price": 2299,
        "mrp": 3699,
        "badge": "Flagship Hero",
        "badge_class": "badge-exclusive",
        "desc": "An iconic 3-piece festive ensemble featuring a straight-cut Chanderi kurta with intricate antique gold zari neckline embroidery, tailored cigarette trousers, and a sheer fluid organza dupatta that drapes with regal grace for celebratory occasions.",
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
    },
    {
        "id": "JAB26SS05740",
        "code": "JAB26SS05740",
        "name": "Roohani Chanderi Sharara Festive Set",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Lustrous Chanderi Silk with Zari & Organza Dupatta",
        "color": "Royal Emerald & Gold",
        "price": 2399,
        "mrp": 3799,
        "badge": "New Arrival",
        "badge_class": "badge-exclusive",
        "desc": "A regal festive ensemble. Crafted in lustrous Chanderi silk with intricate neck zari embroidery, paired with voluminous tiered Sharara pants and a scalloped golden-lace organza dupatta.",
        "img_file": "JAB26SS05740.jpg"
    },
    {
        "id": "JAB25ST02661",
        "code": "JAB25ST02661",
        "name": "Noor Chanderi Silk Straight Kurta Suit",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Pure Chanderi Silk Blend with Hand Zari Detailing",
        "color": "Golden Honey & Teal",
        "price": 2199,
        "mrp": 3499,
        "badge": "Only 3 Left",
        "badge_class": "badge-scarcity",
        "desc": "Graceful poise in pure Chanderi silk. Tailored straight kurta accented with delicate hand-piped neckline zari, paired with coordinating cigarette trousers and a lightweight sheer dupatta for timeless festive charm.",
        "img_file": "JAB25ST02661.jpg"
    },
    {
        "id": "JAB26ST05754",
        "code": "JAB26ST05754",
        "name": "Shahi Chanderi Royal Festive Ensemble",
        "category": "festive",
        "cat_label": "Festive Suits",
        "fabric": "Royal Chanderi Silk & Zari with Golden Border Dupatta",
        "color": "Regal Mustard & Magenta",
        "price": 2299,
        "mrp": 3699,
        "badge": "Trending",
        "badge_class": "badge-trending",
        "desc": "Exquisite craftsmanship from Surat's heritage looms. Straight-cut royal Chanderi kurta featuring heritage bootis and zari threadwork, paired with ankle-cut trousers and an opulent woven border dupatta.",
        "img_file": "JAB26ST05754.jpg"
    }
]

print("Loading base64 for products...")
for p in products:
    p["b64"] = get_b64(os.path.join(highres_dir, p["img_file"]))

# Build cards HTML
cards_html = ""
for p in products:
    discount = round(((p["mrp"] - p["price"]) / p["mrp"]) * 100)
    cards_html += f"""
    <div class="product-card" data-category="{p['category']}" data-id="{p['id']}" onclick="openProductPage('{p['id']}')">
      <div class="card-thumb">
        <span class="card-badge {p['badge_class']}">{p['badge']}</span>
        <button class="card-wishlist-btn" onclick="event.stopPropagation(); toggleWishlistProduct('{p['id']}')" title="Save to Wishlist" id="wishBtn_{p['id']}" aria-label="Save to Wishlist">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
        </button>
        <img src="{p['b64']}" alt="{p['name']}" loading="lazy">
        <div class="card-quick-actions">
          <button class="btn-quick-view" onclick="event.stopPropagation(); openQuickView('{p['id']}')" title="Quick View">QUICK VIEW</button>
        </div>
      </div>
      <div class="card-body">
        <span class="card-cat">{p['cat_label']}</span>
        <h3 class="card-title">{p['name']}</h3>
        <div class="card-fabric">{p['fabric']}</div>
        <div class="card-price-row">
          <span class="price-main">&#8377;{p['price']:,}</span>
          <span class="price-mrp">&#8377;{p['mrp']:,}</span>
          <span class="price-discount">{discount}% OFF</span>
        </div>
        <div class="card-sizes-row">
          <div class="size-pills">
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'M')">M (38)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'L')">L (40)</span>
            <span class="size-chip" onclick="event.stopPropagation(); quickAddCart('{p['id']}', 'XL')">XL (42)</span>
          </div>
          <span class="stock-chip">Only 3 Left</span>
        </div>
      </div>
    </div>
    """

js_products_data = json.dumps([{
    "id": p["id"],
    "code": p["code"],
    "name": p["name"],
    "category": p["category"],
    "cat_label": p["cat_label"],
    "fabric": p["fabric"],
    "color": p["color"],
    "price": p["price"],
    "mrp": p["mrp"],
    "desc": p["desc"],
    "badge": p["badge"],
    "badge_class": p["badge_class"],
    "b64": p["b64"]
} for p in products])

html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meenu Label • Contemporary Ethnic & Fusion Wear | meenulabel.com</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-primary: #FAF8F5;
      --bg-card: #FFFFFF;
      --bg-surface: #F3EFE8;
      --text-main: #141210;
      --text-muted: #7A7267;
      --text-light: #9B9387;
      --border-color: #E8E2D8;
      --accent-gold: #9E7D47;
      --accent-rose: #B83A3A;
      --accent-green: #2B6E44;
      --btn-dark: #141210;
      --btn-hover: #2E2925;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    /* Top Marquee */
    .announcement-bar {{
      background: var(--text-main);
      color: #FAF8F5;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      padding: 9px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .announcement-bar a {{ color: #E8D3B9; text-decoration: none; margin-left: 14px; }}

    /* Snitch-Style Minimalist Luxury Header */
    header {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 34px;
      z-index: 90;
      transition: all 0.3s ease;
    }}
    .header-bar {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 12px 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
    }}
    .header-left {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: flex-start;
    }}
    .hamburger-btn {{
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      border-radius: 4px;
      transition: color 0.2s, background 0.2s;
    }}
    .hamburger-btn:hover {{
      background: var(--bg-surface);
      color: var(--accent-gold);
    }}
    .hamburger-btn svg {{
      width: 22px;
      height: 22px;
      display: block;
      pointer-events: none;
    }}
    .header-center {{
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .brand-logo-img {{
      height: 52px;
      width: auto;
      display: block;
      transition: transform 0.2s ease;
    }}
    .brand-logo-img:hover {{
      transform: scale(1.02);
    }}
    .header-right {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 18px;
    }}
    .header-icon-action {{
      background: none;
      border: none;
      cursor: pointer;
      color: #111111;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      position: relative;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      padding: 0;
      transition: all 0.2s ease;
    }}
    .header-icon-action:hover {{
      color: var(--accent-gold);
      background: var(--bg-surface);
      transform: translateY(-1px);
    }}
    .header-icon-action svg {{
      width: 22px;
      height: 22px;
      display: block;
      stroke-width: 1.6;
      pointer-events: none;
    }}
    .header-badge-pill {{
      position: absolute;
      top: 4px;
      right: 2px;
      background: var(--text-main);
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 700;
      min-width: 16px;
      height: 16px;
      line-height: 16px;
      border-radius: 8px;
      text-align: center;
      padding: 0 4px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.18);
      pointer-events: none;
      transition: transform 0.2s ease, background 0.2s;
    }}
    .header-icon-action:hover .header-badge-pill {{
      background: var(--accent-gold);
    }}

    /* Slide-Down Search Overlay Bar */
    .search-overlay-bar {{
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      width: 100%;
      background: #FFFFFF;
      border-bottom: 1px solid var(--border-color);
      box-shadow: 0 16px 36px rgba(0,0,0,0.08);
      padding: 24px 36px;
      transform: translateY(-10px);
      opacity: 0;
      pointer-events: none;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
      z-index: 89;
    }}
    .search-overlay-bar.open {{
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }}
    .search-overlay-inner {{
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
    }}
    .search-input-box {{
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 2px solid var(--text-main);
      padding-bottom: 10px;
    }}
    .search-input-box svg {{
      width: 22px;
      height: 22px;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .search-input-box input {{
      flex: 1;
      border: none;
      outline: none;
      font-family: inherit;
      font-size: 17px;
      color: var(--text-main);
      background: transparent;
      letter-spacing: 0.3px;
    }}
    .search-input-box input::placeholder {{
      color: #999;
      font-size: 15px;
    }}
    .search-clear-btn {{
      background: none;
      border: none;
      font-size: 18px;
      color: #888;
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 4px;
      line-height: 1;
    }}
    .search-clear-btn:hover {{ color: #111; }}
    .search-quick-tags {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 12px;
    }}
    .quick-tag-label {{
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      font-size: 11px;
      margin-right: 4px;
    }}
    .quick-tag {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 5px 14px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      color: var(--text-main);
      transition: all 0.18s ease;
    }}
    .quick-tag:hover {{
      background: var(--text-main);
      color: #FFFFFF;
      border-color: var(--text-main);
    }}
    .search-close-action {{
      position: absolute;
      top: 0;
      right: 0;
      background: none;
      border: none;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      padding: 4px 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .search-close-action:hover {{ color: var(--text-main); }}

    /* Card Wishlist Button */
    .card-wishlist-btn {{
      position: absolute;
      top: 12px;
      right: 12px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(4px);
      border: 1px solid rgba(0,0,0,0.06);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 4;
      transition: all 0.2s ease;
      color: #333333;
      padding: 0;
    }}
    .card-wishlist-btn:hover {{
      background: #FFFFFF;
      transform: scale(1.1);
      color: #E53935;
    }}
    .card-wishlist-btn svg {{
      width: 18px;
      height: 18px;
      display: block;
      transition: fill 0.2s ease, stroke 0.2s ease;
      pointer-events: none;
    }}
    .card-wishlist-btn.active {{
      color: #E53935;
    }}
    .card-wishlist-btn.active svg {{
      fill: #E53935;
      stroke: #E53935;
    }}

    /* =========================================================================
       SNITCH 1500x708 CINEMATIC HERO SLIDER ARCHITECTURE
       ========================================================================= */
    .snitch-hero-section {{
      width: 100%;
      background: #FAF8F5;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0px;
      margin: 0px;
      overflow: hidden;
      border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }}
    .snitch-hero-viewport {{
      /* Auto layout directly matching Snitch */
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      padding: 0px;
      position: relative;
      width: 1500px;
      max-width: 100%;
      height: 708px;
      margin: 0 auto;
      overflow: hidden;
      background: #1A1816;
      user-select: none;
    }}
    .snitch-track {{
      display: flex;
      width: 400%;
      height: 100%;
      transition: transform 1.6s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform;
    }}
    .snitch-slide {{
      width: 25%;
      height: 100%;
      position: relative;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      cursor: pointer;
      overflow: hidden;
    }}

    /* Floating Luxury Content Layer on the Left Negative Space */
    .slide-overlay-content {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      left: 85px;
      max-width: 500px;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 14px;
    }}
    .slide-overlay-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(10px);
      color: #38322C;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    }}
    .slide-overlay-pill .pill-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #C59B27;
    }}
    .slide-overlay-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 52px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #1A1816;
      line-height: 1.08;
      text-transform: uppercase;
      text-shadow: 0 2px 20px rgba(255, 255, 255, 0.65);
    }}
    .slide-overlay-light {{
      font-weight: 300;
      color: #2D2721;
    }}
    .slide-overlay-desc {{
      font-size: 15px;
      color: #554D43;
      line-height: 1.5;
      text-shadow: 0 1px 10px rgba(255, 255, 255, 0.85);
    }}
    .slide-overlay-specs {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11.5px;
      font-weight: 700;
      color: #7A6F62;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .slide-overlay-btn {{
      margin-top: 10px;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: #1A1816;
      color: #FAF8F5;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 4px;
      padding: 15px 32px;
      font-size: 13.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(26, 24, 22, 0.22);
      transition: all 0.25s ease;
    }}
    .slide-overlay-btn:hover {{
      background: #38322C;
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(26, 24, 22, 0.32);
    }}

    /* Slide 1 Special CTA: Sits below the baked MEENU LABEL brand logo */
    .slide-1-cta-box {{
      position: absolute;
      bottom: 115px;
      left: 85px;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }}

    .slider-chevron {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 24px;
      color: #141210;
      z-index: 20;
      transition: all 0.25s ease;
      opacity: 0.85;
    }}
    .slider-chevron:hover {{
      background: #141210;
      color: #FFFFFF;
      opacity: 1;
      transform: translateY(-50%) scale(1.08);
    }}
    .chevron-prev {{ left: 24px; }}
    .chevron-next {{ right: 24px; }}

    /* Dots / Indicators at Bottom */
    .slider-dots-wrap {{
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 20;
      background: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(8px);
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid rgba(0, 0, 0, 0.06);
    }}
    .slider-dot {{
      width: 10px;
      height: 10px;
      border-radius: 5px;
      background: #D4CCC1;
      border: none;
      cursor: pointer;
      transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
    }}
    .slider-dot.active {{
      width: 32px;
      background: #141210;
    }}

    /* Snitch Bottom-Right Atelier Pill */
    .atelier-pill {{
      position: absolute;
      bottom: 24px;
      right: 36px;
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 6px;
      padding: 8px 16px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.06);
      cursor: pointer;
      z-index: 20;
      transition: all 0.2s ease;
    }}
    .atelier-pill:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }}
    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #2B6E44;
      display: inline-block;
      animation: pulse 1.8s infinite;
    }}
    @keyframes pulse {{
      0% {{ transform: scale(0.95); opacity: 0.7; }}
      50% {{ transform: scale(1.3); opacity: 1; }}
      100% {{ transform: scale(0.95); opacity: 0.7; }}
    }}

    /* Slideout Navigation Drawer */
    .nav-drawer-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.45);
      backdrop-filter: blur(4px);
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }}
    .nav-drawer-backdrop.open {{
      opacity: 1;
      pointer-events: auto;
    }}
    .nav-drawer {{
      position: fixed;
      top: 0;
      left: -340px;
      width: 340px;
      height: 100%;
      background: #FFFFFF;
      z-index: 210;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      box-shadow: 4px 0 24px rgba(0,0,0,0.15);
    }}
    .nav-drawer.open {{
      transform: translateX(340px);
    }}
    .nav-drawer-header {{
      padding: 24px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-color);
    }}
    .nav-drawer-body {{
      padding: 24px 28px;
      flex: 1;
      overflow-y: auto;
    }}
    .nav-drawer-links {{
      list-style: none;
    }}
    .nav-drawer-links li {{
      margin-bottom: 18px;
    }}
    .nav-drawer-links a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: block;
      transition: color 0.15s;
    }}
    .nav-drawer-links a:hover {{
      color: var(--accent-gold);
    }}

    /* Catalog Section */
    .catalog-section {{
      max-width: 1440px;
      margin: 50px auto 40px;
      padding: 0 36px;
    }}
    
    /* Sticky Category Selection Header */
    .sticky-catalog-header {{
      position: sticky;
      top: 108px;
      z-index: 85;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 14px 28px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      transition: all 0.25s ease;
    }}
    .sticky-header-info {{
      display: flex;
      flex-direction: column;
    }}
    .sticky-count-pill {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--accent-gold);
      text-transform: uppercase;
    }}

    .section-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 30px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 18px;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .section-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 38px;
      font-weight: 600;
      letter-spacing: -0.01em;
      color: var(--text-main);
    }}
    .section-sub {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }}

    .filter-tabs {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .filter-tab {{
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-tab:hover {{
      border-color: var(--text-main);
      color: var(--text-main);
    }}
    .filter-tab.active {{
      background: var(--text-main);
      color: #FAF8F5;
      border-color: var(--text-main);
    }}

    /* Product Grid */
    .product-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 28px;
    }}
    .product-card {{
      background: var(--bg-card);
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      display: flex;
      flex-direction: column;
    }}
    .product-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 14px 30px rgba(0, 0, 0, 0.08);
    }}
    .card-thumb {{
      position: relative;
      aspect-ratio: 1 / 1.18;
      overflow: hidden;
      background: #EFEFEF;
      cursor: pointer;
    }}
    .card-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      transition: transform 0.4s ease;
      display: block;
    }}
    .product-card:hover .card-thumb img {{
      transform: scale(1.05);
    }}
    .card-badge {{
      position: absolute;
      top: 12px;
      left: 12px;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      z-index: 2;
    }}
    .badge-scarcity {{ background: #FFE8E8; color: var(--accent-rose); }}
    .badge-exclusive {{ background: #F6EBD9; color: var(--accent-gold); }}
    .badge-trending {{ background: #E6F4EA; color: var(--accent-green); }}

    .card-quick-actions {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      right: 12px;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.2s ease;
      z-index: 3;
    }}
    .product-card:hover .card-quick-actions {{
      opacity: 1;
      transform: translateY(0);
    }}
    .btn-quick-view {{
      width: 100%;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(0,0,0,0.1);
      padding: 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      cursor: pointer;
      color: var(--text-main);
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      transition: background 0.15s;
    }}
    .btn-quick-view:hover {{ background: #FFFFFF; color: var(--accent-gold); }}

    .card-body {{
      padding: 18px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .card-cat {{
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }}
    .card-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 19px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 6px;
      line-height: 1.25;
      cursor: pointer;
    }}
    .card-title:hover {{ color: var(--accent-gold); }}
    .card-fabric {{
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .card-price-row {{
      display: flex;
      align-items: baseline;
      gap: 8px;
      margin-top: auto;
      margin-bottom: 12px;
    }}
    .price-main {{
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .price-mrp {{
      font-size: 13px;
      color: var(--text-light);
      text-decoration: line-through;
    }}
    .price-discount {{
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-rose);
    }}

    .card-sizes-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      border-top: 1px solid rgba(230, 224, 214, 0.6);
    }}
    .size-pills {{
      display: flex;
      gap: 5px;
    }}
    .size-chip {{
      font-size: 10px;
      font-weight: 600;
      background: var(--bg-surface);
      padding: 3px 7px;
      border-radius: 3px;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }}
    .size-chip:hover {{
      background: var(--text-main);
      color: #FFF;
    }}
    .stock-chip {{
      font-size: 10px;
      font-weight: 600;
      color: var(--accent-rose);
    }}

    /* Value Strip */
    .value-strip {{
      background: #FFFFFF;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
      padding: 32px 0;
      margin-top: 60px;
    }}
    .value-inner {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 36px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 40px;
    }}
    .value-item {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .value-icon {{
      font-size: 28px;
    }}
    .value-title {{
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 3px;
      letter-spacing: 0.02em;
    }}
    .value-desc {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Founder Section (Minimal Luxury Editorial) */
    .founder-section {{
      max-width: 880px;
      margin: 70px auto 80px;
      padding: 0 36px;
      text-align: center;
    }}
    .founder-content .tag {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--accent-gold);
      display: inline-block;
      margin-bottom: 12px;
    }}
    .founder-content h3 {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(28px, 3.2vw, 38px);
      line-height: 1.25;
      margin-bottom: 16px;
      color: var(--text-main);
      font-weight: 600;
    }}
    .founder-content p {{
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.8;
      margin: 0 auto 16px;
      max-width: 720px;
      font-weight: 400;
    }}
    .founder-sig {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 34px;
      font-style: italic;
      color: var(--text-main);
      margin-top: 22px;
    }}
    .founder-role {{
      font-size: 10.5px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--text-light);
      margin-top: 4px;
    }}

    /* Footer */
    footer {{
      background: #141210;
      color: #FAF8F5;
      padding: 60px 0 24px;
    }}
    .footer-inner {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 36px;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.2fr;
      gap: 40px;
      padding-bottom: 40px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .footer-col h4 {{
      font-size: 13px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 16px;
      color: #FFFFFF;
    }}
    .footer-col p {{
      font-size: 12.5px;
      color: #A39B90;
      line-height: 1.6;
      margin-bottom: 12px;
    }}
    .footer-col ul {{
      list-style: none;
    }}
    .footer-col ul li {{
      margin-bottom: 8px;
    }}
    .footer-col ul a {{
      color: #A39B90;
      text-decoration: none;
      font-size: 12.5px;
      transition: color 0.15s;
    }}
    .footer-col ul a:hover {{
      color: #FFFFFF;
    }}
    .footer-bottom {{
      max-width: 1440px;
      margin: 24px auto 0;
      padding: 0 36px;
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: #726A60;
    }}

    /* Modals & Cart Drawer */
    .modal-backdrop, .cart-backdrop {{
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(4px);
      z-index: 300;
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s ease;
    }}
    .modal-backdrop.open, .cart-backdrop.open {{
      opacity: 1; pointer-events: auto;
    }}

    .product-modal {{
      position: fixed;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%) scale(0.96);
      width: 900px;
      max-width: 94vw;
      max-height: 90vh;
      background: #FFFFFF;
      border-radius: 12px;
      overflow: hidden;
      display: grid;
      grid-template-columns: 1fr 1fr;
      z-index: 310;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
      transition: transform 0.25s ease;
    }}
    .modal-backdrop.open .product-modal {{
      transform: translate(-50%, -50%) scale(1);
    }}
    .modal-media {{
      background: #F5F2EB;
      position: relative;
      height: 100%;
    }}
    .modal-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .modal-info {{
      padding: 36px;
      overflow-y: auto;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
    }}
    .modal-close {{
      position: absolute;
      top: 16px; right: 16px;
      background: #FAF8F5;
      border: 1px solid var(--border-color);
      width: 34px; height: 34px;
      border-radius: 50%;
      cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      font-size: 16px;
      z-index: 10;
      transition: background 0.15s;
    }}
    .modal-close:hover {{ background: #EFEFEF; }}

    .modal-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 600;
      margin-bottom: 4px;
    }}
    .modal-code {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-light);
      letter-spacing: 0.08em;
      margin-bottom: 14px;
    }}
    .modal-price-wrap {{
      display: flex;
      align-items: baseline;
      gap: 10px;
      margin-bottom: 16px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
    }}
    .modal-price-cur {{ font-size: 24px; font-weight: 700; color: var(--text-main); }}
    .modal-price-mrp {{ font-size: 15px; color: var(--text-light); text-decoration: line-through; }}
    .modal-price-off {{ font-size: 12px; font-weight: 700; color: var(--accent-rose); }}

    .modal-desc {{ font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 20px; }}
    .modal-meta-row {{ font-size: 12px; margin-bottom: 8px; color: var(--text-main); }}
    .modal-meta-row strong {{ color: var(--text-muted); }}

    .modal-size-select {{ margin-top: 16px; margin-bottom: 20px; }}
    .modal-size-label {{ display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 8px; }}
    .modal-sizes-group {{ display: flex; gap: 10px; }}
    .modal-size-btn {{
      flex: 1;
      padding: 10px;
      border: 1px solid var(--border-color);
      background: #FFFFFF;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
    }}
    .modal-size-btn.selected {{
      background: var(--text-main);
      color: #FFF;
      border-color: var(--text-main);
    }}

    .modal-btn-primary {{
      background: var(--btn-dark);
      color: #FAF8F5;
      border: none;
      padding: 14px 20px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      width: 100%;
      margin-bottom: 10px;
      transition: background 0.15s;
    }}
    .modal-btn-primary:hover {{ background: var(--btn-hover); }}

    .modal-btn-whatsapp {{
      background: #25D366;
      color: #FFFFFF;
      border: none;
      padding: 12px 20px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-bottom: 14px;
      transition: background 0.15s;
    }}
    .modal-btn-whatsapp:hover {{ background: #20BD5A; }}

    /* Cart Drawer */
    .cart-drawer {{
      position: fixed;
      top: 0; right: -420px;
      width: 420px;
      max-width: 92vw;
      height: 100%;
      background: #FFFFFF;
      z-index: 320;
      box-shadow: -4px 0 30px rgba(0, 0, 0, 0.15);
      display: flex;
      flex-direction: column;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .cart-drawer.open {{
      transform: translateX(-420px);
    }}
    .cart-header {{
      padding: 22px 26px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .cart-body {{
      padding: 22px 26px;
      flex: 1;
      overflow-y: auto;
    }}
    .cart-footer {{
      padding: 22px 26px;
      border-top: 1px solid var(--border-color);
      background: #FAF8F5;
    }}
    .cart-item {{
      display: flex;
      gap: 14px;
      margin-bottom: 18px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border-color);
    }}
    .cart-item img {{
      width: 70px;
      height: 85px;
      object-fit: cover;
      border-radius: 6px;
    }}
    .cart-item-details {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .cart-item-title {{ font-size: 13px; font-weight: 700; color: var(--text-main); }}
    .cart-item-meta {{ font-size: 11px; color: var(--text-muted); }}
    .cart-item-price {{ font-size: 13px; font-weight: 700; }}
    .cart-item-remove {{
      background: none; border: none; font-size: 11px; color: var(--accent-rose);
      cursor: pointer; text-decoration: underline; padding: 0;
    }}

    .toast-note {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: #141210;
      color: #FAF8F5;
      padding: 12px 24px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 600;
      z-index: 500;
      box-shadow: 0 6px 24px rgba(0,0,0,0.25);
      display: none;
    }}

    @media (max-width: 1024px) {{
      .product-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .snitch-hero-viewport {{ height: 50vh; min-height: 400px; }}
      .value-inner {{ grid-template-columns: 1fr; gap: 20px; }}
      .founder-section {{ grid-template-columns: 1fr; }}
      .footer-inner {{ grid-template-columns: 1fr 1fr; }}
    }}
  
    /* =========================================================================
       DEDICATED FULL PRODUCT DETAIL PAGE (PDP) ARCHITECTURE
       ========================================================================= */
    .pdp-section {{
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      padding: 32px 36px 80px;
    }}
    .pdp-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-color);
      gap: 16px;
      flex-wrap: wrap;
    }}
    .pdp-back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 8px 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .pdp-back-btn:hover {{
      background: var(--text-main);
      color: #FFFFFF;
      border-color: var(--text-main);
      transform: translateX(-3px);
    }}
    .pdp-breadcrumb {{
      font-size: 12px;
      color: var(--text-muted);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      font-weight: 500;
    }}
    .pdp-breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .pdp-breadcrumb a:hover {{
      color: var(--accent-gold);
    }}

    /* 2-Column Luxury PDP Layout */
    .pdp-grid {{
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 56px;
      align-items: flex-start;
    }}
    @media (max-width: 992px) {{
      .pdp-grid {{
        grid-template-columns: 1fr;
        gap: 36px;
      }}
    }}

    /* Left Gallery */
    .pdp-gallery-col {{
      position: sticky;
      top: 100px;
    }}
    .pdp-main-image-wrap {{
      position: relative;
      width: 100%;
      border-radius: 12px;
      overflow: hidden;
      background: #F4EFEB;
      border: 1px solid var(--border-color);
      box-shadow: 0 12px 30px rgba(0,0,0,0.04);
    }}
    .pdp-main-image {{
      width: 100%;
      aspect-ratio: 4 / 5;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.4s ease;
    }}
    .pdp-main-image-wrap:hover .pdp-main-image {{
      transform: scale(1.02);
    }}
    .pdp-gallery-badges {{
      position: absolute;
      top: 18px;
      left: 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 2;
    }}
    .pdp-badge-pill {{
      background: rgba(24, 22, 20, 0.9);
      backdrop-filter: blur(8px);
      color: #FFFFFF;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 16px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .pdp-badge-gold {{
      background: #B8860B;
      color: #FFFFFF;
    }}
    .pdp-wishlist-toggle {{
      position: absolute;
      top: 18px;
      right: 18px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(0,0,0,0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 3;
      transition: all 0.2s ease;
      color: #222;
      padding: 0;
    }}
    .pdp-wishlist-toggle:hover {{
      background: #FFFFFF;
      transform: scale(1.1);
      color: #E53935;
    }}
    .pdp-wishlist-toggle.active {{
      color: #E53935;
    }}
    .pdp-wishlist-toggle.active svg {{
      fill: #E53935;
      stroke: #E53935;
    }}
    .pdp-trust-pills {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 18px;
    }}
    .pdp-trust-pill {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      font-size: 11px;
      color: var(--text-main);
      font-weight: 600;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }}
    .pdp-trust-pill-icon {{
      font-size: 18px;
    }}

    /* Right Information & Purchase Column */
    .pdp-info-col {{
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}
    .pdp-tag-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .pdp-collection-tag {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-gold);
    }}
    .pdp-code-tag {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }}
    .pdp-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 34px;
      line-height: 1.15;
      font-weight: 600;
      color: var(--text-main);
      margin: 0;
    }}
    .pdp-price-row {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-color);
    }}
    .pdp-price-main {{
      font-size: 28px;
      font-weight: 800;
      color: var(--text-main);
    }}
    .pdp-price-mrp {{
      font-size: 18px;
      color: var(--text-muted);
      text-decoration: line-through;
    }}
    .pdp-price-discount {{
      background: #E8F5E9;
      color: #2E7D32;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 12px;
    }}
    .pdp-tax-note {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: -6px;
    }}

    /* Scarcity Banner */
    .pdp-scarcity-banner {{
      background: #FFF9E6;
      border: 1px solid #FFE082;
      border-radius: 8px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12px;
      color: #8D6E1A;
      font-weight: 600;
      line-height: 1.4;
    }}
    .pdp-scarcity-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #D97706;
      flex-shrink: 0;
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.2);
    }}

    /* Meta Highlights */
    .pdp-meta-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px 16px;
      font-size: 13px;
    }}
    .pdp-meta-label {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 2px;
    }}
    .pdp-meta-val {{
      font-weight: 600;
      color: var(--text-main);
    }}

    /* Size Selection */
    .pdp-size-section {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .pdp-size-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .pdp-size-label {{
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-main);
    }}
    .pdp-size-chart-link {{
      font-size: 12px;
      font-weight: 600;
      color: var(--accent-gold);
      cursor: pointer;
      text-decoration: underline;
    }}
    .pdp-size-pills {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }}
    .pdp-size-btn {{
      background: #FFFFFF;
      border: 1.5px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 10px;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }}
    .pdp-size-btn:hover {{
      border-color: var(--text-main);
      background: var(--bg-surface);
    }}
    .pdp-size-btn.selected {{
      border-color: var(--text-main);
      background: var(--text-main);
      color: #FFFFFF;
    }}
    .pdp-size-btn.selected .pdp-size-sub {{
      color: rgba(255, 255, 255, 0.8);
    }}
    .pdp-size-btn.selected .pdp-size-stock {{
      color: #FFD54F;
    }}
    .pdp-size-name {{
      font-size: 15px;
      font-weight: 700;
    }}
    .pdp-size-sub {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .pdp-size-stock {{
      font-size: 10px;
      font-weight: 700;
      color: #D97706;
      text-transform: uppercase;
    }}

    /* Actions */
    .pdp-actions-row {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 4px;
    }}
    .pdp-btn-primary {{
      width: 100%;
      background: var(--text-main);
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 16px 24px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }}
    .pdp-btn-primary:hover {{
      background: #333333;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    }}
    .pdp-btn-buy {{
      width: 100%;
      background: #B8860B;
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 14px 24px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .pdp-btn-buy:hover {{
      background: #996F07;
      transform: translateY(-2px);
    }}
    .pdp-btn-whatsapp {{
      width: 100%;
      background: #25D366;
      color: #FFFFFF;
      border: none;
      border-radius: 6px;
      padding: 14px 20px;
      font-family: inherit;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.2s ease;
    }}
    .pdp-btn-whatsapp:hover {{
      background: #1EBE5D;
      transform: translateY(-2px);
    }}

    /* Accordions */
    .pdp-accordions {{
      display: flex;
      flex-direction: column;
      border-top: 1px solid var(--border-color);
      margin-top: 10px;
    }}
    .pdp-accordion-item {{
      border-bottom: 1px solid var(--border-color);
    }}
    .pdp-accordion-header {{
      padding: 16px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--text-main);
      transition: color 0.2s;
    }}
    .pdp-accordion-header:hover {{
      color: var(--accent-gold);
    }}
    .pdp-accordion-icon {{
      font-size: 18px;
      transition: transform 0.2s ease;
    }}
    .pdp-accordion-content {{
      padding: 0 0 16px 0;
      font-size: 13px;
      line-height: 1.6;
      color: var(--text-main);
      display: none;
    }}
    .pdp-accordion-item.open .pdp-accordion-content {{
      display: block;
    }}
    .pdp-accordion-item.open .pdp-accordion-icon {{
      transform: rotate(45deg);
    }}

    /* Related Section */
    .pdp-related-section {{
      margin-top: 80px;
      padding-top: 40px;
      border-top: 1px solid var(--border-color);
    }}
    .pdp-related-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 28px;
      font-weight: 600;
      margin-bottom: 6px;
    }}
    .pdp-related-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}
    .pdp-related-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }}
    @media (max-width: 900px) {{
      .pdp-related-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

  
    /* ========================================================
       SNITCH-STYLE LUXURY LOGIN INTERFACE & MODAL
       ======================================================== */
    .snitch-login-backdrop {{
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 500;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .snitch-login-backdrop.open {{
      display: flex;
      opacity: 1;
    }}

    .snitch-login-dialog {{
      width: 100%;
      max-width: 1040px;
      height: min(650px, 90vh);
      background: #000000;
      border-radius: 22px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 32px 90px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(255, 255, 255, 0.04);
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      overflow: hidden;
      position: relative;
      transform: scale(0.97) translateY(12px);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .snitch-login-backdrop.open .snitch-login-dialog {{
      transform: scale(1) translateY(0);
    }}

    /* Top Action Buttons (Back chevron & Close) */
    .snitch-dialog-back {{
      position: absolute;
      top: 20px;
      left: 20px;
      z-index: 40;
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .snitch-dialog-back:hover {{
      background: rgba(255, 255, 255, 0.2);
      transform: scale(1.06);
    }}
    .snitch-dialog-back svg {{
      width: 18px;
      height: 18px;
    }}

    .snitch-dialog-close {{
      position: absolute;
      top: 18px;
      right: 20px;
      z-index: 40;
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 24px;
      line-height: 1;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .snitch-dialog-close:hover {{
      background: rgba(255, 255, 255, 0.2);
      transform: scale(1.06);
    }}

    /* Left Campaign Column */
    .snitch-login-campaign {{
      position: relative;
      height: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      background: #0a0a0a;
    }}
    .snitch-campaign-photo {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 25%;
    }}
    .snitch-campaign-vignette {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.12) 0%,
        rgba(0, 0, 0, 0.05) 45%,
        rgba(0, 0, 0, 0.65) 75%,
        rgba(0, 0, 0, 0.94) 100%
      );
    }}
    .snitch-campaign-text {{
      position: relative;
      z-index: 2;
      padding: 40px 48px;
      max-width: 580px;
    }}
    .snitch-campaign-pill {{
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: #D4AF37;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 5px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    .snitch-campaign-headline {{
      font-size: clamp(30px, 3.4vw, 46px);
      font-weight: 800;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      line-height: 1.1;
      color: #ffffff;
      margin-bottom: 10px;
      text-shadow: 0 2px 14px rgba(0,0,0,0.6);
    }}
    .snitch-headline-accent {{
      font-style: italic;
      font-family: 'Playfair Display', Georgia, serif;
      font-weight: 700;
      color: #E2725B;
      text-transform: none;
      letter-spacing: 0.02em;
    }}
    .snitch-campaign-atelier {{
      font-size: 12px;
      color: rgba(255, 255, 255, 0.75);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 500;
    }}

    /* Right Form Column */
    .snitch-login-content {{
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
      padding: 32px 28px;
      height: 100%;
    }}

    /* The Snitch Charcoal Card */
    .snitch-login-card {{
      width: 100%;
      max-width: 420px;
      background: #161616;
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 22px;
      padding: 42px 36px 34px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.03);
      position: relative;
    }}

    .snitch-brand-block {{
      text-align: center;
      margin-bottom: 32px;
    }}
    .snitch-brand-title {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0.22em;
      color: #ffffff;
      text-transform: uppercase;
      margin: 0;
      line-height: 1.2;
    }}
    .snitch-brand-tag {{
      font-size: 10px;
      color: #777777;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-top: 6px;
      font-weight: 500;
    }}

    .snitch-input-heading {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #8E8E93;
      margin-bottom: 14px;
      display: block;
    }}

    .snitch-input-row {{
      display: flex;
      align-items: center;
      border-bottom: 1.5px solid #333333;
      padding-bottom: 10px;
      margin-bottom: 24px;
      transition: border-color 0.25s ease;
    }}
    .snitch-input-row:focus-within {{
      border-bottom-color: #D4AF37;
    }}
    .snitch-cc-badge {{
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      margin-right: 14px;
      display: flex;
      align-items: center;
      letter-spacing: 0.04em;
      user-select: none;
    }}
    .snitch-mobile-field {{
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      font-family: inherit;
      font-size: 16px;
      font-weight: 500;
      color: #ffffff;
      letter-spacing: 0.08em;
    }}
    .snitch-mobile-field::placeholder {{
      color: #4A4A4F;
      font-weight: 400;
    }}

    .snitch-validation-error {{
      font-size: 12px;
      color: #ff6b6b;
      margin-top: -16px;
      margin-bottom: 18px;
      display: none;
    }}

    /* Primary Action Button (White with black text and right arrow) */
    .snitch-submit-btn {{
      width: 100%;
      height: 48px;
      background: #ffffff;
      color: #000000;
      border: none;
      border-radius: 8px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
      margin-bottom: 22px;
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.1);
    }}
    .snitch-submit-btn:hover {{
      background: #f0f0f0;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(255, 255, 255, 0.18);
    }}
    .snitch-submit-btn:active {{
      transform: translateY(0);
    }}
    .snitch-submit-btn svg {{
      width: 16px;
      height: 16px;
      transition: transform 0.2s;
    }}
    .snitch-submit-btn:hover svg {{
      transform: translateX(3px);
    }}

    .snitch-legal-note {{
      font-size: 11px;
      line-height: 1.6;
      color: #666666;
      text-align: center;
    }}
    .snitch-legal-note a {{
      color: #999999;
      text-decoration: underline;
      text-underline-offset: 2px;
      transition: color 0.2s;
    }}
    .snitch-legal-note a:hover {{
      color: #ffffff;
    }}

    /* OTP Inputs */
    .snitch-otp-sent-info {{
      color: #aaaaaa;
      margin-top: 6px;
      font-size: 12px;
      text-transform: none;
      letter-spacing: 0;
    }}
    .snitch-edit-phone-btn {{
      background: none;
      border: none;
      color: #D4AF37;
      cursor: pointer;
      font-weight: 600;
      margin-left: 6px;
      text-decoration: underline;
      font-size: 12px;
    }}
    .snitch-otp-grid {{
      display: flex;
      gap: 12px;
      justify-content: center;
      margin: 22px 0 16px;
    }}
    .snitch-digit-box {{
      width: 52px;
      height: 56px;
      background: #202020;
      border: 1.5px solid #333333;
      border-radius: 10px;
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      text-align: center;
      font-family: inherit;
      outline: none;
      transition: all 0.2s;
    }}
    .snitch-digit-box:focus {{
      border-color: #D4AF37;
      background: #252525;
      box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
    }}
    .snitch-resend-bar {{
      text-align: center;
      margin-bottom: 20px;
      font-size: 12px;
      color: #777777;
    }}
    .snitch-resend-action {{
      background: none;
      border: none;
      color: #D4AF37;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: underline;
    }}
    .snitch-demo-badge {{
      font-size: 11px;
      color: #777777;
      text-align: center;
      margin-top: 10px;
    }}

    /* VIP Privé Dashboard */
    .snitch-vip-avatar {{
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: rgba(37, 211, 102, 0.12);
      border: 1.5px solid #25D366;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 14px;
      color: #25D366;
    }}
    .snitch-vip-status-tag {{
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #D4AF37;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 4px 10px;
      border-radius: 14px;
      margin-bottom: 8px;
    }}
    .snitch-vip-user {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 18px;
      letter-spacing: 0.04em;
    }}
    .snitch-vip-perks {{
      background: #202020;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 20px;
      text-align: left;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .snitch-perk-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .snitch-perk-icon {{
      font-size: 16px;
      line-height: 1.2;
    }}
    .snitch-perk-text strong {{
      display: block;
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
    }}
    .snitch-perk-text span {{
      display: block;
      color: #888888;
      font-size: 11px;
    }}
    .snitch-vip-concierge-btn {{
      display: block;
      width: 100%;
      padding: 11px 16px;
      border-radius: 8px;
      background: rgba(37, 211, 102, 0.1);
      border: 1px solid rgba(37, 211, 102, 0.3);
      color: #25D366;
      text-decoration: none;
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 14px;
      transition: background 0.2s;
    }}
    .snitch-vip-concierge-btn:hover {{
      background: rgba(37, 211, 102, 0.18);
    }}
    .snitch-signout-btn {{
      background: none;
      border: none;
      color: #777777;
      font-size: 12px;
      cursor: pointer;
      text-decoration: underline;
      transition: color 0.2s;
    }}
    .snitch-signout-btn:hover {{
      color: #ffffff;
    }}

    /* Header Active User Indicator Dot */
    .account-active-badge {{
      position: absolute;
      top: 4px;
      right: 4px;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #25D366;
      border: 1.5px solid #ffffff;
      display: none;
    }}

    /* Responsive Snitch Login Dialog */
    @media (max-width: 860px) {{
      .snitch-login-dialog {{
        grid-template-columns: 1fr;
        height: 94vh;
        max-height: none;
        overflow-y: auto;
      }}
      .snitch-login-campaign {{
        height: 200px;
        min-height: 200px;
      }}
      .snitch-campaign-text {{
        padding: 20px 24px;
      }}
      .snitch-campaign-headline {{
        font-size: 24px;
      }}
      .snitch-login-content {{
        padding: 20px 16px 28px;
      }}
      .snitch-login-card {{
        padding: 28px 20px 24px;
      }}
    }}

      /* WhatsApp Benefit Hint Box */
    .whatsapp-benefit-box {{
      background: #F4FAF6;
      border: 1px solid rgba(37, 211, 102, 0.35);
      border-radius: 8px;
      padding: 11px 14px;
      margin-top: 10px;
      font-size: 12px;
      line-height: 1.55;
      color: #1B4D30;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      text-align: left;
    }}
    .whatsapp-benefit-box strong {{
      color: #0F3820;
      font-weight: 700;
    }}
    .whatsapp-benefit-box .wa-icon {{
      font-size: 16px;
      line-height: 1.2;
      flex-shrink: 0;
      margin-top: 2px;
    }}

  
    /* ========================================================
       THE CAMPAIGN EDIT / ASYMMETRICAL EDITORIAL LOOKBOOK
       ======================================================== */
    .campaign-edit-section {{
      max-width: 1440px;
      margin: 80px auto 70px;
      padding: 0 36px;
    }}

    .campaign-header {{
      text-align: center;
      margin-bottom: 38px;
    }}
    .campaign-eyebrow {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 8px;
      display: inline-block;
    }}
    .campaign-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(28px, 3.4vw, 42px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0 0 10px;
      line-height: 1.18;
    }}
    .campaign-title .accent {{
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      color: #E2725B;
      text-transform: none;
      font-weight: 600;
    }}
    .campaign-sub {{
      font-size: 13px;
      color: var(--text-muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-weight: 500;
      max-width: 620px;
      margin: 0 auto;
    }}

    /* Asymmetrical Grid: Left (58%) & Right (42%) */
    .campaign-grid {{
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: 24px;
      align-items: stretch;
    }}

    /* Left Hero Card */
    .campaign-hero-card {{
      position: relative;
      border-radius: 18px;
      overflow: hidden;
      min-height: 640px;
      background: #0D0D0D;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08);
      cursor: pointer;
    }}
    .campaign-hero-img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 25%;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .campaign-hero-card:hover .campaign-hero-img {{
      transform: scale(1.04);
    }}
    .campaign-hero-vignette {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.08) 0%,
        rgba(0, 0, 0, 0.15) 50%,
        rgba(0, 0, 0, 0.72) 80%,
        rgba(0, 0, 0, 0.94) 100%
      );
    }}
    .campaign-hero-content {{
      position: relative;
      z-index: 2;
      padding: 36px 40px;
    }}
    .campaign-badge {{
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #D4AF37;
      background: rgba(0, 0, 0, 0.55);
      border: 1px solid rgba(212, 175, 55, 0.4);
      padding: 5px 12px;
      border-radius: 20px;
      margin-bottom: 12px;
      backdrop-filter: blur(8px);
    }}
    .campaign-hero-name {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(26px, 2.6vw, 34px);
      font-weight: 700;
      color: #FFFFFF;
      margin: 0 0 6px;
      line-height: 1.2;
    }}
    .campaign-hero-meta {{
      font-size: 13px;
      color: rgba(255, 255, 255, 0.85);
      margin-bottom: 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .campaign-price {{
      font-size: 18px;
      font-weight: 700;
      color: #FFFFFF;
    }}
    .campaign-mrp {{
      font-size: 14px;
      color: rgba(255, 255, 255, 0.55);
      text-decoration: line-through;
    }}
    .campaign-hero-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .btn-campaign-primary {{
      background: #FFFFFF;
      color: #000000;
      border: none;
      padding: 12px 22px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .btn-campaign-primary:hover {{
      background: #EAEAEA;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
    }}
    .btn-campaign-secondary {{
      background: rgba(255, 255, 255, 0.15);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 12px 20px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      cursor: pointer;
      backdrop-filter: blur(8px);
      transition: all 0.2s ease;
    }}
    .btn-campaign-secondary:hover {{
      background: rgba(255, 255, 255, 0.3);
      border-color: #FFFFFF;
    }}

    /* Right Stack Column (2 Cards) */
    .campaign-stack {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .campaign-sub-card {{
      position: relative;
      border-radius: 18px;
      overflow: hidden;
      flex: 1;
      min-height: 308px;
      background: #0D0D0D;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
      cursor: pointer;
    }}
    .campaign-sub-img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 25%;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .campaign-sub-card:hover .campaign-sub-img {{
      transform: scale(1.04);
    }}
    .campaign-sub-vignette {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.05) 0%,
        rgba(0, 0, 0, 0.2) 40%,
        rgba(0, 0, 0, 0.75) 80%,
        rgba(0, 0, 0, 0.92) 100%
      );
    }}
    .campaign-sub-content {{
      position: relative;
      z-index: 2;
      padding: 24px 28px;
    }}
    .campaign-sub-name {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 700;
      color: #FFFFFF;
      margin: 0 0 4px;
    }}
    .campaign-sub-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 10px;
    }}
    .campaign-sub-price {{
      font-size: 15px;
      font-weight: 700;
      color: #FFFFFF;
    }}
    .btn-campaign-sub {{
      background: #FFFFFF;
      color: #000000;
      border: none;
      padding: 8px 14px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .btn-campaign-sub:hover {{
      background: #EAEAEA;
    }}

    /* Responsive */
    @media (max-width: 900px) {{
      .campaign-grid {{
        grid-template-columns: 1fr;
      }}
      .campaign-hero-card {{
        min-height: 480px;
      }}
      .campaign-hero-content {{
        padding: 24px 20px;
      }}
      .campaign-sub-card {{
        min-height: 260px;
      }}
      .campaign-sub-content {{
        padding: 20px 20px;
      }}
    }}

  
    /* ========================================================
       TOUCH & FEEL: FABRIC SPOTLIGHT (MINIMAL ON-IMAGE LUXURY)
       ======================================================== */
    .craftsmanship-section {{
      max-width: 1440px;
      margin: 20px auto 80px;
      padding: 0 36px;
    }}
    .craftsmanship-header {{
      text-align: center;
      margin-bottom: 36px;
    }}
    .craftsmanship-eyebrow {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 8px;
      display: inline-block;
    }}
    .craftsmanship-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 3.2vw, 40px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0;
      line-height: 1.18;
    }}
    .craftsmanship-title .accent {{
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      color: #E2725B;
      text-transform: none;
      font-weight: 600;
    }}

    .craftsmanship-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }}
    .craft-card {{
      position: relative;
      height: 560px;
      border-radius: 14px;
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
      background: #111111;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .craft-card:hover {{
      transform: translateY(-6px);
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.20);
    }}
    .craft-card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      transition: transform 0.8s cubic-bezier(0.2, 1, 0.3, 1);
      display: block;
    }}
    .craft-card:hover .craft-card-img {{
      transform: scale(1.05);
    }}
    .craft-card-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0) 35%, rgba(0,0,0,0.85) 100%);
      pointer-events: none;
      transition: background 0.4s ease;
    }}
    .craft-card:hover .craft-card-overlay {{
      background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 30%, rgba(0,0,0,0.92) 100%);
    }}
    .craft-card-badge {{
      position: absolute;
      top: 20px;
      left: 20px;
      background: rgba(18, 18, 18, 0.65);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #F7EFE6;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 20px;
      z-index: 2;
    }}
    .craft-card-content {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 32px 28px;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }}
    .craft-card-eyebrow {{
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #E6C285;
      text-shadow: 0 1px 3px rgba(0,0,0,0.6);
    }}
    .craft-card-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 2.2vw, 32px);
      font-weight: 700;
      color: #FFFFFF;
      margin: 0;
      line-height: 1.15;
      letter-spacing: 0.02em;
      text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }}
    .craft-card-cta {{
      margin-top: 6px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.95);
      color: #111111;
      padding: 11px 22px;
      border-radius: 30px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }}
    .craft-card:hover .craft-card-cta {{
      background: #D4AF37;
      color: #111111;
      transform: translateX(4px);
    }}
    .craft-card-cta svg {{
      transition: transform 0.3s ease;
    }}
    .craft-card:hover .craft-card-cta svg {{
      transform: translateX(3px);
    }}

    @media (max-width: 1024px) {{
      .craftsmanship-grid {{
        grid-template-columns: 1fr;
        gap: 20px;
      }}
      .craft-card {{
        height: 480px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Marquee -->
  <div class="announcement-bar">
    <div>⚡ DEBUT DROP 01 LIVE &bull; 100% PURE BREATHABLE SILHOUETTES &bull; CHANDIGARH</div>
    <div>
      <span>FREE 24-HR EXPRESS TRICITY DELIVERY</span>
      <a href="javascript:void(0)" onclick="openSizeGuide()">SIZE GUIDE</a>
    </div>
  </div>

  <!-- Snitch-Style Minimalist Luxury Header -->
  <header>
    <div class="header-bar">
      <!-- Left: Hamburger Menu Icon (Kept in place) -->
      <div class="header-left">
        <button class="hamburger-btn" onclick="openNavDrawer()" title="Open Navigation Menu" aria-label="Open Navigation Menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Middle: Centered Authentic Canva Brand Logo -->
      <div class="header-center">
        <a href="javascript:void(0)" onclick="closeProductPage()" title="Meenu Label Homepage">
          <img src="{logo_b64}" alt="Meenu Label" class="brand-logo-img">
        </a>
      </div>

      <!-- Right: Snitch 4 Minimalist Line Icons (Search, Bag, Wishlist, User) -->
      <div class="header-right">
        <!-- 1. Search -->
        <button class="header-icon-action" onclick="toggleSearchBar()" title="Search Drop 01" aria-label="Search">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="7.5"></circle>
            <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
          </svg>
        </button>

        <!-- 2. Shopping Bag -->
        <button class="header-icon-action" onclick="toggleCart()" title="Shopping Bag" aria-label="Shopping Bag">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
            <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
          </svg>
          <span class="header-badge-pill" id="headerCartCount">0</span>
        </button>

        <!-- 3. Wishlist (Heart) -->
        <button class="header-icon-action" onclick="toggleWishlistDrawer()" title="Saved Wishlist" aria-label="Wishlist">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
          </svg>
          <span class="header-badge-pill" id="headerWishlistCount">0</span>
        </button>

        <!-- 4. User Account -->
        <button class="header-icon-action" onclick="openAccountModal()" title="Account & VIP Login" aria-label="Account" style="position:relative;">
        <span class="account-active-badge" id="accountActiveBadge"></span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="7.5" r="4"></circle>
            <path d="M5 20.5a7 7 0 0 1 14 0"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Slide-Down Search Overlay -->
    <div class="search-overlay-bar" id="searchOverlayBar">
      <div class="search-overlay-inner">
        <button class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>
        <div class="search-input-box">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="7.5"></circle>
            <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
          </svg>
          <input type="text" id="searchInput" placeholder="Search by silhouette, style code (e.g. JAB26ST05010), fabric, color..." onkeyup="searchProducts()">
          <button class="search-clear-btn" onclick="clearSearch()" title="Clear">&times;</button>
        </div>
        <div class="search-quick-tags">
          <span class="quick-tag-label">Popular Searches:</span>
          <button type="button" class="quick-tag" onclick="quickSearch('Festive')">Festive Suits</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Co-ord')">Co-ord Sets</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Chanderi')">Chanderi Silk</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Sharara')">Sharara</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Dress')">Midi Dress</button>
          <button type="button" class="quick-tag" onclick="quickSearch('Cotton')">Pure Cotton</button>
        </div>
      </div>
    </div>
  </header>

  <!-- Snitch 1500x708 Auto-Layout Hero Slider Section -->
  <!-- Main Storefront Home View (Hero, Filter Tabs, 16 Silhouettes Grid, Founder) -->
  <div id="storefrontHomeView">
<section class="snitch-hero-section">
    <div class="snitch-hero-viewport" id="heroSlider">
      <div class="snitch-track" id="sliderTrack">
        
        <!-- Slide 1: Flagship Royal Wine Courtyard Elegance (JAB26ST05010) -->
        <div class="snitch-slide" style="background-image: url('{banner_1_b64}');" onclick="openProductPage('JAB26ST05010')">
          <div class="slide-1-cta-box">
            <div class="slide-overlay-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; 100% PURE CHANDERI SILK
            </div>
            <div class="slide-overlay-specs" style="color: #4A4036; text-shadow: 0 1px 8px rgba(255,255,255,0.9);">
              <span>Jaipur Heritage Looms</span> &bull; <span>Strictly 3 Pieces (M, L, XL)</span> &bull; <span>₹2,299</span>
            </div>
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductPage('JAB26ST05010')">
              SHOP FESTIVE SUIT &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 2: Royal Gulabi Pavilion (JAC25ST03063) -->
        <div class="snitch-slide" style="background-image: url('{banner_2_b64}');" onclick="openProductPage('JAC25ST03063')">
          <div class="slide-overlay-content">
            <div class="slide-overlay-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; LIMITED EDITION
            </div>
            <h1 class="slide-overlay-title">
              GULABI,<br>
              <span class="slide-overlay-light">POWDER PINK GRACE.</span>
            </h1>
            <p class="slide-overlay-desc">
              Pure Cotton Silk straight-cut kurta with delicate golden neckline zari, tailored trousers, and floral-printed organza dupatta.
            </p>
            <div class="slide-overlay-specs">
              <span>Cotton Silk 3-Pc</span> &bull; <span>Organza Dupatta</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductPage('JAC25ST03063')">
              VIEW GULABI SUIT &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 3: Retro Polka Dot Veranda (JAA26DR03942) -->
        <div class="snitch-slide" style="background-image: url('{banner_3_b64}');" onclick="openProductPage('JAA26DR03942')">
          <div class="slide-overlay-content">
            <div class="slide-overlay-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; SCARCITY EDIT
            </div>
            <h1 class="slide-overlay-title">
              RETRO,<br>
              <span class="slide-overlay-light">BREATHABLE, BETTER.</span>
            </h1>
            <p class="slide-overlay-desc">
              100% Breathable Pure Cotton with cinched waist sash, flared A-line drape, and timeless vintage chic.
            </p>
            <div class="slide-overlay-specs">
              <span>Flared Wrap Dress</span> &bull; <span>Pure Cotton</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductPage('JAA26DR03942')">
              EXPLORE WRAP DRESS &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 4: Lime Halter Luxury Terrace (SET916) -->
        <div class="snitch-slide" style="background-image: url('{banner_4_b64}');" onclick="openProductPage('SET916')">
          <div class="slide-overlay-content">
            <div class="slide-overlay-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; TRENDING EDIT
            </div>
            <h1 class="slide-overlay-title">
              EFFORTLESS,<br>
              <span class="slide-overlay-light">FLOWING, CHIC.</span>
            </h1>
            <p class="slide-overlay-desc">
              High-neck halter top in textured dobby chiffon paired with fluid wide-leg palazzo pants in striking chartreuse lime.
            </p>
            <div class="slide-overlay-specs">
              <span>Palazzo Co-ord Set</span> &bull; <span>Dobby Chiffon</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductPage('SET916')">
              SHOP CO-ORD SET &rarr;
            </button>
          </div>
        </div>

      </div>

      <!-- Navigation Chevrons -->
      <button class="slider-chevron chevron-prev" onclick="prevSlide()" aria-label="Previous Slide">&#x2039;</button>
      <button class="slider-chevron chevron-next" onclick="nextSlide()" aria-label="Next Slide">&#x203A;</button>

      <!-- Bottom Center Progress Dots -->
      <div class="slider-dots-wrap" id="sliderDots">
        <button class="slider-dot active" onclick="goToSlide(0)"></button>
        <button class="slider-dot" onclick="goToSlide(1)"></button>
        <button class="slider-dot" onclick="goToSlide(2)"></button>
        <button class="slider-dot" onclick="goToSlide(3)"></button>
      </div>

      <!-- Snitch Bottom-Right Atelier Pill -->
      <div class="atelier-pill" onclick="document.getElementById('catalog').scrollIntoView({{behavior:'smooth'}})">
        <span class="pulse-dot"></span> Drop 01 &bull; Strictly 48 Pieces Total
      </div>
    </div>
  </section>

  <!-- Slideout Navigation Drawer -->
  

  <!-- ========================================================
       THE CAMPAIGN EDIT / ASYMMETRICAL EDITORIAL LOOKBOOK
       ======================================================== -->
  <section class="campaign-edit-section">
    <div class="campaign-header">
      <span class="campaign-eyebrow">Atelier Capsule 01 &bull; Editorial Lookbook</span>
      <h2 class="campaign-title">
        THE CAMPAIGN EDIT: EFFORTLESS CHANDIGARH MORNINGS TO <span class="accent">REGAL EVENINGS</span>
      </h2>
      <p class="campaign-sub">Curated silhouettes styled in natural daylight across Chandigarh's iconic verandahs and promenades.</p>
    </div>

    <div class="campaign-grid">
      <!-- Left Main Feature (58%): The Royal Wine Chanderi Festive Suit (SKU: JAB26ST05010) -->
      <div class="campaign-hero-card" onclick="openProductPage('JAB26ST05010')">
        <img src="{campaign_cafe_b64}" alt="The Royal Wine Chanderi Festive Suit" class="campaign-hero-img">
        <div class="campaign-hero-vignette"></div>
        <div class="campaign-hero-content">
          <span class="campaign-badge">Editorial Drop Headliner &bull; Garden Verandah</span>
          <h3 class="campaign-hero-name">The Royal Wine Chanderi Festive Suit</h3>
          <div class="campaign-hero-meta">
            <span class="campaign-price">&#8377;2,299</span>
            <span class="campaign-mrp">&#8377;3,699</span>
            <span style="font-size:11px; background:rgba(37,211,102,0.2); color:#25D366; padding:2px 8px; border-radius:12px; font-weight:700;">38% OFF</span>
            <span style="font-size:12px; color:rgba(255,255,255,0.7);">&bull; Handcrafted Chanderi &amp; Zari</span>
          </div>
          <div class="campaign-hero-actions" onclick="event.stopPropagation()">
            <button class="btn-campaign-primary" onclick="openProductPage('JAB26ST05010')">
              <span>SHOP SILHOUETTE</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </button>
            <button class="btn-campaign-secondary" onclick="openQuickView('JAB26ST05010')">
              &#9881; QUICK VIEW
            </button>
          </div>
        </div>
      </div>

      <!-- Right Stack (42%): 2 Companion Silhouettes -->
      <div class="campaign-stack">
        <!-- Top Right Card: Mustard Crepe Angrakha Co-ord Set (SKU: SET974) -->
        <div class="campaign-sub-card" onclick="openProductPage('SET974')">
          <img src="{campaign_balcony_b64}" alt="Mustard Crepe Angrakha Co-ord Set" class="campaign-sub-img">
          <div class="campaign-sub-vignette"></div>
          <div class="campaign-sub-content">
            <span class="campaign-badge" style="font-size:9px; padding:3px 8px;">The Balcony Edit &bull; Modern Wrap</span>
            <h4 class="campaign-sub-name">Mustard Crepe Angrakha Co-ord</h4>
            <p style="font-size:12px; color:rgba(255,255,255,0.75); margin:0 0 8px;">Gold Gota Trim with Side Tie-Up Tassels</p>
            <div class="campaign-sub-meta" onclick="event.stopPropagation()">
              <div>
                <span class="campaign-sub-price">&#8377;1,699</span>
                <span style="font-size:11px; color:rgba(255,255,255,0.5); text-decoration:line-through; margin-left:6px;">&#8377;2,799</span>
              </div>
              <button class="btn-campaign-sub" onclick="openProductPage('SET974')">
                <span>SHOP LOOK</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Bottom Right Card: White Porcelain Floral Wrap Dress (SKU: JNE4046) -->
        <div class="campaign-sub-card" onclick="openProductPage('JNE4046')">
          <img src="{campaign_sukhna_b64}" alt="White Porcelain Floral Wrap Dress" class="campaign-sub-img">
          <div class="campaign-sub-vignette"></div>
          <div class="campaign-sub-content">
            <span class="campaign-badge" style="font-size:9px; padding:3px 8px;">Sukhna Promenade &bull; Resort Elegance</span>
            <h4 class="campaign-sub-name">White Porcelain Floral Wrap Dress</h4>
            <p style="font-size:12px; color:rgba(255,255,255,0.75); margin:0 0 8px;">Featherlight Georgette with Circular Waist Belt</p>
            <div class="campaign-sub-meta" onclick="event.stopPropagation()">
              <div>
                <span class="campaign-sub-price">&#8377;1,599</span>
                <span style="font-size:11px; color:rgba(255,255,255,0.5); text-decoration:line-through; margin-left:6px;">&#8377;2,599</span>
              </div>
              <button class="btn-campaign-sub" onclick="openProductPage('JNE4046')">
                <span>SHOP LOOK</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

        <!-- ========================================================
       TOUCH & FEEL: FABRIC SPOTLIGHT (MINIMAL ON-IMAGE LUXURY)
       ======================================================== -->
  <section class="craftsmanship-section">
    <div class="craftsmanship-header">
      <span class="craftsmanship-eyebrow">Atelier Textile Mastery &bull; Artisanal Heritage</span>
      <h2 class="craftsmanship-title">
        TOUCH &amp; FEEL: THE ANATOMY OF <span class="accent">BESPOKE LUXURY</span>
      </h2>
    </div>

    <div class="craftsmanship-grid">
      <!-- Card 1: Hand-Woven Chanderi Silk -->
      <div class="craft-card" onclick="filterCategory('festive'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <img src="{craft_chanderi_b64}" alt="Hand-Woven Chanderi Silk" class="craft-card-img" loading="lazy">
        <div class="craft-card-overlay"></div>
        <span class="craft-card-badge">Chanderi Silk</span>
        <div class="craft-card-content">
          <span class="craft-card-eyebrow">Jaipur Heritage Looms</span>
          <h3 class="craft-card-title">Festive Chanderi Suits</h3>
          <div class="craft-card-cta">
            <span>EXPLORE SUITS</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>

      <!-- Card 2: Fluid Crepe Silk Co-ords -->
      <div class="craft-card" onclick="filterCategory('coord'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <img src="{craft_crepe_b64}" alt="Fluid Crepe Silk Co-ords" class="craft-card-img" loading="lazy">
        <div class="craft-card-overlay"></div>
        <span class="craft-card-badge">Fluid Silk Crepe</span>
        <div class="craft-card-content">
          <span class="craft-card-eyebrow">Anti-Wrinkle Drape</span>
          <h3 class="craft-card-title">Angrakha Co-ord Sets</h3>
          <div class="craft-card-cta">
            <span>EXPLORE CO-ORDS</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>

      <!-- Card 3: Organza Sheer & Gota Detailing -->
      <div class="craft-card" onclick="filterCategory('all'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <img src="{craft_organza_b64}" alt="Organza Sheer & Gota Detailing" class="craft-card-img" loading="lazy">
        <div class="craft-card-overlay"></div>
        <span class="craft-card-badge">Organza &amp; Gota Patti</span>
        <div class="craft-card-content">
          <span class="craft-card-eyebrow">Chandigarh Atelier</span>
          <h3 class="craft-card-title">Handcrafted Silhouettes</h3>
          <div class="craft-card-cta">
            <span>EXPLORE COLLECTION</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Catalog Section -->
  <section class="catalog-section" id="catalog">
    <!-- Sticky Category Selection Header Bar -->
    <div class="sticky-catalog-header" id="stickyCatalogHeader">
      <div class="sticky-header-info">
        <div style="display:flex; align-items:center; gap:10px;">
          <h2 class="section-title" style="margin:0; font-size:22px; letter-spacing:0.02em;">Signature Silhouettes</h2>
          <span class="sticky-count-pill" id="activeCategoryCount">HANDCRAFTED EDITIONS</span>
        </div>
        <p class="section-sub" style="margin:4px 0 0 0; font-size:12px;">Limited Atelier Run &bull; Strictly 1 piece per size (M, L, XL)</p>
      </div>

      <div class="filter-tabs">
        <button class="filter-tab active" data-cat="all" onclick="filterCategory('all', this)">All Silhouettes</button>
        <button class="filter-tab" data-cat="coord" onclick="filterCategory('coord', this)">Co-ord Sets</button>
        <button class="filter-tab" data-cat="festive" onclick="filterCategory('festive', this)">Festive Suits</button>
        <button class="filter-tab" data-cat="dress" onclick="filterCategory('dress', this)">Midi Dresses</button>
        <button class="filter-tab" data-cat="top" onclick="filterCategory('top', this)">Tops &amp; Blouses</button>
      </div>
    </div>

    <div class="product-grid" id="productGrid">
      {cards_html}
    </div>
  </section>

    


  <!-- Value Props -->
  <div class="value-strip">
    <div class="value-inner">
      <div class="value-item">
        <div class="value-icon">⚡</div>
        <div>
          <div class="value-title">Tricity 24-Hr Express Dispatch</div>
          <div class="value-desc">Priority same-day packing and next-day delivery across Chandigarh, Mohali, and Panchkula.</div>
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
        <div class="value-icon">🔄</div>
        <div>
          <div class="value-title">7-Day Easy Size Exchange</div>
          <div class="value-desc">Hassle-free door-to-door size exchange. Delivered pristine in our reusable EVA zipper bags.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Founder Story & Transparency Section -->
  <!-- Founder Section (Centered Minimal Editorial) -->
  <section class="founder-section" id="founder">
    <div class="founder-content">
      <span class="tag">Chandigarh Atelier &bull; Conscious Creation</span>
      <h3>Mindful Elegance, Tailored in Limited Batches.</h3>
      <p>
        In an era of mass-produced polyester, Meenu Label was founded on a simple promise: 
        <strong>pure breathable fabrics, timeless silhouettes, and mindful small-batch creation.</strong>
      </p>
      <div class="founder-sig">Meenu</div>
      <div class="founder-role">Founder, Meenu Label &bull; Chandigarh</div>
    </div>
  </section>
  </div>

  <!-- DEDICATED FULL PRODUCT DETAIL VIEW (PDP) -->
  <div id="productDetailView" style="display:none;">
    <div class="pdp-section">
      <!-- PDP Top Navigation & Breadcrumbs -->
      <div class="pdp-top-bar">
        <button class="pdp-back-btn" onclick="closeProductPage()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          BACK TO DROP 01
        </button>
        <div class="pdp-breadcrumb">
          <a href="javascript:void(0)" onclick="closeProductPage()">HOME</a> &nbsp;/&nbsp;
          <span id="pdpBreadcrumbCat">FESTIVE SUITS</span> &nbsp;/&nbsp;
          <span id="pdpBreadcrumbTitle" style="color:var(--text-main); font-weight:700;">JAIPUR CHANDERI SILK FESTIVE SUIT</span>
        </div>
      </div>

      <!-- Main PDP 2-Column Grid -->
      <div class="pdp-grid">
        <!-- Left: Visual Gallery -->
        <div class="pdp-gallery-col">
          <div class="pdp-main-image-wrap">
            <div class="pdp-gallery-badges">
              <span class="pdp-badge-pill" id="pdpBadgePill">DROP 01 STAR</span>
              <span class="pdp-badge-pill pdp-badge-gold">STRICTLY 3 PIECES CRAFTED</span>
            </div>
            <button class="pdp-wishlist-toggle" id="pdpWishlistBtn" onclick="togglePdpWishlist()" title="Save to Wishlist" aria-label="Save to Wishlist">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
            </button>
            <img id="pdpMainImg" src="" alt="Silhouette" class="pdp-main-image">
          </div>

          <!-- Trust Badges -->
          <div class="pdp-trust-pills">
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#10024;</span>
              <span>Chandigarh Atelier</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Handcrafted Precision</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128666;</span>
              <span>Free 24-Hr Express</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Tricity Priority Courier</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128207;</span>
              <span>Complimentary Fit</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Studio Hem Adjustments</span>
            </div>
          </div>
        </div>

        <!-- Right: Comprehensive Product Info & Checkout Actions -->
        <div class="pdp-info-col">
          <div class="pdp-tag-row">
            <span class="pdp-collection-tag">MEENU LABEL &bull; AUTUMN/WINTER 2026 DEBUT</span>
            <span class="pdp-code-tag" id="pdpCodeTag">STYLE #JAB26ST05010</span>
          </div>

          <h1 class="pdp-title" id="pdpTitle">The Royal Wine Chanderi Festive Suit</h1>

          <div class="pdp-price-row">
            <span class="pdp-price-main" id="pdpPriceMain">&#8377;2,299</span>
            <span class="pdp-price-mrp" id="pdpPriceMrp">&#8377;3,699</span>
            <span class="pdp-price-discount" id="pdpDiscount">38% OFF</span>
          </div>
          <div class="pdp-tax-note">Inclusive of all taxes &bull; Free express delivery across India</div>

          <!-- Scarcity Callout -->
          <div class="pdp-scarcity-banner">
            <span class="pdp-scarcity-dot"></span>
            <span>STRICT ATELIER SCARCITY: Strictly 1 piece per size (M, L, XL). Only 3 pieces produced nationwide.</span>
          </div>

          <!-- Meta Highlights Grid -->
          <div class="pdp-meta-grid">
            <div>
              <div class="pdp-meta-label">Fabric & Weave</div>
              <div class="pdp-meta-val" id="pdpMetaFabric">Chanderi Silk & Zari with Organza Dupatta</div>
            </div>
            <div>
              <div class="pdp-meta-label">Color Palette</div>
              <div class="pdp-meta-val" id="pdpMetaColor">Royal Wine & Antique Gold</div>
            </div>
          </div>

          <!-- Size Selection -->
          <div class="pdp-size-section">
            <div class="pdp-size-header">
              <span class="pdp-size-label">Select Size (Standard Indian Pret)</span>
              <span class="pdp-size-chart-link" onclick="openSizeGuide()">&#128207; View Detailed Measurements</span>
            </div>
            <div class="pdp-size-pills">
              <button type="button" class="pdp-size-btn selected" id="pdpSizeBtn_M" onclick="selectPdpSize('M', this)">
                <span class="pdp-size-name">M (38)</span>
                <span class="pdp-size-sub">Bust 38" | Waist 34"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_L" onclick="selectPdpSize('L', this)">
                <span class="pdp-size-name">L (40)</span>
                <span class="pdp-size-sub">Bust 40" | Waist 36"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
              <button type="button" class="pdp-size-btn" id="pdpSizeBtn_XL" onclick="selectPdpSize('XL', this)">
                <span class="pdp-size-name">XL (42)</span>
                <span class="pdp-size-sub">Bust 42" | Waist 38"</span>
                <span class="pdp-size-stock">Only 1 Left</span>
              </button>
            </div>
          </div>

          <!-- Actions -->
          <div class="pdp-actions-row">
            <button class="pdp-btn-primary" onclick="addPdpProductToCart()">ADD TO SHOPPING BAG</button>
            <button class="pdp-btn-buy" onclick="buyPdpProductNow()">BUY IT NOW &rarr;</button>
            <a id="pdpWhatsAppBtn" class="pdp-btn-whatsapp" href="#" target="_blank">
              <span style="font-size:20px;">&#128172;</span> ORDER VIA WHATSAPP ATELIER CONCIERGE
            </a>
            <div class="whatsapp-benefit-box">
              <span class="wa-icon">&#128172;</span>
              <div>
                <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
                Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
              </div>
            </div>
          </div>

          <!-- Pincode Checker -->
          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:8px; padding:14px 16px;">
            <div style="font-size:11px; text-transform:uppercase; letter-spacing:0.08em; font-weight:700; color:var(--text-muted); margin-bottom:8px;">Check Express Dispatch to Your Pincode</div>
            <div style="display:flex; gap:8px;">
              <input type="text" id="pdpPincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" maxlength="6" style="flex:1; padding:8px 12px; border:1px solid var(--border-color); border-radius:4px; font-size:13px; outline:none; background:#FFF;">
              <button onclick="checkPdpPincode()" style="padding:8px 16px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">CHECK</button>
            </div>
            <div id="pdpPincodeResult" style="font-size:12px; margin-top:8px; font-weight:600; display:none;"></div>
          </div>

          <!-- Accordions -->
          <div class="pdp-accordions">
            <div class="pdp-accordion-item open">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>The Silhouette & Drape</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content" id="pdpDescContent"></div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Fabric & Handloom Heritage</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content" id="pdpFabricContent"></div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Garment Care & Maintenance</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content">
                Professional dry clean recommended for silk and Chanderi pret to preserve natural luster and delicate zari embroidery. Cotton silhouettes can be gently hand-washed in cold water using mild detergent. Always steam iron on reverse side. Store in the breathable archival muslin dust bag provided with your order.
              </div>
            </div>

            <div class="pdp-accordion-item">
              <div class="pdp-accordion-header" onclick="togglePdpAccordion(this)">
                <span>Complimentary Atelier Alterations & Returns</span>
                <span class="pdp-accordion-icon">&plus;</span>
              </div>
              <div class="pdp-accordion-content">
                Because each Drop 01 silhouette is strictly 1 piece per size, we provide complimentary bespoke sleeve and hem tailoring at our Sector 17-C Chandigarh Design Studio or through our WhatsApp styling team. Standard 7-day hassle-free exchange policy applies if unworn and tags remain intact.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Curated Recommendations (Complete The Look) -->
      <div class="pdp-related-section">
        <h3 class="pdp-related-title">Complete The Look &bull; Curated Drop 01 Pieces</h3>
        <p class="pdp-related-sub">Other strictly limited silhouettes from our Autumn/Winter 2026 debut</p>
        <div class="pdp-related-grid" id="pdpRelatedGrid">
          <!-- Dynamically populated with 4 other silhouettes -->
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div class="footer-col">
        <img src="{logo_b64}" alt="Meenu Label" style="height: 48px; width: auto; filter: invert(1); display: block; margin-bottom: 16px;">
        <p>Contemporary Indian ethnic wear and modern fusion silhouettes. Handcrafted elegance for everyday grace.</p>
        <p style="font-size: 11px; color: #82786D;">
          <strong>Meenu Label &bull; Independent Luxury Label</strong><br>
          Chandigarh, India &bull; Official Domain: <strong>meenulabel.com</strong>
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
          <li><a href="javascript:void(0)" onclick="openSizeGuide()">Size & Fit Guide (M-XL)</a></li>
          <li><a href="javascript:void(0)">7-Day Exchange Policy</a></li>
          <li><a href="javascript:void(0)">Tricity 24-Hr Dispatch</a></li>
          <li><a href="mailto:meenulabel24@gmail.com">meenulabel24@gmail.com</a></li>
          <li><a href="https://wa.me/919988898845" target="_blank">WhatsApp Concierge</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Newsletter</h4>
        <p>Receive exclusive early access to Drop 02 and private founder trunk shows.</p>
        <div style="display: flex; gap: 8px; margin-top: 12px;">
          <input type="email" placeholder="Enter your email..." style="padding: 10px 14px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.08); color: #FFF; font-size: 13px; flex: 1;">
          <button class="modal-btn-primary" style="padding: 10px 18px; width:auto; margin:0;" onclick="showToast('Thank you for subscribing!')">JOIN</button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Meenu Label. All rights reserved.</div>
      <div>🔒 256-Bit SSL Encrypted &bull; Shopify Online Store 2.0 Ready &bull; meenulabel.com</div>
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
        <span class="card-badge badge-scarcity" id="modalBadge">ONLY 1 LEFT IN SIZE M</span>
        <h2 class="modal-title" id="modalTitle">Product Title</h2>
        <div class="modal-code" id="modalCode">Product Code</div>
        <div class="modal-price-wrap">
          <span class="modal-price-cur" id="modalPrice">₹1,499</span>
          <span class="modal-price-mrp" id="modalMrp">₹2,499</span>
          <span class="modal-price-off" id="modalOff">40% OFF</span>
        </div>
        <p class="modal-desc" id="modalDesc"></p>
        
        <div class="modal-meta-row"><strong>Fabric:</strong> <span id="modalFabric"></span></div>
        <div class="modal-meta-row"><strong>Origin:</strong> Handcrafted in Surat &bull; Hand-Finished in Chandigarh</div>
        <div class="modal-meta-row"><strong>Dispatch:</strong> ⚡ 24-Hr Priority Tricity Delivery</div>

        <div class="modal-size-select">
          <div class="modal-size-label">
            <span>SELECT SIZE</span>
            <a href="javascript:void(0)" onclick="openSizeGuide()" style="color: var(--accent-gold); text-decoration: none;">📏 Size Chart</a>
          </div>
          <div class="modal-sizes-group">
            <button class="modal-size-btn selected" onclick="selectModalSize('M', this)">M (38")</button>
            <button class="modal-size-btn" onclick="selectModalSize('L', this)">L (40")</button>
            <button class="modal-size-btn" onclick="selectModalSize('XL', this)">XL (42")</button>
          </div>
        </div>

        <!-- Pincode Checker -->
        <div style="margin-bottom: 20px; background: var(--bg-surface); padding: 12px 16px; border-radius: 8px;">
          <div style="font-size: 11px; font-weight: 700; margin-bottom: 6px;">DELIVERY CHECKER</div>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="pincodeInput" placeholder="Enter 6-digit Pincode (e.g. 160017)" style="padding: 7px 12px; border-radius: 4px; border: 1px solid var(--border-color); font-size: 12px; flex: 1;">
            <button onclick="checkPincode()" style="padding: 7px 14px; background: var(--text-main); color: #FFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer;">CHECK</button>
          </div>
          <div id="pincodeResult" style="font-size: 11px; margin-top: 6px; font-weight: 600;"></div>
        </div>

        <button class="modal-btn-primary" onclick="addCurrentProductToCart()">ADD TO BAG 🛍️</button>
        <a id="modalWhatsAppBtn" class="modal-btn-whatsapp" href="#" target="_blank">
          <span>💬</span> DIRECT ORDER VIA WHATSAPP CONCIERGE
        </a>
        <div class="whatsapp-benefit-box">
          <span class="wa-icon">&#128172;</span>
          <div>
            <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
            Chat directly with our Chandigarh stylist to confirm sizing, request custom alterations, or view unedited fabric videos.
          </div>
        </div>
      </div>
    </div>
  </div>

    <!-- Navigation Drawer (Global at Root Level) -->
  <div class="nav-drawer-backdrop" id="navDrawerBackdrop" onclick="closeNavDrawer()">
    <div class="nav-drawer" id="navDrawer" onclick="event.stopPropagation()">
      <div class="nav-drawer-header">
        <img src="{logo_b64}" alt="Meenu Label" style="height: 38px; width: auto;">
        <button style="background:none; border:none; font-size:24px; cursor:pointer; color:var(--text-main); padding:4px 8px; line-height:1;" onclick="closeNavDrawer()">&times;</button>
      </div>
      <div class="nav-drawer-body">
        <ul class="nav-drawer-links">
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('all')">All Silhouettes</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('coord')">Co-ord Sets</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('festive')">Festive Suits</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('dress')">Midi Dresses</a></li>
          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('top')">Tops &amp; Blouses</a></li>
          <li style="border-top:1px solid var(--border-color); margin-top:18px; padding-top:18px;">
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal();" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openSizeGuide();">&#128207; Size &amp; Fit Guide (M-XL)</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); closeProductPage(); var f = document.getElementById('founder'); if (f) f.scrollIntoView();">&#128081; Behind The Label (Transparency)</a>
          </li>
          <li>
            <a href="https://wa.me/919988898845" target="_blank" style="color:#25D366;">&#128172; WhatsApp Concierge (+91 99888 98845)</a>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Shopping Cart Drawer (Global at Root Level) -->
  <div class="cart-backdrop" id="cartBackdrop" onclick="toggleCart()"></div>
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-header">
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">Shopping Bag (<span id="cartCount">0</span>)</h3>
      <button style="background:none; border:none; font-size:22px; cursor:pointer; color:var(--text-main);" onclick="toggleCart()">&times;</button>
    </div>
    <div style="background: #FAF8F5; padding: 10px 24px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--accent-gold); font-weight: 700; border-bottom: 1px solid var(--border-color);">
      &#10024; Unlocked: FREE Express Shipping Across India
    </div>
    <div class="cart-body" id="cartItemsList">
      <!-- Items dynamically populated -->
    </div>
    <div class="cart-footer">
      <div style="display: flex; gap: 8px; margin-bottom: 14px;">
        <input type="text" id="couponCode" placeholder="Promo code (e.g. DEBUT10)" style="flex: 1; padding: 10px 12px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 12px; text-transform: uppercase;">
        <button onclick="applyCoupon()" style="padding: 10px 16px; background: var(--text-main); color: #FFF; border: none; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; text-transform: uppercase;">Apply</button>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: var(--text-muted);">
        <span>Subtotal</span>
        <span id="cartSubtotal">&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: #25D366;">
        <span>Promo Discount</span>
        <span id="cartDiscount">-&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px; color: var(--text-muted);">
        <span>Estimated GST (5% included)</span>
        <span id="cartGst">&#8377;0</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 14px; color: #25D366; font-weight: 700;">
        <span>Express Courier Dispatch</span>
        <span>FREE</span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 17px; font-weight: 800; border-top: 1px solid var(--border-color); padding-top: 12px; margin-bottom: 16px;">
        <span>Total Payable</span>
        <span id="cartTotal">&#8377;0</span>
      </div>
      <button class="modal-btn-primary" onclick="proceedToCheckout()" style="width: 100%; padding: 14px; font-size: 12px; letter-spacing: 0.1em; font-weight: 700;">PROCEED TO CHECKOUT &#8250;</button>
    </div>
  </div>

  <!-- Wishlist Drawer -->
  <div class="cart-backdrop" id="wishlistBackdrop" onclick="toggleWishlistDrawer()"></div>
  <div class="cart-drawer" id="wishlistDrawer">
    <div class="cart-header">
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 22px;">Saved Wishlist (<span id="wishlistDrawerCount">0</span>)</h3>
      <button style="background:none; border:none; font-size:22px; cursor:pointer; color:var(--text-main);" onclick="toggleWishlistDrawer()">&times;</button>
    </div>
    <div class="cart-body" id="wishlistItemsList">
      <!-- Items dynamically injected -->
    </div>
    <div class="cart-footer" id="wishlistFooter" style="display:none;">
      <button class="modal-btn-primary" onclick="addAllWishlistToCart()" style="margin-bottom:8px;">ADD ALL TO BAG</button>
      <div style="font-size:11px; color:var(--text-muted); text-align:center;">
        Pieces reserved in your bag for 15 minutes
      </div>
    </div>
  </div>

    <!-- Snitch-Style Split-Screen Login & VIP Atelier Modal -->
  <div class="snitch-login-backdrop" id="accountModalBackdrop" onclick="closeAccountModal(event)">
    <div class="snitch-login-dialog" onclick="event.stopPropagation()">
      <!-- Top Actions: Back Chevron on Left, Close X on Right -->
      <button class="snitch-dialog-back" onclick="closeAccountModalDirect()" title="Back to Store" aria-label="Back">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="snitch-dialog-close" onclick="closeAccountModalDirect()" title="Close Modal" aria-label="Close">&times;</button>

      <!-- Left Column: High-Fashion Campaign Photography -->
      <div class="snitch-login-campaign">
        <img src="{login_campaign_b64}" alt="Meenu Label Campaign" class="snitch-campaign-photo">
        <div class="snitch-campaign-vignette"></div>
        <div class="snitch-campaign-text">
          <div class="snitch-campaign-pill">Signature Silhouettes</div>
          <h2 class="snitch-campaign-headline">
            WEAR WHAT'S <span class="snitch-headline-accent">TIMELESS</span>
          </h2>
          <p class="snitch-campaign-atelier">Chandigarh Atelier &bull; Handcrafted Pure Silks</p>
        </div>
      </div>

      <!-- Right Column: Matte Charcoal Card matching Snitch -->
      <div class="snitch-login-content">
        <div class="snitch-login-card">
          <!-- Step 1: Mobile Number Input -->
          <div id="loginStepPhone">
            <div class="snitch-brand-block">
              <h2 class="snitch-brand-title">MEENU LABEL</h2>
              <div class="snitch-brand-tag">CHANDIGARH &bull; LUXURY ETHNIC</div>
            </div>

            <label class="snitch-input-heading" for="snitchMobileInput">ENTER MOBILE NUMBER</label>
            <div class="snitch-input-row" id="snitchPhoneRow">
              <div class="snitch-cc-badge">+91</div>
              <input 
                type="tel" 
                id="snitchMobileInput" 
                class="snitch-mobile-field" 
                placeholder="99999 99999" 
                maxlength="10" 
                autocomplete="tel"
                oninput="onSnitchPhoneInput(this)" 
                onkeydown="if(event.key==='Enter') requestSnitchOtp()"
              >
            </div>
            <div id="snitchPhoneError" class="snitch-validation-error">Please enter a valid 10-digit mobile number</div>

            <button class="snitch-submit-btn" id="snitchSendOtpBtn" onclick="requestSnitchOtp()">
              <span>SEND OTP</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>

            <p class="snitch-legal-note">
              By continuing, you agree to MEENU LABEL's 
              <a href="javascript:void(0)" onclick="alert('MEENU LABEL TERMS: All silhouettes handcrafted in Chandigarh. Express dispatch within 24-48 hours with door-to-door tracking.')">Terms &amp; Conditions</a> 
              and 
              <a href="javascript:void(0)" onclick="alert('MEENU LABEL PRIVACY: Your phone number is strictly encrypted and used solely for VIP order tracking & delivery notifications.')">Privacy Policy</a>
            </p>
          </div>

          <!-- Step 2: OTP Verification -->
          <div id="loginStepOtp" style="display:none;">
            <div class="snitch-brand-block" style="margin-bottom: 20px;">
              <h2 class="snitch-brand-title" style="font-size: 20px;">VERIFY OTP</h2>
              <div class="snitch-otp-sent-info">
                Code sent to <strong id="snitchOtpPhoneDisplay" style="color:#ffffff;">+91 99999 99999</strong>
                <button type="button" class="snitch-edit-phone-btn" onclick="snitchEditPhone()">Edit</button>
              </div>
            </div>

            <div class="snitch-otp-grid">
              <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp1" oninput="snitchOtpNext(this, 'sOtp2')" onkeydown="snitchOtpBack(event, this, null)">
              <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp2" oninput="snitchOtpNext(this, 'sOtp3')" onkeydown="snitchOtpBack(event, this, 'sOtp1')">
              <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp3" oninput="snitchOtpNext(this, 'sOtp4')" onkeydown="snitchOtpBack(event, this, 'sOtp2')">
              <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp4" oninput="snitchOtpNext(this, null)" onkeydown="snitchOtpBack(event, this, 'sOtp3')">
            </div>

            <div class="snitch-resend-bar">
              <span id="snitchTimerTxt">Resend OTP in <strong id="snitchCountdown" style="color:#bbbbbb;">0:28</strong></span>
              <button type="button" id="snitchResendBtn" class="snitch-resend-action" style="display:none;" onclick="snitchResendOtp()">Resend OTP via SMS / WhatsApp</button>
            </div>

            <button class="snitch-submit-btn" onclick="verifySnitchOtp()">
              <span>VERIFY &amp; PROCEED</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>

            <div class="snitch-demo-badge">&bull; Demo Mode: Type any 4 digits (e.g. 1 2 3 4) to login</div>
          </div>

          <!-- Step 3: VIP Atelier Privé Dashboard -->
          <div id="loginStepVip" style="display:none; text-align:center;">
            <div class="snitch-vip-avatar">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
            <div class="snitch-vip-status-tag">&#10024; ATELIER PRIV&Eacute; VIP MEMBER</div>
            <h3 class="snitch-vip-user" id="snitchVipUserDisplay">+91 99888 98845</h3>
            <div class="snitch-vip-perks">
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#128666;</div>
                <div class="snitch-perk-text">
                  <strong>Free 24-Hr Tricity Delivery</strong>
                  <span>Direct courier from Sector 17 Atelier</span>
                </div>
              </div>
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#128087;</div>
                <div class="snitch-perk-text">
                  <strong>Bespoke Atelier Fittings</strong>
                  <span>Private trial room appointments in Chandigarh</span>
                </div>
              </div>
            </div>

            <div class="snitch-vip-actions">
              <button class="snitch-submit-btn" style="margin-bottom: 12px;" onclick="closeAccountModalDirect()">
                <span>CONTINUE SHOPPING</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </button>
              <a href="https://wa.me/919988898845?text=Hi%20Meenu%20Label%2C%20I%20am%20a%20VIP%20member%20inquiring%20about%20my%20orders." target="_blank" class="snitch-vip-concierge-btn">
                &#128172; Open Master Stylist WhatsApp Concierge
              </a>
              <button type="button" class="snitch-signout-btn" onclick="signOutSnitchUser()">Sign Out / Change Account</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Size Guide Modal -->
  <div class="modal-backdrop" id="sizeGuideBackdrop" onclick="closeSizeGuide(event)">
    <div class="product-modal" style="width: 650px; grid-template-columns: 1fr; padding: 36px;">
      <button class="modal-close" onclick="closeSizeGuideDirect()">✕</button>
      <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; margin-bottom: 6px;">Meenu Label Size Chart</h3>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 20px;">
        All measurements in inches. Designed with relaxed comfort ease for modern Indian women.
      </p>
      <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; margin-bottom: 20px;">
        <thead>
          <tr style="background: var(--bg-surface); border-bottom: 2px solid var(--border-color);">
            <th style="padding: 10px;">Size</th>
            <th style="padding: 10px;">Bust (in)</th>
            <th style="padding: 10px;">Waist (in)</th>
            <th style="padding: 10px;">Hip (in)</th>
            <th style="padding: 10px;">Ideal Height</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 10px; font-weight: 700;">M (38)</td>
            <td style="padding: 10px;">38"</td>
            <td style="padding: 10px;">32" - 34"</td>
            <td style="padding: 10px;">40" - 42"</td>
            <td style="padding: 10px;">5'2" - 5'6"</td>
          </tr>
          <tr style="border-bottom: 1px solid var(--border-color);">
            <td style="padding: 10px; font-weight: 700;">L (40)</td>
            <td style="padding: 10px;">40"</td>
            <td style="padding: 10px;">34" - 36"</td>
            <td style="padding: 10px;">42" - 44"</td>
            <td style="padding: 10px;">5'3" - 5'7"</td>
          </tr>
          <tr>
            <td style="padding: 10px; font-weight: 700;">XL (42)</td>
            <td style="padding: 10px;">42"</td>
            <td style="padding: 10px;">36" - 38"</td>
            <td style="padding: 10px;">44" - 46"</td>
            <td style="padding: 10px;">5'4" - 5'8"</td>
          </tr>
        </tbody>
      </table>
      <div style="font-size: 12px; color: var(--text-muted); background: var(--bg-surface); padding: 12px 16px; border-radius: 6px;">
        💡 <strong>Fit Advice:</strong> If you are in between sizes, we recommend sizing up for a relaxed, breathable drape. Every order includes a complimentary 7-day size exchange guarantee.
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast-note" id="toastNote"></div>

  <script>
    var productsData = {js_products_data};
    var cart = [];
    var activeModalProduct = null;
    var selectedSize = 'M';
    var discountPercent = 0.0;

    /* Snitch Slider Logic: Auto-slide and very slowly */
    var currentSlide = 0;
    var totalSlides = 4;
    var slideInterval = 6000; // 6 seconds per slide
    var slideTimer = null;
    var track = document.getElementById('sliderTrack');
    var dotsContainer = document.getElementById('sliderDots');

    function updateSlider() {{
      track.style.transform = 'translateX(-' + (currentSlide * 25) + '%)';
      var dots = dotsContainer.querySelectorAll('.slider-dot');
      dots.forEach(function(dot, idx) {{
        if (idx === currentSlide) {{
          dot.classList.add('active');
        }} else {{
          dot.classList.remove('active');
        }}
      }});
    }}

    function nextSlide() {{
      currentSlide = (currentSlide + 1) % totalSlides;
      updateSlider();
    }}

    function prevSlide() {{
      currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
      updateSlider();
    }}

    function goToSlide(idx) {{
      currentSlide = idx;
      updateSlider();
      resetAutoSlide();
    }}

    function startAutoSlide() {{
      stopAutoSlide();
      slideTimer = setInterval(function() {{
        nextSlide();
      }}, slideInterval);
    }}

    function stopAutoSlide() {{
      if (slideTimer) {{
        clearInterval(slideTimer);
        slideTimer = null;
      }}
    }}

    function resetAutoSlide() {{
      stopAutoSlide();
      startAutoSlide();
    }}

    // Pause on mouse hover for user convenience
    var heroEl = document.getElementById('heroSlider');
    heroEl.addEventListener('mouseenter', stopAutoSlide);
    heroEl.addEventListener('mouseleave', startAutoSlide);

    // Touch swipe support for smooth mobile interaction
    var touchStartX = 0;
    var touchEndX = 0;
    heroEl.addEventListener('touchstart', function(e) {{
      touchStartX = e.changedTouches[0].screenX;
      stopAutoSlide();
    }}, {{passive: true}});
    heroEl.addEventListener('touchend', function(e) {{
      touchEndX = e.changedTouches[0].screenX;
      if (touchEndX < touchStartX - 50) {{
        nextSlide();
      }} else if (touchEndX > touchStartX + 50) {{
        prevSlide();
      }}
      startAutoSlide();
    }}, {{passive: true}});

    // Initialize Auto-slide on load
    startAutoSlide();

    /* Navigation Drawer Functions */
    function openNavDrawer() {{
      document.getElementById('navDrawer').classList.add('open');
      document.getElementById('navDrawerBackdrop').classList.add('open');
    }}
    function closeNavDrawer() {{
      document.getElementById('navDrawer').classList.remove('open');
      document.getElementById('navDrawerBackdrop').classList.remove('open');
    }}

    /* Category Filtering */
        function filterCategory(cat, btn) {{
      closeProductPage();
      var cards = document.querySelectorAll('.product-card');
      var matchedCount = 0;
      cards.forEach(function(card) {{
        if (cat === 'all' || card.getAttribute('data-category') === cat) {{
          card.style.display = 'flex';
          matchedCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      // Update active state on matching tabs
      document.querySelectorAll('.filter-tab').forEach(function(t) {{
        t.classList.remove('active');
        if (t.getAttribute('data-cat') === cat) {{
          t.classList.add('active');
        }}
      }});
      if (btn) btn.classList.add('active');

      // Update category pill label
      var countEl = document.getElementById('activeCategoryCount');
      if (countEl) {{
        var catTitles = {{
          'all': 'HANDCRAFTED EDITIONS',
          'coord': 'CO-ORD SETS',
          'festive': 'FESTIVE SUITS',
          'dress': 'MIDI DRESSES',
          'top': 'TOPS & BLOUSES'
        }};
        countEl.textContent = catTitles[cat] || 'HANDCRAFTED EDITIONS';
      }}

      // Only scroll down to catalog if the user is currently ABOVE the catalog (e.g. up in the hero banner)
      var catalogEl = document.getElementById('catalog');
      if (catalogEl && typeof catalogEl.getBoundingClientRect === 'function') {{
        var rect = catalogEl.getBoundingClientRect();
        if (rect.top > 160) {{
          catalogEl.scrollIntoView({{ behavior: 'smooth' }});
        }}
        // If already scrolling through the catalog, do NOT scroll up the page! The sticky bar filters instantly in place!
      }}
    }}

    /* Search Products */
    
    /* =========================================================================
       DEDICATED FULL PRODUCT DETAIL PAGE (PDP) LOGIC
       ========================================================================= */
    var activePdpProductId = null;
    var pdpSelectedSize = 'M';

    function openQuickView(prodId) {{
      openProductModal(prodId);
    }}

    function openProductPage(prodId) {{
      var p = productsData.find(function(item) {{ return item.id === prodId; }});
      if (!p) return;

      activePdpProductId = prodId;
      pdpSelectedSize = 'M';

      // Close Quick View modal if open
      closeModal();

      // Update browser hash
      try {{
        window.location.hash = '#product-' + prodId;
      }} catch(e) {{}}

      // Switch views: Hide Home view, Show PDP view
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (homeView) homeView.style.display = 'none';
      if (pdpView) pdpView.style.display = 'block';

      // Scroll smoothly to top
      window.scrollTo(0, 0);

      // Breadcrumbs
      var breadCat = document.getElementById('pdpBreadcrumbCat');
      if (breadCat) breadCat.textContent = (p.cat_label || 'Collection').toUpperCase();
      var breadTitle = document.getElementById('pdpBreadcrumbTitle');
      if (breadTitle) breadTitle.textContent = (p.name + ' (' + p.code + ')').toUpperCase();

      // Main Visual
      var mainImg = document.getElementById('pdpMainImg');
      if (mainImg) {{
        mainImg.src = p.b64;
        mainImg.alt = p.name;
      }}
      var badgePill = document.getElementById('pdpBadgePill');
      if (badgePill) badgePill.textContent = (p.badge || 'Drop 01 Exclusive').toUpperCase();

      // Wishlist toggle state
      var wishBtn = document.getElementById('pdpWishlistBtn');
      if (wishBtn) {{
        if (wishlist.indexOf(p.id) !== -1) {{
          wishBtn.classList.add('active');
        }} else {{
          wishBtn.classList.remove('active');
        }}
      }}

      // Titles & Code
      var codeTag = document.getElementById('pdpCodeTag');
      if (codeTag) codeTag.textContent = 'STYLE #' + p.code;
      var titleEl = document.getElementById('pdpTitle');
      if (titleEl) titleEl.textContent = p.name;

      // Price block
      var priceMain = document.getElementById('pdpPriceMain');
      if (priceMain) priceMain.innerHTML = '&#8377;' + p.price.toLocaleString('en-IN');
      var priceMrp = document.getElementById('pdpPriceMrp');
      if (priceMrp) priceMrp.innerHTML = '&#8377;' + p.mrp.toLocaleString('en-IN');
      var discEl = document.getElementById('pdpDiscount');
      if (discEl) {{
        var discount = Math.round(((p.mrp - p.price) / p.mrp) * 100);
        discEl.textContent = discount + '% OFF';
      }}

      // Meta highlights
      var metaFabric = document.getElementById('pdpMetaFabric');
      if (metaFabric) metaFabric.textContent = p.fabric || 'Pure Artisanal Fabric';
      var metaColor = document.getElementById('pdpMetaColor');
      if (metaColor) metaColor.textContent = p.color || 'Artisanal Palette';

      // Accordion contents
      var descContent = document.getElementById('pdpDescContent');
      if (descContent) descContent.textContent = p.desc;
      var fabContent = document.getElementById('pdpFabricContent');
      if (fabContent) fabContent.textContent = (p.fabric || 'Luxury Weave') + '. Meticulously hand-loomed with precision thread density and finished by master artisans in Jaipur and Surat. Exceptionally soft on skin, breathable, and designed for a flattering luxury drape.';

      // Reset Pincode
      var pinInp = document.getElementById('pdpPincodeInput');
      if (pinInp) pinInp.value = '';
      var pinRes = document.getElementById('pdpPincodeResult');
      if (pinRes) pinRes.style.display = 'none';

      // Size buttons
      selectPdpSize('M', document.getElementById('pdpSizeBtn_M'));

      // WhatsApp concierge link
      updatePdpWhatsAppLink(p, 'M');

      // Populate Curated Recommendations
      populatePdpRelated(p.id);
    }}

    function closeProductPage() {{
      var homeView = document.getElementById('storefrontHomeView');
      var pdpView = document.getElementById('productDetailView');
      if (homeView) homeView.style.display = 'block';
      if (pdpView) pdpView.style.display = 'none';

      try {{
        window.location.hash = '#catalog';
      }} catch(e) {{}}

      if (activePdpProductId) {{
        var card = document.querySelector('.product-card[data-id="' + activePdpProductId + '"]');
        if (card) {{
          card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        }}
      }}
    }}

    function selectPdpSize(size, btn) {{
      pdpSelectedSize = size;
      document.querySelectorAll('.pdp-size-btn').forEach(function(b) {{
        b.classList.remove('selected');
      }});
      if (btn) {{
        btn.classList.add('selected');
      }} else {{
        var autoBtn = document.getElementById('pdpSizeBtn_' + size);
        if (autoBtn) autoBtn.classList.add('selected');
      }}
      var p = productsData.find(function(item) {{ return item.id === activePdpProductId; }});
      if (p) updatePdpWhatsAppLink(p, size);
    }}

    function updatePdpWhatsAppLink(product, size) {{
      var text = encodeURIComponent('Hi Meenu Label Atelier! I would like to order "' + product.name + '" (Style #' + product.code + ') in Size ' + size + ' from Drop 01. Please confirm piece reservation and express Tricity delivery details.');
      var btn = document.getElementById('pdpWhatsAppBtn');
      if (btn) btn.href = 'https://wa.me/919988898845?text=' + text;
    }}

    function addPdpProductToCart() {{
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }}

    function buyPdpProductNow() {{
      if (!activePdpProductId) return;
      quickAddCart(activePdpProductId, pdpSelectedSize);
      toggleCart();
    }}

    function togglePdpWishlist() {{
      if (!activePdpProductId) return;
      toggleWishlistProduct(activePdpProductId);
      var btn = document.getElementById('pdpWishlistBtn');
      if (btn) {{
        if (wishlist.indexOf(activePdpProductId) !== -1) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }}
    }}

    function checkPdpPincode() {{
      var pinInp = document.getElementById('pdpPincodeInput');
      var pinRes = document.getElementById('pdpPincodeResult');
      if (!pinInp || !pinRes) return;
      var pin = pinInp.value.trim();
      pinRes.style.display = 'block';

      if (pin.length !== 6 || isNaN(pin)) {{
        pinRes.style.color = '#E53935';
        pinRes.textContent = 'Please enter a valid 6-digit Indian PIN code.';
        return;
      }}

      // Tricity Pincodes (Chandigarh 160xxx, Mohali 140xxx / 160xxx, Panchkula 134xxx)
      if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {{
        pinRes.style.color = '#128C7E';
        pinRes.textContent = '✓ FREE 24-HR EXPRESS TRICITY DELIVERY: Dispatch directly from Sector 17 Atelier. Estimated delivery tomorrow before 6:00 PM via Private Courier.';
      }} else {{
        pinRes.style.color = '#128C7E';
        pinRes.textContent = '✓ EXPRESS AIR COURIER: Dispatch within 24 hours. Estimated delivery in 3 to 4 business days via BlueDart / Delhivery Air.';
      }}
    }}

    function togglePdpAccordion(headerEl) {{
      var item = headerEl.parentElement;
      item.classList.toggle('open');
    }}

    function populatePdpRelated(currentId) {{
      var container = document.getElementById('pdpRelatedGrid');
      if (!container) return;
      container.innerHTML = '';

      var related = productsData.filter(function(item) {{ return item.id !== currentId; }}).slice(0, 4);
      var html = '';
      related.forEach(function(r) {{
        var discount = Math.round(((r.mrp - r.price) / r.mrp) * 100);
        html += '<div class="product-card" data-pid="' + r.id + '" onclick="openProductPage(this.dataset.pid)">';
        html += '<div class="card-thumb">';
        html += '<span class="card-badge ' + r.badge_class + '">' + r.badge + '</span>';
        html += '<button class="card-wishlist-btn" data-pid="' + r.id + '" onclick="event.stopPropagation(); toggleWishlistProduct(this.dataset.pid)" title="Save to Wishlist">';
        html += '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>';
        html += '</button>';
        html += '<img src="' + r.b64 + '" alt="' + r.name + '" loading="lazy">';
        html += '<div class="card-quick-actions">';
        html += '<button class="btn-quick-view" data-pid="' + r.id + '" onclick="event.stopPropagation(); openQuickView(this.dataset.pid)">QUICK VIEW</button>';
        html += '</div>';
        html += '</div>';
        html += '<div class="card-body">';
        html += '<span class="card-cat">' + r.cat_label + '</span>';
        html += '<h3 class="card-title">' + r.name + '</h3>';
        html += '<div class="card-fabric">' + r.fabric + '</div>';
        html += '<div class="card-price-row">';
        html += '<span class="price-main">&#8377;' + r.price.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-mrp">&#8377;' + r.mrp.toLocaleString('en-IN') + '</span>';
        html += '<span class="price-discount">' + discount + '% OFF</span>';
        html += '</div>';
        html += '</div>';
        html += '</div>';
      }});
      container.innerHTML = html;
    }}


    /* Wishlist System */
    var wishlist = [];

    function toggleWishlistProduct(prodId) {{
      var idx = wishlist.indexOf(prodId);
      var btn = document.getElementById('wishBtn_' + prodId);
      if (idx === -1) {{
        wishlist.push(prodId);
        if (btn) btn.classList.add('active');
        showToast('Added to your Wishlist!');
      }} else {{
        wishlist.splice(idx, 1);
        if (btn) btn.classList.remove('active');
        showToast('Removed from your Wishlist.');
      }}
      updateWishlistUI();
    }}

    
    function moveWishlistToCart(pid) {{
      quickAddCart(pid, 'M');
      toggleWishlistProduct(pid);
    }}

    function updateWishlistUI() {{
      var countEl = document.getElementById('headerWishlistCount');
      if (countEl) countEl.textContent = wishlist.length;
      var drawerCountEl = document.getElementById('wishlistDrawerCount');
      if (drawerCountEl) drawerCountEl.textContent = wishlist.length;
      var container = document.getElementById('wishlistItemsList');
      var footer = document.getElementById('wishlistFooter');
      if (!container) return;

      if (wishlist.length === 0) {{
        container.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 36px; margin-bottom: 12px; color: #CCC;">&hearts;</div><p style="font-size: 15px; font-weight: 600; color: var(--text-main); margin-bottom: 6px;">Your Wishlist is Empty</p><p style="font-size: 12px;">Explore Drop 01 and tap the heart icon on any silhouette to save your favorites.</p></div>';
        if (footer) footer.style.display = 'none';
        return;
      }}

      if (footer) footer.style.display = 'block';
      var html = '';
      wishlist.forEach(function(pid) {{
        var p = productsData.find(function(item) {{ return item.id === pid; }});
        if (p) {{
          html += '<div style="display:flex; gap:14px; padding:16px 0; border-bottom:1px solid var(--border-color); align-items:center;">';
          html += '<img src="' + p.b64 + '" style="width:68px; height:85px; object-fit:cover; border-radius:6px;">';
          html += '<div style="flex:1;">';
          html += '<div style="font-size:11px; color:var(--accent-gold); font-weight:700; letter-spacing:0.5px; text-transform:uppercase;">' + p.code + '</div>';
          html += '<div style="font-size:13px; font-weight:700; color:var(--text-main); margin:2px 0;">' + p.name + '</div>';
          html += '<div style="font-size:13px; font-weight:700; color:var(--text-main);">&#8377;' + p.price.toLocaleString('en-IN') + '</div>';
          html += '</div>';
          html += '<div style="display:flex; flex-direction:column; gap:6px; align-items:flex-end;">';
          html += '<button data-pid="' + p.id + '" onclick="moveWishlistToCart(this.dataset.pid)" style="padding:6px 12px; background:var(--text-main); color:#FFF; border:none; border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">MOVE TO BAG</button>';
          html += '<button data-pid="' + p.id + '" onclick="toggleWishlistProduct(this.dataset.pid)" style="background:none; border:none; font-size:11px; color:var(--text-muted); cursor:pointer; text-decoration:underline;">Remove</button>';
          html += '</div>';
          html += '</div>';
        }}
      }});
      container.innerHTML = html;
    }}

    function toggleWishlistDrawer() {{
      var drawer = document.getElementById('wishlistDrawer');
      var backdrop = document.getElementById('wishlistBackdrop');
      drawer.classList.toggle('open');
      backdrop.classList.toggle('open');
      updateWishlistUI();
    }}

    function addAllWishlistToCart() {{
      if (wishlist.length === 0) return;
      wishlist.forEach(function(pid) {{
        quickAddCart(pid, 'M');
      }});
      wishlist = [];
      document.querySelectorAll('.card-wishlist-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      updateWishlistUI();
      toggleWishlistDrawer();
      toggleCart();
      showToast('All favorites moved to your bag!');
    }}

    /* Search Bar Overlay Logic */
    function toggleSearchBar() {{
      var bar = document.getElementById('searchOverlayBar');
      bar.classList.toggle('open');
      if (bar.classList.contains('open')) {{
        setTimeout(function() {{
          var inp = document.getElementById('searchInput');
          if (inp) inp.focus();
        }}, 120);
      }}
    }}

    function clearSearch() {{
      var inp = document.getElementById('searchInput');
      if (inp) inp.value = '';
      searchProducts();
      if (inp) inp.focus();
    }}

    function quickSearch(tag) {{
      var inp = document.getElementById('searchInput');
      if (inp) inp.value = tag;
      searchProducts();
      var coll = document.getElementById('collectionSection');
      if (coll) coll.scrollIntoView({{ behavior: 'smooth' }});
    }}

    /* Snitch Login & VIP Privé Authentication Logic */
    var snitchCurrentUser = null;
    var snitchOtpInterval = null;

    function isSnitchLoggedIn() {{
      if (snitchCurrentUser) return true;
      try {{
        var stored = localStorage.getItem('meenu_vip_user');
        if (stored) {{
          snitchCurrentUser = JSON.parse(stored);
          return true;
        }}
      }} catch(e) {{}}
      return false;
    }}

    function updateAccountHeaderIcon() {{
      var badge = document.getElementById('accountActiveBadge');
      if (badge) {{
        badge.style.display = isSnitchLoggedIn() ? 'block' : 'none';
      }}
    }}

    function openAccountModal() {{
      var backdrop = document.getElementById('accountModalBackdrop');
      if (!backdrop) return;
      backdrop.classList.add('open');
      
      if (isSnitchLoggedIn()) {{
        var p = document.getElementById('loginStepPhone');
        var o = document.getElementById('loginStepOtp');
        var v = document.getElementById('loginStepVip');
        if (p) p.style.display = 'none';
        if (o) o.style.display = 'none';
        if (v) v.style.display = 'block';
        var u = document.getElementById('snitchVipUserDisplay');
        if (u) u.textContent = snitchCurrentUser.phone || '+91 99888 98845';
      }} else {{
        var p = document.getElementById('loginStepPhone');
        var o = document.getElementById('loginStepOtp');
        var v = document.getElementById('loginStepVip');
        if (p) p.style.display = 'block';
        if (o) o.style.display = 'none';
        if (v) v.style.display = 'none';
        setTimeout(function() {{
          var inp = document.getElementById('snitchMobileInput');
          if (inp) inp.focus();
        }}, 200);
      }}
    }}

    function closeAccountModalDirect() {{
      var backdrop = document.getElementById('accountModalBackdrop');
      if (backdrop) backdrop.classList.remove('open');
      clearInterval(snitchOtpInterval);
    }}

    function closeAccountModal(e) {{
      if (e.target.id === 'accountModalBackdrop') {{
        closeAccountModalDirect();
      }}
    }}

    function onSnitchPhoneInput(el) {{
      el.value = el.value.replace(/\\D/g, '');
      var err = document.getElementById('snitchPhoneError');
      if (err) err.style.display = 'none';
    }}

    function requestSnitchOtp() {{
      var inp = document.getElementById('snitchMobileInput');
      var phone = inp ? inp.value.trim() : '';
      if (phone.length < 10) {{
        var err = document.getElementById('snitchPhoneError');
        if (err) err.style.display = 'block';
        if (inp) inp.focus();
        return;
      }}
      
      var displayEl = document.getElementById('snitchOtpPhoneDisplay');
      if (displayEl) displayEl.textContent = '+91 ' + phone;
      
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      if (p) p.style.display = 'none';
      if (o) o.style.display = 'block';
      
      ['sOtp1', 'sOtp2', 'sOtp3', 'sOtp4'].forEach(function(id) {{
        var el = document.getElementById(id);
        if (el) el.value = '';
      }});
      var firstBox = document.getElementById('sOtp1');
      if (firstBox) firstBox.focus();
      
      startSnitchOtpTimer();
    }}

    function snitchEditPhone() {{
      clearInterval(snitchOtpInterval);
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      if (o) o.style.display = 'none';
      if (p) p.style.display = 'block';
      var inp = document.getElementById('snitchMobileInput');
      if (inp) inp.focus();
    }}

    function snitchOtpNext(curr, nextId) {{
      curr.value = curr.value.replace(/\\D/g, '');
      if (curr.value && nextId) {{
        var next = document.getElementById(nextId);
        if (next) next.focus();
      }}
      var code = (document.getElementById('sOtp1')?.value || '') +
                 (document.getElementById('sOtp2')?.value || '') +
                 (document.getElementById('sOtp3')?.value || '') +
                 (document.getElementById('sOtp4')?.value || '');
      if (code.length === 4) {{
        setTimeout(verifySnitchOtp, 200);
      }}
    }}

    function snitchOtpBack(e, curr, prevId) {{
      if (e.key === 'Backspace' && !curr.value && prevId) {{
        var prev = document.getElementById(prevId);
        if (prev) {{
          prev.focus();
          prev.value = '';
        }}
      }}
    }}

    function startSnitchOtpTimer() {{
      var sec = 28;
      var timerTxt = document.getElementById('snitchTimerTxt');
      var countdown = document.getElementById('snitchCountdown');
      var resendBtn = document.getElementById('snitchResendBtn');
      if (timerTxt) timerTxt.style.display = 'inline';
      if (resendBtn) resendBtn.style.display = 'none';
      
      clearInterval(snitchOtpInterval);
      snitchOtpInterval = setInterval(function() {{
        sec--;
        if (sec <= 0) {{
          clearInterval(snitchOtpInterval);
          if (timerTxt) timerTxt.style.display = 'none';
          if (resendBtn) resendBtn.style.display = 'inline';
        }} else {{
          if (countdown) countdown.textContent = '0:' + (sec < 10 ? '0' : '') + sec;
        }}
      }}, 1000);
    }}

    function snitchResendOtp() {{
      var inp = document.getElementById('snitchMobileInput');
      var phone = inp ? inp.value.trim() : '';
      alert('New VIP OTP dispatched to +91 ' + phone + ' via SMS & WhatsApp!');
      startSnitchOtpTimer();
    }}

    function verifySnitchOtp() {{
      clearInterval(snitchOtpInterval);
      var inp = document.getElementById('snitchMobileInput');
      var phone = (inp && inp.value.trim()) ? inp.value.trim() : '9988898845';
      snitchCurrentUser = {{
        phone: '+91 ' + phone,
        loggedInAt: new Date().toISOString(),
        tier: 'Atelier Privé VIP'
      }};
      try {{
        localStorage.setItem('meenu_vip_user', JSON.stringify(snitchCurrentUser));
      }} catch(e) {{}}
      
      updateAccountHeaderIcon();
      
      var o = document.getElementById('loginStepOtp');
      var v = document.getElementById('loginStepVip');
      if (o) o.style.display = 'none';
      if (v) v.style.display = 'block';
      var u = document.getElementById('snitchVipUserDisplay');
      if (u) u.textContent = snitchCurrentUser.phone;
      
      showToast('✓ Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
    }}

    function signOutSnitchUser() {{
      snitchCurrentUser = null;
      try {{
        localStorage.removeItem('meenu_vip_user');
      }} catch(e) {{}}
      updateAccountHeaderIcon();
      
      var p = document.getElementById('loginStepPhone');
      var v = document.getElementById('loginStepVip');
      if (v) v.style.display = 'none';
      if (p) p.style.display = 'block';
      var inp = document.getElementById('snitchMobileInput');
      if (inp) {{
        inp.value = '';
        inp.focus();
      }}
      showToast('Signed out successfully.');
    }}


    function searchProducts() {{
      var q = document.getElementById('searchInput').value.toLowerCase().trim();
      var cards = document.querySelectorAll('.product-card');
      cards.forEach(function(card) {{
        var title = card.querySelector('.card-title').textContent.toLowerCase();
        var fabric = card.querySelector('.card-fabric').textContent.toLowerCase();
        if (title.indexOf(q) !== -1 || fabric.indexOf(q) !== -1) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    /* Product Detail Modal */
    function openProductModal(id) {{
      var p = null;
      for (var i = 0; i < productsData.length; i++) {{
        if (productsData[i].id === id) {{ p = productsData[i]; break; }}
      }}
      if (!p) return;

      activeModalProduct = p;
      selectedSize = 'M';

      document.getElementById('modalImg').src = p.b64;
      document.getElementById('modalTitle').textContent = p.name;
      document.getElementById('modalCode').textContent = 'SKU: ' + p.code + ' • CHANDIGARH DROP 01';
      document.getElementById('modalBadge').textContent = p.badge.toUpperCase();
      document.getElementById('modalBadge').className = 'card-badge ' + p.badge_class;
      document.getElementById('modalPrice').textContent = '₹' + p.price.toLocaleString('en-IN');
      document.getElementById('modalMrp').textContent = '₹' + p.mrp.toLocaleString('en-IN');
      var off = Math.round(((p.mrp - p.price) / p.mrp) * 100);
      document.getElementById('modalOff').textContent = off + '% OFF';
      document.getElementById('modalDesc').textContent = p.desc;
      document.getElementById('modalFabric').textContent = p.fabric;

      var btns = document.querySelectorAll('.modal-size-btn');
      btns.forEach(function(b, idx) {{
        if (idx === 0) b.classList.add('selected');
        else b.classList.remove('selected');
      }});

      updateWhatsAppLink(p, 'M');
      document.getElementById('productModalBackdrop').classList.add('open');
    }}

    function closeModal() {{
      document.getElementById('productModalBackdrop').classList.remove('open');
    }}
    function closeModalOnBackdrop(e) {{
      if (e.target.id === 'productModalBackdrop') closeModal();
    }}

    function selectModalSize(size, el) {{
      selectedSize = size;
      document.querySelectorAll('.modal-size-btn').forEach(function(b) {{ b.classList.remove('selected'); }});
      if (el) el.classList.add('selected');
      if (activeModalProduct) updateWhatsAppLink(activeModalProduct, size);
    }}

    function updateWhatsAppLink(product, size) {{
      var text = encodeURIComponent('Hi Meenu Label! I would like to order "' + product.name + '" (Code: ' + product.code + ') in Size ' + size + ' for ₹' + product.price + '. Please confirm delivery details.');
      document.getElementById('modalWhatsAppBtn').href = 'https://wa.me/919988898845?text=' + text;
    }}

    /* Pincode Checker */
    function checkPincode() {{
      var pin = document.getElementById('pincodeInput').value.trim();
      var res = document.getElementById('pincodeResult');
      if (pin.length !== 6 || isNaN(pin)) {{
        res.textContent = '❌ Please enter a valid 6-digit Indian pincode.';
        res.style.color = '#B83A3A';
        return;
      }}
      if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {{
        res.textContent = '⚡ Tricity Priority! Arrives Tomorrow by 2 PM via Express Courier.';
        res.style.color = '#2B6E44';
      }} else {{
        res.textContent = '✓ Available! Estimated delivery within 2-3 business days.';
        res.style.color = '#2B6E44';
      }}
    }}

    /* Cart Operations */
    function quickAddCart(id, size) {{
      var p = null;
      for (var i = 0; i < productsData.length; i++) {{
        if (productsData[i].id === id) {{ p = productsData[i]; break; }}
      }}
      if (!p) return;
      addToCart(p, size);
    }}

    function addCurrentProductToCart() {{
      if (!activeModalProduct) return;
      addToCart(activeModalProduct, selectedSize);
      closeModal();
    }}

    function addToCart(product, size) {{
      var existing = null;
      for (var i = 0; i < cart.length; i++) {{
        if (cart[i].id === product.id && cart[i].size === size) {{
          existing = cart[i];
          break;
        }}
      }}
      if (existing) {{
        existing.qty += 1;
      }} else {{
        cart.push({{
          id: product.id,
          name: product.name,
          price: product.price,
          size: size,
          img: product.b64,
          qty: 1
        }});
      }}
      updateCartUI();
      openCart();
      showToast('Added ' + product.name + ' (' + size + ') to Bag!');
    }}

    function removeFromCart(id, size) {{
      cart = cart.filter(function(item) {{
        return !(item.id === id && item.size === size);
      }});
      updateCartUI();
    }}

    function updateCartUI() {{
      var totalItems = 0;
      for (var i = 0; i < cart.length; i++) totalItems += cart[i].qty;
      document.getElementById('cartCount').textContent = totalItems;
      document.getElementById('headerCartCount').textContent = totalItems;

      var listEl = document.getElementById('cartItemsList');
      var subtotalEl = document.getElementById('cartSubtotal');
      var discountEl = document.getElementById('cartDiscount');
      var gstEl = document.getElementById('cartGst');
      var totalEl = document.getElementById('cartTotal');

      if (cart.length === 0) {{
        listEl.innerHTML = '<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 40px; margin-bottom: 12px;">🛍️</div><div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">Your bag is empty</div><div style="font-size: 13px;">Explore our debut 13 silhouettes and find your fit.</div></div>';
        subtotalEl.textContent = '₹0';
        discountEl.textContent = '-₹0';
        gstEl.textContent = '₹0';
        totalEl.textContent = '₹0';
        return;
      }}

      var subtotal = 0;
      var html = '';
      for (var j = 0; j < cart.length; j++) {{
        var it = cart[j];
        subtotal += it.price * it.qty;
        html += '<div class="cart-item"><img src="' + it.img + '" alt="' + it.name + '"><div class="cart-item-details"><div class="cart-item-title">' + it.name + '</div><div class="cart-item-meta">Size: <strong>' + it.size + '</strong> &bull; Qty: ' + it.qty + '</div><div style="display:flex; justify-content:space-between; align-items:center;"><span class="cart-item-price">₹' + (it.price * it.qty).toLocaleString('en-IN') + '</span><button class="cart-item-remove" onclick="removeFromCart(\\'' + it.id + '\\', \\'' + it.size + '\\')">Remove</button></div></div></div>';
      }}
      listEl.innerHTML = html;

      var discountAmt = Math.round(subtotal * discountPercent);
      var finalTotal = subtotal - discountAmt;
      var gstAmt = Math.round(finalTotal * 0.05);

      subtotalEl.textContent = '₹' + subtotal.toLocaleString('en-IN');
      discountEl.textContent = '-₹' + discountAmt.toLocaleString('en-IN');
      gstEl.textContent = '₹' + gstAmt.toLocaleString('en-IN');
      totalEl.textContent = '₹' + finalTotal.toLocaleString('en-IN');
    }}

    function toggleCart() {{
      document.getElementById('cartDrawer').classList.toggle('open');
      document.getElementById('cartBackdrop').classList.toggle('open');
    }}
    function openCart() {{
      document.getElementById('cartDrawer').classList.add('open');
      document.getElementById('cartBackdrop').classList.add('open');
    }}

    function applyCoupon() {{
      var code = document.getElementById('couponCode').value.trim().toUpperCase();
      if (code === 'DEBUT10') {{
        discountPercent = 0.10;
        updateCartUI();
        showToast('🎉 Promo code DEBUT10 applied! 10% discount added.');
      }} else {{
        showToast('❌ Invalid code. Try "DEBUT10" for 10% off.');
      }}
    }}

    function proceedToCheckout() {{
      if (cart.length === 0) {{
        alert('Your bag is empty!');
        return;
      }}
      alert('🔒 Redirecting to Shopify 1-Click Secure Razorpay / Cashfree Gateway for meenulabel.com...');
    }}

    function openSizeGuide() {{
      document.getElementById('sizeGuideBackdrop').classList.add('open');
    }}
    function closeSizeGuideDirect() {{
      document.getElementById('sizeGuideBackdrop').classList.remove('open');
    }}
    function closeSizeGuide(e) {{
      if (e.target.id === 'sizeGuideBackdrop') closeSizeGuideDirect();
    }}

    function showToast(msg) {{
      var t = document.getElementById('toastNote');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(function() {{ t.style.display = 'none'; }}, 3200);
    }}
  </script>
</body>
</html>
"""

# Write to Downloads and Brain
out_downloads = os.path.join(downloads_dir, "Meenu_Label_Desktop_Storefront.html")
with open(out_downloads, "w", encoding="utf-8") as f:
    f.write(html_code)

out_artifacts = os.path.join(artifacts_dir, "Meenu_Label_Desktop_Storefront.html")
with open(out_artifacts, "w", encoding="utf-8") as f:
    f.write(html_code)

print("SUCCESS: Written Snitch-style auto-sliding storefront to Downloads & Brain!")
