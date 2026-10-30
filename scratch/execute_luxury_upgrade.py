import os, re

# Paths
storefront_builder = r'scratch/build_snitch_storefront.py'
shopify_builder = r'scratch/build_shopify_theme.py'

with open(storefront_builder, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update image loader paths to craft_*_lux.jpg
text = text.replace("craft_chanderi = 'scratch/craft_chanderi.jpg'", "craft_chanderi = 'scratch/craft_chanderi_lux.jpg'")
text = text.replace("craft_crepe = 'scratch/craft_crepe.jpg'", "craft_crepe = 'scratch/craft_crepe_lux.jpg'")
text = text.replace("craft_organza = 'scratch/craft_organza.jpg'", "craft_organza = 'scratch/craft_organza_lux.jpg'")
text = text.replace("r'scratch/craft_chanderi.jpg'", "r'scratch/craft_chanderi_lux.jpg'")
text = text.replace("r'scratch/craft_crepe.jpg'", "r'scratch/craft_crepe_lux.jpg'")
text = text.replace("r'scratch/craft_organza.jpg'", "r'scratch/craft_organza_lux.jpg'")

# 2. Update CSS block
old_css_start = "/* ========================================================\n       TOUCH & FEEL: FABRIC & CRAFTSMANSHIP SPOTLIGHT\n       ======================================================== */"
old_css_end = "@media (max-width: 960px) {{\n      .craftsmanship-grid {{\n        grid-template-columns: 1fr;\n        gap: 24px;\n      }}\n      .craft-card-media {{\n        height: 260px;\n      }}\n    }}"

new_css = """/* ========================================================
       TOUCH & FEEL: FABRIC & CRAFTSMANSHIP SPOTLIGHT (REFINED LUXURY)
       ======================================================== */
    .craftsmanship-section {{
      max-width: 1440px;
      margin: 30px auto 90px;
      padding: 0 36px;
    }}
    .craftsmanship-header {{
      text-align: center;
      margin-bottom: 48px;
    }}
    .craftsmanship-eyebrow {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 10px;
      display: inline-block;
    }}
    .craftsmanship-title {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(28px, 3.4vw, 44px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0 0 12px;
      line-height: 1.18;
    }}
    .craftsmanship-title .accent {{
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      color: #E2725B;
      text-transform: none;
      font-weight: 600;
    }}
    .craftsmanship-sub {{
      font-size: 13px;
      color: var(--text-muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-weight: 500;
      max-width: 720px;
      margin: 0 auto;
      line-height: 1.6;
    }}

    .craftsmanship-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }}
    .craft-card {{
      background: #FFFFFF;
      border: 1px solid #ECE7E1;
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 20px rgba(28, 22, 17, 0.04);
      cursor: pointer;
      position: relative;
    }}
    .craft-card:hover {{
      transform: translateY(-6px);
      box-shadow: 0 18px 48px rgba(44, 32, 22, 0.10);
      border-color: #D4AF37;
    }}
    .craft-card-media {{
      position: relative;
      width: 100%;
      height: 440px;
      overflow: hidden;
      background: #111111;
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
      transform: scale(1.04);
    }}
    .craft-card-tag {{
      position: absolute;
      top: 18px;
      left: 18px;
      background: rgba(18, 18, 18, 0.72);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #F7EFE6;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 20px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      z-index: 2;
    }}
    .craft-card-body {{
      padding: 28px 26px 24px;
      display: flex;
      flex-direction: column;
      flex: 1;
      background: #FFFFFF;
    }}
    .craft-num {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.20em;
      text-transform: uppercase;
      color: #A67C52;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .craft-num-diamond {{
      color: #D4AF37;
      font-size: 10px;
    }}
    .craft-name {{
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 26px;
      font-weight: 700;
      color: #1A1A1A;
      margin: 0 0 10px;
      line-height: 1.22;
      letter-spacing: 0.01em;
    }}
    .craft-desc {{
      font-size: 13.5px;
      color: #5C5248;
      line-height: 1.65;
      margin: 0 0 18px;
      flex: 1;
      font-weight: 400;
    }}
    .craft-highlights {{
      display: flex;
      flex-direction: column;
      gap: 9px;
      padding: 16px 0;
      border-top: 1px solid #F0EAE1;
      border-bottom: 1px solid #F0EAE1;
      margin-bottom: 18px;
    }}
    .craft-hl-row {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 12.5px;
      color: #2D251E;
      line-height: 1.45;
    }}
    .craft-hl-diamond {{
      color: #A67C52;
      font-size: 10px;
      margin-top: 2px;
      flex-shrink: 0;
    }}
    .craft-hl-row strong {{
      color: #1A1A1A;
      font-weight: 600;
    }}
    .craft-spec-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 20px;
    }}
    .craft-chip {{
      background: #FAF7F2;
      border: 1px solid #ECE4DA;
      color: #6B5E52;
      font-size: 10.5px;
      font-weight: 600;
      letter-spacing: 0.06em;
      padding: 4px 10px;
      border-radius: 4px;
      text-transform: uppercase;
    }}
    .craft-action-cta {{
      background: #FAF7F2;
      color: #1A1A1A;
      border: 1px solid #ECE4DA;
      padding: 13px 18px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.3s ease;
      cursor: pointer;
    }}
    .craft-card:hover .craft-action-cta {{
      background: #1A1A1A;
      color: #FAF7F2;
      border-color: #1A1A1A;
    }}
    .craft-action-icon {{
      transition: transform 0.3s ease;
      display: flex;
      align-items: center;
    }}
    .craft-card:hover .craft-action-icon {{
      transform: translateX(4px);
    }}

    @media (max-width: 1024px) {{
      .craftsmanship-grid {{
        grid-template-columns: 1fr;
        gap: 28px;
      }}
      .craft-card-media {{
        height: 380px;
      }}
    }}"""

# Find and replace CSS
idx_css = text.find('/* ========================================================\n       TOUCH & FEEL')
idx_css_end = text.find('</style>', idx_css)
if idx_css != -1 and idx_css_end != -1:
    text = text[:idx_css] + new_css + "\n  " + text[idx_css_end:]
    print("Replaced CSS successfully!")
else:
    print("Could not find CSS markers, check indices!")

# 3. Update HTML block
new_html = """  <!-- ========================================================
       TOUCH & FEEL: FABRIC & CRAFTSMANSHIP SPOTLIGHT (REFINED LUXURY)
       ======================================================== -->
  <section class="craftsmanship-section">
    <div class="craftsmanship-header">
      <span class="craftsmanship-eyebrow">Atelier Textile Mastery &bull; Artisanal Heritage</span>
      <h2 class="craftsmanship-title">
        TOUCH &amp; FEEL: THE ANATOMY OF <span class="accent">BESPOKE LUXURY</span>
      </h2>
      <p class="craftsmanship-sub">Crafted in Chandigarh from hand-selected pure weaves. Designed for skin-first comfort, zero synthetic itch, and all-day fluid drape.</p>
    </div>

    <div class="craftsmanship-grid">
      <!-- Card 1: Chanderi Silk & Zari -->
      <div class="craft-card" onclick="filterCategory('festive'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <div class="craft-card-media">
          <img src="{craft_chanderi_b64}" alt="Handcrafted Chanderi Silk" class="craft-card-img" loading="lazy">
          <span class="craft-card-tag">Traditional Chanderi Weave</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num"><span class="craft-num-diamond">&#10022;</span> ARTISANAL PILLAR 01</div>
          <h3 class="craft-name">Hand-Woven Chanderi Silk</h3>
          <p class="craft-desc">Featherlight sheer texture enriched with pure gold and silver zari threadwork. Possesses a subtle natural luster that catches soft daylight without artificial synthetic gloss.</p>
          <div class="craft-highlights">
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>100% Breathable</strong> &bull; Pure Cotton Mulmul Lining</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Jaipur Heritage Looms</strong> &bull; Authentic Gold & Silver Zari</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Skin-First Drape</strong> &bull; Zero Prickle for Daylong Celebrations</span></div>
          </div>
          <div class="craft-spec-chips">
            <span class="craft-chip">Pure Mulmul</span>
            <span class="craft-chip">Handloom Zari</span>
            <span class="craft-chip">Featherlight 70 GSM</span>
          </div>
          <div class="craft-action-cta">
            <span>EXPLORE FESTIVE SUITS</span>
            <span class="craft-action-icon">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </span>
          </div>
        </div>
      </div>

      <!-- Card 2: Crepe Silk Co-ord -->
      <div class="craft-card" onclick="filterCategory('coord'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <div class="craft-card-media">
          <img src="{craft_crepe_b64}" alt="Fluid Crepe Silk" class="craft-card-img" loading="lazy">
          <span class="craft-card-tag">All-Day Fluidity</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num"><span class="craft-num-diamond">&#10022;</span> ARTISANAL PILLAR 02</div>
          <h3 class="craft-name">Fluid Crepe Silk Co-ords</h3>
          <p class="craft-desc">Tailored with high-twist crepe yarns for naturally wrinkle-resistant drape. Glides effortlessly across the body, offering tailored elegance from morning coffee to intimate evenings.</p>
          <div class="craft-highlights">
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>High-Twist Silk Crepe</strong> &bull; Natural Anti-Wrinkle Resilience</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Crossover Angrakha</strong> &bull; Handcrafted Side Tie-Up Tassels</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Tailored Ease</strong> &bull; Graceful Comfort Around Hips & Thighs</span></div>
          </div>
          <div class="craft-spec-chips">
            <span class="craft-chip">Anti-Wrinkle</span>
            <span class="craft-chip">Fluid Drape</span>
            <span class="craft-chip">Atelier Tassels</span>
          </div>
          <div class="craft-action-cta">
            <span>EXPLORE CO-ORD SETS</span>
            <span class="craft-action-icon">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </span>
          </div>
        </div>
      </div>

      <!-- Card 3: Organza Sheer & Gota Detailing -->
      <div class="craft-card" onclick="filterCategory('all'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <div class="craft-card-media">
          <img src="{craft_organza_b64}" alt="Organza Sheer & Gota Detailing" class="craft-card-img" loading="lazy">
          <span class="craft-card-tag">Atelier Hand-Embroidery</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num"><span class="craft-num-diamond">&#10022;</span> ARTISANAL PILLAR 03</div>
          <h3 class="craft-name">Organza Sheer &amp; Gota Detailing</h3>
          <p class="craft-desc">Delicate organza dupattas finished with scalloped needlework borders and hand-affixed gota patti. Finished with artisanal hand-tied silk tassels crafted in our Chandigarh atelier.</p>
          <div class="craft-highlights">
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Hand-Attached Gota</strong> &bull; Scalloped Borders with Zero Scratch</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>Translucent Organza</strong> &bull; Luminous Golden Hour Reflection</span></div>
            <div class="craft-hl-row"><span class="craft-hl-diamond">&#10022;</span> <span><strong>3-Tier Atelier Inspection</strong> &bull; Rigorous Thread-Level QA</span></div>
          </div>
          <div class="craft-spec-chips">
            <span class="craft-chip">Scalloped Gota</span>
            <span class="craft-chip">Pure Organza</span>
            <span class="craft-chip">Hand-Tied Tassels</span>
          </div>
          <div class="craft-action-cta">
            <span>EXPLORE SIGNATURE SILHOUETTES</span>
            <span class="craft-action-icon">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>

  """

idx_html = text.find('<!-- ========================================================\n       TOUCH & FEEL')
idx_html_end = text.find('<!-- Catalog Section -->')
if idx_html != -1 and idx_html_end != -1:
    text = text[:idx_html] + new_html + text[idx_html_end:]
    print("Replaced HTML successfully!")
else:
    print("Could not find HTML markers, check indices!")

with open(storefront_builder, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated scratch/build_snitch_storefront.py successfully!")

# Now update Shopify theme builder as well
with open(shopify_builder, 'r', encoding='utf-8') as f:
    s_text = f.read()

# Update CSS in Shopify builder
idx_s_css = s_text.find('/* ========================================================\n   TOUCH & FEEL')
idx_s_css_end = s_text.find('`', idx_s_css)
if idx_s_css != -1 and idx_s_css_end != -1:
    # Notice in Shopify builder, curly braces are single, not double!
    s_new_css = new_css.replace('{{', '{').replace('}}', '}')
    s_text = s_text[:idx_s_css] + s_new_css + "\n" + s_text[idx_s_css_end:]
    print("Updated Shopify CSS successfully!")

# Update Liquid section in Shopify builder
# Let's inspect where craftsmanship-spotlight.liquid is in s_text
idx_liquid = s_text.find('craftsmanship-spotlight.liquid')
if idx_liquid != -1:
    idx_content_start = s_text.find("'''", idx_liquid)
    idx_content_end = s_text.find("'''", idx_content_start + 3)
    if idx_content_start != -1 and idx_content_end != -1:
        # Create liquid markup version of new_html
        s_liquid = new_html.replace('{craft_chanderi_b64}', "{{ 'craft_chanderi.jpg' | asset_url }}")\
                           .replace('{craft_crepe_b64}', "{{ 'craft_crepe.jpg' | asset_url }}")\
                           .replace('{craft_organza_b64}', "{{ 'craft_organza.jpg' | asset_url }}")\
                           .replace('{{', '{').replace('}}', '}')
        s_text = s_text[:idx_content_start+3] + "\n" + s_liquid + "\n" + s_text[idx_content_end:]
        print("Updated craftsmanship-spotlight.liquid in Shopify builder successfully!")

with open(shopify_builder, 'w', encoding='utf-8') as f:
    f.write(s_text)
print("Updated scratch/build_shopify_theme.py successfully!")
