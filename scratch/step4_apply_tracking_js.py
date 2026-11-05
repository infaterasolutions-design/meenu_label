import sys
sys.stdout.reconfigure(encoding='utf-8')

js_code = """
/* =========================================================================
   TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM
   ========================================================================= */

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
    if (isSnitchLoggedIn()) {
      badge.classList.add('active');
      badge.style.display = 'block';
    } else {
      badge.classList.remove('active');
      badge.style.display = 'none';
    }
  }
}

function switchAccountTab(tabName) {
  var tabTrack = document.getElementById('tabBtnTrack');
  var tabLogin = document.getElementById('tabBtnLogin');
  var viewTrack = document.getElementById('accountViewTrack');
  var viewLogin = document.getElementById('accountViewLogin');

  if (tabTrack) tabTrack.classList.toggle('active', tabName === 'track');
  if (tabLogin) tabLogin.classList.toggle('active', tabName === 'login');

  if (viewTrack) {
    viewTrack.classList.toggle('active', tabName === 'track');
    viewTrack.style.display = tabName === 'track' ? 'block' : 'none';
  }
  if (viewLogin) {
    viewLogin.classList.toggle('active', tabName === 'login');
    viewLogin.style.display = tabName === 'login' ? 'block' : 'none';
  }

  if (tabName === 'track') {
    setTimeout(function() {
      var inp = document.getElementById('orderTrackingInput');
      if (inp) inp.focus();
    }, 150);
  } else if (tabName === 'login') {
    if (isSnitchLoggedIn()) {
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      var v = document.getElementById('loginStepVip');
      if (p) p.style.display = 'none';
      if (o) o.style.display = 'none';
      if (v) v.style.display = 'block';
      var u = document.getElementById('snitchVipUserDisplay');
      if (u) u.textContent = (snitchCurrentUser && snitchCurrentUser.phone) ? snitchCurrentUser.phone : '+91 85116 16133';
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
      }, 150);
    }
  }
}

function openAccountModal(initialTab) {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (!backdrop) return;
  backdrop.classList.add('open');
  switchAccountTab(initialTab || 'track');
  updateAccountHeaderIcon();
}

function closeAccountModalDirect() {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
  clearInterval(snitchOtpInterval);
}

function closeAccountModal(e) {
  if (e.target.id === 'accountModalBackdrop') {
    closeAccountModalDirect();
  }
}

function fillAndTrackDemo(orderId) {
  switchAccountTab('track');
  var inp = document.getElementById('orderTrackingInput');
  if (inp) inp.value = orderId;
  executeOrderTracking();
}

function executeOrderTracking() {
  var inp = document.getElementById('orderTrackingInput');
  var rawVal = inp ? inp.value.trim() : '';
  var err = document.getElementById('orderTrackingError');
  var container = document.getElementById('trackingResultContainer');

  if (!rawVal) {
    if (err) {
      err.textContent = 'Please enter an Order ID (e.g. #ML-1042) or your 10-digit mobile number.';
      err.style.display = 'block';
    }
    if (inp) inp.focus();
    return;
  }
  if (err) err.style.display = 'none';

  var cleanVal = rawVal.toUpperCase();
  var isDelivered = cleanVal.indexOf('1035') !== -1;
  var isTransit = cleanVal.indexOf('1042') !== -1 || cleanVal.indexOf('8511616133') !== -1;

  var orderNum = isDelivered ? '#ML-1035' : (isTransit ? '#ML-1042' : (cleanVal.startsWith('#') ? cleanVal : '#' + cleanVal));
  var productName = isDelivered ? 'Noor Zari Silk Anarkali Set (Size: S)' : (isTransit ? 'Gulab Organza Embroidered Kurta Set (Size: M)' : 'Atelier Drop 01 Handcrafted Silhouette');
  var awbInfo = isDelivered ? 'BlueDart Air • AWB #BD-9918231' : (isTransit ? 'Delhivery Express • AWB #DEL-85116133-TRC' : 'Assigned Upon Dispatch • Express Courier');
  var dest = isDelivered ? 'Gurugram, Haryana' : (isTransit ? 'Sector 17, Chandigarh (Tricity Express)' : 'Tricity / All India Delivery');
  var statusBadge = isDelivered ? 'Delivered' : (isTransit ? 'In Express Transit' : 'Confirmed & In Production');
  var badgeColor = isDelivered ? '#25D366' : '#C8A364';

  var step1Class = 'timeline-step completed';
  var step2Class = (isDelivered || isTransit) ? 'timeline-step completed' : 'timeline-step active';
  var step3Class = isDelivered ? 'timeline-step completed' : (isTransit ? 'timeline-step active' : 'timeline-step');
  var step4Class = isDelivered ? 'timeline-step completed' : 'timeline-step';

  var waMessage = encodeURIComponent('Hi Meenu Label! I am inquiring about my Order ' + orderNum + ' (' + productName + '). Please share latest delivery updates.');

  var html = '<div class="shipment-card">' +
    '<div class="shipment-header">' +
      '<div>' +
        '<div class="shipment-order-id">' + orderNum + '</div>' +
        '<div style="font-size: 11.5px; color: rgba(255,255,255,0.7); margin-top:2px;">' + productName + '</div>' +
      '</div>' +
      '<span class="shipment-badge" style="background: rgba(' + (isDelivered ? '37, 211, 102' : '200, 163, 100') + ', 0.15); color: ' + badgeColor + '; border-color: ' + badgeColor + ';">' + statusBadge + '</span>' +
    '</div>' +
    '<div class="shipment-timeline">' +
      '<div class="' + step1Class + '">' +
        '<div class="timeline-title">Order Confirmed &amp; Atelier Assigned</div>' +
        '<div class="timeline-desc">Handcrafted silk fabrics reserved &bull; Chandigarh Studio</div>' +
      '</div>' +
      '<div class="' + step2Class + '">' +
        '<div class="timeline-title">Handcrafted &amp; Master Quality Checked</div>' +
        '<div class="timeline-desc">' + (isDelivered || isTransit ? 'Passed 14-point artisan luxury inspection' : 'In progress at Sector 17 Atelier') + '</div>' +
      '</div>' +
      '<div class="' + step3Class + '">' +
        '<div class="timeline-title">Dispatched in Express Transit</div>' +
        '<div class="timeline-desc">' + awbInfo + '</div>' +
      '</div>' +
      '<div class="' + step4Class + '">' +
        '<div class="timeline-title">Out for Delivery &amp; VIP Handover</div>' +
        '<div class="timeline-desc">' + (isDelivered ? 'Delivered with Signature Handover' : 'Expected delivery to ' + dest) + '</div>' +
      '</div>' +
    '</div>' +
    '<div class="shipment-meta-row">' +
      '<span>Destination: <strong>' + dest + '</strong></span>' +
      '<span>ETA: <strong>' + (isDelivered ? 'Delivered' : (isTransit ? 'Today by 7:00 PM' : '24-48 Hours')) + '</strong></span>' +
    '</div>' +
    '<a href="https://wa.me/918511616133?text=' + waMessage + '" target="_blank" class="shipment-wa-btn">' +
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.073.043.419-.101.824z"/></svg>' +
      'Instant WhatsApp Inquiry with Atelier' +
    '</a>' +
  '</div>';

  if (container) {
    container.innerHTML = html;
    container.style.display = 'block';
  }
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
  
  var displayEl = document.getElementById('snitchOtpPhoneDisplay');
  if (displayEl) displayEl.textContent = '+91 ' + phone;
  
  var p = document.getElementById('loginStepPhone');
  var o = document.getElementById('loginStepOtp');
  if (p) p.style.display = 'none';
  if (o) o.style.display = 'block';
  
  ['sOtp1', 'sOtp2', 'sOtp3', 'sOtp4'].forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.value = '';
  });
  var firstBox = document.getElementById('sOtp1');
  if (firstBox) firstBox.focus();
  
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
  var code = ((document.getElementById('sOtp1') && document.getElementById('sOtp1').value) || '') +
             ((document.getElementById('sOtp2') && document.getElementById('sOtp2').value) || '') +
             ((document.getElementById('sOtp3') && document.getElementById('sOtp3').value) || '') +
             ((document.getElementById('sOtp4') && document.getElementById('sOtp4').value) || '');
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
  var phone = (inp && inp.value.trim()) ? inp.value.trim() : '8511616133';
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
  
  if (typeof showMeenuToast === 'function') {
    showMeenuToast('Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
  } else if (typeof showToast === 'function') {
    showToast('Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
  }
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
  if (typeof showMeenuToast === 'function') {
    showMeenuToast('Signed out of VIP Atelier account.');
  } else if (typeof showToast === 'function') {
    showToast('Signed out of VIP Atelier account.');
  }
}

// Auto update header icon on load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', updateAccountHeaderIcon);
} else {
  updateAccountHeaderIcon();
}
"""

theme_js_files = ['assets/meenu-theme.js', 'meenu-label-shopify-theme/assets/meenu-theme.js']
for p in theme_js_files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'TRACK MY ORDER & VIP ACCOUNT DRAWER SYSTEM' not in content:
        content = content + "\n\n" + js_code.strip() + "\n"
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Appended tracking & VIP JS to {p}")
    else:
        print(f"Tracking JS already present in {p}")

# Now update index.html: replace existing snitch functions with the updated version
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

# Replace the snitch functions block in index.html
start_marker = "/* Snitch Login & VIP Privé Authentication Logic */"
end_marker = "function searchProducts() {"

if start_marker in h and end_marker in h:
    idx1 = h.find(start_marker)
    idx2 = h.find(end_marker)
    h = h[:idx1] + js_code.strip() + "\n\n    " + h[idx2:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(h)
    print("Replaced account & tracking JS in index.html")
else:
    print(f"Could not find start/end markers in index.html: start={start_marker in h}, end={end_marker in h}")

