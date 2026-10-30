import os

script_path = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(script_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Update image loading (lines 20-24)
new_img_load = [
    "# 2. Load High-Res Clean Product Images for the Hero Showcase Cards\n",
    "p_img_polka = get_b64(os.path.join(highres_dir, 'JAA26DR03942.jpg'))\n",
    "p_img_chanderi = get_b64(os.path.join(highres_dir, 'JAB26ST05010.jpg'))\n",
    "p_img_coord = get_b64(os.path.join(highres_dir, 'SET916.jpg'))\n",
    "p_img_gulabi = get_b64(os.path.join(highres_dir, 'JAC25ST03063.jpg'))\n",
]

# Find where "# 2. Load 4 Snitch Banners" is
img_start = -1
for i, l in enumerate(lines):
    if "# 2. Load 4 Snitch Banners" in l:
        img_start = i
        break
assert img_start != -1, "Could not find image load block!"

lines[img_start:img_start+5] = new_img_load
print("Replaced image load block.")

# 2. Update CSS block (around line 504)
new_css_block = """    /* Snitch-Style 1500x708 Luxury Architectural Hero Slider */
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
      background: #FAF8F5;
      user-select: none;
    }}
    .snitch-track {{
      display: flex;
      width: 400%;
      height: 100%;
      transition: transform 1.4s cubic-bezier(0.25, 1, 0.5, 1);
      will-change: transform;
    }}
    .snitch-slide {{
      width: 25%;
      height: 100%;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 40px 75px;
      box-sizing: border-box;
      background: #FAF8F5;
      cursor: pointer;
      overflow: hidden;
    }}

    /* Left Editorial Typography */
    .slide-left-col {{
      flex: 0 0 450px;
      max-width: 470px;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 12px;
    }}
    .slide-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #EFE9DE;
      color: #4A4036;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }}
    .slide-badge-pill .pill-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #B8860B;
    }}
    .slide-title-wrap {{
      display: flex;
      flex-direction: column;
      line-height: 1.08;
      margin-top: 4px;
    }}
    .slide-title-bold {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 52px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #1A1816;
      text-transform: uppercase;
    }}
    .slide-title-light {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 42px;
      font-weight: 300;
      letter-spacing: -0.01em;
      color: #2D2721;
      text-transform: uppercase;
    }}
    .slide-sub-text {{
      font-size: 15px;
      color: #7A7064;
      line-height: 1.5;
      margin-top: 2px;
    }}
    .slide-specs-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: #A39B90;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}
    .slide-cta-btn {{
      margin-top: 12px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: #1A1816;
      color: #FAF8F5;
      border: none;
      border-radius: 4px;
      padding: 14px 28px;
      font-size: 13.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .slide-cta-btn:hover {{
      background: #38322C;
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }}

    /* Center Model Editorial Portrait Card */
    .slide-center-col {{
      flex: 0 0 510px;
      height: 610px;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 4;
      position: relative;
    }}
    .slide-card-wrap {{
      width: 100%;
      height: 100%;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(30, 25, 20, 0.10);
      border: 1px solid rgba(0, 0, 0, 0.06);
      background: #F0ECE4;
      position: relative;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }}
    .slide-card-wrap:hover {{
      transform: scale(1.015);
      box-shadow: 0 28px 65px rgba(30, 25, 20, 0.16);
    }}
    .slide-card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
    }}
    .slide-card-tag {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(8px);
      padding: 5px 12px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: #B22222;
      border: 1px solid rgba(0,0,0,0.05);
    }}

    /* Right Flank: Snitch Minimal Quote */
    .slide-right-col {{
      flex: 0 0 240px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      z-index: 5;
      padding-left: 24px;
      border-left: 1px solid rgba(0, 0, 0, 0.07);
    }}
    .slide-quote-bold {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: #2D2721;
      line-height: 1.15;
      text-transform: uppercase;
    }}
    .slide-quote-light {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 20px;
      font-weight: 400;
      color: #8C8275;
      line-height: 1.15;
      text-transform: uppercase;
      margin-top: 2px;
    }}
    .slide-quote-cite {{
      margin-top: 14px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #B5AC9E;
      text-transform: uppercase;
    }}
"""

css_start = -1
css_end = -1
for i, l in enumerate(lines):
    if "/* Snitch-Style Full-Bleed Wide Cinematic Banner Slider" in l:
        css_start = i
    if css_start != -1 and ".slider-chevron" in l and i > css_start:
        css_end = i
        break

assert css_start != -1 and css_end != -1, f"Could not find CSS boundaries ({css_start}, {css_end})"
lines[css_start:css_end] = [new_css_block + "\n"]
print(f"Replaced CSS block (lines {css_start} to {css_end}).")

# 3. Update HTML block
new_slider_html_block = """  <!-- Snitch 1500x708 Auto-Layout Hero Slider Section -->
  <section class="snitch-hero-section">
    <div class="snitch-hero-viewport" id="heroSlider">
      <div class="snitch-track" id="sliderTrack">
        
        <!-- Slide 1: Polka Dot Dress -->
        <div class="snitch-slide" onclick="openProductModal('JAA26DR03942')">
          <div class="slide-left-col">
            <div class="slide-badge-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; SCARCITY EDIT
            </div>
            <div class="slide-title-wrap">
              <span class="slide-title-bold">RETRO,</span>
              <span class="slide-title-light">BREATHABLE, BETTER.</span>
            </div>
            <p class="slide-sub-text">
              100% Breathable Pure Cotton with cinched waist sash, flared A-line drape, and timeless vintage silhouette.
            </p>
            <div class="slide-specs-row">
              <span>Flared Wrap Dress</span> &bull; <span>Pure Cotton</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-cta-btn" onclick="event.stopPropagation(); openProductModal('JAA26DR03942')">
              EXPLORE WRAP DRESS &rarr;
            </button>
          </div>

          <div class="slide-center-col">
            <div class="slide-card-wrap">
              <img src="{p_img_polka}" alt="The Retro Polka Dot Wrap Dress" class="slide-card-img">
              <div class="slide-card-tag">Only 3 Left &bull; Scarcity</div>
            </div>
          </div>

          <div class="slide-right-col">
            <span class="slide-quote-bold">MORE BREEZE.</span>
            <span class="slide-quote-light">MORE ATTITUDE.</span>
            <span class="slide-quote-cite">DEBUT CAMPAIGN &bull; CHANDIGARH</span>
          </div>
        </div>

        <!-- Slide 2: Chanderi Festive Suit -->
        <div class="snitch-slide" onclick="openProductModal('JAB26ST05010')">
          <div class="slide-left-col">
            <div class="slide-badge-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; FESTIVE STAR
            </div>
            <div class="slide-title-wrap">
              <span class="slide-title-bold">REGAL,</span>
              <span class="slide-title-light">AIRY, FESTIVE.</span>
            </div>
            <p class="slide-sub-text">
              Pure Jaipur Chanderi Silk 3-piece suit with delicate hand-piped zari V-neck, cigarette pants, and printed organza dupatta.
            </p>
            <div class="slide-specs-row">
              <span>Chanderi Silk 3-Pc</span> &bull; <span>Zari Detailing</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-cta-btn" onclick="event.stopPropagation(); openProductModal('JAB26ST05010')">
              SHOP FESTIVE SUIT &rarr;
            </button>
          </div>

          <div class="slide-center-col">
            <div class="slide-card-wrap">
              <img src="{p_img_chanderi}" alt="Jaipur Chanderi Silk Festive Suit" class="slide-card-img">
              <div class="slide-card-tag">Drop 01 Star &bull; Limited</div>
            </div>
          </div>

          <div class="slide-right-col">
            <span class="slide-quote-bold">LIGHTWEIGHT SILK.</span>
            <span class="slide-quote-light">ROYAL CELEBRATION.</span>
            <span class="slide-quote-cite">HERITAGE WEAVE &bull; JAIPUR</span>
          </div>
        </div>

        <!-- Slide 3: Pleated Halter Co-ord -->
        <div class="snitch-slide" onclick="openProductModal('SET916')">
          <div class="slide-left-col">
            <div class="slide-badge-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; TRENDING EDIT
            </div>
            <div class="slide-title-wrap">
              <span class="slide-title-bold">EFFORTLESS,</span>
              <span class="slide-title-light">FLOWING, CHIC.</span>
            </div>
            <p class="slide-sub-text">
              High-neck halter top tailored in textured dobby chiffon paired with fluid wide-leg palazzo pants in striking chartreuse lime.
            </p>
            <div class="slide-specs-row">
              <span>Palazzo Co-ord Set</span> &bull; <span>Dobby Chiffon</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-cta-btn" onclick="event.stopPropagation(); openProductModal('SET916')">
              SHOP CO-ORD SET &rarr;
            </button>
          </div>

          <div class="slide-center-col">
            <div class="slide-card-wrap">
              <img src="{p_img_coord}" alt="Lime Halter Dobby Palazzo Set" class="slide-card-img">
              <div class="slide-card-tag">Trending Now &bull; Exclusive</div>
            </div>
          </div>

          <div class="slide-right-col">
            <span class="slide-quote-bold">MINIMAL CUT.</span>
            <span class="slide-quote-light">TIMELESS COMFORT.</span>
            <span class="slide-quote-cite">MODERN RESORT &bull; CHANDIGARH</span>
          </div>
        </div>

        <!-- Slide 4: Gulabi Organza Festive Suit -->
        <div class="snitch-slide" onclick="openProductModal('JAC25ST03063')">
          <div class="slide-left-col">
            <div class="slide-badge-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; LIMITED EDITION
            </div>
            <div class="slide-title-wrap">
              <span class="slide-title-bold">GULABI,</span>
              <span class="slide-title-light">POWDER PINK GRACE.</span>
            </div>
            <p class="slide-sub-text">
              Straight-cut kurta with delicate golden neckline zari, tailored trousers, and heritage floral-printed organza dupatta.
            </p>
            <div class="slide-specs-row">
              <span>Cotton Silk 3-Pc</span> &bull; <span>Organza Dupatta</span> &bull; <span>Strictly 3 Pieces</span>
            </div>
            <button class="slide-cta-btn" onclick="event.stopPropagation(); openProductModal('JAC25ST03063')">
              VIEW GULABI SUIT &rarr;
            </button>
          </div>

          <div class="slide-center-col">
            <div class="slide-card-wrap">
              <img src="{p_img_gulabi}" alt="The Gulabi Organza Festive Suit" class="slide-card-img">
              <div class="slide-card-tag">Only 3 Left &bull; Handcrafted</div>
            </div>
          </div>

          <div class="slide-right-col">
            <span class="slide-quote-bold">SUBTLE LUXURY.</span>
            <span class="slide-quote-light">HERITAGE PRINTS.</span>
            <span class="slide-quote-cite">SURAT ATELIER &bull; EXCLUSIVE</span>
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
"""

html_start = -1
html_end = -1
for i, l in enumerate(lines):
    if "<!-- Snitch-Style Full-Bleed Wide Cinematic Banner Slider" in l:
        html_start = i
    if html_start != -1 and "<!-- Slideout Navigation Drawer -->" in l and i > html_start:
        html_end = i
        break

assert html_start != -1 and html_end != -1, f"Could not find HTML boundaries ({html_start}, {html_end})"
lines[html_start:html_end] = [new_slider_html_block + "\n"]
print(f"Replaced HTML block (lines {html_start} to {html_end}).")

with open(script_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("SUCCESS: Refactored build_snitch_storefront.py with pure Snitch 1500x708 layout!")
