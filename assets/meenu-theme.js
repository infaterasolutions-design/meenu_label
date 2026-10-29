
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
