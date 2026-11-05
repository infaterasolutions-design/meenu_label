import os, base64, subprocess

artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66"
highres_dir = os.path.join(artifacts_dir, "scratch", "highres_products")
downloads_dir = r"C:\Users\sande\Downloads"

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

# Product catalogue master data in order of Surat Catalog Pages 1 to 16
products = [
    {
        "page": 1,
        "code": "SET974",
        "name": "The Gulzar Angrakha Crepe Silk Set",
        "category": "2-Pc Festive Set",
        "fabric": "Artisanal Crepe Silk & Chiffon Dupatta",
        "color": "Mustard Marigold & Ochre",
        "wsp": 555,
        "price": 2399,
        "mrp": 3799,
        "expenses": 850,
        "profit": 994,
        "margin_pct": 41.4,
        "img": "SET974.jpg",
        "highlight": "Best Seller Tier"
    },
    {
        "page": 2,
        "code": "TXC26KB04820",
        "name": "The Mehr Lime Silk Blend Tunic Set",
        "category": "2-Pc Tunic Set",
        "fabric": "Pure Silk Blend with Intricate Zari V-Neck",
        "color": "Zesty Lime & Chartreuse",
        "wsp": 685,
        "price": 2499,
        "mrp": 3999,
        "expenses": 850,
        "profit": 964,
        "margin_pct": 38.6,
        "img": "TXC26KB04820.jpg",
        "highlight": "Daytime Festive"
    },
    {
        "page": 3,
        "code": "JAC25ST03063",
        "name": "The Gulabi Organza Festive Suit",
        "category": "3-Pc Anarkali Suit",
        "fabric": "Airy Cotton-Silk Blend with Embroidered Organza",
        "color": "Gulabi Rose Pink",
        "wsp": 655,
        "price": 2499,
        "mrp": 3999,
        "expenses": 850,
        "profit": 994,
        "margin_pct": 39.8,
        "img": "JAC25ST03063.jpg",
        "highlight": "Crowd Favorite"
    },
    {
        "page": 4,
        "code": "JAB24ST00932",
        "name": "The Midnight Botanical Fusion Set",
        "category": "3-Pc Straight Suit",
        "fabric": "Fluid Crepe Silk with Botanical Print",
        "color": "Midnight Navy & Indigo",
        "wsp": 595,
        "price": 2399,
        "mrp": 3799,
        "expenses": 850,
        "profit": 954,
        "margin_pct": 39.8,
        "img": "JAB24ST00932.jpg",
        "highlight": "Artisanal Print"
    },
    {
        "page": 5,
        "code": "SET916",
        "name": "The Sitara Lime Dobby Palazzo Set",
        "category": "2-Pc Palazzo Set",
        "fabric": "Textured Dobby Chiffon & Flared Palazzo",
        "color": "Pistachio & Lime Green",
        "wsp": 675,
        "price": 2499,
        "mrp": 3999,
        "expenses": 850,
        "profit": 974,
        "margin_pct": 39.0,
        "img": "SET916.jpg",
        "highlight": "Sunset Soirée"
    },
    {
        "page": 6,
        "code": "JAC25CD03428",
        "name": "The Porcelain Ivory Resort Co-ord",
        "category": "Luxury Co-ord Set",
        "fabric": "Breathable Cotton Blend Comfort Weave",
        "color": "Ivory Porcelain & Soft Sage",
        "wsp": 555,
        "price": 2399,
        "mrp": 3799,
        "expenses": 850,
        "profit": 994,
        "margin_pct": 41.4,
        "img": "JAC25CD03428.jpg",
        "highlight": "Resort & Travel"
    },
    {
        "page": 7,
        "code": "JAA26DR04449",
        "name": "The Neelam Botanical Georgette Midi",
        "category": "Tiered Midi Dress",
        "fabric": "Featherlight Flowing Georgette",
        "color": "Royal Navy & Floral Azure",
        "wsp": 645,
        "price": 2499,
        "mrp": 3999,
        "expenses": 850,
        "profit": 1004,
        "margin_pct": 40.2,
        "img": "JAA26DR04449.jpg",
        "highlight": "High Tea Edit"
    },
    {
        "page": 8,
        "code": "JNE4046",
        "name": "The White Porcelain Floral Wrap Dress",
        "category": "Wrap Midi Dress",
        "fabric": "Lined Premium Georgette Wrap",
        "color": "Porcelain White & Coral Blossom",
        "wsp": 575,
        "price": 2399,
        "mrp": 3799,
        "expenses": 850,
        "profit": 974,
        "margin_pct": 40.6,
        "img": "JNE4046.jpg",
        "highlight": "Parisian Silhouette"
    },
    {
        "page": 9,
        "code": "JAA26DR03942",
        "name": "The Retro Polka Dot Cotton Midi Dress",
        "category": "Vintage Cotton Dress",
        "fabric": "100% Breathable Crisp Fine Cotton",
        "color": "Monochrome Noir & Polka White",
        "wsp": 595,
        "price": 2399,
        "mrp": 3799,
        "expenses": 850,
        "profit": 954,
        "margin_pct": 39.8,
        "img": "JAA26DR03942.jpg",
        "highlight": "Timeless Retro"
    },
    {
        "page": 10,
        "code": "TXC26TP04108",
        "name": "The Artisanal Abstract V-Neck Blouse",
        "category": "Designer Top",
        "fabric": "Semi-Sheer Flowing Fine Chiffon",
        "color": "Multicolor Terracotta & Amber",
        "wsp": 395,
        "price": 1899,
        "mrp": 2999,
        "expenses": 850,
        "profit": 654,
        "margin_pct": 34.4,
        "img": "TXC26TP04108.jpg",
        "highlight": "Atelier Everyday"
    },
    {
        "page": 11,
        "code": "TXC26TP04098",
        "name": "The Monochrome Foliage V-Neck Top",
        "category": "Designer Top",
        "fabric": "Smooth Poly-Crepe Fluid Drape",
        "color": "Ebony & Chalk White",
        "wsp": 295,
        "price": 1799,
        "mrp": 2899,
        "expenses": 850,
        "profit": 654,
        "margin_pct": 36.4,
        "img": "TXC26TP04098.jpg",
        "highlight": "Workwear Luxury"
    },
    {
        "page": 12,
        "code": "ZAC26TP04826",
        "name": "The Contemporary Floral Everyday Blouse",
        "category": "Designer Blouse",
        "fabric": "Wrinkle-Resistant Poly-Crepe Comfort Weave",
        "color": "Midnight Floral & Subtle Slate",
        "wsp": 345,
        "price": 1899,
        "mrp": 2999,
        "expenses": 850,
        "profit": 704,
        "margin_pct": 37.1,
        "img": "ZAC26TP04826.jpg",
        "highlight": "Desk to Dinner"
    },
    {
        "page": 13,
        "code": "JAB26ST05010",
        "name": "The Royal Wine Chanderi Festive Suit",
        "category": "Flagship 3-Pc Hero Suit",
        "fabric": "Pure Handloom Chanderi Silk with Intricate Zari",
        "color": "Deep Festive Wine / Maroon",
        "wsp": 925,
        "price": 2799,
        "mrp": 4499,
        "expenses": 850,
        "profit": 1024,
        "margin_pct": 36.6,
        "img": "JAB26ST05010.jpg",
        "highlight": "FLAGSHIP DEBUT HERO"
    },
    {
        "page": 14,
        "code": "JAB26SS05740",
        "name": "The Roohani Champagne Sharara Set",
        "category": "3-Pc Sleeveless Sharara",
        "fabric": "Lustrous Silk Blend with Gold Zari & Scalloped Dupatta",
        "color": "Almond Champagne Gold",
        "wsp": 1245,
        "price": 3199,
        "mrp": 4999,
        "expenses": 850,
        "profit": 1104,
        "margin_pct": 34.5,
        "img": "JAB26SS05740.jpg",
        "highlight": "HIGHEST MARGIN SUIT"
    },
    {
        "page": 15,
        "code": "JAB25ST02661",
        "name": "The Noor Petrol Teal Chanderi Suit",
        "category": "3-Pc Straight Kurta Suit",
        "fabric": "Pure Chanderi Silk with Intricate Floral Zari",
        "color": "Petrol Teal Blue",
        "wsp": 1085,
        "price": 2999,
        "mrp": 4799,
        "expenses": 850,
        "profit": 1064,
        "margin_pct": 35.5,
        "img": "JAB25ST02661.jpg",
        "highlight": "Regal Heritage"
    },
    {
        "page": 16,
        "code": "JAB26ST05754",
        "name": "The Shahi Lilac Flared Festive Ensemble",
        "category": "3-Pc Front-Slit Flared Suit",
        "fabric": "Lustrous Silk Blend Front-Slit Kurta with Zari",
        "color": "Royal Lilac / Lavender",
        "wsp": 1165,
        "price": 2999,
        "mrp": 4799,
        "expenses": 850,
        "profit": 984,
        "margin_pct": 32.8,
        "img": "JAB26ST05754.jpg",
        "highlight": "Royal Statement"
    }
]

# Embed Base64 images
for p in products:
    p["b64"] = get_b64(os.path.join(highres_dir, p["img"]))

total_wsp = sum(p["wsp"] for p in products)
total_price = sum(p["price"] for p in products)
total_profit = sum(p["profit"] for p in products)
avg_profit = total_profit / len(products)
avg_margin = (total_profit / total_price) * 100

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Meenu Label - Master Catalog & Margin Breakdown (Option B)</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 15mm 15mm 15mm;
      @bottom-right {{
        content: counter(page) " of " counter(pages);
        font-size: 8pt;
        color: #888;
      }}
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1a1a1a;
      background: #ffffff;
      font-size: 10pt;
      line-height: 1.4;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    
    .page {{
      page-break-after: always;
      height: 100%;
      display: flex;
      flex-direction: column;
    }}
    .page:last-child {{
      page-break-after: avoid;
    }}
    
    /* Luxury Header */
    .catalog-header {{
      border-bottom: 2px solid #111;
      padding-bottom: 12px;
      margin-bottom: 18px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    .brand-title {{
      font-family: "Georgia", serif;
      font-size: 26pt;
      letter-spacing: 4px;
      font-weight: 700;
      color: #0f172a;
      line-height: 1;
    }}
    .brand-subtitle {{
      font-size: 8.5pt;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #64748b;
      margin-top: 5px;
      font-weight: 600;
    }}
    .header-meta {{
      text-align: right;
    }}
    .meta-badge {{
      display: inline-block;
      background: #0f172a;
      color: #f8fafc;
      font-size: 8pt;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 4px;
    }}
    .meta-date {{
      font-size: 8pt;
      color: #64748b;
    }}
    
    /* Cover Financial Highlights Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }}
    .kpi-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px;
      text-align: center;
    }}
    .kpi-label {{
      font-size: 7.5pt;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: #64748b;
      font-weight: 600;
      margin-bottom: 4px;
    }}
    .kpi-val {{
      font-family: "Georgia", serif;
      font-size: 16pt;
      font-weight: 700;
      color: #0f172a;
    }}
    .kpi-val.green {{
      color: #15803d;
    }}
    .kpi-sub {{
      font-size: 7pt;
      color: #94a3b8;
      margin-top: 2px;
    }}
    
    /* Expense Structure Box */
    .expense-box {{
      background: #fafaf9;
      border: 1px solid #e7e5e4;
      border-left: 4px solid #b45309;
      border-radius: 6px;
      padding: 12px 16px;
      margin-bottom: 20px;
    }}
    .expense-title {{
      font-size: 9.5pt;
      font-weight: 700;
      color: #78350f;
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .expense-row {{
      display: flex;
      justify-content: space-between;
      font-size: 8.5pt;
      color: #44403c;
      padding: 3px 0;
      border-bottom: 1px dashed #e7e5e4;
    }}
    .expense-row:last-child {{
      border-bottom: none;
      font-weight: 700;
      color: #0f172a;
      padding-top: 6px;
    }}
    
    /* Table Styling */
    table.catalog-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8pt;
      margin-top: 8px;
    }}
    table.catalog-table th {{
      background: #0f172a;
      color: #ffffff;
      padding: 7px 6px;
      text-align: left;
      font-size: 7pt;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    table.catalog-table td {{
      padding: 6px 6px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
    }}
    table.catalog-table tr:nth-child(even) {{
      background: #f8fafc;
    }}
    table.catalog-table tr.hero-row {{
      background: #fef2f2 !important;
      border-left: 3px solid #b91c1c;
      font-weight: 600;
    }}
    .thumb-mini {{
      width: 28px;
      height: 38px;
      object-fit: cover;
      border-radius: 3px;
      border: 1px solid #cbd5e1;
    }}
    .tag-badge {{
      display: inline-block;
      font-size: 6.5pt;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 3px;
      text-transform: uppercase;
    }}
    .badge-hero {{ background: #fee2e2; color: #991b1b; }}
    .badge-top {{ background: #fef3c7; color: #92400e; }}
    .badge-suit {{ background: #dcfce7; color: #166534; }}
    
    /* Lookbook Visual Card Grid */
    .lookbook-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-top: 10px;
    }}
    .product-card {{
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      height: 220px;
    }}
    .card-img-wrap {{
      width: 42%;
      height: 100%;
      position: relative;
      background: #f1f5f9;
    }}
    .card-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .card-page-badge {{
      position: absolute;
      top: 6px;
      left: 6px;
      background: rgba(15, 23, 42, 0.85);
      color: #ffffff;
      font-size: 6.5pt;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 3px;
      letter-spacing: 0.5px;
    }}
    .card-body {{
      width: 58%;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .card-cat {{
      font-size: 7pt;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: #94a3b8;
      font-weight: 700;
    }}
    .card-title {{
      font-family: "Georgia", serif;
      font-size: 10pt;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.25;
      margin: 2px 0 4px 0;
    }}
    .card-code {{
      font-size: 7.5pt;
      font-family: monospace;
      color: #475569;
      font-weight: 600;
      margin-bottom: 4px;
    }}
    .card-specs {{
      font-size: 7pt;
      color: #64748b;
      line-height: 1.35;
      margin-bottom: 6px;
    }}
    .card-price-row {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 6px 8px;
    }}
    .price-main {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
    }}
    .price-selling {{
      font-size: 12pt;
      font-weight: 800;
      color: #0f172a;
    }}
    .price-mrp {{
      font-size: 8pt;
      color: #94a3b8;
      text-decoration: line-through;
    }}
    .margin-pill {{
      margin-top: 4px;
      background: #dcfce7;
      color: #15803d;
      font-size: 7.5pt;
      font-weight: 700;
      padding: 3px 6px;
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
    }}
    .wsp-note {{
      font-size: 6.5pt;
      color: #64748b;
      margin-top: 3px;
      display: flex;
      justify-content: space-between;
    }}
    
    .footer-bar {{
      margin-top: auto;
      border-top: 1px solid #e2e8f0;
      padding-top: 8px;
      display: flex;
      justify-content: space-between;
      font-size: 7.5pt;
      color: #94a3b8;
    }}
  </style>
</head>
<body>

  <!-- ==================== PAGE 1: EXECUTIVE FINANCIAL OVERVIEW ==================== -->
  <div class="page">
    <div class="catalog-header">
      <div>
        <div class="brand-title">MEENU LABEL</div>
        <div class="brand-subtitle">CHANDIGARH • DEBUT INVENTORY DROP 01</div>
      </div>
      <div class="header-meta">
        <div class="meta-badge">FINANCIAL MODEL: OPTION B</div>
        <div class="meta-date">Target Cash Profit: ₹800 – ₹1,100 / Piece</div>
      </div>
    </div>

    <!-- KPI Cards -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Total Collection</div>
        <div class="kpi-val">16 Designs</div>
        <div class="kpi-sub">48 Size Variants (M, L, XL)</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Average Retail ASP</div>
        <div class="kpi-val">₹{int(total_price / len(products)):,}</div>
        <div class="kpi-sub">Option B Tier 1/2 Luxury Range</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Average Net Profit</div>
        <div class="kpi-val green">+₹{int(avg_profit):,}</div>
        <div class="kpi-sub">Clean Cash in Bank / Order</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Average Net Margin</div>
        <div class="kpi-val green">{avg_margin:.1f}%</div>
        <div class="kpi-sub">After Ads, Ship, Pack & Tax</div>
      </div>
    </div>

    <!-- D2C Unit Economics Model Breakdown -->
    <div class="expense-box">
      <div class="expense-title">D2C E-Commerce Operating Cost Benchmark (~₹850 per delivered order)</div>
      <div class="expense-row">
        <span>Meta Ads Blended Customer Acquisition Cost (CAC)</span>
        <span>₹500.00</span>
      </div>
      <div class="expense-row">
        <span>Forward Shipping (Air Express) + Premium Luxury Unboxing (Rigid Box + Butter Paper)</span>
        <span>₹110.00</span>
      </div>
      <div class="expense-row">
        <span>RTO (Return to Origin) & Reverse Logistics Buffer (15–20% rate reserve)</span>
        <span>₹100.00</span>
      </div>
      <div class="expense-row">
        <span>Net Indian GST Outflow (Apparel 5% / 12% minus factory input tax credits)</span>
        <span>₹100.00</span>
      </div>
      <div class="expense-row">
        <span>Payment Gateway Transaction Fee (Razorpay / Cashfree 2% + 18% GST)</span>
        <span>₹40.00</span>
      </div>
      <div class="expense-row">
        <span>Total Non-Product Operating Expense Reserve</span>
        <span>₹850.00 per order</span>
      </div>
    </div>

    <!-- Master Table Summary Preview (Top 8 items) -->
    <h3 style="font-size: 9pt; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; color: #0f172a;">Drop 01 Master Price & Profit Schedule (Part 1: Pages 1 to 8)</h3>
    <table class="catalog-table">
      <thead>
        <tr>
          <th style="width: 25px;">Pg</th>
          <th style="width: 32px;">Img</th>
          <th style="width: 85px;">Code</th>
          <th>Silhouette & Atelier Name</th>
          <th style="width: 80px;">Category</th>
          <th style="width: 50px;">WSP</th>
          <th style="width: 55px;">Selling</th>
          <th style="width: 50px;">MRP</th>
          <th style="width: 75px;">In-Hand Profit</th>
          <th style="width: 45px;">Margin</th>
        </tr>
      </thead>
      <tbody>
""" + "\n".join([f"""        <tr>
          <td>{p['page']:02d}</td>
          <td><img src="{p['b64']}" class="thumb-mini"></td>
          <td><strong>{p['code']}</strong></td>
          <td>{p['name']}</td>
          <td>{p['category']}</td>
          <td>₹{p['wsp']:,}</td>
          <td><strong>₹{p['price']:,}</strong></td>
          <td style="color:#94a3b8; text-decoration:line-through;">₹{p['mrp']:,}</td>
          <td style="color:#15803d; font-weight:700;">+₹{p['profit']:,}</td>
          <td>{p['margin_pct']}%</td>
        </tr>""" for p in products[:8]]) + """
      </tbody>
    </table>

    <div class="footer-bar">
      <span>Meenu Label Atelier • Chandigarh, India</span>
      <span>Confidential • Pricing & Financial Master Sheet (Option B)</span>
      <span>Page 1</span>
    </div>
  </div>

  <!-- ==================== PAGE 2: MASTER TABLE PART 2 & FESTIVE HERO SUITS ==================== -->
  <div class="page">
    <div class="catalog-header">
      <div>
        <div class="brand-title">MEENU LABEL</div>
        <div class="brand-subtitle">CHANDIGARH • DEBUT INVENTORY DROP 01</div>
      </div>
      <div class="header-meta">
        <div class="meta-badge">FINANCIAL MODEL: OPTION B</div>
        <div class="meta-date">High-Ticket Luxury Festive Suits</div>
      </div>
    </div>

    <h3 style="font-size: 9pt; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; color: #0f172a;">Drop 01 Master Price & Profit Schedule (Part 2: Pages 9 to 16)</h3>
    <table class="catalog-table">
      <thead>
        <tr>
          <th style="width: 25px;">Pg</th>
          <th style="width: 32px;">Img</th>
          <th style="width: 85px;">Code</th>
          <th>Silhouette & Atelier Name</th>
          <th style="width: 80px;">Category</th>
          <th style="width: 50px;">WSP</th>
          <th style="width: 55px;">Selling</th>
          <th style="width: 50px;">MRP</th>
          <th style="width: 75px;">In-Hand Profit</th>
          <th style="width: 45px;">Margin</th>
        </tr>
      </thead>
      <tbody>
""" + "\n".join([f"""        <tr class="{'hero-row' if p['code'] == 'JAB26ST05010' else ''}">
          <td>{p['page']:02d}</td>
          <td><img src="{p['b64']}" class="thumb-mini"></td>
          <td><strong>{p['code']}</strong></td>
          <td>{p['name']} {'<span class=\"tag-badge badge-hero\">FLAGSHIP HERO</span>' if p['code'] == 'JAB26ST05010' else ''}</td>
          <td>{p['category']}</td>
          <td>₹{p['wsp']:,}</td>
          <td><strong>₹{p['price']:,}</strong></td>
          <td style="color:#94a3b8; text-decoration:line-through;">₹{p['mrp']:,}</td>
          <td style="color:#15803d; font-weight:700;">+₹{p['profit']:,}</td>
          <td>{p['margin_pct']}%</td>
        </tr>""" for p in products[8:]]) + f"""
        <tr style="background:#0f172a; color:#ffffff; font-weight:700;">
          <td colspan="5" style="padding:8px 6px; text-transform:uppercase;">Drop 01 Grand Totals & Averages</td>
          <td style="padding:8px 6px;">₹{total_wsp:,}</td>
          <td style="padding:8px 6px;">₹{total_price:,}</td>
          <td style="padding:8px 6px;">—</td>
          <td style="padding:8px 6px; color:#4ade80;">+₹{total_profit:,}</td>
          <td style="padding:8px 6px; color:#4ade80;">{avg_margin:.1f}%</td>
        </tr>
      </tbody>
    </table>

    <div style="margin-top: 25px; padding: 14px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px;">
      <h4 style="font-size: 8.5pt; text-transform:uppercase; color:#0f172a; margin-bottom: 6px;">Strategic Takeaway on Luxury Festive Positioning (Pages 13 to 16)</h4>
      <p style="font-size: 8pt; color:#475569; line-height:1.5;">
        The 4 Festive Suits from Pages 13 to 16 (<strong style="color:#0f172a;">The Royal Wine Hero, Roohani Sharara, Noor Chanderi, and Shahi Lilac</strong>) represent your highest profit yield, delivering <strong>+₹984 to +₹1,104 clean cash in-hand profit per unit</strong>. 
        Because Indian Tier 1 and Tier 2 festive shoppers regularly pay ₹3,000–₹4,500 for boutique Chanderi ensembles, these four pieces should absorb 70% of your Meta ad spend focus.
      </p>
    </div>

    <div class="footer-bar">
      <span>Meenu Label Atelier • Chandigarh, India</span>
      <span>Confidential • Pricing & Financial Master Sheet (Option B)</span>
      <span>Page 2</span>
    </div>
  </div>
"""

# Now build 4 pages of 4 products each for visual lookbook (Pages 3, 4, 5, 6)
for chunk_idx in range(4):
    start = chunk_idx * 4
    end = start + 4
    chunk = products[start:end]
    page_num = chunk_idx + 3
    
    html += f"""
  <!-- ==================== PAGE {page_num}: VISUAL LOOKBOOK CARDS ==================== -->
  <div class="page">
    <div class="catalog-header">
      <div>
        <div class="brand-title">MEENU LABEL</div>
        <div class="brand-subtitle">DROP 01 LOOKBOOK & COST SPECIFICATION</div>
      </div>
      <div class="header-meta">
        <div class="meta-badge">CATALOG PAGES {chunk[0]['page']:02d} – {chunk[-1]['page']:02d}</div>
        <div class="meta-date">Authentic Surat Loom Inventory</div>
      </div>
    </div>

    <div class="lookbook-grid">
"""
    for p in chunk:
        html += f"""
      <div class="product-card">
        <div class="card-img-wrap">
          <img src="{p['b64']}" alt="{p['name']}">
          <span class="card-page-badge">PAGE {p['page']:02d}</span>
        </div>
        <div class="card-body">
          <div>
            <span class="card-cat">{p['category']}</span>
            <div class="card-title">{p['name']}</div>
            <div class="card-code">Code: {p['code']}</div>
            <div class="card-specs">
              <strong>Fabric:</strong> {p['fabric']}<br>
              <strong>Color:</strong> {p['color']}
            </div>
          </div>
          <div class="card-price-row">
            <div class="price-main">
              <span class="price-selling">₹{p['price']:,}</span>
              <span class="price-mrp">MRP ₹{p['mrp']:,}</span>
            </div>
            <div class="margin-pill">
              <span>NET IN-HAND CASH:</span>
              <span>+₹{p['profit']:,}</span>
            </div>
            <div class="wsp-note">
              <span>Factory WSP: ₹{p['wsp']}</span>
              <span>D2C Exp: ₹850</span>
            </div>
          </div>
        </div>
      </div>
"""
    html += f"""
    </div>

    <div class="footer-bar">
      <span>Meenu Label Atelier • Chandigarh, India</span>
      <span>Confidential • Pricing & Financial Master Sheet (Option B)</span>
      <span>Page {page_num}</span>
    </div>
  </div>
"""

html += """
</body>
</html>
"""

# Write HTML file
html_path = os.path.join(downloads_dir, "Meenu_Label_Option_B_Catalog.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

brain_html = os.path.join(artifacts_dir, "Meenu_Label_Option_B_Catalog.html")
with open(brain_html, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved HTML catalog:", html_path)

# Run Chrome Headless to generate luxury PDF
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
pdf_dest1 = os.path.join(downloads_dir, "Meenu_Label_Option_B_Catalog.pdf")
pdf_dest2 = os.path.join(artifacts_dir, "Meenu_Label_Option_B_Catalog.pdf")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_dest1}",
    html_path
]

print("Executing Chrome headless PDF generation...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

if os.path.exists(pdf_dest1):
    import shutil
    shutil.copy2(pdf_dest1, pdf_dest2)
    size_mb = os.path.getsize(pdf_dest1) / (1024 * 1024)
    print(f"SUCCESS: Generated PDF at {pdf_dest1} ({size_mb:.2f} MB)")
else:
    print("Error: PDF not found. STDERR:", res.stderr)
