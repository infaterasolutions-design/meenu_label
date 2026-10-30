import shutil
import os, json, zipfile, csv

theme_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme"
downloads_dir = r"C:\Users\sande\Downloads"

# =========================================================================
# 1. LAYOUT
# =========================================================================
theme_liquid = """<!doctype html>
<html class="no-js" lang="{{ request.locale.iso_code }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="#FAF8F5">
    <link rel="canonical" href="{{ canonical_url }}">
    
    <title>{{ page_title }} – {{ shop.name }}</title>
    {% if page_description %}
      <meta name="description" content="{{ page_description | escape }}">
    {% endif %}

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    {{ 'meenu-luxury.css' | asset_url | stylesheet_tag }}

    {{ content_for_header }}
  </head>

  <body class="template-{{ template.name }}">
    {% section 'announcement-bar' %}
    {% section 'header' %}

    <main id="MainContent" class="content-for-layout focus-none" role="main" tabindex="-1">
      {{ content_for_layout }}
    </main>

    {% section 'footer' %}

    {% render 'nav-drawer' %}
  {% render 'snitch-login-modal' %}
  {% render 'cart-drawer' %}
    {% render 'size-guide-modal' %}

    <script src="{{ 'meenu-theme.js' | asset_url }}" defer="defer"></script>
  </body>
</html>
"""
with open(os.path.join(theme_dir, "layout", "theme.liquid"), "w", encoding="utf-8") as f:
    f.write(theme_liquid)

# =========================================================================
# 2. CONFIG
# =========================================================================
settings_schema = [
    {
        "name": "Theme Colors",
        "settings": [
            {"type": "color", "id": "color_bg", "label": "Background (Ivory)", "default": "#FAF8F5"},
            {"type": "color", "id": "color_text", "label": "Text (Charcoal)", "default": "#1E1C19"},
            {"type": "color", "id": "color_accent", "label": "Accent (Gold)", "default": "#9E7D47"}
        ]
    },
    {
        "name": "Social & Contact",
        "settings": [
            {"type": "text", "id": "whatsapp_number", "label": "WhatsApp Order Number", "default": "919876543210"},
            {"type": "text", "id": "contact_email", "label": "Support Email", "default": "meenulabel24@gmail.com"}
        ]
    }
]
with open(os.path.join(theme_dir, "config", "settings_schema.json"), "w", encoding="utf-8") as f:
    json.dump(settings_schema, f, indent=2)

settings_data = {
    "current": {
        "color_bg": "#FAF8F5",
        "color_text": "#1E1C19",
        "color_accent": "#9E7D47",
        "whatsapp_number": "919876543210",
        "contact_email": "meenulabel24@gmail.com",
        "sections": {}
    }
}
with open(os.path.join(theme_dir, "config", "settings_data.json"), "w", encoding="utf-8") as f:
    json.dump(settings_data, f, indent=2)

# =========================================================================
# 3. LOCALES
# =========================================================================
locales_en = {
    "general": {
        "cart": {
            "view": "View bag",
            "item_added": "Item added to bag"
        }
    }
}
with open(os.path.join(theme_dir, "locales", "en.default.json"), "w", encoding="utf-8") as f:
    json.dump(locales_en, f, indent=2)

# =========================================================================
# 4. ASSETS (CSS & JS)
# =========================================================================
meenu_css = """
:root {
  --bg-primary: #FAF8F5;
  --bg-card: #FFFFFF;
  --bg-surface: #F3EFE8;
  --text-main: #1E1C19;
  --text-muted: #7A7267;
  --border-color: #E6E0D6;
  --accent-gold: #9E7D47;
  --accent-rose: #B83A3A;
  --accent-green: #2B6E44;
  --btn-dark: #1E1C19;
  --btn-hover: #332F2A;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-main);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

/* Announcement Bar */
.announcement-bar {
  background: var(--text-main);
  color: #FAF8F5;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 9px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}
.announcement-bar a { color: #E8D3B9; text-decoration: none; margin-left: 12px; }

/* Header */
header {
  background: rgba(250, 248, 245, 0.96);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 34px;
  z-index: 90;
}
.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  padding: 16px 40px;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}
.brand-logo {
  font-family: 'Cormorant Garamond', serif;
  font-size: 34px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--text-main);
  text-decoration: none;
  text-align: center;
  display: block;
}
.brand-sub {
  font-size: 10px;
  letter-spacing: 0.2em;
  color: var(--text-muted);
  text-transform: uppercase;
  display: block;
  margin-top: -4px;
  text-align: center;
}
.nav-links { display: flex; gap: 28px; list-style: none; }
.nav-links a {
  color: var(--text-main);
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  transition: color 0.15s;
}
.nav-links a:hover { color: var(--accent-gold); }
.header-actions { display: flex; justify-content: flex-end; align-items: center; gap: 16px; }
.header-btn {
  background: none; border: none; cursor: pointer;
  font-size: 14px; font-weight: 600; color: var(--text-main);
  padding: 6px 12px; border-radius: 6px; display: flex; align-items: center; gap: 6px;
}
.cart-badge {
  background: var(--text-main); color: #FFF; font-size: 11px;
  padding: 2px 7px; border-radius: 10px; font-weight: 700;
}

/* Hero Section */
.hero-section {
  max-width: 1400px; margin: 30px auto; padding: 0 40px;
  display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: center;
}
.hero-card {
  background: #FAF5ED; border-radius: 16px; padding: 50px 40px;
  border: 1px solid var(--border-color);
}
.hero-tag {
  display: inline-block; background: #EFE4D2; color: var(--accent-gold);
  font-size: 11px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase;
  padding: 4px 12px; border-radius: 20px; margin-bottom: 18px;
}
.hero-heading {
  font-family: 'Cormorant Garamond', serif; font-size: 48px;
  line-height: 1.15; font-weight: 600; color: var(--text-main); margin-bottom: 16px;
}
.hero-desc { font-size: 15px; color: var(--text-muted); line-height: 1.6; margin-bottom: 26px; }
.btn-primary {
  background: var(--btn-dark); color: #FAF8F5; padding: 13px 26px;
  border-radius: 6px; text-decoration: none; font-size: 12px; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase; display: inline-block; border: none; cursor: pointer;
}
.btn-primary:hover { background: var(--btn-hover); }
.hero-media {
  height: 520px; border-radius: 16px; overflow: hidden;
  border: 1px solid var(--border-color); box-shadow: 0 15px 35px rgba(0,0,0,0.08);
}
.hero-media img { width: 100%; height: 100%; object-fit: cover; }

/* Product Grid */
.sticky-catalog-header {
  position: sticky;
  top: 98px;
  z-index: 85;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(16px);
  padding: 14px 28px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
  margin-bottom: 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}
.catalog-section { max-width: 1400px; margin: 50px auto; padding: 0 40px; }
.section-header {
  display: flex; justify-content: space-between; align-items: flex-end;
  margin-bottom: 28px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px;
}
.section-title { font-family: 'Cormorant Garamond', serif; font-size: 36px; font-weight: 600; }
.product-grid {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 26px;
}
.product-card {
  background: var(--bg-card); border-radius: 12px; overflow: hidden;
  border: 1px solid var(--border-color); transition: transform 0.2s, box-shadow 0.2s;
  display: flex; flex-direction: column;
}
.product-card:hover { transform: translateY(-4px); box-shadow: 0 10px 24px rgba(0,0,0,0.06); }
.card-thumb { height: 370px; background: #F4EFEB; position: relative; overflow: hidden; }
.card-thumb img { width: 100%; height: 100%; object-fit: cover; }
.card-badge {
  position: absolute; top: 12px; left: 12px; font-size: 10px; font-weight: 700;
  letter-spacing: 0.06em; text-transform: uppercase; padding: 3px 8px; border-radius: 4px;
}
.badge-scarcity { background: var(--accent-rose); color: #FFF; }
.badge-exclusive { background: var(--accent-green); color: #FFF; }
.card-body { padding: 16px; flex-grow: 1; display: flex; flex-direction: column; }
.card-title {
  font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600;
  color: var(--text-main); margin-bottom: 4px; text-decoration: none;
}
.card-price-row { display: flex; align-items: baseline; gap: 8px; margin-bottom: 12px; }
.price-main { font-size: 17px; font-weight: 700; color: var(--text-main); }
.price-mrp { font-size: 13px; text-decoration: line-through; color: var(--text-muted); }
.size-chips { display: flex; gap: 6px; margin-top: auto; padding-top: 10px; border-top: 1px solid #F0EAE1; }
.size-chip {
  font-size: 11px; font-weight: 600; padding: 3px 7px; border: 1px solid var(--border-color);
  border-radius: 4px; background: #FAF8F5; cursor: pointer;
}

/* Value Strip */
.value-strip {
  background: #F4EFEB; border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color); margin: 60px 0; padding: 36px 0;
}
.value-inner {
  max-width: 1400px; margin: 0 auto; padding: 0 40px;
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;
}
.value-item { display: flex; gap: 14px; }
.value-icon { font-size: 26px; }
.value-title { font-weight: 700; font-size: 14px; margin-bottom: 2px; }
.value-desc { font-size: 12px; color: var(--text-muted); }


/* WhatsApp Benefit Hint */
.whatsapp-benefit-box {
  background: #F4FAF6;
  border: 1px solid rgba(37, 211, 102, 0.35);
  border-radius: 8px;
  padding: 11px 14px;
  margin-top: 10px;
  font-size: 12px;
  line-height: 1.55;
  color: #1B4D30;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  text-align: left;
}
.whatsapp-benefit-box strong {
  color: #0F3820;
  font-weight: 700;
}
.whatsapp-benefit-box .wa-icon {
  font-size: 16px;
  line-height: 1.2;
  flex-shrink: 0;
  margin-top: 2px;
}

/* Cart Drawer */
.cart-drawer-backdrop {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(15, 14, 12, 0.5); z-index: 300; display: none;
}
.cart-drawer-backdrop.open { display: block; }
.cart-drawer {
  position: fixed; top: 0; right: -460px; bottom: 0; width: 100%; max-width: 440px;
  background: var(--bg-primary); z-index: 310; box-shadow: -10px 0 30px rgba(0,0,0,0.15);
  display: flex; flex-direction: column; transition: right 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.cart-drawer.open { right: 0; }
.cart-header {
  padding: 18px 24px; border-bottom: 1px solid var(--border-color);
  display: flex; justify-content: space-between; align-items: center;
}
.cart-items { flex: 1; overflow-y: auto; padding: 20px; }
.cart-footer { padding: 20px; border-top: 1px solid var(--border-color); background: #FFF; }

/* Responsive */
@media (max-width: 1024px) {
  .product-grid { grid-template-columns: repeat(2, 1fr); }
  .hero-section { grid-template-columns: 1fr; }
  .value-inner { grid-template-columns: repeat(2, 1fr); }
  .header-inner { padding: 14px 20px; }
}
"""

meenu_css += """
/* ========================================================
   TOUCH & FEEL: FABRIC SPOTLIGHT (MINIMAL ON-IMAGE LUXURY)
       ======================================================== */
    .craftsmanship-section {
      max-width: 1440px;
      margin: 20px auto 80px;
      padding: 0 36px;
    }
    .craftsmanship-header {
      text-align: center;
      margin-bottom: 36px;
    }
    .craftsmanship-eyebrow {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: var(--accent-gold);
      margin-bottom: 8px;
      display: inline-block;
    }
    .craftsmanship-title {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 3.2vw, 40px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      color: var(--text-main);
      margin: 0;
      line-height: 1.18;
    }
    .craftsmanship-title .accent {
      font-family: 'Playfair Display', Georgia, serif;
      font-style: italic;
      color: #E2725B;
      text-transform: none;
      font-weight: 600;
    }

    .craftsmanship-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    .craft-card {
      position: relative;
      height: 560px;
      border-radius: 14px;
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
      background: #111111;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .craft-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.20);
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
      transform: scale(1.05);
    }
    .craft-card-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0) 35%, rgba(0,0,0,0.85) 100%);
      pointer-events: none;
      transition: background 0.4s ease;
    }
    .craft-card:hover .craft-card-overlay {
      background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 30%, rgba(0,0,0,0.92) 100%);
    }
    .craft-card-badge {
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
    }
    .craft-card-content {
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
    }
    .craft-card-eyebrow {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #E6C285;
      text-shadow: 0 1px 3px rgba(0,0,0,0.6);
    }
    .craft-card-title {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 2.2vw, 32px);
      font-weight: 700;
      color: #FFFFFF;
      margin: 0;
      line-height: 1.15;
      letter-spacing: 0.02em;
      text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }
    .craft-card-cta {
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
    }
    .craft-card:hover .craft-card-cta {
      background: #D4AF37;
      color: #111111;
      transform: translateX(4px);
    }
    .craft-card-cta svg {
      transition: transform 0.3s ease;
    }
    .craft-card:hover .craft-card-cta svg {
      transform: translateX(3px);
    }

    @media (max-width: 1024px) {
      .craftsmanship-grid {
        grid-template-columns: 1fr;
        gap: 20px;
      }
      .craft-card {
        height: 480px;
      }
    }
"""
with open(os.path.join(theme_dir, "assets", "meenu-luxury.css"), "w", encoding="utf-8") as f:
    f.write(meenu_css)

meenu_js = """
// Meenu Label Shopify Theme JS
document.addEventListener('DOMContentLoaded', function() {
  console.log('Meenu Label Theme Initialized');
});


/* Snitch Login JS */
var snitchCurrentUser = null;
var snitchOtpInterval = null;

function isSnitchLoggedIn() {
  if (snitchCurrentUser) return true;
  try {
    var stored = localStorage.getItem('meenu_vip_user');
    if (stored) {
      snitchCurrentUser = JSON.parse(stored);
      return true;
    }
  } catch(e) {}
  return false;
}

function updateAccountHeaderIcon() {
  var badge = document.getElementById('accountActiveBadge');
  if (badge) {
    badge.style.display = isSnitchLoggedIn() ? 'block' : 'none';
  }
}

function openAccountModal() {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (!backdrop) return;
  backdrop.classList.add('open');
  if (isSnitchLoggedIn()) {
    var p = document.getElementById('loginStepPhone');
    var o = document.getElementById('loginStepOtp');
    var v = document.getElementById('loginStepVip');
    if (p) p.style.display = 'none';
    if (o) o.style.display = 'none';
    if (v) v.style.display = 'block';
    var u = document.getElementById('snitchVipUserDisplay');
    if (u) u.textContent = snitchCurrentUser.phone || '+91 99888 98845';
  } else {
    var p = document.getElementById('loginStepPhone');
    var o = document.getElementById('loginStepOtp');
    var v = document.getElementById('loginStepVip');
    if (p) p.style.display = 'block';
    if (o) o.style.display = 'none';
    if (v) v.style.display = 'none';
    setTimeout(function() {
      var inp = document.getElementById('snitchMobileInput');
      if (inp) inp.focus();
    }, 200);
  }
}

function closeAccountModalDirect() {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
  clearInterval(snitchOtpInterval);
}

function closeAccountModal(e) {
  if (e.target.id === 'accountModalBackdrop') closeAccountModalDirect();
}

function onSnitchPhoneInput(el) {
  el.value = el.value.replace(/\\D/g, '');
  var err = document.getElementById('snitchPhoneError');
  if (err) err.style.display = 'none';
}

function requestSnitchOtp() {
  var inp = document.getElementById('snitchMobileInput');
  var phone = inp ? inp.value.trim() : '';
  if (phone.length < 10) {
    var err = document.getElementById('snitchPhoneError');
    if (err) err.style.display = 'block';
    if (inp) inp.focus();
    return;
  }
  var d = document.getElementById('snitchOtpPhoneDisplay');
  if (d) d.textContent = '+91 ' + phone;
  var p = document.getElementById('loginStepPhone');
  var o = document.getElementById('loginStepOtp');
  if (p) p.style.display = 'none';
  if (o) o.style.display = 'block';
  ['sOtp1','sOtp2','sOtp3','sOtp4'].forEach(function(id){
    var el = document.getElementById(id);
    if (el) el.value = '';
  });
  var f = document.getElementById('sOtp1');
  if (f) f.focus();
  startSnitchOtpTimer();
}

function snitchEditPhone() {
  clearInterval(snitchOtpInterval);
  var p = document.getElementById('loginStepPhone');
  var o = document.getElementById('loginStepOtp');
  if (o) o.style.display = 'none';
  if (p) p.style.display = 'block';
  var inp = document.getElementById('snitchMobileInput');
  if (inp) inp.focus();
}

function snitchOtpNext(curr, nextId) {
  curr.value = curr.value.replace(/\\D/g, '');
  if (curr.value && nextId) {
    var next = document.getElementById(nextId);
    if (next) next.focus();
  }
  var code = (document.getElementById('sOtp1')?.value || '') +
             (document.getElementById('sOtp2')?.value || '') +
             (document.getElementById('sOtp3')?.value || '') +
             (document.getElementById('sOtp4')?.value || '');
  if (code.length === 4) {
    setTimeout(verifySnitchOtp, 200);
  }
}

function snitchOtpBack(e, curr, prevId) {
  if (e.key === 'Backspace' && !curr.value && prevId) {
    var prev = document.getElementById(prevId);
    if (prev) {
      prev.focus();
      prev.value = '';
    }
  }
}

function startSnitchOtpTimer() {
  var sec = 28;
  var timerTxt = document.getElementById('snitchTimerTxt');
  var countdown = document.getElementById('snitchCountdown');
  var resendBtn = document.getElementById('snitchResendBtn');
  if (timerTxt) timerTxt.style.display = 'inline';
  if (resendBtn) resendBtn.style.display = 'none';
  clearInterval(snitchOtpInterval);
  snitchOtpInterval = setInterval(function() {
    sec--;
    if (sec <= 0) {
      clearInterval(snitchOtpInterval);
      if (timerTxt) timerTxt.style.display = 'none';
      if (resendBtn) resendBtn.style.display = 'inline';
    } else {
      if (countdown) countdown.textContent = '0:' + (sec < 10 ? '0' : '') + sec;
    }
  }, 1000);
}

function snitchResendOtp() {
  var inp = document.getElementById('snitchMobileInput');
  var phone = inp ? inp.value.trim() : '';
  alert('New VIP OTP dispatched to +91 ' + phone + ' via SMS & WhatsApp!');
  startSnitchOtpTimer();
}

function verifySnitchOtp() {
  clearInterval(snitchOtpInterval);
  var inp = document.getElementById('snitchMobileInput');
  var phone = (inp && inp.value.trim()) ? inp.value.trim() : '9988898845';
  snitchCurrentUser = {
    phone: '+91 ' + phone,
    loggedInAt: new Date().toISOString(),
    tier: 'Atelier Privé VIP'
  };
  try {
    localStorage.setItem('meenu_vip_user', JSON.stringify(snitchCurrentUser));
  } catch(e) {}
  updateAccountHeaderIcon();
  var o = document.getElementById('loginStepOtp');
  var v = document.getElementById('loginStepVip');
  if (o) o.style.display = 'none';
  if (v) v.style.display = 'block';
  var u = document.getElementById('snitchVipUserDisplay');
  if (u) u.textContent = snitchCurrentUser.phone;
}

function signOutSnitchUser() {
  snitchCurrentUser = null;
  try {
    localStorage.removeItem('meenu_vip_user');
  } catch(e) {}
  updateAccountHeaderIcon();
  var p = document.getElementById('loginStepPhone');
  var v = document.getElementById('loginStepVip');
  if (v) v.style.display = 'none';
  if (p) p.style.display = 'block';
  var inp = document.getElementById('snitchMobileInput');
  if (inp) {
    inp.value = '';
    inp.focus();
  }
}

function openNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.add('open');
  if (b) b.classList.add('open');
}
function closeNavDrawer() {
  var d = document.getElementById('navDrawer');
  var b = document.getElementById('navDrawerBackdrop');
  if (d) d.classList.remove('open');
  if (b) b.classList.remove('open');
}
function toggleCartDrawer() {
  const drawer = document.getElementById('CartDrawer');
  const backdrop = document.getElementById('CartBackdrop');
  if (drawer && backdrop) {
    drawer.classList.toggle('open');
    backdrop.classList.toggle('open');
  }
}

function openSizeGuideModal() {
  const modal = document.getElementById('SizeGuideModal');
  if (modal) modal.style.display = 'flex';
}

function closeSizeGuideModal() {
  const modal = document.getElementById('SizeGuideModal');
  if (modal) modal.style.display = 'none';
}

function checkTricityPincode(pin) {
  const res = document.getElementById('PincodeResult');
  if (!res) return;
  if (!pin || pin.length !== 6) {
    res.textContent = 'Please enter a valid 6-digit Pincode';
    res.style.color = '#B83A3A';
    return;
  }
  if (pin.startsWith('160') || pin.startsWith('140') || pin.startsWith('134')) {
    res.textContent = '⚡ Tricity Priority! Delivery Tomorrow by 2 PM via Express Dispatch.';
    res.style.color = '#2B6E44';
  } else {
    res.textContent = '✓ Express Delivery Available within 2-3 business days.';
    res.style.color = '#2B6E44';
  }
}
"""
with open(os.path.join(theme_dir, "assets", "meenu-theme.js"), "w", encoding="utf-8") as f:
    f.write(meenu_js)

# =========================================================================
# 5. SECTIONS
# =========================================================================
# announcement-bar.liquid
ann_liquid = """
<div class="announcement-bar">
  <div class="left">📍 CHANDIGARH • PANCHKULA • MOHALI</div>
  <div class="center">{{ section.settings.message }}</div>
  <div class="right">
    <a href="javascript:void(0)" onclick="openSizeGuideModal()">SIZE GUIDE</a>
  </div>
</div>

{% schema %}
{
  "name": "Announcement Bar",
  "settings": [
    {
      "type": "text",
      "id": "message",
      "label": "Announcement Text",
      "default": "✨ DROP 01 LIVE • FREE SHIPPING IN TRICITY • LIMITED 3 PCS PER SIZE"
    }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "announcement-bar.liquid"), "w", encoding="utf-8") as f:
    f.write(ann_liquid)

# header.liquid
header_liquid = """
<header>
  <div class="header-inner">
    <!-- Left: Hamburger Menu Icon -->
    <div class="header-left">
      <button class="hamburger-btn" onclick="openNavDrawer()" aria-label="Open Navigation Menu" title="Open Navigation Menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none;">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Middle: Centered Brand Logo -->
    <div class="header-center">
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>

    <!-- Right: Snitch 4 Minimalist Line Icons -->
    <div class="header-actions">
      <!-- 1. Search -->
      <a href="/search" class="header-icon-link" aria-label="Search" title="Search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
      </a>

      <!-- 2. Shopping Bag -->
      <button class="header-icon-btn" onclick="toggleCartDrawer()" aria-label="Shopping Bag" title="Shopping Bag">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
          <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
        </svg>
        <span class="header-badge-pill" id="cartBadgeCount">{{ cart.item_count }}</span>
      </button>

      <!-- 3. Wishlist (Heart) -->
      <a href="/pages/wishlist" class="header-icon-link" aria-label="Wishlist" title="Wishlist">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
      </a>

      <!-- 4. User Account -->
      <a href="/account" class="header-icon-link" aria-label="Account" title="Account" onclick="openAccountModal(); return false;" style="position:relative;">
        <span class="account-active-badge" id="accountActiveBadge"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
      </a>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "announcement-bar.liquid"), "w", encoding="utf-8") as f:
    f.write(ann_liquid)

# header.liquid
header_liquid = """
<header>
  <div class="header-inner">
    <!-- Brand Logo on Left (Clean layout matching Snitch) -->
    <div>
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH &bull; ESTD 2026</span>
    </div>

    <!-- Snitch-Style Minimalist Outline Icons -->
    <div class="header-actions">
      <!-- 1. Search -->
      <a href="/search" class="header-icon-link" aria-label="Search" title="Search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="7.5"></circle>
          <line x1="16.5" y1="16.5" x2="22" y2="22"></line>
        </svg>
      </a>

      <!-- 2. Shopping Bag -->
      <button class="header-icon-btn" onclick="toggleCartDrawer()" aria-label="Shopping Bag" title="Shopping Bag">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <rect x="4.5" y="8" width="15" height="13" rx="1.5"></rect>
          <path d="M8.5 8V6a3.5 3.5 0 0 1 7 0v2"></path>
        </svg>
        <span class="header-badge-pill" id="cartBadgeCount">{{ cart.item_count }}</span>
      </button>

      <!-- 3. Wishlist (Heart) -->
      <a href="/pages/wishlist" class="header-icon-link" aria-label="Wishlist" title="Wishlist">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
      </a>

      <!-- 4. User Account -->
      <a href="/account" class="header-icon-link" aria-label="Account" title="Account" onclick="openAccountModal(); return false;" style="position:relative;">
        <span class="account-active-badge" id="accountActiveBadge"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="7.5" r="4"></circle>
          <path d="M5 20.5a7 7 0 0 1 14 0"></path>
        </svg>
      </a>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "announcement-bar.liquid"), "w", encoding="utf-8") as f:
    f.write(ann_liquid)

# header.liquid
header_liquid = """
<header>
  <div class="header-inner">
    <nav>
      <ul class="nav-links">
        <li><a href="/collections/all">All Silhouettes</a></li>
        <li><a href="/collections/co-ord-sets">Co-ord Sets</a></li>
        <li><a href="/collections/festive-suits">Festive Suits</a></li>
        <li><a href="/collections/dresses">Dresses</a></li>
        <li><a href="/collections/tops">Tops</a></li>
      </ul>
    </nav>

    <div>
      <a href="/" class="brand-logo">{{ shop.name | default: 'MEENU LABEL' }}</a>
      <span class="brand-sub">CHANDIGARH • ESTD 2026</span>
    </div>

    <div class="header-actions">
      <button class="header-btn" onclick="openSizeGuideModal()">📏 Guide</button>
      <button class="header-btn" onclick="toggleCartDrawer()">
        🛍️ Bag <span class="cart-badge">{{ cart.item_count }}</span>
      </button>
    </div>
  </div>
</header>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "header.liquid"), "w", encoding="utf-8") as f:
    f.write(header_liquid)

# hero-editorial.liquid
hero_liquid = """
<section class="hero-section">
  <div class="hero-card">
    <span class="hero-tag">{{ section.settings.tagline }}</span>
    <h1 class="hero-heading">{{ section.settings.heading }}</h1>
    <p class="hero-desc">{{ section.settings.description }}</p>
    <div>
      <a href="{{ section.settings.btn_link }}" class="btn-primary">{{ section.settings.btn_label }}</a>
    </div>
  </div>

  <div class="hero-media">
    {% if section.settings.hero_image %}
      <img src="{{ section.settings.hero_image | image_url: width: 1200 }}" alt="{{ section.settings.heading }}">
    {% else %}
      <div style="background: #EFE8DC; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-family: 'Cormorant Garamond', serif; font-size: 28px; color: #8A7E70;">
        MEENU LABEL DEBUT HERO
      </div>
    {% endif %}
  </div>
</section>

{% schema %}
{
  "name": "Editorial Hero",
  "settings": [
    {
      "type": "text",
      "id": "tagline",
      "label": "Tagline",
      "default": "Debut Collection • Drop 01"
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Effortless Everyday Luxury Silhouettes"
    },
    {
      "type": "textarea",
      "id": "description",
      "label": "Description",
      "default": "Crafted in pure breathable cottons, fluid chanderi silks, and textured dobby chiffons. Tailored in Chandigarh for the modern woman who refuses to compromise between comfort and elegance."
    },
    {
      "type": "image_picker",
      "id": "hero_image",
      "label": "Hero Image"
    },
    {
      "type": "text",
      "id": "btn_label",
      "label": "Button Label",
      "default": "EXPLORE DROP 01 →"
    },
    {
      "type": "url",
      "id": "btn_link",
      "label": "Button Link",
      "default": "/collections/all"
    }
  ],
  "presets": [
    {
      "name": "Editorial Hero"
    }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "hero-editorial.liquid"), "w", encoding="utf-8") as f:
    f.write(hero_liquid)

# featured-collection.liquid
featured_liquid = """
<section class="catalog-section" id="collection-grid">
  <div class="section-header">
    <div>
      <h2 class="section-title">{{ section.settings.title }}</h2>
      <p style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">{{ section.settings.subtitle }}</p>
    </div>
  </div>

  <div class="product-grid">
    {% assign collection = section.settings.collection %}
    {% if collection != blank and collection.products_count > 0 %}
      {% for product in collection.products limit: section.settings.products_to_show %}
        {% render 'product-card', product: product %}
      {% endfor %}
    {% else %}
      {% for i in (1..4) %}
        <div class="product-card">
          <div class="card-thumb" style="display:flex; align-items:center; justify-content:center; color:#9B9387;">Catalog Silhouette</div>
          <div class="card-body">
            <span class="card-title">Debut Silhouette #{{ i }}</span>
            <div class="card-price-row"><span class="price-main">₹1,499</span></div>
          </div>
        </div>
      {% endfor %}
    {% endif %}
  </div>
</section>

{% schema %}
{
  "name": "Featured Collection",
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Title",
      "default": "Signature Silhouettes"
    },
    {
      "type": "text",
      "id": "subtitle",
      "label": "Subtitle",
      "default": "Authentic catalog pieces ordered from Surat. Strictly 3 exclusive pieces per design (M, L, XL)."
    },
    {
      "type": "collection",
      "id": "collection",
      "label": "Collection"
    },
    {
      "type": "range",
      "id": "products_to_show",
      "min": 4,
      "max": 16,
      "step": 1,
      "default": 16,
      "label": "Products to show"
    }
  ],
  "presets": [
    {
      "name": "Featured Collection"
    }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "featured-collection.liquid"), "w", encoding="utf-8") as f:
    f.write(featured_liquid)

# main-product.liquid
main_product_liquid = """
<section style="max-width: 1200px; margin: 40px auto; padding: 0 40px; display: grid; grid-template-columns: 1fr 1fr; gap: 50px;">
  <div style="border-radius: 12px; overflow: hidden; border: 1px solid var(--border-color); background: #F4EFEB;">
    {% if product.featured_image %}
      <img src="{{ product.featured_image | image_url: width: 1000 }}" alt="{{ product.title }}" style="width: 100%; height: auto; display: block;">
    {% endif %}
  </div>

  <div>
    <span style="font-size: 11px; font-weight: 700; color: var(--accent-rose); letter-spacing: 0.1em; text-transform: uppercase;">
      🔥 ONLY 1 PIECE LEFT PER SIZE
    </span>
    <h1 style="font-family: 'Cormorant Garamond', serif; font-size: 38px; font-weight: 600; margin: 8px 0 4px;">{{ product.title }}</h1>
    <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">SKU: {{ product.selected_or_first_available_variant.sku }}</div>

    <div style="display: flex; align-items: baseline; gap: 12px; padding: 14px 0; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); margin-bottom: 24px;">
      <span style="font-size: 26px; font-weight: 700;">{{ product.price | money }}</span>
      {% if product.compare_at_price > product.price %}
        <span style="font-size: 16px; text-decoration: line-through; color: var(--text-muted);">{{ product.compare_at_price | money }}</span>
        <span style="font-size: 11px; font-weight: 700; color: var(--accent-green); background: #EBF7EE; padding: 3px 8px; border-radius: 4px;">40% OFF</span>
      {% endif %}
    </div>

    <!-- Size Selector -->
    <div style="margin-bottom: 20px;">
      <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 12px; font-weight: 700;">
        <span>SELECT SIZE (INDIAN BUST MEASUREMENTS)</span>
        <a href="javascript:void(0)" onclick="openSizeGuideModal()" style="color: var(--accent-gold);">📏 Size Chart</a>
      </div>
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
        {% for variant in product.variants %}
          <div style="border: 1.5px solid var(--border-color); padding: 10px; border-radius: 6px; text-align: center; cursor: pointer;">
            <strong>{{ variant.title }}</strong>
            <span style="display:block; font-size: 10px; color: var(--accent-rose);">Only 1 Left!</span>
          </div>
        {% endfor %}
      </div>
    </div>

    <!-- Pincode Checker -->
    <div style="background: #FAF5ED; padding: 14px; border-radius: 8px; margin-bottom: 24px; border: 1px solid var(--border-color);">
      <div style="font-size: 12px; font-weight: 700; margin-bottom: 6px;">📍 Check Tricity Express Delivery</div>
      <div style="display: flex; gap: 8px;">
        <input type="text" id="pdpPincode" placeholder="Enter 6-digit Pincode" maxlength="6" style="padding: 8px; border: 1px solid var(--border-color); border-radius: 4px; flex: 1;">
        <button class="btn-primary" style="padding: 8px 14px;" onclick="checkTricityPincode(document.getElementById('pdpPincode').value)">Check</button>
      </div>
      <div id="PincodeResult" style="font-size: 12px; margin-top: 6px; font-weight: 600;"></div>
    </div>

    <!-- Shopify Product Form -->
    {% form 'product', product %}
      <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
      <button type="submit" class="btn-primary" style="width: 100%; padding: 16px; margin-bottom: 10px;">ADD TO BAG 🛍️</button>
    {% endform %}

    <!-- Direct WhatsApp Order -->
    <a href="https://wa.me/{{ settings.whatsapp_number }}?text=Hi%20Meenu%20Label!%20I%20would%20like%20to%20order%20{{ product.title | url_encode }}" target="_blank" style="display: block; text-align: center; background: #E8F5E9; color: #1B5E20; border: 1px solid #C8E6C9; padding: 13px; border-radius: 6px; font-weight: 700; text-decoration: none;">
      💬 Order Directly via WhatsApp
    </a>
    <div class="whatsapp-benefit-box">
      <span class="wa-icon">&#128172;</span>
      <div>
        <strong>Shoppers with size doubts, customization questions, or first-time hesitation:</strong>
        Chat directly with our Chandigarh atelier stylist to verify exact measurements, request custom sleeve/kurta length, or view unedited daylight fabric videos before ordering.
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Product Main",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "main-product.liquid"), "w", encoding="utf-8") as f:
    f.write(main_product_liquid)

# value-props.liquid
value_liquid = """
<div class="value-strip">
  <div class="value-inner">
    <div class="value-item">
      <div class="value-icon">⚡</div>
      <div>
        <div class="value-title">Tricity 24-Hr Express Dispatch</div>
        <div class="value-desc">Priority same-day packing & next-day delivery in Chandigarh, Mohali, and Panchkula.</div>
      </div>
    </div>
    <div class="value-item">
      <div class="value-icon">🌿</div>
      <div>
        <div class="value-title">100% Breathable Fabrics</div>
        <div class="value-desc">Pure cottons, chanderi silks & dobby chiffons tested for long working days.</div>
      </div>
    </div>
    <div class="value-item">
      <div class="value-icon">📏</div>
      <div>
        <div class="value-title">True-to-Size M, L, XL Fits</div>
        <div class="value-desc">Standard Indian bust measurements (38", 40", 42") tailored to flatter your silhouette.</div>
      </div>
    </div>
    <div class="value-item">
      <div class="value-icon">🔄</div>
      <div>
        <div class="value-title">7-Day Easy Size Exchange</div>
        <div class="value-desc">Doorstep size exchange kept pristine in our reusable EVA frosted zipper bags.</div>
      </div>
    </div>
  </div>
</div>

{% schema %}
{
  "name": "Value Propositions",
  "settings": [],
  "presets": [
    {
      "name": "Value Propositions"
    }
  ]
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "value-props.liquid"), "w", encoding="utf-8") as f:
    f.write(value_liquid)

# founder-story.liquid
founder_liquid = """
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
"""
with open(os.path.join(theme_dir, "sections", "founder-story.liquid"), "w", encoding="utf-8") as f:
    f.write(founder_liquid)

# footer.liquid
footer_liquid = """
<footer style="background: #1E1C19; color: #FAF8F5; padding: 60px 40px 24px;">
  <div style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px; padding-bottom: 40px; border-bottom: 1px solid rgba(255,255,255,0.1);">
    <div>
      <h4 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; letter-spacing: 0.15em; margin-bottom: 12px;">MEENU LABEL</h4>
      <p style="font-size: 13px; color: #A8A095; line-height: 1.6; max-width: 400px;">
        Contemporary Indian ethnic wear & modern fusion silhouettes. Independent Luxury Ethnic Label, Chandigarh.
      </p>
    </div>
    <div>
      <h5 style="font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 14px;">Client Care</h5>
      <ul style="list-style: none; font-size: 13px; color: #C0B7AB; line-height: 2;">
        <li><a href="javascript:void(0)" onclick="openSizeGuideModal()" style="color: inherit; text-decoration: none;">Size Chart (M-XL)</a></li>
        <li><a href="mailto:{{ settings.contact_email }}" style="color: inherit; text-decoration: none;">{{ settings.contact_email }}</a></li>
        <li><a href="https://wa.me/{{ settings.whatsapp_number }}" style="color: inherit; text-decoration: none;">WhatsApp Concierge</a></li>
      </ul>
    </div>
    <div>
      <h5 style="font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 14px;">Tricity Guarantee</h5>
      <p style="font-size: 12px; color: #A8A095; line-height: 1.6;">
        Express 24-hr priority dispatch across Chandigarh, Mohali & Panchkula. Safe contactless delivery.
      </p>
    </div>
  </div>
  <div style="max-width: 1400px; margin: 20px auto 0; font-size: 11px; color: #7A7267; text-align: center;">
    © {{ 'now' | date: '%Y' }} Meenu Label. Official Store: meenulabel.com
  </div>
</footer>

{% schema %}
{
  "name": "Footer",
  "settings": []
}
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "footer.liquid"), "w", encoding="utf-8") as f:
    f.write(footer_liquid)

# campaign-edit.liquid
campaign_liquid = """
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
          <img src="{{ 'campaign_cafe.jpg' | asset_url }}" alt="The Royal Wine Chanderi Festive Suit" class="snitch-campaign-img">
          <div class="snitch-campaign-overlay"></div>
          <div class="snitch-campaign-content">
            <span class="snitch-campaign-badge">Editorial Drop Headliner &bull; Garden Verandah</span>
            <h3 class="snitch-campaign-name">The Royal Wine Chanderi Festive Suit</h3>
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
"""
with open(os.path.join(theme_dir, "sections", "campaign-edit.liquid"), "w", encoding="utf-8") as f:
    f.write(campaign_liquid)

# craftsmanship-spotlight.liquid
craftsmanship_liquid = """
<section class="craftsmanship-section">
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
{% endschema %}
"""
with open(os.path.join(theme_dir, "sections", "craftsmanship-spotlight.liquid"), "w", encoding="utf-8") as f:
    f.write(craftsmanship_liquid)


# =========================================================================
# 6. SNIPPETS
# =========================================================================
# product-card.liquid
card_liquid = """
<div class="product-card">
  <div class="card-thumb">
    <span class="card-badge badge-scarcity">ONLY 3 LEFT</span>
    <a href="{{ product.url }}">
      {% if product.featured_image %}
        <img src="{{ product.featured_image | image_url: width: 600 }}" alt="{{ product.title }}">
      {% else %}
        <div style="width: 100%; height: 100%; background: #FAF5ED;"></div>
      {% endif %}
    </a>
  </div>
  <div class="card-body">
    <a href="{{ product.url }}" class="card-title">{{ product.title }}</a>
    <div class="card-price-row">
      <span class="price-main">{{ product.price | money }}</span>
      {% if product.compare_at_price > product.price %}
        <span class="price-mrp">{{ product.compare_at_price | money }}</span>
      {% endif %}
    </div>
    <div class="size-chips">
      <span class="size-chip">M (38)</span>
      <span class="size-chip">L (40)</span>
      <span class="size-chip">XL (42)</span>
    </div>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "product-card.liquid"), "w", encoding="utf-8") as f:
    f.write(card_liquid)

# nav-drawer.liquid
nav_drawer_liquid = """
<div class="nav-drawer-backdrop" id="navDrawerBackdrop" onclick="closeNavDrawer()">
  <div class="nav-drawer" id="navDrawer" onclick="event.stopPropagation()">
    <div class="nav-drawer-header">
      <span class="brand-logo" style="font-size:20px;">{{ shop.name | default: 'MEENU LABEL' }}</span>
      <button style="background:none; border:none; font-size:24px; cursor:pointer; color:var(--text-color); padding:4px 8px; line-height:1;" onclick="closeNavDrawer()">&times;</button>
    </div>
    <div class="nav-drawer-body">
      <ul class="nav-drawer-links" style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:16px;">
        <li><a href="/collections/all" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">All Silhouettes</a></li>
        <li><a href="/collections/co-ord-sets" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Co-ord Sets</a></li>
        <li><a href="/collections/festive-suits" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Festive Suits</a></li>
        <li><a href="/collections/dresses" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Midi Dresses</a></li>
        <li><a href="/collections/tops" style="text-decoration:none; color:var(--text-color); font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.08em;">Tops &amp; Blouses</a></li>
        <li style="border-top:1px solid var(--border-color); margin-top:16px; padding-top:16px;">
          <a href="javascript:void(0)" onclick="closeNavDrawer(); openSizeGuideModal();" style="text-decoration:none; color:var(--text-color); font-size:13px;">&#128207; Size &amp; Fit Guide</a>
        </li>
        <li>
          <a href="https://wa.me/919988898845" target="_blank" style="text-decoration:none; color:#25D366; font-size:13px;">&#128172; WhatsApp Concierge (+91 99888 98845)</a>
        </li>
      </ul>
    </div>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "nav-drawer.liquid"), "w", encoding="utf-8") as f:
    f.write(nav_drawer_liquid)

# snitch-login-modal.liquid
snitch_login_liquid = """
<div class="snitch-login-backdrop" id="accountModalBackdrop" onclick="closeAccountModal(event)">
  <div class="snitch-login-dialog" onclick="event.stopPropagation()">
    <!-- Top Action Buttons -->
    <button class="snitch-dialog-back" onclick="closeAccountModalDirect()" title="Back to Store" aria-label="Back">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
    </button>
    <button class="snitch-dialog-close" onclick="closeAccountModalDirect()" title="Close" aria-label="Close">&times;</button>

    <!-- Left Column: Editorial Campaign -->
    <div class="snitch-login-campaign">
      <img src="{{ 'hero_2_gulabi.jpg' | asset_url }}" alt="{{ shop.name }}" class="snitch-campaign-photo">
      <div class="snitch-campaign-vignette"></div>
      <div class="snitch-campaign-text">
        <div class="snitch-campaign-pill">Signature Silhouettes</div>
        <h2 class="snitch-campaign-headline">
          WEAR WHAT'S <span class="snitch-headline-accent">TIMELESS</span>
        </h2>
        <p class="snitch-campaign-atelier">Chandigarh Atelier &bull; Handcrafted Pure Silks</p>
      </div>
    </div>

    <!-- Right Column: Snitch Dark Card -->
    <div class="snitch-login-content">
      <div class="snitch-login-card">
        <!-- Step 1: Mobile Input -->
        <div id="loginStepPhone">
          <div class="snitch-brand-block">
            <h2 class="snitch-brand-title">{{ shop.name | default: 'MEENU LABEL' }}</h2>
            <div class="snitch-brand-tag">CHANDIGARH &bull; LUXURY ETHNIC</div>
          </div>

          <label class="snitch-input-heading" for="snitchMobileInput">ENTER MOBILE NUMBER</label>
          <div class="snitch-input-row" id="snitchPhoneRow">
            <div class="snitch-cc-badge">+91</div>
            <input 
              type="tel" 
              id="snitchMobileInput" 
              class="snitch-mobile-field" 
              placeholder="99999 99999" 
              maxlength="10" 
              autocomplete="tel"
              oninput="onSnitchPhoneInput(this)" 
              onkeydown="if(event.key==='Enter') requestSnitchOtp()"
            >
          </div>
          <div id="snitchPhoneError" class="snitch-validation-error">Please enter a valid 10-digit mobile number</div>

          <button class="snitch-submit-btn" id="snitchSendOtpBtn" onclick="requestSnitchOtp()">
            <span>SEND OTP</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>

          <p class="snitch-legal-note">
            By continuing, you agree to {{ shop.name | default: 'MEENU LABEL' }}'s 
            <a href="/policies/terms-of-service">Terms &amp; Conditions</a> and 
            <a href="/policies/privacy-policy">Privacy Policy</a>
          </p>
        </div>

        <!-- Step 2: OTP Verification -->
        <div id="loginStepOtp" style="display:none;">
          <div class="snitch-brand-block" style="margin-bottom: 20px;">
            <h2 class="snitch-brand-title" style="font-size: 20px;">VERIFY OTP</h2>
            <div class="snitch-otp-sent-info">
              Code sent to <strong id="snitchOtpPhoneDisplay" style="color:#fff;">+91 99999 99999</strong>
              <button type="button" class="snitch-edit-phone-btn" onclick="snitchEditPhone()">Edit</button>
            </div>
          </div>

          <div class="snitch-otp-grid">
            <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp1" oninput="snitchOtpNext(this, 'sOtp2')" onkeydown="snitchOtpBack(event, this, null)">
            <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp2" oninput="snitchOtpNext(this, 'sOtp3')" onkeydown="snitchOtpBack(event, this, 'sOtp1')">
            <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp3" oninput="snitchOtpNext(this, 'sOtp4')" onkeydown="snitchOtpBack(event, this, 'sOtp2')">
            <input type="text" maxlength="1" class="snitch-digit-box" id="sOtp4" oninput="snitchOtpNext(this, null)" onkeydown="snitchOtpBack(event, this, 'sOtp3')">
          </div>

          <div class="snitch-resend-bar">
            <span id="snitchTimerTxt">Resend OTP in <strong id="snitchCountdown" style="color:#bbb;">0:28</strong></span>
            <button type="button" id="snitchResendBtn" class="snitch-resend-action" style="display:none;" onclick="snitchResendOtp()">Resend OTP via SMS / WhatsApp</button>
          </div>

          <button class="snitch-submit-btn" onclick="verifySnitchOtp()">
            <span>VERIFY &amp; PROCEED</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>

          <div class="snitch-demo-badge">&bull; Demo Mode: Type any 4 digits (e.g. 1 2 3 4) to verify</div>
        </div>

        <!-- Step 3: VIP Privé Member Dashboard -->
        <div id="loginStepVip" style="display:none; text-align:center;">
          <div class="snitch-vip-avatar">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <div class="snitch-vip-status-tag">&#10024; ATELIER PRIV&Eacute; VIP MEMBER</div>
          <h3 class="snitch-vip-user" id="snitchVipUserDisplay">+91 99888 98845</h3>
          <div class="snitch-vip-perks">
            <div class="snitch-perk-item">
              <div class="snitch-perk-icon">&#128666;</div>
              <div class="snitch-perk-text">
                <strong>Free 24-Hr Tricity Delivery</strong>
                <span>Sector 17 Chandigarh Atelier Express Dispatch</span>
              </div>
            </div>
            <div class="snitch-perk-item">
              <div class="snitch-perk-icon">&#128087;</div>
              <div class="snitch-perk-text">
                <strong>VIP Atelier Fittings</strong>
                <span>Private suite fitting bookings in Chandigarh</span>
              </div>
            </div>
          </div>

          <div class="snitch-vip-actions">
            <button class="snitch-submit-btn" style="margin-bottom: 12px;" onclick="closeAccountModalDirect()">
              <span>CONTINUE SHOPPING</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
            <a href="https://wa.me/919988898845?text=Hi%20Meenu%20Label%2C%20I%20am%20a%20VIP%20member." target="_blank" class="snitch-vip-concierge-btn">
              &#128172; Open Stylist WhatsApp Concierge
            </a>
            <button type="button" class="snitch-signout-btn" onclick="signOutSnitchUser()">Sign Out / Change Account</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "snitch-login-modal.liquid"), "w", encoding="utf-8") as f:
    f.write(snitch_login_liquid)

# cart-drawer.liquid
drawer_liquid = """
<div class="cart-drawer-backdrop" id="CartBackdrop" onclick="toggleCartDrawer()"></div>
<div class="cart-drawer" id="CartDrawer">
  <div class="cart-header">
    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px;">Your Shopping Bag ({{ cart.item_count }})</h3>
    <button onclick="toggleCartDrawer()" style="background: none; border: none; font-size: 20px; cursor: pointer;">✕</button>
  </div>
  <div class="cart-items">
    {% if cart.item_count > 0 %}
      {% for item in cart.items %}
        <div style="display: flex; gap: 12px; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--border-color);">
          <img src="{{ item.image | image_url: width: 150 }}" style="width: 70px; height: 90px; object-fit: cover; border-radius: 4px;">
          <div style="flex: 1;">
            <div style="font-size: 13px; font-weight: 700;">{{ item.product.title }}</div>
            <div style="font-size: 11px; color: var(--text-muted);">Size: {{ item.variant.title }} • Qty: {{ item.quantity }}</div>
            <div style="font-size: 13px; font-weight: 700; margin-top: 4px;">{{ item.final_line_price | money }}</div>
          </div>
        </div>
      {% endfor %}
    {% else %}
      <div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">
        Your bag is currently empty.
      </div>
    {% endif %}
  </div>
  <div class="cart-footer">
    <div style="display: flex; justify-content: space-between; font-weight: 700; font-size: 16px; margin-bottom: 14px;">
      <span>Subtotal</span>
      <span>{{ cart.total_price | money }}</span>
    </div>
    <a href="/checkout" class="btn-primary" style="width: 100%; text-align: center; display: block;">PROCEED TO CHECKOUT 🔒</a>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "cart-drawer.liquid"), "w", encoding="utf-8") as f:
    f.write(drawer_liquid)

# size-guide-modal.liquid
guide_liquid = """
<div id="SizeGuideModal" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); z-index: 500; align-items: center; justify-content: center; padding: 20px;">
  <div style="background: #FFF; border-radius: 12px; max-width: 580px; width: 100%; padding: 32px; position: relative;">
    <button onclick="closeSizeGuideModal()" style="position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 18px; cursor: pointer;">✕</button>
    <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 26px; margin-bottom: 6px;">Meenu Label Standard Size Chart</h3>
    <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 16px;">All measurements in inches. True to standard Indian fit.</p>
    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: center; margin-bottom: 16px;">
      <thead>
        <tr style="background: #FAF5ED;">
          <th style="padding: 8px; border: 1px solid var(--border-color);">Size</th>
          <th style="padding: 8px; border: 1px solid var(--border-color);">Bust</th>
          <th style="padding: 8px; border: 1px solid var(--border-color);">Waist</th>
          <th style="padding: 8px; border: 1px solid var(--border-color);">Hip</th>
        </tr>
      </thead>
      <tbody>
        <tr><td style="padding: 8px; border: 1px solid var(--border-color);"><strong>M (38)</strong></td><td style="border: 1px solid var(--border-color);">38"</td><td style="border: 1px solid var(--border-color);">34"</td><td style="border: 1px solid var(--border-color);">41"</td></tr>
        <tr><td style="padding: 8px; border: 1px solid var(--border-color);"><strong>L (40)</strong></td><td style="border: 1px solid var(--border-color);">40"</td><td style="border: 1px solid var(--border-color);">36"</td><td style="border: 1px solid var(--border-color);">43"</td></tr>
        <tr><td style="padding: 8px; border: 1px solid var(--border-color);"><strong>XL (42)</strong></td><td style="border: 1px solid var(--border-color);">42"</td><td style="border: 1px solid var(--border-color);">38"</td><td style="border: 1px solid var(--border-color);">45"</td></tr>
      </tbody>
    </table>
    <div style="background: #FAF8F5; padding: 10px; border-radius: 6px; font-size: 11px; color: var(--text-muted);">
      💡 <strong>Fit Tip:</strong> True-to-size. For wrap dresses, the tie-belt allows customized waist cinching.
    </div>
  </div>
</div>
"""
with open(os.path.join(theme_dir, "snippets", "size-guide-modal.liquid"), "w", encoding="utf-8") as f:
    f.write(guide_liquid)

# =========================================================================
# 7. TEMPLATES (JSON)
# =========================================================================
index_json = {
    "sections": {
        "hero": {"type": "hero-editorial", "settings": {}},
        "collection": {"type": "featured-collection", "settings": {}},
        "values": {"type": "value-props", "settings": {}},
        "founder": {"type": "founder-story", "settings": {}},
        "campaign_edit": {"type": "campaign-edit", "settings": {}},
        "craftsmanship": {"type": "craftsmanship-spotlight", "settings": {}}
    },
    "order": ["hero", "campaign_edit", "craftsmanship", "collection", "values", "founder"]
}
with open(os.path.join(theme_dir, "templates", "index.json"), "w", encoding="utf-8") as f:
    json.dump(index_json, f, indent=2)

product_json = {
    "sections": {
        "main": {"type": "main-product", "settings": {}}
    },
    "order": ["main"]
}
with open(os.path.join(theme_dir, "templates", "product.json"), "w", encoding="utf-8") as f:
    json.dump(product_json, f, indent=2)

for t in ["collection", "cart", "404"]:
    with open(os.path.join(theme_dir, "templates", f"{t}.json"), "w", encoding="utf-8") as f:
        json.dump({"sections": {}, "order": []}, f, indent=2)

print("Shopify Theme Files written successfully!")


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

# =========================================================================
# 8. ZIP PACKAGING
# =========================================================================
zip_path = os.path.join(downloads_dir, "Meenu_Label_Shopify_Theme.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, rel_path)

print(f"Created ready-to-upload ZIP: {zip_path}")
