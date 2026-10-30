import re, os, base64, io
from PIL import Image

# 1. First, create an optimized JPEG for the login campaign banner
brain_dir = r'C:/Users/sande/.gemini/antigravity/brain/1d796c0f-b986-45c2-b599-b8a1dc691d66'
campaign_src = os.path.join(brain_dir, 'meenu_label_angrakha_balcony_v2_1792254010513.jpg')
campaign_opt = 'scratch/login_campaign_banner.jpg'

if os.path.exists(campaign_src):
    im = Image.open(campaign_src)
    # Resize slightly if too large, maintain high quality
    if im.width > 1000:
        ratio = 1000.0 / im.width
        new_h = int(im.height * ratio)
        im = im.resize((1000, new_h), Image.Resampling.LANCZOS)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.save(campaign_opt, format='JPEG', quality=86, optimize=True)
    print(f"Created optimized campaign banner: {os.path.getsize(campaign_opt)/1024:.1f} KB")

# 2. Read build_snitch_storefront.py
with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 3. Add login_campaign_b64 loader at top
if "login_campaign_b64" not in code:
    loader_target = "banner_4_b64 = get_b64(os.path.join(banners_dir, 'hero_4_lime.jpg'))"
    loader_repl = loader_target + """\nlogin_campaign_b64 = get_b64(r'scratch/login_campaign_banner.jpg')"""
    if loader_target in code:
        code = code.replace(loader_target, loader_repl)
        print("Added login_campaign_b64 variable definition.")
    else:
        print("ERROR: Could not find loader_target in code!")

# 4. Add CSS for Snitch Login Modal
snitch_login_css = """
    /* ========================================================
       SNITCH-STYLE LUXURY LOGIN INTERFACE & MODAL
       ======================================================== */
    .snitch-login-backdrop {{
      position: fixed;
      inset: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 500;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
      opacity: 0;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .snitch-login-backdrop.open {{
      display: flex;
      opacity: 1;
    }}

    .snitch-login-dialog {{
      width: 100%;
      max-width: 1040px;
      height: min(650px, 90vh);
      background: #000000;
      border-radius: 22px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 32px 90px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(255, 255, 255, 0.04);
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      overflow: hidden;
      position: relative;
      transform: scale(0.97) translateY(12px);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .snitch-login-backdrop.open .snitch-login-dialog {{
      transform: scale(1) translateY(0);
    }}

    /* Top Action Buttons (Back chevron & Close) */
    .snitch-dialog-back {{
      position: absolute;
      top: 20px;
      left: 20px;
      z-index: 40;
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .snitch-dialog-back:hover {{
      background: rgba(255, 255, 255, 0.2);
      transform: scale(1.06);
    }}
    .snitch-dialog-back svg {{
      width: 18px;
      height: 18px;
    }}

    .snitch-dialog-close {{
      position: absolute;
      top: 18px;
      right: 20px;
      z-index: 40;
      background: rgba(0, 0, 0, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 50%;
      width: 38px;
      height: 38px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 24px;
      line-height: 1;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .snitch-dialog-close:hover {{
      background: rgba(255, 255, 255, 0.2);
      transform: scale(1.06);
    }}

    /* Left Campaign Column */
    .snitch-login-campaign {{
      position: relative;
      height: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      background: #0a0a0a;
    }}
    .snitch-campaign-photo {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 25%;
    }}
    .snitch-campaign-vignette {{
      position: absolute;
      inset: 0;
      background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.12) 0%,
        rgba(0, 0, 0, 0.05) 45%,
        rgba(0, 0, 0, 0.65) 75%,
        rgba(0, 0, 0, 0.94) 100%
      );
    }}
    .snitch-campaign-text {{
      position: relative;
      z-index: 2;
      padding: 40px 48px;
      max-width: 580px;
    }}
    .snitch-campaign-pill {{
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
      margin-bottom: 14px;
    }}
    .snitch-campaign-headline {{
      font-size: clamp(30px, 3.4vw, 46px);
      font-weight: 800;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      line-height: 1.1;
      color: #ffffff;
      margin-bottom: 10px;
      text-shadow: 0 2px 14px rgba(0,0,0,0.6);
    }}
    .snitch-headline-accent {{
      font-style: italic;
      font-family: 'Playfair Display', Georgia, serif;
      font-weight: 700;
      color: #E2725B;
      text-transform: none;
      letter-spacing: 0.02em;
    }}
    .snitch-campaign-atelier {{
      font-size: 12px;
      color: rgba(255, 255, 255, 0.75);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 500;
    }}

    /* Right Form Column */
    .snitch-login-content {{
      display: flex;
      align-items: center;
      justify-content: center;
      background: #000000;
      padding: 32px 28px;
      height: 100%;
    }}

    /* The Snitch Charcoal Card */
    .snitch-login-card {{
      width: 100%;
      max-width: 420px;
      background: #161616;
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 22px;
      padding: 42px 36px 34px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.03);
      position: relative;
    }}

    .snitch-brand-block {{
      text-align: center;
      margin-bottom: 32px;
    }}
    .snitch-brand-title {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0.22em;
      color: #ffffff;
      text-transform: uppercase;
      margin: 0;
      line-height: 1.2;
    }}
    .snitch-brand-tag {{
      font-size: 10px;
      color: #777777;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-top: 6px;
      font-weight: 500;
    }}

    .snitch-input-heading {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #8E8E93;
      margin-bottom: 14px;
      display: block;
    }}

    .snitch-input-row {{
      display: flex;
      align-items: center;
      border-bottom: 1.5px solid #333333;
      padding-bottom: 10px;
      margin-bottom: 24px;
      transition: border-color 0.25s ease;
    }}
    .snitch-input-row:focus-within {{
      border-bottom-color: #D4AF37;
    }}
    .snitch-cc-badge {{
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      margin-right: 14px;
      display: flex;
      align-items: center;
      letter-spacing: 0.04em;
      user-select: none;
    }}
    .snitch-mobile-field {{
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
    .snitch-mobile-field::placeholder {{
      color: #4A4A4F;
      font-weight: 400;
    }}

    .snitch-validation-error {{
      font-size: 12px;
      color: #ff6b6b;
      margin-top: -16px;
      margin-bottom: 18px;
      display: none;
    }}

    /* Primary Action Button (White with black text and right arrow) */
    .snitch-submit-btn {{
      width: 100%;
      height: 48px;
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
      margin-bottom: 22px;
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.1);
    }}
    .snitch-submit-btn:hover {{
      background: #f0f0f0;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(255, 255, 255, 0.18);
    }}
    .snitch-submit-btn:active {{
      transform: translateY(0);
    }}
    .snitch-submit-btn svg {{
      width: 16px;
      height: 16px;
      transition: transform 0.2s;
    }}
    .snitch-submit-btn:hover svg {{
      transform: translateX(3px);
    }}

    .snitch-legal-note {{
      font-size: 11px;
      line-height: 1.6;
      color: #666666;
      text-align: center;
    }}
    .snitch-legal-note a {{
      color: #999999;
      text-decoration: underline;
      text-underline-offset: 2px;
      transition: color 0.2s;
    }}
    .snitch-legal-note a:hover {{
      color: #ffffff;
    }}

    /* OTP Inputs */
    .snitch-otp-sent-info {{
      color: #aaaaaa;
      margin-top: 6px;
      font-size: 12px;
      text-transform: none;
      letter-spacing: 0;
    }}
    .snitch-edit-phone-btn {{
      background: none;
      border: none;
      color: #D4AF37;
      cursor: pointer;
      font-weight: 600;
      margin-left: 6px;
      text-decoration: underline;
      font-size: 12px;
    }}
    .snitch-otp-grid {{
      display: flex;
      gap: 12px;
      justify-content: center;
      margin: 22px 0 16px;
    }}
    .snitch-digit-box {{
      width: 52px;
      height: 56px;
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
    .snitch-digit-box:focus {{
      border-color: #D4AF37;
      background: #252525;
      box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
    }}
    .snitch-resend-bar {{
      text-align: center;
      margin-bottom: 20px;
      font-size: 12px;
      color: #777777;
    }}
    .snitch-resend-action {{
      background: none;
      border: none;
      color: #D4AF37;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: underline;
    }}
    .snitch-demo-badge {{
      font-size: 11px;
      color: #777777;
      text-align: center;
      margin-top: 10px;
    }}

    /* VIP Privé Dashboard */
    .snitch-vip-avatar {{
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: rgba(37, 211, 102, 0.12);
      border: 1.5px solid #25D366;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 14px;
      color: #25D366;
    }}
    .snitch-vip-status-tag {{
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.16em;
      color: #D4AF37;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 4px 10px;
      border-radius: 14px;
      margin-bottom: 8px;
    }}
    .snitch-vip-user {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 18px;
      letter-spacing: 0.04em;
    }}
    .snitch-vip-perks {{
      background: #202020;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 14px 16px;
      margin-bottom: 20px;
      text-align: left;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .snitch-perk-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .snitch-perk-icon {{
      font-size: 16px;
      line-height: 1.2;
    }}
    .snitch-perk-text strong {{
      display: block;
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
    }}
    .snitch-perk-text span {{
      display: block;
      color: #888888;
      font-size: 11px;
    }}
    .snitch-vip-concierge-btn {{
      display: block;
      width: 100%;
      padding: 11px 16px;
      border-radius: 8px;
      background: rgba(37, 211, 102, 0.1);
      border: 1px solid rgba(37, 211, 102, 0.3);
      color: #25D366;
      text-decoration: none;
      font-size: 12px;
      font-weight: 600;
      margin-bottom: 14px;
      transition: background 0.2s;
    }}
    .snitch-vip-concierge-btn:hover {{
      background: rgba(37, 211, 102, 0.18);
    }}
    .snitch-signout-btn {{
      background: none;
      border: none;
      color: #777777;
      font-size: 12px;
      cursor: pointer;
      text-decoration: underline;
      transition: color 0.2s;
    }}
    .snitch-signout-btn:hover {{
      color: #ffffff;
    }}

    /* Header Active User Indicator Dot */
    .account-active-badge {{
      position: absolute;
      top: 4px;
      right: 4px;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #25D366;
      border: 1.5px solid #ffffff;
      display: none;
    }}

    /* Responsive Snitch Login Dialog */
    @media (max-width: 860px) {{
      .snitch-login-dialog {{
        grid-template-columns: 1fr;
        height: 94vh;
        max-height: none;
        overflow-y: auto;
      }}
      .snitch-login-campaign {{
        height: 200px;
        min-height: 200px;
      }}
      .snitch-campaign-text {{
        padding: 20px 24px;
      }}
      .snitch-campaign-headline {{
        font-size: 24px;
      }}
      .snitch-login-content {{
        padding: 20px 16px 28px;
      }}
      .snitch-login-card {{
        padding: 28px 20px 24px;
      }}
    }}
"""

# Insert CSS before </style>
if "snitch-login-backdrop" not in code:
    code = code.replace("</style>", snitch_login_css + "\n  </style>")
    print("Inserted Snitch Login CSS.")

# 5. Replace accountModalBackdrop markup
snitch_login_markup = """  <!-- Snitch-Style Split-Screen Login & VIP Atelier Modal -->
  <div class="snitch-login-backdrop" id="accountModalBackdrop" onclick="closeAccountModal(event)">
    <div class="snitch-login-dialog" onclick="event.stopPropagation()">
      <!-- Top Actions: Back Chevron on Left, Close X on Right -->
      <button class="snitch-dialog-back" onclick="closeAccountModalDirect()" title="Back to Store" aria-label="Back">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button class="snitch-dialog-close" onclick="closeAccountModalDirect()" title="Close Modal" aria-label="Close">&times;</button>

      <!-- Left Column: High-Fashion Campaign Photography -->
      <div class="snitch-login-campaign">
        <img src="{login_campaign_b64}" alt="Meenu Label Campaign" class="snitch-campaign-photo">
        <div class="snitch-campaign-vignette"></div>
        <div class="snitch-campaign-text">
          <div class="snitch-campaign-pill">The Debut 16 Silhouettes</div>
          <h2 class="snitch-campaign-headline">
            WEAR WHAT'S <span class="snitch-headline-accent">TIMELESS</span>
          </h2>
          <p class="snitch-campaign-atelier">Chandigarh Atelier &bull; Handcrafted Pure Silks</p>
        </div>
      </div>

      <!-- Right Column: Matte Charcoal Card matching Snitch -->
      <div class="snitch-login-content">
        <div class="snitch-login-card">
          <!-- Step 1: Mobile Number Input -->
          <div id="loginStepPhone">
            <div class="snitch-brand-block">
              <h2 class="snitch-brand-title">MEENU LABEL</h2>
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
              By continuing, you agree to MEENU LABEL's 
              <a href="javascript:void(0)" onclick="alert('MEENU LABEL TERMS: All silhouettes handcrafted in Chandigarh. Express dispatch within 24-48 hours with door-to-door tracking.')">Terms &amp; Conditions</a> 
              and 
              <a href="javascript:void(0)" onclick="alert('MEENU LABEL PRIVACY: Your phone number is strictly encrypted and used solely for VIP order tracking & delivery notifications.')">Privacy Policy</a>
            </p>
          </div>

          <!-- Step 2: OTP Verification -->
          <div id="loginStepOtp" style="display:none;">
            <div class="snitch-brand-block" style="margin-bottom: 20px;">
              <h2 class="snitch-brand-title" style="font-size: 20px;">VERIFY OTP</h2>
              <div class="snitch-otp-sent-info">
                Code sent to <strong id="snitchOtpPhoneDisplay" style="color:#ffffff;">+91 99999 99999</strong>
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
              <span id="snitchTimerTxt">Resend OTP in <strong id="snitchCountdown" style="color:#bbbbbb;">0:28</strong></span>
              <button type="button" id="snitchResendBtn" class="snitch-resend-action" style="display:none;" onclick="snitchResendOtp()">Resend OTP via SMS / WhatsApp</button>
            </div>

            <button class="snitch-submit-btn" onclick="verifySnitchOtp()">
              <span>VERIFY &amp; PROCEED</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>

            <div class="snitch-demo-badge">&bull; Demo Mode: Type any 4 digits (e.g. 1 2 3 4) to login</div>
          </div>

          <!-- Step 3: VIP Atelier Privé Dashboard -->
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
                  <span>Direct courier from Sector 17 Atelier</span>
                </div>
              </div>
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#128087;</div>
                <div class="snitch-perk-text">
                  <strong>Bespoke Atelier Fittings</strong>
                  <span>Private trial room appointments in Chandigarh</span>
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
              <a href="https://wa.me/919988898845?text=Hi%20Meenu%20Label%2C%20I%20am%20a%20VIP%20member%20inquiring%20about%20my%20orders." target="_blank" class="snitch-vip-concierge-btn">
                &#128172; Open Master Stylist WhatsApp Concierge
              </a>
              <button type="button" class="snitch-signout-btn" onclick="signOutSnitchUser()">Sign Out / Change Account</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""

pos_modal_start = code.find('<!-- Account & Concierge Modal -->')
pos_modal_end = code.find('<!-- Size Guide Modal -->')

if pos_modal_start != -1 and pos_modal_end != -1:
    code = code[:pos_modal_start] + snitch_login_markup + "\n\n  " + code[pos_modal_end:]
    print("Replaced account modal markup with Snitch-style login markup.")
else:
    print(f"ERROR: Could not find account modal positions: start={pos_modal_start}, end={pos_modal_end}")

# 6. Add active badge indicator to account icon in header
hdr_acc_target = """<button class="header-icon-action" onclick="openAccountModal()" title="Meenu Atelier VIP & Concierge" aria-label="Account">"""
hdr_acc_repl = """<button class="header-icon-action" onclick="openAccountModal()" title="Account & VIP Login" aria-label="Account" style="position:relative;">
        <span class="account-active-badge" id="accountActiveBadge"></span>"""

if hdr_acc_target in code:
    code = code.replace(hdr_acc_target, hdr_acc_repl)
    print("Added accountActiveBadge to header account icon.")

# 7. Add account login link into nav drawer
nav_acc_target = """<li><a href="javascript:void(0)" onclick="closeNavDrawer(); filterCategory('top')">Tops &amp; Blouses (3)</a></li>"""
nav_acc_repl = nav_acc_target + """\n          <li><a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal();" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a></li>"""

if nav_acc_target in code and "VIP Atelier Login / Account" not in code:
    code = code.replace(nav_acc_target, nav_acc_repl)
    print("Added VIP Atelier Login / Account link to nav drawer.")

# 8. Replace Account Modal JavaScript Logic
js_target_start = code.find('/* Account Modal Logic */')
js_target_end = code.find('function searchProducts()')

snitch_login_js = """/* Snitch Login & VIP Privé Authentication Logic */
    var snitchCurrentUser = null;
    var snitchOtpInterval = null;

    function isSnitchLoggedIn() {{
      if (snitchCurrentUser) return true;
      try {{
        var stored = localStorage.getItem('meenu_vip_user');
        if (stored) {{
          snitchCurrentUser = JSON.parse(stored);
          return true;
        }}
      }} catch(e) {{}}
      return false;
    }}

    function updateAccountHeaderIcon() {{
      var badge = document.getElementById('accountActiveBadge');
      if (badge) {{
        badge.style.display = isSnitchLoggedIn() ? 'block' : 'none';
      }}
    }}

    function openAccountModal() {{
      var backdrop = document.getElementById('accountModalBackdrop');
      if (!backdrop) return;
      backdrop.classList.add('open');
      
      if (isSnitchLoggedIn()) {{
        var p = document.getElementById('loginStepPhone');
        var o = document.getElementById('loginStepOtp');
        var v = document.getElementById('loginStepVip');
        if (p) p.style.display = 'none';
        if (o) o.style.display = 'none';
        if (v) v.style.display = 'block';
        var u = document.getElementById('snitchVipUserDisplay');
        if (u) u.textContent = snitchCurrentUser.phone || '+91 99888 98845';
      }} else {{
        var p = document.getElementById('loginStepPhone');
        var o = document.getElementById('loginStepOtp');
        var v = document.getElementById('loginStepVip');
        if (p) p.style.display = 'block';
        if (o) o.style.display = 'none';
        if (v) v.style.display = 'none';
        setTimeout(function() {{
          var inp = document.getElementById('snitchMobileInput');
          if (inp) inp.focus();
        }}, 200);
      }}
    }}

    function closeAccountModalDirect() {{
      var backdrop = document.getElementById('accountModalBackdrop');
      if (backdrop) backdrop.classList.remove('open');
      clearInterval(snitchOtpInterval);
    }}

    function closeAccountModal(e) {{
      if (e.target.id === 'accountModalBackdrop') {{
        closeAccountModalDirect();
      }}
    }}

    function onSnitchPhoneInput(el) {{
      el.value = el.value.replace(/\\D/g, '');
      var err = document.getElementById('snitchPhoneError');
      if (err) err.style.display = 'none';
    }}

    function requestSnitchOtp() {{
      var inp = document.getElementById('snitchMobileInput');
      var phone = inp ? inp.value.trim() : '';
      if (phone.length < 10) {{
        var err = document.getElementById('snitchPhoneError');
        if (err) err.style.display = 'block';
        if (inp) inp.focus();
        return;
      }}
      
      var displayEl = document.getElementById('snitchOtpPhoneDisplay');
      if (displayEl) displayEl.textContent = '+91 ' + phone;
      
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      if (p) p.style.display = 'none';
      if (o) o.style.display = 'block';
      
      ['sOtp1', 'sOtp2', 'sOtp3', 'sOtp4'].forEach(function(id) {{
        var el = document.getElementById(id);
        if (el) el.value = '';
      }});
      var firstBox = document.getElementById('sOtp1');
      if (firstBox) firstBox.focus();
      
      startSnitchOtpTimer();
    }}

    function snitchEditPhone() {{
      clearInterval(snitchOtpInterval);
      var p = document.getElementById('loginStepPhone');
      var o = document.getElementById('loginStepOtp');
      if (o) o.style.display = 'none';
      if (p) p.style.display = 'block';
      var inp = document.getElementById('snitchMobileInput');
      if (inp) inp.focus();
    }}

    function snitchOtpNext(curr, nextId) {{
      curr.value = curr.value.replace(/\\D/g, '');
      if (curr.value && nextId) {{
        var next = document.getElementById(nextId);
        if (next) next.focus();
      }}
      var code = (document.getElementById('sOtp1')?.value || '') +
                 (document.getElementById('sOtp2')?.value || '') +
                 (document.getElementById('sOtp3')?.value || '') +
                 (document.getElementById('sOtp4')?.value || '');
      if (code.length === 4) {{
        setTimeout(verifySnitchOtp, 200);
      }}
    }}

    function snitchOtpBack(e, curr, prevId) {{
      if (e.key === 'Backspace' && !curr.value && prevId) {{
        var prev = document.getElementById(prevId);
        if (prev) {{
          prev.focus();
          prev.value = '';
        }}
      }}
    }}

    function startSnitchOtpTimer() {{
      var sec = 28;
      var timerTxt = document.getElementById('snitchTimerTxt');
      var countdown = document.getElementById('snitchCountdown');
      var resendBtn = document.getElementById('snitchResendBtn');
      if (timerTxt) timerTxt.style.display = 'inline';
      if (resendBtn) resendBtn.style.display = 'none';
      
      clearInterval(snitchOtpInterval);
      snitchOtpInterval = setInterval(function() {{
        sec--;
        if (sec <= 0) {{
          clearInterval(snitchOtpInterval);
          if (timerTxt) timerTxt.style.display = 'none';
          if (resendBtn) resendBtn.style.display = 'inline';
        }} else {{
          if (countdown) countdown.textContent = '0:' + (sec < 10 ? '0' : '') + sec;
        }}
      }}, 1000);
    }}

    function snitchResendOtp() {{
      var inp = document.getElementById('snitchMobileInput');
      var phone = inp ? inp.value.trim() : '';
      alert('New VIP OTP dispatched to +91 ' + phone + ' via SMS & WhatsApp!');
      startSnitchOtpTimer();
    }}

    function verifySnitchOtp() {{
      clearInterval(snitchOtpInterval);
      var inp = document.getElementById('snitchMobileInput');
      var phone = (inp && inp.value.trim()) ? inp.value.trim() : '9988898845';
      snitchCurrentUser = {{
        phone: '+91 ' + phone,
        loggedInAt: new Date().toISOString(),
        tier: 'Atelier Privé VIP'
      }};
      try {{
        localStorage.setItem('meenu_vip_user', JSON.stringify(snitchCurrentUser));
      }} catch(e) {{}}
      
      updateAccountHeaderIcon();
      
      var o = document.getElementById('loginStepOtp');
      var v = document.getElementById('loginStepVip');
      if (o) o.style.display = 'none';
      if (v) v.style.display = 'block';
      var u = document.getElementById('snitchVipUserDisplay');
      if (u) u.textContent = snitchCurrentUser.phone;
      
      showToast('✓ Welcome back, ' + snitchCurrentUser.phone + '! VIP Atelier privileges unlocked.');
    }}

    function signOutSnitchUser() {{
      snitchCurrentUser = null;
      try {{
        localStorage.removeItem('meenu_vip_user');
      }} catch(e) {{}}
      updateAccountHeaderIcon();
      
      var p = document.getElementById('loginStepPhone');
      var v = document.getElementById('loginStepVip');
      if (v) v.style.display = 'none';
      if (p) p.style.display = 'block';
      var inp = document.getElementById('snitchMobileInput');
      if (inp) {{
        inp.value = '';
        inp.focus();
      }}
      showToast('Signed out successfully.');
    }}
"""

if js_target_start != -1 and js_target_end != -1:
    code = code[:js_target_start] + snitch_login_js + "\n\n    " + code[js_target_end:]
    print("Replaced account modal JavaScript with Snitch authentication logic.")
else:
    print(f"ERROR: Could not find JS positions: start={js_target_start}, end={js_target_end}")

# Also call updateAccountHeaderIcon() on page load
if "updateAccountHeaderIcon();" not in code:
    code = code.replace("window.onload = function() {", "window.onload = function() {\n      updateAccountHeaderIcon();")
    print("Called updateAccountHeaderIcon() on window.onload.")

with open('scratch/build_snitch_storefront.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved scratch/build_snitch_storefront.py successfully!")
