import os

# 1. Update build_snitch_storefront.py
storefront_builder = r'scratch/build_snitch_storefront.py'
with open(storefront_builder, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace CSS for founder-section
old_founder_css = """    /* Founder & Transparency Section */
    .founder-section {{
      max-width: 1440px;
      margin: 60px auto;
      padding: 0 36px;
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 50px;
      align-items: center;
    }}
    .founder-content .tag {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent-gold);
      display: block;
      margin-bottom: 8px;
    }}
    .founder-content h3 {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 34px;
      line-height: 1.25;
      margin-bottom: 18px;
    }}
    .founder-content p {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.7;
      margin-bottom: 14px;
    }}
    .founder-sig {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 30px;
      font-style: italic;
      color: var(--text-main);
      margin-top: 14px;
    }}
    .founder-role {{
      font-size: 11px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-light);
    }}
    .founder-stat-box {{
      background: #FAF5ED;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      padding: 34px;
    }}
    .stat-row {{
      display: flex;
      justify-content: space-between;
      padding: 11px 0;
      border-bottom: 1px solid rgba(230, 224, 214, 0.7);
      font-size: 13px;
    }}
    .stat-row:last-child {{ border-bottom: none; }}
    .stat-label {{ color: var(--text-muted); }}
    .stat-val {{ font-weight: 700; color: var(--text-main); }}"""

new_founder_css = """    /* Founder Section (Minimal Luxury Editorial) */
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
    }}"""

if old_founder_css in text:
    text = text.replace(old_founder_css, new_founder_css)
    print("Replaced founder CSS in build_snitch_storefront.py!")
else:
    print("Warning: old_founder_css exact match not found in build_snitch_storefront.py, attempting index search...")
    idx1 = text.find('/* Founder & Transparency Section */')
    idx2 = text.find('/* Footer */', idx1)
    if idx1 != -1 and idx2 != -1:
        text = text[:idx1] + new_founder_css + "\n\n    " + text[idx2:]
        print("Replaced founder CSS by slice successfully!")

# Replace HTML for founder-section
old_founder_html = """  <!-- Transparency Section -->
  <section class="founder-section" id="founder">
    <div class="founder-content">
      <span class="tag">Chandigarh Atelier &bull; Conscious Creation</span>
      <h3>Why we only craft 3 pieces per size.</h3>
      <p>
        In an era of mass-produced polyester and fast fashion landfills, Meenu Label was founded on a simple promise: 
        <strong>Breathable fabrics, timeless cuts, and zero inventory waste.</strong>
      </p>
      <p>
        Every piece in our Debut Drop is hand-shortlisted directly from master textile weavers in Surat, tailored in small, mindful batches of just 3 pieces per size.
      </p>
      <div class="founder-sig">Meenu</div>
      <div class="founder-role">Founder, Meenu Label</div>
    </div>

    <div class="founder-stat-box">
      <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; margin-bottom: 16px;">Drop 01 Transparency</h4>
      <div class="stat-row">
        <span class="stat-label">Total Curated Designs</span>
        <span class="stat-val">Signature Capsule</span>
      </div>
      <div class="stat-row">
        <span class="stat-label">Inventory Production</span>
        <span class="stat-val">48 Pieces Total (Strict Scarcity)</span>
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
        <span class="stat-label">Brand Ownership</span>
        <span class="stat-val">Meenu Label (Independent Atelier)</span>
      </div>
    </div>
  </section>"""

new_founder_html = """  <!-- Founder Section (Centered Minimal Editorial) -->
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
  </section>"""

if old_founder_html in text:
    text = text.replace(old_founder_html, new_founder_html)
    print("Replaced founder HTML in build_snitch_storefront.py!")
else:
    idx_h1 = text.find('<!-- Transparency Section -->')
    idx_h2 = text.find('<!-- Footer -->', idx_h1)
    if idx_h1 != -1 and idx_h2 != -1:
        text = text[:idx_h1] + new_founder_html + "\n\n  " + text[idx_h2:]
        print("Replaced founder HTML by slice successfully!")

with open(storefront_builder, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated build_snitch_storefront.py successfully!")

# 2. Update build_shopify_theme.py
shopify_builder = r'scratch/build_shopify_theme.py'
with open(shopify_builder, 'r', encoding='utf-8') as f:
    s_text = f.read()

new_founder_liquid = """founder_liquid = \"\"\"
<section style="max-width: 880px; margin: 70px auto 80px; padding: 0 36px; text-align: center;">
  <div>
    <span style="font-size: 11px; font-weight: 700; color: var(--accent-gold); letter-spacing: 0.22em; text-transform: uppercase; display: inline-block; margin-bottom: 12px;">CHANDIGARH ATELIER &bull; CONSCIOUS CREATION</span>
    <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 38px; line-height: 1.25; margin-bottom: 16px; color: var(--text-main); font-weight: 600;">Mindful Elegance, Tailored in Limited Batches.</h3>
    <p style="font-size: 15px; color: var(--text-muted); line-height: 1.8; margin: 0 auto 16px; max-width: 720px; font-weight: 400;">
      In an era of mass-produced polyester, Meenu Label was founded on a simple promise: 
      <strong>pure breathable fabrics, timeless silhouettes, and mindful small-batch creation.</strong>
    </p>
    <div style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 34px; font-style: italic; color: var(--text-main); margin-top: 22px;">Meenu</div>
    <div style="font-size: 10.5px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-muted); margin-top: 4px;">Founder, Meenu Label &bull; Chandigarh</div>
  </div>
</section>

{% schema %}
{
  "name": "Founder Story",
  "settings": [],
  "presets": [
    {
      "name": "Founder Story"
    }
  ]
}
{% endschema %}
\"\"\""""

idx_s1 = s_text.find('founder_liquid = """')
idx_s2 = s_text.find('with open(os.path.join(theme_dir, "sections", "founder-story.liquid")', idx_s1)
if idx_s1 != -1 and idx_s2 != -1:
    s_text = s_text[:idx_s1] + new_founder_liquid + "\n" + s_text[idx_s2:]
    print("Updated founder_liquid in build_shopify_theme.py!")

with open(shopify_builder, 'w', encoding='utf-8') as f:
    f.write(s_text)
print("Updated build_shopify_theme.py successfully!")
