import os

with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Define snitch-login-modal.liquid snippet
snitch_modal_snippet = '''# snitch-login-modal.liquid
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
        <div class="snitch-campaign-pill">The Debut 16 Silhouettes</div>
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
'''

if "snitch_login_liquid" not in code:
    pos_drawer = code.find('# cart-drawer.liquid')
    if pos_drawer != -1:
        code = code[:pos_drawer] + snitch_modal_snippet + "\n" + code[pos_drawer:]
        print("Inserted snitch-login-modal.liquid snippet code.")

# 2. Render snippet in theme.liquid
if "{% render 'snitch-login-modal' %}" not in code:
    code = code.replace("{% render 'cart-drawer' %}", "{% render 'snitch-login-modal' %}\n  {% render 'cart-drawer' %}")
    print("Rendered snitch-login-modal in theme.liquid.")

# 3. Update header account icon to trigger modal
acc_link = '<a href="/account" class="header-icon-link" aria-label="Account" title="Account">'
acc_link_new = '<a href="/account" class="header-icon-link" aria-label="Account" title="Account" onclick="openAccountModal(); return false;" style="position:relative;">\n        <span class="account-active-badge" id="accountActiveBadge"></span>'
if acc_link in code:
    code = code.replace(acc_link, acc_link_new)
    print("Updated header account link to openAccountModal().")

# 4. Insert Snitch login JavaScript into theme JS
snitch_js_shopify = """
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
"""

if "function openAccountModal" not in code:
    code = code.replace("function openNavDrawer() {", snitch_js_shopify + "\nfunction openNavDrawer() {")
    print("Added Snitch login JavaScript functions to theme JS.")

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_shopify_theme.py with Snitch Login!")
