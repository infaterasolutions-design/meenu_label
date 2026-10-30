import re

html_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Policy Modal CSS
policy_css = """
    /* Interactive Policy Modal */
    .policy-modal-card {
      background: #FFFFFF;
      max-width: 720px;
      width: 92vw;
      max-height: 85vh;
      border-radius: 8px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 40px rgba(0,0,0,0.25);
      border: 1px solid var(--border-color);
    }
    .policy-modal-header {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .policy-modal-body {
      padding: 24px 28px;
      overflow-y: auto;
      font-size: 13.5px;
      line-height: 1.7;
      color: #3A352F;
    }
    .policy-modal-body h3 {
      font-size: 14.5px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #1E1C19;
      margin-top: 18px;
      margin-bottom: 6px;
    }
    .policy-modal-body ul, .policy-modal-body ol {
      padding-left: 20px;
      margin: 8px 0;
    }
    .policy-modal-body li {
      margin-bottom: 6px;
    }
"""

css_anchor = "/* ==================== DEDICATED FULL CART PAGE STYLES ==================== */"
if css_anchor in content:
    content = content.replace(css_anchor, policy_css + "\n    " + css_anchor, 1)
    print("Added Policy Modal CSS")

# 2. Update Footer Client Care Links
old_client_care = """      <div class="footer-col">
        <h4>Client Care</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="openSizeGuide()">Size & Fit Guide (M-XL)</a></li>
          <li><a href="javascript:void(0)">7-Day Exchange Policy</a></li>
          <li><a href="javascript:void(0)">Tricity 24-Hr Dispatch</a></li>
          <li><a href="mailto:meenulabel24@gmail.com">meenulabel24@gmail.com</a></li>
          <li><a href="https://wa.me/919988898845" target="_blank">WhatsApp Concierge</a></li>
        </ul>
      </div>"""

new_client_care = """      <div class="footer-col">
        <h4>Client Care</h4>
        <ul>
          <li><a href="javascript:void(0)" onclick="openPolicyModal('about')">About Us (Our Story)</a></li>
          <li><a href="javascript:void(0)" onclick="openPolicyModal('shipping')">Shipping & Delivery Policy</a></li>
          <li><a href="javascript:void(0)" onclick="openPolicyModal('exchange')">7-Day Exchange & Returns</a></li>
          <li><a href="javascript:void(0)" onclick="openPolicyModal('privacy')">Privacy Policy & Terms</a></li>
          <li><a href="javascript:void(0)" onclick="openPolicyModal('contact')">Contact & Grievance Redressal</a></li>
        </ul>
      </div>"""

if old_client_care in content:
    content = content.replace(old_client_care, new_client_care, 1)
    print("Updated footer links to openPolicyModal()")

# 3. Add Policy Modal HTML right before closing </body>
policy_modal_html = """
  <!-- Interactive Policy Modal Backdrop & Card -->
  <div class="modal-backdrop" id="policyModalBackdrop" onclick="closePolicyModalOnBackdrop(event)">
    <div class="policy-modal-card">
      <div class="policy-modal-header">
        <h2 id="policyModalTitle" style="font-family:'Cormorant Garamond', serif; font-size:26px; margin:0; color:#1E1C19;">Store Policy</h2>
        <button onclick="closePolicyModal()" style="font-size:20px; background:none; border:none; cursor:pointer; color:#1E1C19; padding:4px 8px;">✕</button>
      </div>
      <div class="policy-modal-body" id="policyModalContent">
        <!-- Content injected dynamically -->
      </div>
    </div>
  </div>
</body>"""

content = content.replace("</body>", policy_modal_html, 1)
print("Inserted Policy Modal HTML")

# 4. Add JS functions and policy text dictionary
policy_js = """
    var STORE_POLICIES = {
      about: {
        title: "About Us • The Meenu Label Story",
        html: "<h3>Handcrafted in Chandigarh. Inspired by Grace.</h3><p>Meenu Label is a contemporary designer pret atelier born in Chandigarh, dedicated to crafting breathable, modern silhouettes for women across India.</p><p>The label was founded by Sandeep Singh and named with deep affection after his sister, <strong>Meenu</strong>—embodying a family commitment to thoughtfulness, warmth, and artisanal integrity.</p><h3>Why We Exist</h3><p>For too long, modern women in India have had to settle between stiff, synthetic fast-fashion that wrinkles in hours, or heavy, uncomfortable traditional wear that cannot be worn beyond a single festive celebration.</p><p>We created <strong>Meenu Label</strong> to provide an effortless middle ground:</p><ul><li><strong>100% Pure, Breathable Textiles:</strong> We work exclusively with rich Jaipur cottons, soft muslins, fluid silk crepes, and authentic Chanderi silks. Zero synthetic friction.</li><li><strong>Thoughtful, Functional Tailoring:</strong> Every bottom silhouette features deep, functional pockets that securely hold your smartphone. Tunics and kurtas feature relaxed comfort waistbands and modest, flattering hemlines designed for all-day ease.</li><li><strong>Strict Atelier Scarcity:</strong> We reject mass factory production. Drop 01 is produced in strictly small batches (only 3 pieces per size nationwide) to preserve individuality and minimize textile waste.</li></ul><p><em>From morning work meetings and cafe brunches to intimate evening celebrations, Meenu Label pieces are made to move with you in effortless grace.</em></p>"
      },
      shipping: {
        title: "Shipping & Delivery Policy",
        html: "<h3>Pan-India Priority Dispatch</h3><p>Every Meenu Label garment is hand-inspected, steam-pressed, wrapped in protective butter paper, and packed in our signature atelier box before dispatch from our Chandigarh warehouse.</p><h3>Delivery Timelines</h3><ul><li><strong>Chandigarh Tricity (Chandigarh, Mohali, Panchkula):</strong> 24 to 48 Hours Priority Express Delivery.</li><li><strong>Metro Cities (Delhi-NCR, Mumbai, Bengaluru, Jaipur, Hyderabad, Pune, Kolkata):</strong> 2 to 4 Business Days.</li><li><strong>Rest of India:</strong> 3 to 6 Business Days across 26,000+ serviceable pincodes.</li></ul><h3>Shipping Charges</h3><ul><li><strong>Prepaid Orders (UPI, GPay, PhonePe, Cards, NetBanking):</strong> 100% FREE Express Delivery across India.</li><li><strong>Prepaid Perk:</strong> Enjoy instant ₹100 discount auto-applied at checkout on all online payments.</li></ul><h3>Cash on Delivery (COD) Terms</h3><p>Cash on Delivery is available across all serviceable Indian pincodes. To prevent transit cancellations, all COD orders undergo automated WhatsApp / Phone OTP verification prior to dispatch.</p><h3>Order Tracking</h3><p>As soon as your package is dispatched, you will receive an automated tracking link via SMS and WhatsApp with your Air Waybill (AWB) number and live tracking updates via BlueDart, Delhivery, or Shiprocket.</p>"
      },
      exchange: {
        title: "7-Day Return & Exchange Policy",
        html: "<h3>7-Day Hassle-Free Size Exchange</h3><p>We want you to love how you feel in Meenu Label. If a garment does not fit you perfectly, we offer an effortless <strong>7-Day Doorstep Exchange Policy</strong> from the date of delivery.</p><h3>How to Initiate an Exchange</h3><ol><li>Contact our concierge via WhatsApp or email <strong>care@meenulabel.in</strong> with your Order ID and required size (M, L, XL).</li><li>Our courier partner will arrange a complimentary reverse pickup from your doorstep.</li><li>Once pickup is verified, your new size is dispatched immediately.</li></ol><h3>Conditions for Exchange / Return</h3><ul><li>The garment must be unworn, unwashed, and in original pristine condition with all tags attached.</li><li>Must include original atelier packaging and butter paper wrap.</li><li>Pieces showing makeup stains, perfume odors, or signs of wear cannot be accepted due to hygiene standards.</li></ul><h3>Damaged or Defective Silhouettes</h3><p>Every piece undergoes a 3-tier quality inspection. In the rare case of transit damage or defect, notify us within <strong>48 hours of delivery</strong> with unboxing photos/video for an immediate priority replacement or a 100% full refund.</p><h3>Refund Timelines</h3><ul><li><strong>Prepaid Orders:</strong> Refunded directly to your original payment method (Bank/UPI/Card) within 5–7 business days after passing quality inspection.</li><li><strong>COD Orders:</strong> Refunded via direct IMPS/NEFT bank transfer (customer provides account details) or as lifetime store credit vouchers.</li></ul>"
      },
      privacy: {
        title: "Privacy Policy & Terms of Service",
        html: "<h3>Customer Data Protection</h3><p>We value your trust and protect your personal information in strict accordance with the Information Technology Act, 2000 and the Digital Personal Data Protection Act.</p><h3>Information We Collect</h3><p>We collect your Name, Shipping Address, Phone Number, and Email solely to process orders and provide delivery tracking via SMS/WhatsApp.</p><h3>Zero Payment Card Storage</h3><p>We do not store your credit/debit card numbers, CVVs, or UPI PINs. All transactions are routed through RBI-authorized, PCI-DSS certified payment gateways (Razorpay, Cashfree, PhonePe).</p><p>We never sell, rent, or trade your personal data with third-party advertising brokers.</p><h3>Operating Entity</h3><p>This website is owned and operated by <strong>Infatera Software Solutions OPC Pvt. Ltd.</strong> throughout India. All prices are in Indian Rupees (INR) and inclusive of applicable 5% GST.</p>"
      },
      contact: {
        title: "Contact Us & Grievance Redressal",
        html: "<h3>Official Atelier & Entity Details</h3><ul><li><strong>Brand:</strong> Meenu Label</li><li><strong>Parent Entity:</strong> Infatera Software Solutions OPC Pvt. Ltd.</li><li><strong>Registered Office:</strong> Chandigarh, Punjab & Haryana, India</li><li><strong>Support Email:</strong> care@meenulabel.in</li><li><strong>Support Hours:</strong> Monday – Saturday | 10:00 AM – 7:00 PM IST</li></ul><h3>Designated Grievance Redressal Officer</h3><p>In accordance with the Consumer Protection (E-Commerce) Rules, 2020:</p><ul><li><strong>Officer Name:</strong> Sandeep Singh</li><li><strong>Designation:</strong> Grievance Redressal Officer</li><li><strong>Email:</strong> grievance@meenulabel.in / care@meenulabel.in</li><li><strong>Redressal Timeline:</strong> Grievances acknowledged within 48 hours; resolved within 30 days.</li></ul>"
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
"""

js_target = "function proceedToCheckout() {"
content = content.replace(js_target, policy_js + "\n    " + js_target, 1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Policy modal integrated into Meenu_Label_Desktop_Storefront.html")
