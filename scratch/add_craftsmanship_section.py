import os, re

# 1. Update build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add image loaders at top
if "craft_chanderi_b64" not in code:
    loader_target = "campaign_sukhna_b64 = get_b64(r'scratch/campaign_sukhna.jpg')"
    loader_repl = loader_target + """\ncraft_chanderi_b64 = get_b64(r'scratch/craft_chanderi.jpg')\ncraft_crepe_b64 = get_b64(r'scratch/craft_crepe.jpg')\ncraft_organza_b64 = get_b64(r'scratch/craft_organza.jpg')"""
    if loader_target in code:
        code = code.replace(loader_target, loader_repl)
        print("Added craftsmanship image loaders.")
    else:
        print("ERROR: loader_target not found!")

# Add CSS for Touch & Feel / Craftsmanship Spotlight
craft_css = """
    /* ========================================================
       TOUCH & FEEL / FABRIC & CRAFTSMANSHIP SPOTLIGHT
       ======================================================== */
    .craftsmanship-section {{
      max-width: 1440px;
      margin: 20px auto 80px;
      padding: 0 36px;
    }}
    .craftsmanship-header {{
      text-align: center;
      margin-bottom: 44px;
    }}
    .craftsmanship-eyebrow {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 8px;
      display: inline-block;
    }}
    .craftsmanship-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(28px, 3.4vw, 42px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0 0 10px;
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
      max-width: 680px;
      margin: 0 auto;
    }}

    .craftsmanship-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }}
    .craft-card {{
      background: #FFFFFF;
      border: 1px solid var(--border-color);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
      cursor: pointer;
    }}
    .craft-card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.09);
      border-color: rgba(212, 175, 55, 0.4);
    }}
    .craft-card-media {{
      position: relative;
      height: 310px;
      overflow: hidden;
      background: #0D0D0D;
    }}
    .craft-card-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 20%;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .craft-card:hover .craft-card-img {{
      transform: scale(1.05);
    }}
    .craft-card-tag {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #D4AF37;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 20px;
    }}
    .craft-card-body {{
      padding: 26px 24px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .craft-num {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 6px;
    }}
    .craft-name {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 700;
      color: var(--text-main);
      margin: 0 0 10px;
      line-height: 1.2;
    }}
    .craft-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.6;
      margin: 0 0 16px;
      flex: 1;
    }}
    .craft-bullets {{
      list-style: none;
      padding: 0;
      margin: 0 0 20px;
      border-top: 1px solid var(--border-color);
      padding-top: 14px;
    }}
    .craft-bullets li {{
      font-size: 12px;
      color: var(--text-main);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .craft-bullets li span {{
      color: #25D366;
      font-size: 12px;
    }}
    .craft-link-btn {{
      background: var(--bg-surface);
      color: var(--text-main);
      border: 1px solid var(--border-color);
      padding: 11px 16px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s ease;
      text-decoration: none;
    }}
    .craft-card:hover .craft-link-btn {{
      background: var(--text-main);
      color: #FFFFFF;
      border-color: var(--text-main);
    }}

    @media (max-width: 960px) {{
      .craftsmanship-grid {{
        grid-template-columns: 1fr;
        gap: 24px;
      }}
      .craft-card-media {{
        height: 260px;
      }}
    }}
"""

if "craftsmanship-section" not in code:
    code = code.replace("</style>", craft_css + "\n  </style>")
    print("Inserted Touch & Feel / Craftsmanship CSS.")

# HTML markup for Craftsmanship Spotlight
craft_html = """  <!-- ========================================================
       TOUCH & FEEL / FABRIC & CRAFTSMANSHIP SPOTLIGHT
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
          <img src="{craft_chanderi_b64}" alt="Handcrafted Chanderi Silk" class="craft-card-img">
          <span class="craft-card-tag">Traditional Chanderi Weave</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num">Artisanal Pillar 01</div>
          <h3 class="craft-name">Hand-Woven Chanderi Silk</h3>
          <p class="craft-desc">Featherlight sheer texture enriched with pure gold and silver zari threadwork. Possesses a subtle natural luster that catches soft daylight without artificial synthetic gloss.</p>
          <ul class="craft-bullets">
            <li><span>&#10003;</span> 100% Breathable Pure Cotton Mulmul Lining</li>
            <li><span>&#10003;</span> Sourced from Heritage Handloom Clusters</li>
            <li><span>&#10003;</span> Soft, Skin-First Drape for Daylong Celebrations</li>
          </ul>
          <div class="craft-link-btn">
            <span>EXPLORE FESTIVE SUITS</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>

      <!-- Card 2: Crepe Silk & Angrakha -->
      <div class="craft-card" onclick="filterCategory('coord'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <div class="craft-card-media">
          <img src="{craft_crepe_b64}" alt="Fluid Crepe Silk" class="craft-card-img">
          <span class="craft-card-tag">All-Day Fluidity</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num">Artisanal Pillar 02</div>
          <h3 class="craft-name">Fluid Crepe Silk Co-ords</h3>
          <p class="craft-desc">Tailored with high-twist crepe yarns for naturally wrinkle-resistant drape. Glides effortlessly across the body, offering tailored elegance from boardroom meetings to intimate family dinners.</p>
          <ul class="craft-bullets">
            <li><span>&#10003;</span> Anti-Wrinkle Movement for Busy Workdays</li>
            <li><span>&#10003;</span> Crossover Wrap Silhouette with Custom Tie-Ups</li>
            <li><span>&#10003;</span> Tailored Ease Around Hips &amp; Thighs (Sizes M-XL)</li>
          </ul>
          <div class="craft-link-btn">
            <span>EXPLORE CO-ORD SETS</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>

      <!-- Card 3: Fine Organza & Gota Patti -->
      <div class="craft-card" onclick="filterCategory('all'); var c=document.getElementById('catalog'); if(c) c.scrollIntoView({{behavior:'smooth'}});">
        <div class="craft-card-media">
          <img src="{craft_organza_b64}" alt="Organza & Gota Patti Detail" class="craft-card-img">
          <span class="craft-card-tag">Atelier Hand-Embroidery</span>
        </div>
        <div class="craft-card-body">
          <div class="craft-num">Artisanal Pillar 03</div>
          <h3 class="craft-name">Organza Sheer &amp; Gota Detailing</h3>
          <p class="craft-desc">Delicate organza dupattas finished with scalloped needlework borders and hand-affixed gota patti. Finished with artisanal hand-tied silk tassels crafted in our Chandigarh atelier.</p>
          <ul class="craft-bullets">
            <li><span>&#10003;</span> Hand-Attached Gota Edging (Zero Machine Scratch)</li>
            <li><span>&#10003;</span> Hand-Knotted Tassels &amp; Scalloped Borders</li>
            <li><span>&#10003;</span> Rigorous 3-Tier Quality Inspection Post-Craft</li>
          </ul>
          <div class="craft-link-btn">
            <span>EXPLORE SIGNATURE SILHOUETTES</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

target_catalog = "<!-- Catalog Section -->"
if target_catalog in code and '<section class="craftsmanship-section">' not in code:
    code = code.replace(target_catalog, craft_html + "  " + target_catalog)
    print("Inserted Craftsmanship Spotlight right after Campaign Edit and before Catalog Section!")
else:
    print("Warning: target_catalog not found or craftsmanship-section already present.")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py successfully!")

# 2. Update build_shopify_theme.py
with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    sh_code = f.read()

# Define craftsmanship-spotlight.liquid
sh_craft_snippet = '''# sections/craftsmanship-spotlight.liquid
craft_liquid = """
<section class="craftsmanship-section" style="max-width: 1440px; margin: 20px auto 80px; padding: 0 36px;">
  <div class="craftsmanship-header" style="text-align: center; margin-bottom: 44px;">
    <span class="craftsmanship-eyebrow" style="font-size: 11px; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent-gold); margin-bottom: 8px; display: inline-block;">
      Atelier Textile Mastery • Artisanal Heritage
    </span>
    <h2 class="craftsmanship-title" style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 3.4vw, 42px); font-weight: 700; letter-spacing: 0.03em; text-transform: uppercase; color: var(--text-color); margin: 0 0 10px; line-height: 1.18;">
      TOUCH &amp; FEEL: THE ANATOMY OF BESPOKE LUXURY
    </h2>
    <p class="craftsmanship-sub" style="font-size: 13px; color: var(--text-muted); letter-spacing: 0.08em; text-transform: uppercase; font-weight: 500; max-width: 680px; margin: 0 auto;">
      Crafted in Chandigarh from hand-selected pure weaves. Designed for skin-first comfort, zero synthetic itch, and all-day fluid drape.
    </p>
  </div>

  <div class="craftsmanship-grid">
    <div class="craft-card" onclick="window.location.href='/collections/festive-suits'">
      <div class="craft-card-media">
        <img src="{{ 'hero_1_marigold.jpg' | asset_url }}" alt="Chanderi Silk" class="craft-card-img">
        <span class="craft-card-tag">Traditional Chanderi Weave</span>
      </div>
      <div class="craft-card-body">
        <div class="craft-num">Artisanal Pillar 01</div>
        <h3 class="craft-name">Hand-Woven Chanderi Silk</h3>
        <p class="craft-desc">Featherlight sheer texture enriched with pure gold and silver zari threadwork. Possesses a subtle natural luster that catches soft daylight without artificial synthetic gloss.</p>
        <ul class="craft-bullets">
          <li><span>&#10003;</span> 100% Breathable Pure Cotton Mulmul Lining</li>
          <li><span>&#10003;</span> Sourced from Heritage Handloom Clusters</li>
          <li><span>&#10003;</span> Soft, Skin-First Drape for Daylong Celebrations</li>
        </ul>
        <a href="/collections/festive-suits" class="craft-link-btn">
          <span>EXPLORE FESTIVE SUITS</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>
      </div>
    </div>

    <div class="craft-card" onclick="window.location.href='/collections/co-ord-sets'">
      <div class="craft-card-media">
        <img src="{{ 'hero_2_gulabi.jpg' | asset_url }}" alt="Fluid Crepe Silk" class="craft-card-img">
        <span class="craft-card-tag">All-Day Fluidity</span>
      </div>
      <div class="craft-card-body">
        <div class="craft-num">Artisanal Pillar 02</div>
        <h3 class="craft-name">Fluid Crepe Silk Co-ords</h3>
        <p class="craft-desc">Tailored with high-twist crepe yarns for naturally wrinkle-resistant drape. Glides effortlessly across the body, offering tailored elegance from boardroom meetings to intimate family dinners.</p>
        <ul class="craft-bullets">
          <li><span>&#10003;</span> Anti-Wrinkle Movement for Busy Workdays</li>
          <li><span>&#10003;</span> Crossover Wrap Silhouette with Custom Tie-Ups</li>
          <li><span>&#10003;</span> Tailored Ease Around Hips &amp; Thighs (Sizes M-XL)</li>
        </ul>
        <a href="/collections/co-ord-sets" class="craft-link-btn">
          <span>EXPLORE CO-ORD SETS</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>
      </div>
    </div>

    <div class="craft-card" onclick="window.location.href='/collections/all'">
      <div class="craft-card-media">
        <img src="{{ 'hero_3_polka.jpg' | asset_url }}" alt="Organza Gota Detail" class="craft-card-img">
        <span class="craft-card-tag">Atelier Hand-Embroidery</span>
      </div>
      <div class="craft-card-body">
        <div class="craft-num">Artisanal Pillar 03</div>
        <h3 class="craft-name">Organza Sheer &amp; Gota Detailing</h3>
        <p class="craft-desc">Delicate organza dupattas finished with scalloped needlework borders and hand-affixed gota patti. Finished with artisanal hand-tied silk tassels crafted in our Chandigarh atelier.</p>
        <ul class="craft-bullets">
          <li><span>&#10003;</span> Hand-Attached Gota Edging (Zero Machine Scratch)</li>
          <li><span>&#10003;</span> Hand-Knotted Tassels &amp; Scalloped Borders</li>
          <li><span>&#10003;</span> Rigorous 3-Tier Quality Inspection Post-Craft</li>
        </ul>
        <a href="/collections/all" class="craft-link-btn">
          <span>EXPLORE SIGNATURE SILHOUETTES</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </a>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Craftsmanship Spotlight",
  "settings": [],
  "presets": [
    { "name": "Craftsmanship Spotlight" }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "craftsmanship-spotlight.liquid"), "w", encoding="utf-8") as f:
    f.write(craft_liquid)
'''

if "craftsmanship-spotlight.liquid" not in sh_code:
    pos_camp = sh_code.find('# sections/value-props.liquid')
    if pos_camp != -1:
        sh_code = sh_code[:pos_camp] + sh_craft_snippet + "\n" + sh_code[pos_camp:]
        print("Inserted sections/craftsmanship-spotlight.liquid into build_shopify_theme.py")

# Add CSS to assets/meenu-luxury.css in Shopify
sh_craft_css = """
/* Touch & Feel Craftsmanship */
.craftsmanship-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}
.craft-card {
  background: #FFFFFF;
  border: 1px solid var(--border-color);
  border-radius: 16px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
  cursor: pointer;
}
.craft-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.09);
  border-color: rgba(212, 175, 55, 0.4);
}
.craft-card-media {
  position: relative;
  height: 310px;
  overflow: hidden;
  background: #0D0D0D;
}
.craft-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 20%;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.craft-card:hover .craft-card-img { transform: scale(1.05); }
.craft-card-tag {
  position: absolute; top: 16px; left: 16px;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #D4AF37;
  font-size: 10px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase;
  padding: 5px 12px; border-radius: 20px;
}
.craft-card-body { padding: 26px 24px; display: flex; flex-direction: column; flex: 1; }
.craft-num { font-size: 11px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent-gold); margin-bottom: 6px; }
.craft-name { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-weight: 700; color: var(--text-color); margin: 0 0 10px; line-height: 1.2; }
.craft-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; margin: 0 0 16px; flex: 1; }
.craft-bullets { list-style: none; padding: 0; margin: 0 0 20px; border-top: 1px solid var(--border-color); padding-top: 14px; }
.craft-bullets li { font-size: 12px; color: var(--text-color); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
.craft-bullets li span { color: #25D366; font-size: 12px; }
.craft-link-btn {
  background: var(--bg-surface); color: var(--text-color); border: 1px solid var(--border-color);
  padding: 11px 16px; border-radius: 6px; font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  display: flex; align-items: center; justify-content: space-between; transition: all 0.2s ease; text-decoration: none;
}
.craft-card:hover .craft-link-btn { background: var(--text-color); color: #FFF; border-color: var(--text-color); }
@media (max-width: 960px) {
  .craftsmanship-grid { grid-template-columns: 1fr; gap: 24px; }
  .craft-card-media { height: 260px; }
}
"""

if "craftsmanship-grid" not in sh_code:
    sh_code = sh_code.replace("/* Modals & Cart Drawer */", sh_craft_css + "\n/* Modals & Cart Drawer */")
    print("Added craftsmanship CSS to assets/meenu-luxury.css in Shopify builder.")

# Update index.json order in Shopify builder
old_sh_order = '"order": ["hero", "campaign_edit", "collection", "values", "founder"]'
new_sh_order = '"order": ["hero", "campaign_edit", "craftsmanship", "collection", "values", "founder"]'

if old_sh_order in sh_code:
    sh_code = sh_code.replace('"campaign_edit": {"type": "campaign-edit", "settings": {}}\n    },\n    "order": ["hero", "campaign_edit", "collection", "values", "founder"]',
                             '"campaign_edit": {"type": "campaign-edit", "settings": {}},\n        "craftsmanship": {"type": "craftsmanship-spotlight", "settings": {}}\n    },\n    "order": ["hero", "campaign_edit", "craftsmanship", "collection", "values", "founder"]')
    print("Updated Shopify templates/index.json to include craftsmanship section!")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(sh_code)

print("Saved updated build_shopify_theme.py successfully!")
