
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
  el.value = el.value.replace(/\D/g, '');
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
  curr.value = curr.value.replace(/\D/g, '');
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
  bar.classList.toggle('open');
  if (bar.classList.contains('open')) {
    var inp = document.getElementById('searchInput');
    if (inp) {
      setTimeout(function() { inp.focus(); }, 120);
    }
  }
}

// --- Store Policy Modal Controls (Client Care) ---
var STORE_POLICIES = {
  about: {
    title: "About Us • The Meenu Label Story",
    html: "<h3>Handcrafted in Chandigarh. Inspired by Grace.</h3><p>Meenu Label is a contemporary designer pret atelier born in Chandigarh, dedicated to crafting breathable, modern silhouettes for women across India.</p><p>The label was founded by Sandeep Singh and named with deep affection after his sister, <strong>Meenu</strong>—embodying a family commitment to thoughtfulness, warmth, and artisanal integrity.</p><h3>Why We Exist</h3><p>For too long, modern women in India have had to settle between stiff, synthetic fast-fashion that wrinkles in hours, or heavy, uncomfortable traditional wear that cannot be worn beyond a single festive celebration.</p><p>We created <strong>Meenu Label</strong> to provide an effortless middle ground:</p><ul><li><strong>100% Pure, Breathable Textiles:</strong> We work exclusively with rich Jaipur cottons, soft muslins, fluid silk crepes, and authentic Chanderi silks. Zero synthetic friction.</li><li><strong>Thoughtful, Functional Tailoring:</strong> Every bottom silhouette features deep, functional pockets that securely hold your smartphone. Tunics and kurtas feature relaxed comfort waistbands and modest, flattering hemlines designed for all-day ease.</li><li><strong>Strict Atelier Scarcity:</strong> We reject mass factory production. Drop 01 is produced in strictly small batches (only 3 pieces per size nationwide) to preserve individuality and minimize textile waste.</li></ul><p><em>From morning work meetings and cafe brunches to intimate evening celebrations, Meenu Label pieces are made to move with you in effortless grace.</em></p>"
  },
  shipping: {
    title: "Shipping & Delivery Policy",
    html: "<h3>Pan-India Priority Dispatch</h3><p>Every Meenu Label garment is hand-inspected, steam-pressed, wrapped in protective butter paper, and packed in our signature atelier box before dispatch from our Chandigarh warehouse.</p><h3>Delivery Timelines</h3><ul><li><strong>Chandigarh Tricity (Chandigarh, Mohali, Panchkula):</strong> 24 to 48 Hours Priority Express Delivery.</li><li><strong>Metro Cities (Delhi-NCR, Mumbai, Bengaluru, Jaipur, Hyderabad, Pune, Kolkata):</strong> 2 to 4 Business Days.</li><li><strong>Rest of India:</strong> 3 to 6 Business Days across 26,000+ serviceable pincodes.</li></ul><h3>Shipping Charges</h3><ul><li><strong>Prepaid Orders (UPI, GPay, PhonePe, Cards, NetBanking):</strong> 100% FREE Express Delivery across India.</li><li><strong>Prepaid Perk:</strong> Enjoy instant ₹100 discount auto-applied at checkout on all online payments with code <strong>UPI100</strong>.</li></ul><h3>Cash on Delivery (COD) Terms</h3><p>Cash on Delivery is available across all serviceable Indian pincodes. To prevent transit cancellations, all COD orders undergo automated WhatsApp / Phone verification prior to dispatch.</p><h3>Order Tracking</h3><p>As soon as your package is dispatched, you will receive an automated tracking link via SMS & WhatsApp to monitor live doorstep delivery.</p>"
  },
  exchange: {
    title: "Atelier Sizing Guarantee & Exchange Terms",
    html: "<h3>7-Day Hassle-Free Doorstep Exchange</h3><p>At Meenu Label, we want your silhouette to fit like it was custom-tailored for you. If your piece doesn't fit exactly as desired, we offer a seamless <strong>7-Day Doorstep Size Exchange</strong>.</p><h3>How Exchange Works</h3><ol><li><strong>Initiate:</strong> Send a WhatsApp message to our Concierge Team at <strong>+91 99888 98845</strong> with your Order Number and desired replacement size (M, L, or XL).</li><li><strong>Doorstep Pickup:</strong> Our courier partner will arrive at your address to inspect and pick up the original garment.</li><li><strong>Priority Re-dispatch:</strong> Your fresh replacement piece will be dispatched immediately with zero extra delivery charges.</li></ol><h3>Eligibility Conditions</h3><ul><li>Garment must be unworn, unwashed, and undamaged with all original atelier brand tags intact.</li><li>Must be returned in the original reusable EVA zipper pouch provided.</li><li>Exchange request must be submitted within 7 calendar days of delivery.</li></ul>"
  },
  privacy: {
    title: "Privacy Policy & Terms of Service",
    html: "<h3>Your Privacy is Sacred</h3><p>Meenu Label (operating as a sole proprietorship based in Chandigarh, India) is committed to protecting your personal data in full compliance with Indian Information Technology regulations.</p><h3>Information We Collect</h3><ul><li><strong>Account Details:</strong> Name, contact phone number, and delivery address to fulfill your orders.</li><li><strong>Payment Privacy:</strong> We DO NOT store debit/credit card numbers or UPI PINs. All payments are processed through 256-Bit SSL encrypted, PCI-DSS Level 1 compliant gateways.</li><li><strong>Communication:</strong> Order confirmation, dispatch notifications, and sizing support via SMS and WhatsApp.</li></ul><h3>No Third-Party Sharing</h3><p>We strictly never rent, sell, or trade our client list with external marketing agencies or data brokers. Your information remains confidential with Meenu Label.</p>"
  },
  contact: {
    title: "Contact Us & Customer Care Concierge",
    html: "<h3>Chandigarh Atelier & Client Concierge</h3><p>We are delighted to assist you with sizing advice, custom styling recommendations, or order inquiries.</p><ul><li><strong>WhatsApp Concierge (Fastest Response):</strong> <a href='https://wa.me/919988898845' target='_blank' style='color:#25D366; font-weight:700;'>+91 99888 98845</a> (10:00 AM – 7:00 PM IST, Monday to Saturday)</li><li><strong>Official Email Support:</strong> <a href='mailto:support@meenulabel.com' style='color:#6E1A24; font-weight:700;'>support@meenulabel.com</a></li><li><strong>Atelier Headquarters:</strong> Meenu Label, Chandigarh Tricity, Punjab & Haryana, India</li><li><strong>Official Domain:</strong> <a href='https://meenulabel.com' target='_blank'>meenulabel.com</a> / <a href='https://meenulabel.in' target='_blank'>meenulabel.in</a></li></ul>"
  }
};

function openPolicyModal(type) {
  var pol = STORE_POLICIES[type] || STORE_POLICIES.about;
  var titleEl = document.getElementById('policyModalTitle');
  var contentEl = document.getElementById('policyModalContent');
  var backdrop = document.getElementById('policyModalBackdrop');
  if (titleEl) titleEl.textContent = pol.title;
  if (contentEl) contentEl.innerHTML = pol.html;
  if (backdrop) backdrop.classList.add('open');
}

function closePolicyModal() {
  var backdrop = document.getElementById('policyModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
}

function closePolicyModalOnBackdrop(e) {
  if (e.target.id === 'policyModalBackdrop') {
    closePolicyModal();
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var heroEl = document.getElementById('heroSlider');
  if (heroEl) {
    heroEl.addEventListener('mouseenter', stopAutoSlide);
    heroEl.addEventListener('mouseleave', startAutoSlide);
    startAutoSlide();
  }
});
