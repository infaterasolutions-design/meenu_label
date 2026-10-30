import os, re

storefront_builder = r'scratch/build_snitch_storefront.py'
shopify_builder = r'scratch/build_shopify_theme.py'

# 1. Update build_snitch_storefront.py
with open(storefront_builder, 'r', encoding='utf-8') as f:
    text = f.read()

new_css = """/* ========================================================
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
    }}"""

new_html = """  <!-- ========================================================
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

  """

idx_css = text.find('/* ========================================================\n       TOUCH & FEEL')
idx_css_end = text.find('</style>', idx_css)
if idx_css != -1 and idx_css_end != -1:
    text = text[:idx_css] + new_css + "\n  " + text[idx_css_end:]
    print("Replaced CSS in build_snitch_storefront.py!")
else:
    print("Failed to find CSS markers in build_snitch_storefront.py!")

idx_html = text.find('<!-- ========================================================\n       TOUCH & FEEL')
idx_html_end = text.find('<!-- Catalog Section -->')
if idx_html != -1 and idx_html_end != -1:
    text = text[:idx_html] + new_html + text[idx_html_end:]
    print("Replaced HTML in build_snitch_storefront.py!")
else:
    print("Failed to find HTML markers in build_snitch_storefront.py!")

with open(storefront_builder, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated scratch/build_snitch_storefront.py successfully!")

# 2. Update build_shopify_theme.py
with open(shopify_builder, 'r', encoding='utf-8') as f:
    s_text = f.read()

# Update CSS in Shopify builder
idx_s_css = s_text.find('/* ========================================================\n   TOUCH & FEEL')
idx_s_css_end = s_text.find('"""', idx_s_css)
if idx_s_css != -1 and idx_s_css_end != -1:
    s_new_css = new_css.replace('{{', '{').replace('}}', '}').replace('/* ========================================================\n       ', '/* ========================================================\n   ')
    s_text = s_text[:idx_s_css] + s_new_css + "\n" + s_text[idx_s_css_end:]
    print("Updated CSS in build_shopify_theme.py!")

# Update Liquid section in Shopify builder
idx_craft_liquid = s_text.find('craftsmanship_liquid = """')
if idx_craft_liquid != -1:
    idx_craft_liquid_end = s_text.find('"""', idx_craft_liquid + 26)
    liquid_body = """<section class="craftsmanship-section">
  <div class="craftsmanship-header">
    <span class="craftsmanship-eyebrow">Atelier Textile Mastery &bull; Artisanal Heritage</span>
    <h2 class="craftsmanship-title">
      TOUCH &amp; FEEL: THE ANATOMY OF <span class="accent">BESPOKE LUXURY</span>
    </h2>
  </div>

  <div class="craftsmanship-grid">
    <div class="craft-card" onclick="window.location.href='/collections/festive-suits';">
      <img src="{{ 'craft_chanderi.jpg' | asset_url }}" alt="Hand-Woven Chanderi Silk" class="craft-card-img" loading="lazy">
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

    <div class="craft-card" onclick="window.location.href='/collections/co-ord-sets';">
      <img src="{{ 'craft_crepe.jpg' | asset_url }}" alt="Fluid Crepe Silk Co-ords" class="craft-card-img" loading="lazy">
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

    <div class="craft-card" onclick="window.location.href='/collections/all';">
      <img src="{{ 'craft_organza.jpg' | asset_url }}" alt="Organza Sheer & Gota Detailing" class="craft-card-img" loading="lazy">
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
{% schema %}
{
  "name": "Craftsmanship Spotlight",
  "settings": []
}
{% endschema %}"""
    s_text = s_text[:idx_craft_liquid+26] + "\n" + liquid_body + "\n" + s_text[idx_craft_liquid_end:]
    print("Updated craftsmanship_liquid in build_shopify_theme.py!")

with open(shopify_builder, 'w', encoding='utf-8') as f:
    f.write(s_text)
print("Updated scratch/build_shopify_theme.py successfully!")
