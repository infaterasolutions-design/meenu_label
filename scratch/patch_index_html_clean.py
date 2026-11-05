import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

new_index_card = """<div class="snitch-login-card">
          <!-- Dual Luxury Tabs: Track My Order | VIP Concierge -->
          <div class="account-modal-tabs">
            <button type="button" class="account-modal-tab active" id="tabBtnTrack" onclick="switchAccountTab('track')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
              Track My Order
            </button>
            <button type="button" class="account-modal-tab" id="tabBtnConcierge" onclick="switchAccountTab('concierge')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
              VIP Concierge
            </button>
          </div>

          <!-- TAB 1: INSTANT ORDER TRACKING (ZERO FRICTION) -->
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

          <!-- TAB 2: VIP CONCIERGE & PRIVILEGES (ZERO FRICTION) -->
          <div id="accountViewConcierge" class="account-view" style="display:none; text-align:center;">
            <div class="snitch-vip-avatar">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
              </svg>
            </div>
            <div class="snitch-vip-status-tag">&#10024; ATELIER PRIV&Eacute; CLIENT CARE</div>
            <h3 class="snitch-vip-user" style="font-size:18px; margin: 4px 0 16px;">Direct Atelier Assistance</h3>

            <div class="snitch-vip-perks">
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#128666;</div>
                <div class="snitch-perk-text">
                  <strong>Free 24-Hr Tricity Delivery</strong>
                  <span>Direct express courier across Chandigarh, Mohali &amp; Panchkula</span>
                </div>
              </div>
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#128087;</div>
                <div class="snitch-perk-text">
                  <strong>VIP Atelier Suite Fittings</strong>
                  <span>Private trial room appointments at Sector 17, Chandigarh</span>
                </div>
              </div>
              <div class="snitch-perk-item">
                <div class="snitch-perk-icon">&#9986;&#65039;</div>
                <div class="snitch-perk-text">
                  <strong>Bespoke Customization</strong>
                  <span>Sleeve &amp; neckline tailoring, or urgent dispatch coordination</span>
                </div>
              </div>
            </div>

            <div class="snitch-vip-actions">
              <a href="https://wa.me/918511616133?text=Hi%20Meenu%20Label%2C%20I%20would%20like%20direct%20styling%20and%20order%20assistance." target="_blank" class="shipment-wa-btn" style="margin-top: 10px; margin-bottom: 14px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.073.043.419-.101.824z"/></svg>
                Chat on WhatsApp (+91 85116 16133)
              </a>

              <!-- Official Shopify Account Link -->
              <div style="margin: 14px 0 10px; display: flex; align-items: center; text-align: center; color: rgba(255,255,255,0.3); font-size: 11px;">
                <span style="flex: 1; border-bottom: 1px solid rgba(255,255,255,0.15);"></span>
                <span style="padding: 0 10px; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4);">PAST ORDERS &amp; INVOICES</span>
                <span style="flex: 1; border-bottom: 1px solid rgba(255,255,255,0.15);"></span>
              </div>

              <a href="javascript:void(0)" onclick="alert('Shopify Account Login redirects to /account on live Shopify store.')" class="snitch-shopify-login-link" style="display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; padding: 11px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); border-radius: 6px; color: #FAF8F5; text-decoration: none; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; transition: all 0.2s ease;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7.5" r="4"></circle></svg>
                Official Shopify Account Portal &rarr;
              </a>

              <button type="button" class="snitch-submit-btn" style="margin-top: 14px; background: rgba(255,255,255,0.08); color:#FAF8F5;" onclick="closeAccountModalDirect()">
                <span>CONTINUE SHOPPING</span>
              </button>
            </div>
          </div>
        </div>"""

# Exact replacement of modal card in HTML
p1 = h.find('<div class="snitch-login-card">')
p2 = h.find('<!-- Size Guide Modal -->')
trailer = '      </div>\n    </div>\n  </div>\n\n  '

h = h[:p1] + new_index_card + "\n" + trailer + h[p2:]
print("Updated modal card in index.html")

# Replace JS logic in index.html
js_frictionless = """/* =========================================================================
   TRACK MY ORDER & VIP ATELIER CONCIERGE DRAWER SYSTEM
   ========================================================================= */

function switchAccountTab(tabName) {
  var tabTrack = document.getElementById('tabBtnTrack');
  var tabConcierge = document.getElementById('tabBtnConcierge');
  var viewTrack = document.getElementById('accountViewTrack');
  var viewConcierge = document.getElementById('accountViewConcierge');

  if (tabTrack) tabTrack.classList.toggle('active', tabName === 'track');
  if (tabConcierge) tabConcierge.classList.toggle('active', tabName === 'concierge');

  if (viewTrack) {
    viewTrack.classList.toggle('active', tabName === 'track');
    viewTrack.style.display = tabName === 'track' ? 'block' : 'none';
  }
  if (viewConcierge) {
    viewConcierge.classList.toggle('active', tabName === 'concierge');
    viewConcierge.style.display = tabName === 'concierge' ? 'block' : 'none';
  }

  if (tabName === 'track') {
    setTimeout(function() {
      var inp = document.getElementById('orderTrackingInput');
      if (inp) inp.focus();
    }, 150);
  }
}

function openAccountModal(initialTab) {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (!backdrop) return;
  backdrop.classList.add('open');
  switchAccountTab(initialTab || 'track');
}

function closeAccountModalDirect() {
  var backdrop = document.getElementById('accountModalBackdrop');
  if (backdrop) backdrop.classList.remove('open');
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
}"""

j1 = h.find('var snitchCurrentUser = null;')
j2 = h.find('function searchProducts() {')
if j1 != -1 and j2 != -1:
    h = h[:j1] + js_frictionless + "\n\n    " + h[j2:]
    print("Replaced JS in index.html")

# Update nav-drawer and footer links in index.html
index_nav_old = """          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('login');" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Login / Account</a>
          </li>"""
index_nav_new = """          <li>
            <a href="javascript:void(0)" onclick="closeNavDrawer(); openAccountModal('concierge');" style="color:var(--accent-gold); font-weight:700;">&#128100; VIP Atelier Concierge</a>
          </li>"""
if index_nav_old in h:
    h = h.replace(index_nav_old, index_nav_new)
    print("Updated nav drawer in index.html")

foot_old = """        <li><a href="javascript:void(0)" onclick="openAccountModal('login')">&#128100; VIP Atelier Account</a></li>"""
foot_new = """        <li><a href="javascript:void(0)" onclick="openAccountModal('concierge')">&#128100; VIP Atelier Concierge</a></li>"""
if foot_old in h:
    h = h.replace(foot_old, foot_new)
    print("Updated footer in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

print("index.html fully updated!")
