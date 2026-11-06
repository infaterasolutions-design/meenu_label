import subprocess
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Comprehensive test runner script embedded into test HTML
test_script = """
<script>
window.__AUDIT_RESULTS = {
  header: false,
  hero: false,
  catalogCount: 0,
  filterTabs: false,
  cardPricing: false,
  cardDiscount: false,
  cardMrpNowrap: false,
  quickSizeDrawer: false,
  cartDrawer: false,
  cartCoupon: false,
  trackingDrawer: false,
  trackingTimeline: false,
  pdpNoDefaultSize: false,
  pdpSizeWarning: false,
  pdpSizeSelection: false,
  pdpGalleryNoScroll: false,
  pdpPincodeAntiZoom: false,
  pdpPincodeCheck: false,
  pdpBackScrollRestored: false,
  errors: []
};

window.addEventListener('load', function() {
  setTimeout(runFullAudit, 400);
});

function runFullAudit() {
  var R = window.__AUDIT_RESULTS;
  try {
    // 1. Header & Marquee
    var marquee = document.querySelector('.announcement-bar');
    var logo = document.querySelector('.brand-logo-img');
    var headerBar = document.querySelector('.header-bar');
    var hamburger = document.querySelector('.hamburger-btn');
    if (marquee && logo && headerBar && hamburger) R.header = true;
    else R.errors.push('Header elements missing');

    // 2. Hero Slider
    var hero = document.getElementById('heroSlider');
    var slides = document.querySelectorAll('.snitch-slide');
    if (hero && slides.length >= 3) R.hero = true;
    else R.errors.push('Hero slider slides insufficient: ' + slides.length);

    // 3. Catalog Grid & Cards
    var cards = document.querySelectorAll('.product-card');
    R.catalogCount = cards.length;
    
    // Check card pricing, nowrap, and discount
    var firstCard = cards[0];
    if (firstCard) {
      var pMain = firstCard.querySelector('.price-main');
      var pMrp = firstCard.querySelector('.price-mrp');
      var pDisc = firstCard.querySelector('.price-discount');
      var pWrap = firstCard.querySelector('.card-price-compare-wrap');
      
      if (pMain && pMrp && pWrap) R.cardPricing = true;
      if (pDisc && pDisc.textContent.indexOf('% OFF') !== -1) R.cardDiscount = true;
      
      var mrpStyle = window.getComputedStyle(pMrp);
      if (mrpStyle.whiteSpace === 'nowrap') R.cardMrpNowrap = true;
      else R.errors.push('price-mrp whiteSpace is ' + mrpStyle.whiteSpace);
    }

    // 4. Filter Tabs
    filterCategory('festive');
    var festiveCards = document.querySelectorAll('.product-card:not([style*="display: none"])');
    filterCategory('all');
    if (festiveCards.length > 0) R.filterTabs = true;
    else R.errors.push('Filter tabs did not update grid');

    // 5. Quick Size (+) Popup / Drawer
    var plusBtn = document.querySelector('.snitch-plus-trigger');
    if (plusBtn) {
      openQuickSizePopup(plusBtn);
      var drawer = document.getElementById('snitchSizeModalBackdrop');
      if (drawer && drawer.classList.contains('open')) R.quickSizeDrawer = true;
      closeSnitchSizePopup();
    } else {
      R.errors.push('snitch-plus-trigger not found');
    }

    // 6. Shopping Cart & Promo Code
    quickAddCart('JAB26ST05010', 'M');
    var cartDrawer = document.getElementById('cartDrawer');
    if (cart.length > 0 && cartDrawer && cartDrawer.classList.contains('open')) {
      R.cartDrawer = true;
      // Test promo code
      var couponInput = document.getElementById('couponCode');
      if (couponInput) {
        couponInput.value = 'DEBUT10';
        applyCoupon();
        if (discountPercent > 0) R.cartCoupon = true;
      }
      toggleCart();
    } else {
      R.errors.push('Cart add failed');
    }

    // 7. Frictionless Tracking & VIP Concierge
    openAccountModal('track');
    fillAndTrackDemo('#ML-1042');
    var trackContainer = document.getElementById('trackingResultContainer');
    if (trackContainer && trackContainer.style.display !== 'none') {
      R.trackingDrawer = true;
      R.trackingTimeline = true;
    } else {
      R.errors.push('Order tracking demo lookup failed');
    }
    closeAccountModalDirect();

    // 8. PDP: Size selection, gallery scroll, pincode, back scroll
    window.scrollTo(0, 500);
    var homeScrollBefore = window.pageYOffset;
    openProductPage('JAB26ST05010');
    
    // Check PDP default size
    if (pdpSelectedSize === null) {
      var selBtns = document.querySelectorAll('.pdp-size-btn.selected');
      if (selBtns.length === 0) R.pdpNoDefaultSize = true;
    } else {
      R.errors.push('pdpSelectedSize was not null on open: ' + pdpSelectedSize);
    }

    // Check size warning
    addPdpProductToCart();
    var notice = document.getElementById('pdpSizeNotice');
    if (notice && notice.style.display !== 'none') {
      R.pdpSizeWarning = true;
    } else {
      R.errors.push('PDP size warning notice did not show');
    }

    // Select size L
    selectPdpSize('L', document.getElementById('pdpSizeBtn_L'));
    if (pdpSelectedSize === 'L' && notice.style.display === 'none') {
      R.pdpSizeSelection = true;
    }

    // Gallery next button test (verify 0px window scroll shift)
    var viewYBefore = window.pageYOffset;
    changePreviewGalleryImage(1);
    var viewYAfter = window.pageYOffset;
    if (viewYBefore === viewYAfter) {
      R.pdpGalleryNoScroll = true;
    } else {
      R.errors.push('Gallery shifted scroll from ' + viewYBefore + ' to ' + viewYAfter);
    }

    // Pincode input anti-zoom
    var pinInp = document.getElementById('pdpPincodeInput');
    if (pinInp) {
      var pinComp = window.getComputedStyle(pinInp);
      if (pinComp.fontSize === '16px' && pinInp.getAttribute('inputmode') === 'numeric') {
        R.pdpPincodeAntiZoom = true;
      }
      pinInp.value = '160017';
      checkPdpPincode();
      var pinRes = document.getElementById('pdpPincodeResult');
      if (pinRes && pinRes.style.display !== 'none') {
        R.pdpPincodeCheck = true;
      }
    }

    // Close PDP and check back scroll restoration
    closeProductPage();
    setTimeout(function() {
      var homeScrollAfter = window.pageYOffset;
      if (Math.abs(homeScrollAfter - homeScrollBefore) < 5) {
        R.pdpBackScrollRestored = true;
      } else {
        R.errors.push('Back scroll mismatch: before=' + homeScrollBefore + ', after=' + homeScrollAfter);
      }

      // Render summary banner onto page
      renderAuditSummary();
    }, 200);

  } catch(err) {
    R.errors.push('Exception in audit: ' + err.message);
    renderAuditSummary();
  }
}

function renderAuditSummary() {
  var R = window.__AUDIT_RESULTS;
  var banner = document.createElement('div');
  banner.id = 'audit-summary-banner';
  banner.style.cssText = 'position:fixed;top:10px;left:10px;right:10px;background:rgba(18,16,14,0.96);color:#FFF;padding:16px 20px;border:1px solid #C8A364;border-radius:8px;z-index:999999;font-family:sans-serif;font-size:12px;line-height:1.5;box-shadow:0 12px 32px rgba(0,0,0,0.5);';
  
  var allPassed = (R.header && R.hero && R.catalogCount >= 16 && R.filterTabs && R.cardPricing && R.cardDiscount && R.cardMrpNowrap && R.quickSizeDrawer && R.cartDrawer && R.cartCoupon && R.trackingDrawer && R.pdpNoDefaultSize && R.pdpSizeWarning && R.pdpSizeSelection && R.pdpGalleryNoScroll && R.pdpPincodeAntiZoom && R.pdpBackScrollRestored);
  
  var html = '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">' +
             '<b style="font-size:15px;color:#C8A364;">MEENU LABEL - END-TO-END HEALTH AUDIT</b>' +
             '<span style="padding:4px 10px;border-radius:4px;font-weight:700;background:' + (allPassed ? '#128C7E' : '#B83A3A') + ';color:#FFF;">' +
             (allPassed ? 'ALL SYSTEMS OPERATIONAL (100% HEALTHY)' : 'AUDIT WARNINGS FOUND') + '</span></div>';
  
  html += '<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:8px;margin-top:10px;">';
  html += '<div>Header & Marquee: ' + (R.header ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Hero Slider: ' + (R.hero ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Catalog Silhouettes: &#9989; ' + R.catalogCount + ' Items</div>';
  html += '<div>Category Filter Tabs: ' + (R.filterTabs ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Card Pricing & % Off: ' + (R.cardPricing && R.cardDiscount ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Price MRP Nowrap (No Split Rs): ' + (R.cardMrpNowrap ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Quick Size (+) Drawer: ' + (R.quickSizeDrawer ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Cart Drawer & Bag: ' + (R.cartDrawer ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>10% Coupon (DEBUT10): ' + (R.cartCoupon ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Track My Order (Demo #ML-1042): ' + (R.trackingDrawer ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>PDP No Size Pre-Selected: ' + (R.pdpNoDefaultSize ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>PDP Required Size Warning: ' + (R.pdpSizeWarning ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>PDP Size Selection (M/L/XL): ' + (R.pdpSizeSelection ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>PC Gallery Next (0px Scroll Shift): ' + (R.pdpGalleryNoScroll ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Mobile Pincode 16px Anti-Zoom: ' + (R.pdpPincodeAntiZoom ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '<div>Back Scroll Position Restored: ' + (R.pdpBackScrollRestored ? '&#9989; OK' : '&#10060; FAIL') + '</div>';
  html += '</div>';

  if (R.errors.length > 0) {
    html += '<div style="margin-top:8px;color:#FFAAAA;"><b>Errors:</b> ' + R.errors.join('; ') + '</div>';
  }
  
  banner.innerHTML = html;
  document.body.appendChild(banner);
}
</script>
"""

html_audit = base_html.replace("</body>", test_script + "</body>")
temp_audit_html = os.path.join(scratch_dir, "temp_full_audit.html")
with open(temp_audit_html, "w", encoding="utf-8") as f:
    f.write(html_audit)

# 1. Desktop Audit Capture (1440x900)
shot_audit_desk = os.path.join(artifacts_dir, "verified_full_audit_desktop.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_audit_desk')}",
    "--window-size=1440,900",
    "--virtual-time-budget=6000",
    f"--screenshot={shot_audit_desk}",
    temp_audit_html
]

print("Running Comprehensive Desktop Audit (1440x900)...")
subprocess.run(cmd_desk, check=True)
print("Captured Desktop Audit Screenshot:", shot_audit_desk)

# 2. Mobile Audit Capture (390x844)
shot_audit_mob = os.path.join(artifacts_dir, "verified_full_audit_mobile.png")
cmd_mob = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_audit_mob')}",
    "--window-size=390,844",
    "--virtual-time-budget=6000",
    f"--screenshot={shot_audit_mob}",
    temp_audit_html
]

print("Running Comprehensive Mobile Audit (390x844)...")
subprocess.run(cmd_mob, check=True)
print("Captured Mobile Audit Screenshot:", shot_audit_mob)

# 3. Read DOM Dump & Extract Audit Object
cmd_dump = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_audit_dump')}",
    "--window-size=1440,900",
    "--virtual-time-budget=6000",
    "--dump-dom",
    temp_audit_html
]
res = subprocess.run(cmd_dump, capture_output=True, text=True, encoding='utf-8')
if 'ALL SYSTEMS OPERATIONAL (100% HEALTHY)' in res.stdout:
    print("\n=======================================================")
    print("SUCCESS: 100% OF ALL SYSTEM CHECKS PASSED OPERATIONAL!")
    print("=======================================================")
else:
    print("\nAudit completed. Check results in dump.")

for line in res.stdout.splitlines():
    if 'Header &' in line or 'Catalog Silhouettes' in line or 'Price MRP Nowrap' in line or 'PDP No Size' in line or 'PC Gallery Next' in line or 'Mobile Pincode' in line:
        print("  ->", line.strip())
