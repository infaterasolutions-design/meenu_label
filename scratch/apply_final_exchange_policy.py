import re

# Precise, protective, boutique atelier policy
final_exchange_text = """### Handcrafted Precision & Sizing Guarantee
At **Meenu Label**, every silhouette undergoes a rigorous 3-point atelier inspection prior to packing: each piece is individually verified against standard Indian pret measurements (Bust, Waist, and Hip in inches).

**Our Guarantee:**  
When you order Size M, we guarantee that you receive an exact, verified Size M—never an incorrect or substitute size.

---

### Built-in Atelier Margins (Instant Local Personalization)
Every woman’s body proportion is uniquely beautiful, and personal ease preferences vary. 

Shipping garments back and forth across India takes 7–10 days and is inconvenient for both you and our atelier. Therefore, all Meenu Label tunics and trousers are thoughtfully tailored with **generous 1.5 to 2-inch internal side seam allowances** and relaxed comfort waistbands.

This allows any minor personal comfort adjustments (tightening or loosening a seam) to be completed effortlessly and instantly by your trusted local tailor in minutes, without the hassle of waiting for courier exchanges.

---

### Strict Exchange Eligibility: When Do We Exchange?

We entertain exchanges **STRICTLY and EXCLUSIVELY in the event of an atelier dispatch discrepancy or transit damage:**

#### 1. Wrong Size or Incorrect Silhouette Delivered (Our Mistake)
If our dispatch team mistakenly delivered a size or style different from what was confirmed on your invoice (e.g., you ordered Size M, but received Size L):
* We provide a **100% Free Doorstep Replacement**.
* We schedule an immediate reverse pickup and re-dispatch the correct verified size at **zero additional cost to you**.

#### 2. Manufacturing Defect or Transit Damage
In the rare event that an item arrives with a genuine manufacturing flaw or transit damage:
* Notify our concierge within **48 hours of delivery** via WhatsApp or email (**care@meenulabel.in**) with an unboxing video or photographs.
* Upon quick verification, an immediate priority replacement will be dispatched.

---

### Final Sale Notice (No Returns for Subjective Fit Preferences)
Because Meenu Label operates on strictly limited small-batch collections (strictly 3 pieces crafted per size nationwide) and provides comprehensive measurement charts prior to checkout:
* **All silhouettes delivered accurately as per the confirmed order size are Final Sale.**
* We do **not** accept returns or exchanges for subjective fit preferences, styling changes of mind, or post-event wear.
* Please consult our detailed **Size Guide** on the product page before placing your order. Our atelier concierge is also available on WhatsApp to verify your exact measurements before you purchase.
"""

# 1. Update Meenu_Label_Official_Policies.md
md_path = r"C:\Users\sande\Downloads\Meenu_Label_Official_Policies.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

sec3_pattern = r"## 3\. RETURN & EXCHANGE POLICY.*?(?=## 4\. TERMS OF SERVICE)"
md_content = re.sub(sec3_pattern, "## 3. RETURN & EXCHANGE POLICY\n\n" + final_exchange_text + "\n---\n\n", md_content, flags=re.DOTALL)
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
print("Updated Meenu_Label_Official_Policies.md")

# 2. Update Meenu_Label_Policies_Shopify_Ready.html
html_ready_path = r"C:\Users\sande\Downloads\Meenu_Label_Policies_Shopify_Ready.html"
with open(html_ready_path, "r", encoding="utf-8") as f:
    ready_content = f.read()

final_exchange_html = """      <h3>Handcrafted Precision & Sizing Guarantee</h3>
      <p>At <strong>Meenu Label</strong>, every silhouette undergoes a rigorous 3-point atelier inspection prior to packing: each piece is individually verified against standard Indian pret measurements (Bust, Waist, and Hip in inches).</p>
      
      <p><strong>Our Guarantee:</strong> When you order Size M, we guarantee that you receive an exact, verified Size M—never an incorrect or substitute size.</p>

      <h3>Built-in Atelier Margins (Instant Local Personalization)</h3>
      <p>Every woman’s body proportion is uniquely beautiful, and personal ease preferences vary. Shipping garments back and forth across India takes 7–10 days and is inconvenient for both you and our atelier.</p>
      <p>Therefore, all Meenu Label tunics and trousers are thoughtfully tailored with <strong>generous 1.5 to 2-inch internal side seam allowances</strong> and relaxed comfort waistbands. This allows any minor personal fit adjustments (loosening or tightening) to be completed effortlessly and instantly by your trusted local tailor in minutes.</p>

      <h3>Strict Exchange Eligibility: When Do We Exchange?</h3>
      <p>We entertain exchanges <strong>strictly and exclusively</strong> in the event of an atelier dispatch discrepancy or transit damage:</p>
      
      <h4>1. Wrong Size or Incorrect Silhouette Delivered (Our Mistake)</h4>
      <p>If our dispatch team mistakenly delivered a size or style different from what was confirmed on your invoice (e.g., you ordered Size M, but received Size L):</p>
      <ul>
        <li>We provide a <strong>100% Free Doorstep Replacement</strong> at zero extra cost.</li>
        <li>We arrange immediate reverse pickup from your doorstep and priority re-dispatch.</li>
      </ul>

      <h4>2. Manufacturing Defect or Transit Damage</h4>
      <p>In the rare event that an item arrives with a genuine manufacturing flaw or transit damage, notify us within <strong>48 hours of delivery</strong> via WhatsApp or email (<strong>care@meenulabel.in</strong>) with an unboxing video or photographs for an immediate priority replacement.</p>

      <h3>Final Sale Notice (No Returns for Subjective Fit Preferences)</h3>
      <p>Because Meenu Label operates on strictly limited small-batch collections (strictly 3 pieces crafted per size nationwide) and provides comprehensive measurement charts prior to checkout:</p>
      <ul>
        <li><strong>All silhouettes delivered accurately as per the confirmed order size are Final Sale.</strong></li>
        <li>We do not accept returns or exchanges for subjective personal fit preferences, styling changes of mind, or post-event wear.</li>
        <li>Please consult our detailed <strong>Size Guide</strong> on the product page before placing your order, or chat with our atelier concierge on WhatsApp to verify your exact measurements before purchasing.</li>
      </ul>"""

ready_target = re.search(r'<div id="secReturns">.*?</div>\s*</div>', ready_content, re.DOTALL)
if ready_target:
    ready_content = ready_content[:ready_target.start()] + '<div id="secReturns">\n' + final_exchange_html + '\n    </div>\n  </div>' + ready_content[ready_target.end():]
    with open(html_ready_path, "w", encoding="utf-8") as f:
        f.write(ready_content)
    print("Updated Meenu_Label_Policies_Shopify_Ready.html")

# 3. Update Meenu_Label_Desktop_Storefront.html modal JS
storefront_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(storefront_path, "r", encoding="utf-8") as f:
    sf_content = f.read()

sf_exchange_js_html = final_exchange_html.replace('"', '\\"').replace('\n', '')

sf_target_pattern = r'exchange:\s*\{\s*title:\s*"[^"]*",\s*html:\s*"[^"]*"\s*\}'
sf_replacement = f'exchange: {{\n        title: "Atelier Sizing Guarantee & Exchange Terms",\n        html: "{sf_exchange_js_html}"\n      }}'

sf_content = re.sub(sf_target_pattern, sf_replacement, sf_content)
with open(storefront_path, "w", encoding="utf-8") as f:
    f.write(sf_content)

print("SUCCESS: Updated Meenu_Label_Desktop_Storefront.html with Final Protected Exchange Policy!")
