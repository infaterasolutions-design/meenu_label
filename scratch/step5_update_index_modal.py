import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

card_start = '<div class="snitch-login-card">'
card_end = '<!-- Size Guide Modal -->'

idx1 = h.find(card_start)
idx2 = h.find(card_end)

if idx1 == -1 or idx2 == -1:
    print(f"Error: Markers not found: start={idx1}, end={idx2}")
    sys.exit(1)

# Find the end of the snitch-login-card:
# Just before <!-- Size Guide Modal --> there are 4 closing </div>s:
# </div> (card)
# </div> (content)
# </div> (dialog)
# </div> (backdrop)
# Let's locate the exact closing </div> of snitch-login-card.
sub = h[idx1:idx2]
# We want to replace from '<div class="snitch-login-card">' up to the </div> before '</div>\n    </div>\n  </div>\n\n  <!-- Size Guide Modal -->'
# Let's check the ending of sub:
print("End of sub snippet:")
print(repr(sub[-60:]))

new_card_content = """<div class="snitch-login-card">
          <!-- Dual Tabs: Track My Order | VIP Privé / Login -->
          <div class="account-modal-tabs">
            <button type="button" class="account-modal-tab active" id="tabBtnTrack" onclick="switchAccountTab('track')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
              Track My Order
            </button>
            <button type="button" class="account-modal-tab" id="tabBtnLogin" onclick="switchAccountTab('login')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7.5" r="4"></circle></svg>
              VIP Privé / Login
            </button>
          </div>

          <!-- TAB 1: TRACK MY ORDER VIEW -->
          <div id="accountViewTrack" class="account-view active">
            <div class="snitch-brand-block" style="margin-bottom: 16px;">
              <h2 class="snitch-brand-title">MEENU LABEL</h2>
              <div class="snitch-brand-tag">EXPRESS ORDER TRACKING &bull; TRICITY &amp; ALL INDIA</div>
            </div>

            <label class="snitch-input-heading" for="orderTrackingInput">ENTER ORDER NUMBER OR MOBILE</label>
            <div class="tracking-input-wrap">
              <input 
                type="text" 
                id="orderTrackingInput" 
                class="tracking-input-field" 
                placeholder="e.g. #ML-1042 or 9876543210" 
                autocomplete="off"
                onkeydown="if(event.key==='Enter') executeOrderTracking()"
              >
              <div class="tracking-demo-chips">
                <span>Quick Demo:</span>
                <button type="button" class="tracking-demo-chip" onclick="fillAndTrackDemo('#ML-1042')">#ML-1042 (In Transit)</button>
                <button type="button" class="tracking-demo-chip" onclick="fillAndTrackDemo('#ML-1035')">#ML-1035 (Delivered)</button>
              </div>
            </div>
            <div id="orderTrackingError" class="snitch-validation-error" style="display:none; margin-bottom:12px;">Please enter an Order ID (e.g. #ML-1042) or a 10-digit mobile number</div>

            <button class="snitch-submit-btn" id="trackOrderSubmitBtn" onclick="executeOrderTracking()">
              <span>TRACK SHIPMENT</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>

            <!-- Dynamic Shipment Result Card -->
            <div id="trackingResultContainer" style="display:none;"></div>
          </div>

          <!-- TAB 2: VIP PRIVÉ / LOGIN VIEW -->
          <div id="accountViewLogin" class="account-view" style="display:none;">
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

              <div style="margin: 18px 0 12px; display: flex; align-items: center; text-align: center; color: rgba(255,255,255,0.3); font-size: 11px;">
                <span style="flex: 1; border-bottom: 1px solid rgba(255,255,255,0.15);"></span>
                <span style="padding: 0 10px; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">OR VIA SHOPIFY</span>
                <span style="flex: 1; border-bottom: 1px solid rgba(255,255,255,0.15);"></span>
              </div>

              <a href="javascript:void(0)" onclick="alert('Shopify Account Login redirects to /account on live Shopify store.')" class="snitch-shopify-login-link" style="display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; padding: 12px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); border-radius: 6px; color: #FAF8F5; text-decoration: none; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; transition: all 0.2s ease;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7.5" r="4"></circle></svg>
                Official Shopify Account Login &rarr;
              </a>

              <p class="snitch-legal-note" style="margin-top: 14px;">
                By continuing, you agree to MEENU LABEL's 
                <a href="javascript:void(0)" onclick="closeAccountModalDirect(); openPolicyModal('privacy');">Terms &amp; Privacy Policy</a>
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
              <h3 class="snitch-vip-user" id="snitchVipUserDisplay">+91 85116 16133</h3>

              <!-- Atelier Orders List -->
              <div class="vip-recent-orders-block">
                <div class="vip-recent-orders-title">
                  <span>Atelier Orders</span>
                  <span style="font-size:10px; color:rgba(255,255,255,0.4);">2 Records</span>
                </div>
                <div class="vip-order-row">
                  <div class="vip-order-info">
                    <strong>#ML-1042</strong> &bull; Gulab Organza Set
                    <div class="vip-order-date">Dispatched &bull; Delhivery Express</div>
                  </div>
                  <button type="button" class="vip-order-track-btn" onclick="fillAndTrackDemo('#ML-1042')">Track</button>
                </div>
                <div class="vip-order-row">
                  <div class="vip-order-info">
                    <strong>#ML-1035</strong> &bull; Noor Zari Silk Set
                    <div class="vip-order-date">Delivered &bull; Chandigarh Suite</div>
                  </div>
                  <button type="button" class="vip-order-track-btn" onclick="fillAndTrackDemo('#ML-1035')">Track</button>
                </div>
              </div>

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
                <a href="https://wa.me/918511616133?text=Hi%20Meenu%20Label%2C%20I%20am%20a%20VIP%20member%20inquiring%20about%20my%20orders." target="_blank" class="snitch-vip-concierge-btn">
                  &#128172; Open Master Stylist WhatsApp Concierge
                </a>
                <button type="button" class="snitch-signout-btn" onclick="signOutSnitchUser()">Sign Out / Change Account</button>
              </div>
            </div>
          </div>
        </div>"""

# Find the exact closing tags before <!-- Size Guide Modal -->
# Look backwards from idx2 for </div>\n      </div>\n    </div>\n  </div>
closing_marker = '        </div>\n      </div>\n    </div>\n  </div>\n\n  <!-- Size Guide Modal -->'
idx_close = h.find(closing_marker)
if idx_close != -1:
    h = h[:idx1] + new_card_content + h[idx_close + len('        </div>'):]
    print("Replaced snitch-login-card in index.html successfully")
else:
    print("Could not find exact closing marker, trying flexible replacement")
    card_closing = '            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <!-- Size Guide Modal -->'
    idx_close = h.find(card_closing)
    if idx_close != -1:
        # The card ends at idx_close + len('            </div>\n          </div>\n        </div>')
        h = h[:idx1] + new_card_content + h[idx_close + len('            </div>\n          </div>\n        </div>'):]
        print("Replaced with flexible closing marker!")

# Update nav-drawer link in index.html
old_nav_link = """          <li style="border-top:1px solid var(--border-color); margin-top:18px; padding-top:18px;">
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal();" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a>
          </li>"""

new_nav_link = """          <li style="border-top:1px solid var(--border-color); margin-top:18px; padding-top:18px;">
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('track');" style="color:var(--accent-gold); font-weight:700;">&#128230; Track My Order</a>
          </li>
          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('login');" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a>
          </li>"""

if old_nav_link in h:
    h = h.replace(old_nav_link, new_nav_link)
    print("Updated nav drawer in index.html")
else:
    print("Nav drawer link already updated or not found")

# Update footer links in index.html
old_footer = """        <h4>Client Care</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="openSizeGuide()">Size & Fit Guide (M-XL)</a></li>"""

new_footer = """        <h4>Client Care</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="openAccountModal('track')">&#128230; Track My Order</a></li>
          <li><a href="javascript:void(0)" onclick="openAccountModal('login')">&#128100; VIP Atelier Account</a></li>
          <li><a href="javascript:void(0)" onclick="openSizeGuide()">Size & Fit Guide (M-XL)</a></li>"""

if old_footer in h:
    h = h.replace(old_footer, new_footer)
    print("Updated footer in index.html")
else:
    print("Footer client care already updated or not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)
print("Finished updating index.html")
