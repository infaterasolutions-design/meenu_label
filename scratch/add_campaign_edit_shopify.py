with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Define campaign-edit.liquid section
campaign_liquid_snippet = '''# campaign-edit.liquid
campaign_edit_liquid = """
<section class="campaign-edit-section" style="max-width: 1440px; margin: 80px auto 70px; padding: 0 36px;">
  <div class="campaign-header" style="text-align: center; margin-bottom: 38px;">
    <span class="campaign-eyebrow" style="font-size: 11px; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: var(--accent-gold); margin-bottom: 8px; display: inline-block;">
      {{ section.settings.eyebrow | default: 'Atelier Capsule 01 • Editorial Lookbook' }}
    </span>
    <h2 class="campaign-title" style="font-family: 'Cormorant Garamond', serif; font-size: clamp(28px, 3.4vw, 42px); font-weight: 700; letter-spacing: 0.03em; text-transform: uppercase; color: var(--text-color); margin: 0 0 10px; line-height: 1.18;">
      {{ section.settings.title | default: 'THE CAMPAIGN EDIT: EFFORTLESS CHANDIGARH MORNINGS TO REGAL EVENINGS' }}
    </h2>
    <p class="campaign-sub" style="font-size: 13px; color: var(--text-muted); letter-spacing: 0.08em; text-transform: uppercase; font-weight: 500; max-width: 620px; margin: 0 auto;">
      {{ section.settings.subtitle | default: "Curated silhouettes styled in natural daylight across Chandigarh's iconic verandahs and promenades." }}
    </p>
  </div>

  <div class="campaign-grid">
    <!-- Left Hero (58%): Jaipur Chanderi Festive Suit -->
    <div class="campaign-hero-card" onclick="window.location.href='/products/jaipur-chanderi-silk-festive-suit'">
      <img src="{{ 'hero_1_marigold.jpg' | asset_url }}" alt="Jaipur Chanderi Silk Festive Suit" class="campaign-hero-img">
      <div class="campaign-hero-vignette"></div>
      <div class="campaign-hero-content">
        <span class="campaign-badge">Editorial Drop Headliner • Garden Verandah</span>
        <h3 class="campaign-hero-name">Jaipur Chanderi Silk Festive Suit</h3>
        <div class="campaign-hero-meta">
          <span class="campaign-price">₹2,299</span>
          <span class="campaign-mrp">₹3,699</span>
          <span style="font-size:11px; background:rgba(37,211,102,0.2); color:#25D366; padding:2px 8px; border-radius:12px; font-weight:700;">38% OFF</span>
          <span style="font-size:12px; color:rgba(255,255,255,0.7);">&bull; Handcrafted Chanderi &amp; Zari</span>
        </div>
        <div class="campaign-hero-actions" onclick="event.stopPropagation()">
          <a href="/products/jaipur-chanderi-silk-festive-suit" class="btn-campaign-primary">
            <span>SHOP SILHOUETTE</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </a>
        </div>
      </div>
    </div>

    <!-- Right Stack (42%): 2 Companion Cards -->
    <div class="campaign-stack">
      <!-- Card 1: Mustard Crepe Angrakha -->
      <div class="campaign-sub-card" onclick="window.location.href='/products/mustard-crepe-angrakha-co-ord-set'">
        <img src="{{ 'hero_2_gulabi.jpg' | asset_url }}" alt="Mustard Crepe Angrakha Co-ord Set" class="campaign-sub-img">
        <div class="campaign-sub-vignette"></div>
        <div class="campaign-sub-content">
          <span class="campaign-badge" style="font-size:9px; padding:3px 8px;">The Balcony Edit • Modern Wrap</span>
          <h4 class="campaign-sub-name">Mustard Crepe Angrakha Co-ord</h4>
          <p style="font-size:12px; color:rgba(255,255,255,0.75); margin:0 0 8px;">Gold Gota Trim with Side Tie-Up Tassels</p>
          <div class="campaign-sub-meta" onclick="event.stopPropagation()">
            <div>
              <span class="campaign-sub-price">₹1,699</span>
              <span style="font-size:11px; color:rgba(255,255,255,0.5); text-decoration:line-through; margin-left:6px;">₹2,799</span>
            </div>
            <a href="/products/mustard-crepe-angrakha-co-ord-set" class="btn-campaign-sub">
              <span>SHOP LOOK</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Card 2: White Porcelain Floral Wrap Dress -->
      <div class="campaign-sub-card" onclick="window.location.href='/products/white-porcelain-floral-wrap-dress'">
        <img src="{{ 'hero_3_polka.jpg' | asset_url }}" alt="White Porcelain Floral Wrap Dress" class="campaign-sub-img">
        <div class="campaign-sub-vignette"></div>
        <div class="campaign-sub-content">
          <span class="campaign-badge" style="font-size:9px; padding:3px 8px;">Sukhna Promenade • Resort Elegance</span>
          <h4 class="campaign-sub-name">White Porcelain Floral Wrap Dress</h4>
          <p style="font-size:12px; color:rgba(255,255,255,0.75); margin:0 0 8px;">Featherlight Georgette with Circular Waist Belt</p>
          <div class="campaign-sub-meta" onclick="event.stopPropagation()">
            <div>
              <span class="campaign-sub-price">₹1,599</span>
              <span style="font-size:11px; color:rgba(255,255,255,0.5); text-decoration:line-through; margin-left:6px;">₹2,599</span>
            </div>
            <a href="/products/white-porcelain-floral-wrap-dress" class="btn-campaign-sub">
              <span>SHOP LOOK</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Campaign Edit Lookbook",
  "settings": [
    { "type": "text", "id": "eyebrow", "label": "Eyebrow Text", "default": "Atelier Capsule 01 • Editorial Lookbook" },
    { "type": "text", "id": "title", "label": "Heading", "default": "THE CAMPAIGN EDIT: EFFORTLESS CHANDIGARH MORNINGS TO REGAL EVENINGS" },
    { "type": "textarea", "id": "subtitle", "label": "Sub-heading", "default": "Curated silhouettes styled in natural daylight across Chandigarh's iconic verandahs and promenades." }
  ],
  "presets": [
    { "name": "Campaign Edit Lookbook" }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "campaign-edit.liquid"), "w", encoding="utf-8") as f:
    f.write(campaign_edit_liquid)
'''

if "campaign_edit_liquid" not in code:
    pos_sec = code.find('# sections/value-props.liquid')
    if pos_sec != -1:
        code = code[:pos_sec] + campaign_liquid_snippet + "\n" + code[pos_sec:]
        print("Inserted sections/campaign-edit.liquid definition into build_shopify_theme.py")

# 2. Add campaign-edit CSS into assets/meenu-luxury.css
campaign_css_shopify = """
/* The Campaign Edit Lookbook */
.campaign-grid {
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 24px;
  align-items: stretch;
}
.campaign-hero-card {
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
}
.campaign-hero-img {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: center 25%;
  transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
.campaign-hero-card:hover .campaign-hero-img { transform: scale(1.04); }
.campaign-hero-vignette {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.08) 0%, rgba(0,0,0,0.15) 50%, rgba(0,0,0,0.72) 80%, rgba(0,0,0,0.94) 100%);
}
.campaign-hero-content { position: relative; z-index: 2; padding: 36px 40px; }
.campaign-badge {
  display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: 0.18em;
  text-transform: uppercase; color: #D4AF37; background: rgba(0,0,0,0.55);
  border: 1px solid rgba(212,175,55,0.4); padding: 5px 12px; border-radius: 20px;
  margin-bottom: 12px; backdrop-filter: blur(8px);
}
.campaign-hero-name { font-family: 'Cormorant Garamond', serif; font-size: clamp(26px, 2.6vw, 34px); font-weight: 700; color: #FFF; margin: 0 0 6px; }
.campaign-hero-meta { font-size: 13px; color: rgba(255,255,255,0.85); margin-bottom: 18px; display: flex; align-items: center; gap: 12px; }
.campaign-price { font-size: 18px; font-weight: 700; color: #FFF; }
.campaign-mrp { font-size: 14px; color: rgba(255,255,255,0.55); text-decoration: line-through; }
.btn-campaign-primary {
  background: #FFF; color: #000; border: none; padding: 12px 22px; border-radius: 6px;
  font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  display: inline-flex; align-items: center; gap: 8px; cursor: pointer; text-decoration: none;
}
.btn-campaign-primary:hover { background: #EAEAEA; transform: translateY(-2px); }
.campaign-stack { display: flex; flex-direction: column; gap: 24px; }
.campaign-sub-card {
  position: relative; border-radius: 18px; overflow: hidden; flex: 1; min-height: 308px;
  background: #0D0D0D; display: flex; flex-direction: column; justify-content: flex-end;
  box-shadow: 0 12px 30px rgba(0,0,0,0.06); cursor: pointer;
}
.campaign-sub-img {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 25%;
  transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
.campaign-sub-card:hover .campaign-sub-img { transform: scale(1.04); }
.campaign-sub-vignette {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.2) 40%, rgba(0,0,0,0.75) 80%, rgba(0,0,0,0.92) 100%);
}
.campaign-sub-content { position: relative; z-index: 2; padding: 24px 28px; }
.campaign-sub-name { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; color: #FFF; margin: 0 0 4px; }
.campaign-sub-meta { display: flex; align-items: center; justify-content: space-between; margin-top: 10px; }
.campaign-sub-price { font-size: 15px; font-weight: 700; color: #FFF; }
.btn-campaign-sub {
  background: #FFF; color: #000; border: none; padding: 8px 14px; border-radius: 4px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  display: inline-flex; align-items: center; gap: 6px; cursor: pointer; text-decoration: none;
}
@media (max-width: 900px) {
  .campaign-grid { grid-template-columns: 1fr; }
  .campaign-hero-card { min-height: 480px; }
  .campaign-sub-card { min-height: 260px; }
}
"""

if "campaign-grid" not in code:
    code = code.replace("/* Modals & Cart Drawer */", campaign_css_shopify + "\n/* Modals & Cart Drawer */")
    print("Added campaign-edit CSS into assets/meenu-luxury.css in build_shopify_theme.py")

# 3. Update index_json order in build_shopify_theme.py
old_index_json = """"order": ["hero", "collection", "values", "founder"]"""
new_index_json = """"campaign_edit": {"type": "campaign-edit", "settings": {}},\n        "order": ["hero", "collection", "campaign_edit", "values", "founder"]"""

if old_index_json in code:
    code = code.replace('"founder": {"type": "founder-story", "settings": {}}\n    },\n    "order": ["hero", "collection", "values", "founder"]',
                         '"founder": {"type": "founder-story", "settings": {}},\n        "campaign_edit": {"type": "campaign-edit", "settings": {}}\n    },\n    "order": ["hero", "collection", "campaign_edit", "values", "founder"]')
    print("Updated index.json to include campaign_edit section.")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved updated build_shopify_theme.py successfully!")
