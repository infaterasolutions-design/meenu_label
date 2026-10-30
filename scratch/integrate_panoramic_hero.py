import os

script_path = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\build_snitch_storefront.py"
with open(script_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Update image loading block (around line 20)
new_img_load = [
    "# 2. Load 4 Full-Bleed 1500x708 Cinematic Editorial Banners\n",
    "banner_1_b64 = get_b64(os.path.join(banners_dir, 'hero_1_marigold.jpg'))\n",
    "banner_2_b64 = get_b64(os.path.join(banners_dir, 'hero_2_gulabi.jpg'))\n",
    "banner_3_b64 = get_b64(os.path.join(banners_dir, 'hero_3_polka.jpg'))\n",
    "banner_4_b64 = get_b64(os.path.join(banners_dir, 'hero_4_lime.jpg'))\n",
]

img_start = -1
for i, l in enumerate(lines):
    if "p_img_polka = get_b64" in l or "banner_1_b64 = get_b64" in l:
        img_start = i - 1 if "# 2." in lines[i-1] else i
        break
assert img_start != -1, "Could not find image load block!"
lines[img_start:img_start+5] = new_img_load
print("Updated image load block.")

# 2. Update CSS block (around line 504)
new_css_block = """    /* =========================================================================
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
"""

css_start = -1
css_end = -1
for i, l in enumerate(lines):
    if "/* Snitch-Style 1500x708 Luxury Architectural Hero Slider" in l or "/* Snitch-Style Full-Bleed Wide Cinematic Banner Slider" in l:
        css_start = i
    if css_start != -1 and ".slider-chevron" in l and i > css_start:
        css_end = i
        break

assert css_start != -1 and css_end != -1, f"Could not find CSS boundaries ({css_start}, {css_end})"
lines[css_start:css_end] = [new_css_block + "\n"]
print(f"Updated CSS block (lines {css_start} to {css_end}).")

# 3. Update HTML block
new_slider_html_block = """  <!-- Snitch 1500x708 Auto-Layout Hero Slider Section -->
  <section class="snitch-hero-section">
    <div class="snitch-hero-viewport" id="heroSlider">
      <div class="snitch-track" id="sliderTrack">
        
        <!-- Slide 1: Flagship Marigold Courtyard Elegance (JAB26ST05010) -->
        <div class="snitch-slide" style="background-image: url('{banner_1_b64}');" onclick="openProductModal('JAB26ST05010')">
          <div class="slide-1-cta-box">
            <div class="slide-overlay-pill">
              <span class="pill-dot"></span> DEBUT DROP 01 &bull; 100% PURE CHANDERI SILK
            </div>
            <div class="slide-overlay-specs" style="color: #4A4036; text-shadow: 0 1px 8px rgba(255,255,255,0.9);">
              <span>Jaipur Heritage Looms</span> &bull; <span>Strictly 3 Pieces (M, L, XL)</span> &bull; <span>₹2,299</span>
            </div>
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductModal('JAB26ST05010')">
              SHOP FESTIVE SUIT &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 2: Royal Gulabi Pavilion (JAC25ST03063) -->
        <div class="snitch-slide" style="background-image: url('{banner_2_b64}');" onclick="openProductModal('JAC25ST03063')">
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
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductModal('JAC25ST03063')">
              VIEW GULABI SUIT &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 3: Retro Polka Dot Veranda (JAA26DR03942) -->
        <div class="snitch-slide" style="background-image: url('{banner_3_b64}');" onclick="openProductModal('JAA26DR03942')">
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
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductModal('JAA26DR03942')">
              EXPLORE WRAP DRESS &rarr;
            </button>
          </div>
        </div>

        <!-- Slide 4: Lime Halter Luxury Terrace (SET916) -->
        <div class="snitch-slide" style="background-image: url('{banner_4_b64}');" onclick="openProductModal('SET916')">
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
            <button class="slide-overlay-btn" onclick="event.stopPropagation(); openProductModal('SET916')">
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
"""

html_start = -1
html_end = -1
for i, l in enumerate(lines):
    if "<!-- Snitch 1500x708 Auto-Layout Hero Slider Section -->" in l or "<!-- Snitch-Style Full-Bleed" in l:
        html_start = i
    if html_start != -1 and "<!-- Slideout Navigation Drawer -->" in l and i > html_start:
        html_end = i
        break

assert html_start != -1 and html_end != -1, f"Could not find HTML boundaries ({html_start}, {html_end})"
lines[html_start:html_end] = [new_slider_html_block + "\n"]
print(f"Updated HTML block (lines {html_start} to {html_end}).")

with open(script_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("SUCCESS: Fully integrated 4 panoramic full-bleed editorial banners into build_snitch_storefront.py!")
