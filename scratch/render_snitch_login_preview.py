import os, base64, io, subprocess
from PIL import Image

def get_b64(path):
    im = Image.open(path)
    buf = io.BytesIO()
    im.save(buf, format='JPEG', quality=85, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode('ascii')

brain_dir = 'C:/Users/sande/.gemini/antigravity/brain/1d796c0f-b986-45c2-b599-b8a1dc691d66'
b64_angrakha = get_b64(os.path.join(brain_dir, 'meenu_label_angrakha_balcony_v2_1792254010513.jpg'))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meenu Label - Snitch Style Login</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,700&family=Playfair+Display:ital,wght@0,600;1,600;1,700&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: #000000;
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top bar matching Snitch */
    .snitch-topbar {{
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      background: #000000;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      position: relative;
      z-index: 20;
    }}
    .snitch-back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: none;
      border: none;
      color: #ffffff;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      padding: 8px 0;
      text-decoration: none;
      transition: opacity 0.2s;
    }}
    .snitch-back-btn:hover {{
      opacity: 0.7;
    }}
    .snitch-back-btn svg {{
      width: 20px;
      height: 20px;
    }}

    /* Main Container */
    .snitch-login-wrapper {{
      flex: 1;
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      min-height: calc(100vh - 56px);
      background: #000000;
    }}

    /* Left Campaign Hero */
    .snitch-campaign-col {{
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      background: #0d0d0d;
    }}
    .snitch-campaign-img {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 25%;
    }}
    .snitch-campaign-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.1) 0%,
        rgba(0, 0, 0, 0.05) 45%,
        rgba(0, 0, 0, 0.6) 75%,
        rgba(0, 0, 0, 0.92) 100%
      );
    }}
    .snitch-campaign-content {{
      position: relative;
      z-index: 2;
      padding: 48px 56px;
      max-width: 620px;
    }}
    .snitch-campaign-badge {{
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.2em;
      color: #D4AF37;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 5px 12px;
      border-radius: 20px;
      margin-bottom: 16px;
    }}
    .snitch-campaign-title {{
      font-size: clamp(34px, 4vw, 54px);
      font-weight: 800;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      line-height: 1.08;
      color: #ffffff;
      margin-bottom: 12px;
      text-shadow: 0 2px 16px rgba(0,0,0,0.6);
    }}
    .snitch-campaign-title .accent {{
      font-style: italic;
      font-family: 'Playfair Display', Georgia, serif;
      font-weight: 700;
      color: #E2725B;
      text-transform: none;
      letter-spacing: 0.01em;
    }}
    .snitch-campaign-sub {{
      font-size: 13px;
      color: rgba(255, 255, 255, 0.75);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 500;
    }}

    /* Right Login Card Column */
    .snitch-form-col {{
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px 32px;
      background: #000000;
    }}

    /* The Snitch Floating Dark Card */
    .snitch-card {{
      width: 100%;
      max-width: 440px;
      background: #161616;
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 22px;
      padding: 44px 38px 36px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.03);
      position: relative;
    }}

    /* Card Brand Header */
    .snitch-card-brand {{
      text-align: center;
      margin-bottom: 34px;
    }}
    .snitch-card-brand h1 {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0.22em;
      color: #ffffff;
      text-transform: uppercase;
      margin: 0;
      line-height: 1.2;
    }}
    .snitch-card-brand p {{
      font-size: 10px;
      color: #777777;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-top: 5px;
      font-weight: 500;
    }}

    /* Form Elements */
    .snitch-field-label {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #8E8E93;
      margin-bottom: 14px;
      display: block;
    }}

    .snitch-phone-group {{
      display: flex;
      align-items: center;
      border-bottom: 1.5px solid #333333;
      padding-bottom: 10px;
      margin-bottom: 26px;
      transition: border-color 0.25s ease;
    }}
    .snitch-phone-group:focus-within {{
      border-bottom-color: #D4AF37;
    }}
    .snitch-country-code {{
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      margin-right: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.04em;
      user-select: none;
    }}
    .snitch-phone-input {{
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      font-family: inherit;
      font-size: 16px;
      font-weight: 500;
      color: #ffffff;
      letter-spacing: 0.08em;
    }}
    .snitch-phone-input::placeholder {{
      color: #4A4A4F;
      font-weight: 400;
    }}

    /* Primary Action Button (White with black text and right arrow) */
    .snitch-btn-primary {{
      width: 100%;
      height: 50px;
      background: #ffffff;
      color: #000000;
      border: none;
      border-radius: 8px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
      margin-bottom: 24px;
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.1);
    }}
    .snitch-btn-primary:hover {{
      background: #f0f0f0;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(255, 255, 255, 0.18);
    }}
    .snitch-btn-primary:active {{
      transform: translateY(0);
    }}
    .snitch-btn-primary svg {{
      width: 16px;
      height: 16px;
      transition: transform 0.2s;
    }}
    .snitch-btn-primary:hover svg {{
      transform: translateX(3px);
    }}

    /* Footer Disclaimer */
    .snitch-disclaimer {{
      font-size: 11px;
      line-height: 1.6;
      color: #666666;
      text-align: center;
    }}
    .snitch-disclaimer a {{
      color: #999999;
      text-decoration: underline;
      text-underline-offset: 2px;
      transition: color 0.2s;
    }}
    .snitch-disclaimer a:hover {{
      color: #ffffff;
    }}

    /* Error Message */
    .snitch-error-msg {{
      font-size: 12px;
      color: #ff6b6b;
      margin-top: -16px;
      margin-bottom: 20px;
      display: none;
    }}

    /* OTP Step Styling */
    .snitch-otp-screen {{
      display: none;
    }}
    .snitch-otp-inputs {{
      display: flex;
      gap: 12px;
      justify-content: center;
      margin: 24px 0;
    }}
    .snitch-otp-digit {{
      width: 54px;
      height: 58px;
      background: #202020;
      border: 1.5px solid #333333;
      border-radius: 10px;
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      text-align: center;
      font-family: inherit;
      outline: none;
      transition: all 0.2s;
    }}
    .snitch-otp-digit:focus {{
      border-color: #D4AF37;
      background: #252525;
      box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
    }}

    /* VIP Privé Dashboard (Post Login) */
    .snitch-vip-screen {{
      display: none;
      text-align: center;
    }}

    /* Responsive */
    @media (max-width: 900px) {{
      .snitch-login-wrapper {{
        grid-template-columns: 1fr;
      }}
      .snitch-campaign-col {{
        min-height: 240px;
        max-height: 280px;
      }}
      .snitch-campaign-content {{
        padding: 24px 28px;
      }}
      .snitch-form-col {{
        padding: 24px 20px;
      }}
      .snitch-card {{
        padding: 32px 24px 28px;
      }}
    }}
  </style>
</head>
<body>
  <!-- Top Bar matching Snitch (< Back to Store) -->
  <header class="snitch-topbar">
    <a href="#" class="snitch-back-btn" onclick="alert('Returns to store'); return false;">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
      <span>Back</span>
    </a>
    <div style="font-size: 11px; color: #777; letter-spacing: 0.1em; text-transform: uppercase;">
      Meenu Label &bull; Chandigarh Atelier
    </div>
  </header>

  <!-- Split Screen Login -->
  <main class="snitch-login-wrapper">
    <!-- Left: Editorial Campaign Photography -->
    <div class="snitch-campaign-col">
      <img src="{b64_angrakha}" alt="Meenu Label Luxury Campaign" class="snitch-campaign-img">
      <div class="snitch-campaign-overlay"></div>
      <div class="snitch-campaign-content">
        <div class="snitch-campaign-badge">The Debut 16 Silhouettes</div>
        <h2 class="snitch-campaign-title">
          WEAR WHAT'S <span class="accent">TIMELESS</span>
        </h2>
        <p class="snitch-campaign-sub">Chandigarh Atelier &bull; Handcrafted Chanderi &amp; Crepe Silks</p>
      </div>
    </div>

    <!-- Right: Snitch-Style Dark Card -->
    <div class="snitch-form-col">
      <div class="snitch-card">
        <!-- Step 1: Phone Entry Screen -->
        <div id="snitchPhoneStep">
          <div class="snitch-card-brand">
            <h1>MEENU LABEL</h1>
            <p>CHANDIGARH &bull; LUXURY ETHNIC</p>
          </div>

          <label class="snitch-field-label" for="loginMobileInput">ENTER MOBILE NUMBER</label>
          <div class="snitch-phone-group">
            <div class="snitch-country-code">
              <span>+91</span>
            </div>
            <input 
              type="tel" 
              id="loginMobileInput" 
              class="snitch-phone-input" 
              placeholder="99999 99999" 
              maxlength="10"
              value=""
              autocomplete="tel"
              oninput="onPhoneInput(this)"
              onkeydown="if(event.key==='Enter') triggerSendOtp()"
            >
          </div>
          <div id="phoneError" class="snitch-error-msg">Please enter a valid 10-digit mobile number</div>

          <button class="snitch-btn-primary" id="btnSendOtp" onclick="triggerSendOtp()">
            <span>SEND OTP</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>

          <p class="snitch-disclaimer">
            By continuing, you agree to MEENU LABEL's 
            <a href="#" onclick="alert('Terms & Conditions: Handcrafted luxury orders, 48-hr dispatch across India.'); return false;">Terms &amp; Conditions</a> 
            and 
            <a href="#" onclick="alert('Privacy Policy: 100% encrypted, no spam.'); return false;">Privacy Policy</a>
          </p>
        </div>

        <!-- Step 2: OTP Verification Screen -->
        <div id="snitchOtpStep" class="snitch-otp-screen">
          <div class="snitch-card-brand" style="margin-bottom: 24px;">
            <h1 style="font-size: 20px;">VERIFY OTP</h1>
            <p id="otpTargetText" style="color: #aaa; margin-top: 8px; font-size: 12px; text-transform: none; letter-spacing: 0;">
              Enter 4-digit code sent to <strong id="maskedPhoneDisplay" style="color:#fff;">+91 99999 99999</strong>
              <button onclick="backToPhoneStep()" style="background:none; border:none; color:#D4AF37; cursor:pointer; font-weight:600; margin-left:6px; text-decoration:underline;">Edit</button>
            </p>
          </div>

          <div class="snitch-otp-inputs">
            <input type="text" maxlength="1" class="snitch-otp-digit" id="otp1" oninput="otpMove(this, 'otp2')" onkeydown="otpBack(event, this, null)">
            <input type="text" maxlength="1" class="snitch-otp-digit" id="otp2" oninput="otpMove(this, 'otp3')" onkeydown="otpBack(event, this, 'otp1')">
            <input type="text" maxlength="1" class="snitch-otp-digit" id="otp3" oninput="otpMove(this, 'otp4')" onkeydown="otpBack(event, this, 'otp2')">
            <input type="text" maxlength="1" class="snitch-otp-digit" id="otp4" oninput="otpMove(this, null)" onkeydown="otpBack(event, this, 'otp3')">
          </div>

          <div style="text-align: center; margin-bottom: 20px;">
            <span id="resendTimer" style="font-size: 12px; color: #777;">Resend OTP in <strong style="color:#bbb;">0:28</strong></span>
            <button id="resendBtn" onclick="resendOtp()" style="display:none; background:none; border:none; color:#D4AF37; font-size: 12px; font-weight: 600; cursor:pointer; text-decoration:underline;">Resend OTP via SMS / WhatsApp</button>
          </div>

          <button class="snitch-btn-primary" onclick="triggerVerifyOtp()">
            <span>VERIFY &amp; PROCEED</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
          
          <div style="font-size: 11px; color: #777; text-align: center; margin-top: 12px;">
            &bull; Demo Mode: Enter any 4 digits (e.g. 1 2 3 4) to verify
          </div>
        </div>

        <!-- Step 3: VIP Privé Dashboard -->
        <div id="snitchVipStep" class="snitch-vip-screen">
          <div style="width: 60px; height: 60px; border-radius: 50%; background: rgba(37, 211, 102, 0.12); border: 1.5px solid #25D366; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: #25D366;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <h2 style="font-size: 20px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 6px;">WELCOME BACK</h2>
          <div id="vipUserPhoneDisplay" style="font-size: 13px; color: #D4AF37; font-weight: 600; margin-bottom: 22px;">+91 99888 98845</div>
          <div style="background: #202020; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 16px; margin-bottom: 24px; text-align: left; font-size: 12px;">
            <div style="color: #fff; font-weight: 700; margin-bottom: 4px;">&#10024; Atelier Priv&eacute; Tier 1</div>
            <div style="color: #888;">Free 24-hr Tricity courier, Sector 17 studio VIP fittings &amp; dedicated stylist on call.</div>
          </div>
          <button class="snitch-btn-primary" onclick="alert('Returning to shopping with VIP privileges active!');">
            <span>CONTINUE SHOPPING</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
          <button onclick="signOutUser()" style="background:none; border:none; color:#777; font-size:12px; cursor:pointer; text-decoration:underline; margin-top:14px;">Sign Out / Change Account</button>
        </div>
      </div>
    </div>
  </main>

  <script>
    var currentPhone = '';
    var timerInterval = null;

    function onPhoneInput(el) {{
      el.value = el.value.replace(/\\D/g, '');
      document.getElementById('phoneError').style.display = 'none';
    }}

    function triggerSendOtp() {{
      var input = document.getElementById('loginMobileInput');
      var val = input.value.trim();
      if (val.length < 10) {{
        document.getElementById('phoneError').style.display = 'block';
        input.focus();
        return;
      }}
      currentPhone = val;
      document.getElementById('maskedPhoneDisplay').textContent = '+91 ' + val;
      document.getElementById('snitchPhoneStep').style.display = 'none';
      document.getElementById('snitchOtpStep').style.display = 'block';
      document.getElementById('otp1').focus();
      startResendTimer();
    }}

    function backToPhoneStep() {{
      clearInterval(timerInterval);
      document.getElementById('snitchOtpStep').style.display = 'none';
      document.getElementById('snitchPhoneStep').style.display = 'block';
      document.getElementById('loginMobileInput').focus();
    }}

    function otpMove(curr, nextId) {{
      curr.value = curr.value.replace(/\\D/g, '');
      if (curr.value && nextId) {{
        var next = document.getElementById(nextId);
        if (next) next.focus();
      }}
      var code = (document.getElementById('otp1').value || '') +
                 (document.getElementById('otp2').value || '') +
                 (document.getElementById('otp3').value || '') +
                 (document.getElementById('otp4').value || '');
      if (code.length === 4) {{
        setTimeout(triggerVerifyOtp, 250);
      }}
    }}

    function otpBack(e, curr, prevId) {{
      if (e.key === 'Backspace' && !curr.value && prevId) {{
        var prev = document.getElementById(prevId);
        if (prev) {{
          prev.focus();
          prev.value = '';
        }}
      }}
    }}

    function startResendTimer() {{
      var sec = 28;
      var timerEl = document.getElementById('resendTimer');
      var btnEl = document.getElementById('resendBtn');
      timerEl.style.display = 'inline';
      btnEl.style.display = 'none';
      clearInterval(timerInterval);
      timerInterval = setInterval(function() {{
        sec--;
        if (sec <= 0) {{
          clearInterval(timerInterval);
          timerEl.style.display = 'none';
          btnEl.style.display = 'inline';
        }} else {{
          timerEl.innerHTML = 'Resend OTP in <strong style="color:#bbb;">0:' + (sec < 10 ? '0' : '') + sec + '</strong>';
        }}
      }}, 1000);
    }}

    function resendOtp() {{
      alert('New OTP sent to +91 ' + currentPhone + ' via SMS & WhatsApp!');
      startResendTimer();
    }}

    function triggerVerifyOtp() {{
      clearInterval(timerInterval);
      document.getElementById('snitchOtpStep').style.display = 'none';
      document.getElementById('snitchVipStep').style.display = 'block';
      document.getElementById('vipUserPhoneDisplay').textContent = '+91 ' + currentPhone;
    }}

    function signOutUser() {{
      document.getElementById('snitchVipStep').style.display = 'none';
      document.getElementById('snitchPhoneStep').style.display = 'block';
      document.getElementById('loginMobileInput').value = '';
    }}
  </script>
</body>
</html>
"""

with open('scratch/snitch_login_preview.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Saved scratch/snitch_login_preview.html')
