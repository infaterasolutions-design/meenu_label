import os
import subprocess
import zipfile

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'

# 1. Update sections/header.liquid
header_path = os.path.join(theme_dir, 'sections', 'header.liquid')
header_content = """
<header>
  <div class="header-bar">
    <!-- Left: Hamburger Menu + Search Icon -->
    <div class="header-left">
      <button class="hamburger-btn" onclick="openNavDrawer()" title="Open Navigation Menu" aria-label="Open Navigation Menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
      <button class="header-icon-action header-search-btn" onclick="toggleSearchBar()" title="Search Drop 01" aria-label="Search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
      </button>
    </div>

    <!-- Middle: Centered Authentic Canva Brand Logo -->
    <div class="header-center">
      <a href="/" title="Meenu Label Homepage">
        <img src="{{ 'logo.png' | asset_url }}" alt="{{ shop.name | default: 'Meenu Label' }}" class="brand-logo-img">
      </a>
    </div>

    <!-- Right: Action Icons (Wishlist, Bag, User) -->
    <div class="header-right">
      <!-- 1. Wishlist (Heart) -->
      <button class="header-icon-action header-wishlist-btn" onclick="openWishlistModal()" title="Saved Wishlist" aria-label="Wishlist">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
        <span class="header-badge-pill" id="headerWishlistCount" style="display:none;">0</span>
      </button>

      <!-- 2. Shopping Bag -->
      <button class="header-icon-action header-bag-btn" onclick="toggleCartDrawer()" title="Shopping Bag" aria-label="Shopping Bag">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
          <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
        </svg>
        <span class="header-badge-pill" id="headerCartCount">{% if cart.item_count > 0 %}{{ cart.item_count }}{% else %}0{% endif %}</span>
      </button>

      <!-- 3. User Account -->
      <button class="header-icon-action header-account-btn" onclick="openAccountModal()" title="Account & VIP Login" aria-label="Account" style="position:relative;">
        <span class="account-active-badge" id="accountActiveBadge"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
      </button>
    </div>
  </div>

  <!-- Slide-Down Search Overlay -->
  <div class="search-overlay-bar" id="searchOverlayBar" style="display:none;">
    <div class="search-overlay-inner">
      <button class="search-close-action" onclick="toggleSearchBar()" title="Close Search">Close &times;</button>
      <form action="/search" method="get" class="search-input-box" role="search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
        <input type="search" name="q" id="searchInput" placeholder="Search by silhouette, style code, fabric, color..." value="{{ search.terms | escape }}">
      </form>
      <div class="search-quick-tags">
        <span class="quick-tag-label">Popular Searches:</span>
        <a href="/collections/festive-suits" class="quick-tag">Festive Suits</a>
        <a href="/collections/co-ord-sets" class="quick-tag">Co-ord Sets</a>
        <a href="/collections/all" class="quick-tag">Chanderi Silk</a>
        <a href="/collections/dresses" class="quick-tag">Midi Dress</a>
        <a href="/collections/all" class="quick-tag">Pure Cotton</a>
      </div>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Luxury Header",
  "settings": []
}
{% endschema %}
"""
with open(header_path, 'w', encoding='utf-8') as f:
    f.write(header_content.strip() + "\n")
print("Updated sections/header.liquid")

# 2. Update sections/hero-editorial.liquid
hero_path = os.path.join(theme_dir, 'sections', 'hero-editorial.liquid')
hero_content = """
<section class="snitch-hero-section">
  <div class="snitch-hero-viewport" id="heroSlider">
    <div class="snitch-track" id="sliderTrack">
      
      <!-- Slide 1: Flagship Marigold Courtyard Elegance (Festive Suit) -->
      <div class="snitch-slide" style="background-image: url('{{ 'banner_2_chanderi.jpg' | asset_url }}');" onclick="window.location.href='/collections/festive-suits'">
        <div class="slide-1-cta-box">
          <div class="slide-overlay-pill">
            <span class="pill-dot"></span> DEBUT DROP 01 &bull; 100% PURE CHANDERI SILK
          </div>
          <div class="slide-overlay-specs" style="color: #4A4036; text-shadow: 0 1px 8px rgba(255,255,255,0.9);">
            <span>Jaipur Heritage Looms</span> &bull; <span>Strictly 3 Pieces (M, L, XL)</span> &bull; <span>₹2,299</span>
          </div>
          <button class="slide-overlay-btn" onclick="event.stopPropagation(); window.location.href='/collections/festive-suits'">
            SHOP FESTIVE SUIT &rarr;
          </button>
        </div>
      </div>

      <!-- Slide 2: Royal Gulabi Pavilion (Gulabi Suit) -->
      <div class="snitch-slide" style="background-image: url('{{ 'banner_3_gulabi.jpg' | asset_url }}');" onclick="window.location.href='/collections/festive-suits'">
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
          <button class="slide-overlay-btn" onclick="event.stopPropagation(); window.location.href='/collections/festive-suits'">
            VIEW GULABI SUIT &rarr;
          </button>
        </div>
      </div>

      <!-- Slide 3: Retro Polka Dot Veranda (Midi Dress) -->
      <div class="snitch-slide" style="background-image: url('{{ 'banner_1_polka.jpg' | asset_url }}');" onclick="window.location.href='/collections/dresses'">
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
          <button class="slide-overlay-btn" onclick="event.stopPropagation(); window.location.href='/collections/dresses'">
            EXPLORE WRAP DRESS &rarr;
          </button>
        </div>
      </div>

      <!-- Slide 4: Lime Halter Luxury Terrace (Co-ord Set) -->
      <div class="snitch-slide" style="background-image: url('{{ 'banner_3_coord.jpg' | asset_url }}');" onclick="window.location.href='/collections/co-ord-sets'">
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
          <button class="slide-overlay-btn" onclick="event.stopPropagation(); window.location.href='/collections/co-ord-sets'">
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
    <div class="atelier-pill" onclick="var c=document.getElementById('collection-grid'); if(c) c.scrollIntoView({behavior:'smooth'})">
      <span class="pulse-dot"></span> Drop 01 &bull; Strictly 48 Pieces Total
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Snitch Luxury Carousel",
  "settings": []
}
{% endschema %}
"""
with open(hero_path, 'w', encoding='utf-8') as f:
    f.write(hero_content.strip() + "\n")
print("Updated sections/hero-editorial.liquid")

# 3. Update assets/meenu-theme.js
js_path = os.path.join(theme_dir, 'assets', 'meenu-theme.js')
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

slider_js = """
// --- Snitch Hero Carousel JS ---
var currentSlide = 0;
var totalSlides = 4;
var slideInterval = 6000;
var slideTimer = null;

function updateSlider() {
  var track = document.getElementById('sliderTrack');
  var dotsContainer = document.getElementById('sliderDots');
  if (track) {
    track.style.transform = 'translateX(-' + (currentSlide * 25) + '%)';
  }
  if (dotsContainer) {
    var dots = dotsContainer.querySelectorAll('.slider-dot');
    dots.forEach(function(dot, idx) {
      if (idx === currentSlide) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  updateSlider();
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  updateSlider();
}

function goToSlide(idx) {
  currentSlide = idx;
  updateSlider();
  resetAutoSlide();
}

function startAutoSlide() {
  stopAutoSlide();
  slideTimer = setInterval(nextSlide, slideInterval);
}

function stopAutoSlide() {
  if (slideTimer) {
    clearInterval(slideTimer);
    slideTimer = null;
  }
}

function resetAutoSlide() {
  stopAutoSlide();
  startAutoSlide();
}

// --- Navigation & Search Bar Controls ---
function toggleSearchBar() {
  var bar = document.getElementById('searchOverlayBar');
  if (!bar) return;
  if (bar.style.display === 'block') {
    bar.style.display = 'none';
  } else {
    bar.style.display = 'block';
    var inp = document.getElementById('searchInput');
    if (inp) inp.focus();
  }
}

function openNavDrawer() {
  var d = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.add('open');
}

function closeNavDrawer() {
  var d = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.remove('open');
}

function toggleCartDrawer() {
  var d = document.getElementById('cartDrawerBackdrop');
  if (d) d.classList.toggle('open');
}

function openSizeGuideModal() {
  var m = document.getElementById('sizeGuideModalBackdrop');
  if (m) m.classList.add('open');
}

function closeSizeGuideModal() {
  var m = document.getElementById('sizeGuideModalBackdrop');
  if (m) m.classList.remove('open');
}

document.addEventListener('DOMContentLoaded', function() {
  var heroEl = document.getElementById('heroSlider');
  if (heroEl) {
    heroEl.addEventListener('mouseenter', stopAutoSlide);
    heroEl.addEventListener('mouseleave', startAutoSlide);
    startAutoSlide();
  }
});
"""

if "updateSlider" not in js_content:
    js_content += "\n" + slider_js
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Updated assets/meenu-theme.js with interactive controls!")

# 4. Git commit and push directly to GitHub repo
subprocess.run(['git', 'add', '.'], cwd=theme_dir, check=True)
subprocess.run(['git', 'commit', '-m', 'Fix header and hero sections with luxury Canva logo, carousel and search overlay'], cwd=theme_dir, check=True)
subprocess.run(['git', 'push', 'origin', 'main'], cwd=theme_dir, check=True)
print("Pushed all fixes to GitHub main branch!")

# 5. Re-package zip
zip_target = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'
with zipfile.ZipFile(zip_target, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        if '.git' in root:
            continue
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Theme re-packaged into {zip_target}")
