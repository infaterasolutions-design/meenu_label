path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\sections\hero-editorial.liquid'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_slide_1 = """      <!-- Slide 1: Flagship Marigold Courtyard Elegance (Festive Suit) -->
      <div class="snitch-slide" style="background-image: url('{{ 'hero_slide_1.jpg' | asset_url }}');" onclick="window.location.href='/collections/festive-suits'">
        <div class="slide-1-cta-box">
          <div class="slide-overlay-specs" style="color: #4A4036; text-shadow: 0 1px 8px rgba(255,255,255,0.9); font-weight: 600;">
            <span>Jaipur Heritage Looms</span> &bull; <span>Strictly 3 Pieces (M, L, XL)</span> &bull; <span>&#8377;2,299</span>
          </div>
          <button class="slide-overlay-btn" onclick="event.stopPropagation(); window.location.href='/collections/festive-suits'">
            SHOP FESTIVE SUIT &rarr;
          </button>
        </div>
      </div>"""

new_slide_1 = """      <!-- Slide 1: Festive Maroon Elegance in Bloom (Flagship Festive Suit) -->
      <div class="snitch-slide snitch-slide-maroon" style="background-image: url('{{ 'banner_festive_maroon.jpg' | asset_url }}'); cursor: pointer;" onclick="window.location.href='/collections/festive-suits'" title="Shop Festive Maroon Elegance in Bloom">
      </div>"""

norm_content = content.replace('\r\n', '\n')
norm_old = old_slide_1.replace('\r\n', '\n')
norm_new = new_slide_1.replace('\r\n', '\n')

if norm_old in norm_content:
    norm_content = norm_content.replace(norm_old, norm_new)
    print("Replaced Slide 1 successfully in sections/hero-editorial.liquid!")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(norm_content)
else:
    print("Could not find norm_old in sections/hero-editorial.liquid!")
