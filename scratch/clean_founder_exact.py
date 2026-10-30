with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('/* Founder Transparency Section */')
idx2 = text.find('/* Footer */', idx1)

new_founder_css = """/* Founder Section (Minimal Luxury Editorial) */
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

if idx1 != -1 and idx2 != -1:
    text = text[:idx1] + new_founder_css + "\n\n    " + text[idx2:]
    print("Replaced CSS properly!")

# Now check HTML part:
idx_h1 = text.find('<section class="founder-section"')
idx_h2 = text.find('<!-- Footer -->', idx_h1)

new_founder_html = """<!-- Founder Section (Centered Minimal Editorial) -->
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

if idx_h1 != -1 and idx_h2 != -1:
    text = text[:idx_h1] + new_founder_html + "\n\n  " + text[idx_h2:]
    print("Replaced HTML properly!")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done!")
