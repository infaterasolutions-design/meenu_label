import os, shutil, json, zipfile

shopify_py = 'scratch/build_shopify_theme.py'

# Let's inspect build_shopify_theme.py and ensure campaign-edit and craftsmanship-spotlight sections are cleanly written
with open(shopify_py, 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure CSS in build_shopify_theme.py includes the new craftsmanship and campaign edit CSS
# Let's check if .craftsmanship-section is in meenu-luxury.css in build_shopify_theme.py
if '.craftsmanship-section {' not in text:
    print("Injecting craftsmanship CSS into meenu-luxury.css...")
    # Find assets/meenu-luxury.css
    idx_css = text.find('with open(os.path.join(theme_dir, "assets", "meenu-luxury.css")')
    if idx_css != -1:
        # Find where css text is defined
        idx_css_def = text.rfind('css = """', 0, idx_css)
        if idx_css_def != -1:
            # Append craftsmanship CSS
            craft_css = """
/* ========================================================
   TOUCH & FEEL: FABRIC & CRAFTSMANSHIP SPOTLIGHT (REFINED LUXURY)
   ======================================================== */
.craftsmanship-section {
  max-width: 1440px;
  margin: 30px auto 90px;
  padding: 0 36px;
}
.craftsmanship-header {
  text-align: center;
  margin-bottom: 48px;
}
.craftsmanship-eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent-gold);
  margin-bottom: 10px;
  display: inline-block;
}
.craftsmanship-title {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(28px, 3.4vw, 44px);
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  color: var(--text-main);
  margin: 0 0 12px;
  line-height: 1.18;
}
.craftsmanship-title .accent {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  color: #E2725B;
  text-transform: none;
  font-weight: 600;
}
.craftsmanship-sub {
  font-size: 13px;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 500;
  max-width: 720px;
  margin: 0 auto;
  line-height: 1.6;
}
.craftsmanship-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}
.craft-card {
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
}
.craft-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 48px rgba(44, 32, 22, 0.10);
  border-color: #D4AF37;
}
.craft-card-media {
  position: relative;
  width: 100%;
  height: 440px;
  overflow: hidden;
  background: #111111;
}
.craft-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  transition: transform 0.8s cubic-bezier(0.2, 1, 0.3, 1);
  display: block;
}
.craft-card:hover .craft-card-img {
  transform: scale(1.04);
}
.craft-card-tag {
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
}
.craft-card-body {
  padding: 28px 26px 24px;
  display: flex;
  flex-direction: column;
  flex: 1;
  background: #FFFFFF;
}
.craft-num {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.20em;
  text-transform: uppercase;
  color: #A67C52;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.craft-num-diamond {
  color: #D4AF37;
  font-size: 10px;
}
.craft-name {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 26px;
  font-weight: 700;
  color: #1A1A1A;
  margin: 0 0 10px;
  line-height: 1.22;
  letter-spacing: 0.01em;
}
.craft-desc {
  font-size: 13.5px;
  color: #5C5248;
  line-height: 1.65;
  margin: 0 0 18px;
  flex: 1;
  font-weight: 400;
}
.craft-highlights {
  display: flex;
  flex-direction: column;
  gap: 9px;
  padding: 16px 0;
  border-top: 1px solid #F0EAE1;
  border-bottom: 1px solid #F0EAE1;
  margin-bottom: 18px;
}
.craft-hl-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 12.5px;
  color: #2D251E;
  line-height: 1.45;
}
.craft-hl-diamond {
  color: #A67C52;
  font-size: 10px;
  margin-top: 2px;
  flex-shrink: 0;
}
.craft-hl-row strong {
  color: #1A1A1A;
  font-weight: 600;
}
.craft-spec-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}
.craft-chip {
  background: #FAF7F2;
  border: 1px solid #ECE4DA;
  color: #6B5E52;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  padding: 4px 10px;
  border-radius: 4px;
  text-transform: uppercase;
}
.craft-action-cta {
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
}
.craft-card:hover .craft-action-cta {
  background: #1A1A1A;
  color: #FAF7F2;
  border-color: #1A1A1A;
}
.craft-action-icon {
  transition: transform 0.3s ease;
  display: flex;
  align-items: center;
}
.craft-card:hover .craft-action-icon {
  transform: translateX(4px);
}
@media (max-width: 1024px) {
  .craftsmanship-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .craft-card-media {
    height: 380px;
  }
}
"""
            # Insert craft_css into meenu-luxury.css
            text = text[:idx_css] + "\ncss += \"\"\"" + craft_css + "\"\"\"\n" + text[idx_css:]

# Check if campaign-edit and craftsmanship-spotlight sections are written
sections_to_add = """
# campaign-edit.liquid
campaign_liquid = \"\"\"
<section class="snitch-campaign-editorial-section">
  <div class="snitch-campaign-container">
    <div class="snitch-campaign-header">
      <span class="snitch-campaign-eyebrow">Atelier Capsule 01 &bull; Editorial Lookbook</span>
      <h2 class="snitch-campaign-title">
        THE CAMPAIGN EDIT: EFFORTLESS CHANDIGARH MORNINGS TO <span class="accent">REGAL EVENINGS</span>
      </h2>
      <p class="snitch-campaign-sub">Curated silhouettes styled in natural daylight across Chandigarh's iconic verandahs and promenades.</p>
    </div>
    <div class="snitch-campaign-grid">
      <div class="snitch-campaign-card card-large">
        <div class="snitch-campaign-img-wrap">
          <img src="{{ 'campaign_cafe.jpg' | asset_url }}" alt="Jaipur Chanderi Festive Suit" class="snitch-campaign-img">
          <div class="snitch-campaign-overlay"></div>
          <div class="snitch-campaign-content">
            <span class="snitch-campaign-badge">Editorial Drop Headliner &bull; Garden Verandah</span>
            <h3 class="snitch-campaign-name">Jaipur Chanderi Silk Festive Suit</h3>
            <div class="snitch-campaign-price-row">
              <span class="snitch-campaign-price">₹2,299</span>
              <span class="snitch-campaign-mrp">₹3,699</span>
              <span class="snitch-campaign-discount">38% OFF</span>
            </div>
            <a href="/products/jaipur-chanderi-silk-festive-suit" class="snitch-campaign-btn">SHOP SILHOUETTE &rarr;</a>
          </div>
        </div>
      </div>
      <div class="snitch-campaign-card card-half">
        <div class="snitch-campaign-img-wrap">
          <img src="{{ 'campaign_balcony.jpg' | asset_url }}" alt="Mustard Crepe Angrakha Co-ord" class="snitch-campaign-img">
          <div class="snitch-campaign-overlay"></div>
          <div class="snitch-campaign-content">
            <span class="snitch-campaign-badge">The Balcony Edit &bull; Modern Wrap</span>
            <h3 class="snitch-campaign-name">Mustard Crepe Angrakha Co-ord</h3>
            <div class="snitch-campaign-price-row">
              <span class="snitch-campaign-price">₹1,699</span>
              <span class="snitch-campaign-mrp">₹2,799</span>
            </div>
            <a href="/products/mustard-crepe-angrakha-co-ord-set" class="snitch-campaign-btn">SHOP LOOK &rarr;</a>
          </div>
        </div>
      </div>
      <div class="snitch-campaign-card card-half">
        <div class="snitch-campaign-img-wrap">
          <img src="{{ 'campaign_sukhna.jpg' | asset_url }}" alt="White Porcelain Floral Wrap Dress" class="snitch-campaign-img">
          <div class="snitch-campaign-overlay"></div>
          <div class="snitch-campaign-content">
            <span class="snitch-campaign-badge">Sukhna Promenade &bull; Resort Elegance</span>
            <h3 class="snitch-campaign-name">White Porcelain Floral Wrap Dress</h3>
            <div class="snitch-campaign-price-row">
              <span class="snitch-campaign-price">₹1,599</span>
              <span class="snitch-campaign-mrp">₹2,599</span>
            </div>
            <a href="/products/white-porcelain-floral-wrap-dress" class="snitch-campaign-btn">SHOP LOOK &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{% schema %}
{
  "name": "Campaign Edit",
  "settings": []
}
{% endschema %}
\"\"\"
with open(os.path.join(theme_dir, "sections", "campaign-edit.liquid"), "w", encoding="utf-8") as f:
    f.write(campaign_liquid)

# craftsmanship-spotlight.liquid
craftsmanship_liquid = \"\"\"
<section class="craftsmanship-section">
  <div class="craftsmanship-header">
    <span class="craftsmanship-eyebrow">Atelier Textile Mastery &bull; Artisanal Heritage</span>
    <h2 class="craftsmanship-title">
      TOUCH &amp; FEEL: THE ANATOMY OF <span class="accent">BESPOKE LUXURY</span>
    </h2>
    <p class="craftsmanship-sub">Crafted in Chandigarh from hand-selected pure weaves. Designed for skin-first comfort, zero synthetic itch, and all-day fluid drape.</p>
  </div>

  <div class="craftsmanship-grid">
    <div class="craft-card" onclick="window.location.href='/collections/festive-suits';">
      <div class="craft-card-media">
        <img src="{{ 'craft_chanderi.jpg' | asset_url }}" alt="Handcrafted Chanderi Silk" class="craft-card-img" loading="lazy">
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

    <div class="craft-card" onclick="window.location.href='/collections/co-ord-sets';">
      <div class="craft-card-media">
        <img src="{{ 'craft_crepe.jpg' | asset_url }}" alt="Fluid Crepe Silk" class="craft-card-img" loading="lazy">
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

    <div class="craft-card" onclick="window.location.href='/collections/all';">
      <div class="craft-card-media">
        <img src="{{ 'craft_organza.jpg' | asset_url }}" alt="Organza Sheer & Gota Detailing" class="craft-card-img" loading="lazy">
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
{% schema %}
{
  "name": "Craftsmanship Spotlight",
  "settings": []
}
{% endschema %}
\"\"\"
with open(os.path.join(theme_dir, "sections", "craftsmanship-spotlight.liquid"), "w", encoding="utf-8") as f:
    f.write(craftsmanship_liquid)
"""

if 'sections", "campaign-edit.liquid"' not in text:
    idx_footer = text.find('with open(os.path.join(theme_dir, "sections", "footer.liquid")')
    if idx_footer != -1:
        idx_footer_end = text.find('\n\n', idx_footer)
        text = text[:idx_footer_end] + "\n" + sections_to_add + text[idx_footer_end:]
        print("Injected campaign-edit.liquid and craftsmanship-spotlight.liquid into build_shopify_theme.py!")

# Also make sure the luxury images are copied into theme_dir/assets
copy_images_code = """
# Copy new luxury craftsmanship and campaign edit images into assets
for img_name, src_path in [
    ('craft_chanderi.jpg', r'scratch/craft_chanderi_lux.jpg'),
    ('craft_crepe.jpg', r'scratch/craft_crepe_lux.jpg'),
    ('craft_organza.jpg', r'scratch/craft_organza_lux.jpg'),
    ('campaign_cafe.jpg', r'scratch/campaign_cafe.jpg'),
    ('campaign_balcony.jpg', r'scratch/campaign_balcony.jpg'),
    ('campaign_sukhna.jpg', r'scratch/campaign_sukhna.jpg')
]:
    if os.path.exists(src_path):
        shutil.copyfile(src_path, os.path.join(theme_dir, "assets", img_name))
"""

if 'craft_chanderi_lux.jpg' not in text:
    idx_zip = text.find('# =========================================================================\n# 8. ZIP PACKAGING')
    if idx_zip != -1:
        text = text[:idx_zip] + copy_images_code + "\n" + text[idx_zip:]
        print("Injected image asset copying code into build_shopify_theme.py!")

with open(shopify_py, 'w', encoding='utf-8') as f:
    f.write(text)
print("build_shopify_theme.py synchronized completely!")
