import re

# New smart, firm, and high-trust policy text
smart_exchange_text = """### Our Commitment to Precision & Sizing Integrity
Every woman’s body is beautifully unique, and ready-to-wear silhouettes naturally drape differently on different body shapes. 

At **Meenu Label**, every silhouette undergoes a rigorous 3-point atelier inspection prior to packing: each piece is individually verified against standard Indian pret measurements (Bust, Waist, and Hip in inches).

**Our Delivery Assurance:**  
When you order Size M, we guarantee that you receive an exact, quality-verified Size M—never a mislabeled or substitute size.

---

### When Is an Exchange Applicable?

#### 1. In the Event of Dispatch Discrepancy or Defect (Our Responsibility)
If our dispatch team mistakenly sent you a wrong size, an incorrect silhouette, or an item with a manufacturing defect:
* We provide a **100% Complimentary Doorstep Replacement**.
* We arrange immediate reverse pickup from your address and dispatch the correct garment at **zero additional cost to you**.
* *Requirement:* Simply report the issue within **48 hours of delivery** via WhatsApp Concierge or email (**care@meenulabel.in**) with a brief unboxing photo or video.

#### 2. Size Exchange for Personal Comfort (Subject to Batch Availability)
We strongly advise reviewing our detailed **Measurement Size Guide** (provided on every product page) before ordering. 
* If you find that you prefer a different size for your personal comfort, we facilitate a **one-time size exchange** within **5 days of delivery**, strictly subject to stock availability in our small-batch inventory.
* If your required exchange size is sold out due to limited atelier quantities, we will issue a **Lifetime Store Credit Voucher** to choose any other silhouette from our current or upcoming drops.

---

### Terms & Non-Eligibility (Anti-Abuse Clause)
Because Meenu Label operates on strict small-batch craftsmanship (only 3 pieces produced per size nationwide) rather than mass industrial inventory, we do not entertain frivolous return abuse or post-event returns:
* **Condition:** Garments must be strictly **unworn, unwashed, unaltered, and free of perfume, deodorant, or makeup marks**, with all original brand tags and atelier packaging intact.
* **No Change-of-Mind Cash Refunds:** Silhouettes crafted and delivered accurately as ordered are eligible for size exchanges or store credit only. Cash refunds are reserved exclusively for genuine transit damage or dispatch discrepancies that cannot be replaced.
"""

# 1. Update Meenu_Label_Official_Policies.md
md_path = r"C:\Users\sande\Downloads\Meenu_Label_Official_Policies.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace Section 3 in MD
sec3_pattern = r"## 3\. RETURN & EXCHANGE POLICY.*?(?=## 4\. TERMS OF SERVICE)"
md_content = re.sub(sec3_pattern, "## 3. RETURN & EXCHANGE POLICY\n\n" + smart_exchange_text + "\n---\n\n", md_content, flags=re.DOTALL)
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
print("Updated Meenu_Label_Official_Policies.md")

# 2. Update Meenu_Label_Policies_Shopify_Ready.html
html_ready_path = r"C:\Users\sande\Downloads\Meenu_Label_Policies_Shopify_Ready.html"
with open(html_ready_path, "r", encoding="utf-8") as f:
    ready_content = f.read()

smart_exchange_html = """      <h3>Our Commitment to Precision & Sizing Integrity</h3>
      <p>Every woman’s body is beautifully unique, and ready-to-wear silhouettes naturally drape differently on different body shapes.</p>
      <p>At <strong>Meenu Label</strong>, every silhouette undergoes a rigorous 3-point atelier inspection prior to packing: each piece is individually verified against standard Indian pret measurements (Bust, Waist, and Hip in inches).</p>
      
      <p><strong>Our Delivery Assurance:</strong> When you order Size M, we guarantee that you receive an exact, quality-verified Size M—never a mislabeled or substitute size.</p>

      <h3>When Is an Exchange Applicable?</h3>
      
      <h4>1. In the Event of Dispatch Discrepancy or Defect (Our Responsibility)</h4>
      <p>If our dispatch team mistakenly sent you a wrong size, an incorrect silhouette, or an item with a transit defect:</p>
      <ul>
        <li>We provide a <strong>100% Complimentary Doorstep Replacement</strong> at zero extra cost.</li>
        <li>We arrange immediate reverse pickup from your doorstep and priority re-dispatch.</li>
        <li><em>Requirement:</em> Report within <strong>48 hours of delivery</strong> via WhatsApp or email (<strong>care@meenulabel.in</strong>) with unboxing photos or video.</li>
      </ul>

      <h4>2. Size Exchange for Personal Comfort (Subject to Availability)</h4>
      <p>We strongly advise checking our detailed <strong>Measurement Size Guide</strong> before ordering. If you still require a different size for personal comfort, we facilitate a <strong>one-time size exchange within 5 days of delivery</strong>, subject to stock availability in our small-batch production.</p>
      <p>If your exchange size is sold out due to limited units, you will receive a <strong>Lifetime Store Credit Voucher</strong> for any current or future drop.</p>

      <h3>Terms & Non-Eligibility (Anti-Abuse Clause)</h3>
      <p>Because Meenu Label produces strictly small-batch designer drops (only 3 pieces per size nationwide) rather than mass factory volumes, we do not support casual return abuse:</p>
      <ul>
        <li>Garments must be strictly <strong>unworn, unwashed, unaltered, and free of perfume, makeup, or stains</strong> with all tags and atelier butter paper intact.</li>
        <li><strong>No Change-of-Mind Cash Refunds:</strong> Accurately delivered silhouettes are eligible for size exchanges or store credit. Cash refunds are reserved strictly for genuine transit damage or dispatch errors that cannot be replaced.</li>
      </ul>"""

ready_target = re.search(r'<div id="secReturns">.*?</div>\s*</div>', ready_content, re.DOTALL)
if ready_target:
    ready_content = ready_content[:ready_target.start()] + '<div id="secReturns">\n' + smart_exchange_html + '\n    </div>\n  </div>' + ready_content[ready_target.end():]
    with open(html_ready_path, "w", encoding="utf-8") as f:
        f.write(ready_content)
    print("Updated Meenu_Label_Policies_Shopify_Ready.html")
else:
    print("ERROR: secReturns not found in ready HTML")

# 3. Update Meenu_Label_Desktop_Storefront.html modal JS
storefront_path = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
with open(storefront_path, "r", encoding="utf-8") as f:
    sf_content = f.read()

sf_exchange_js_html = smart_exchange_html.replace('"', '\\"').replace('\n', '')

# Replace in STORE_POLICIES dictionary
sf_target_pattern = r'exchange:\s*\{\s*title:\s*"[^"]*",\s*html:\s*"[^"]*"\s*\}'
sf_replacement = f'exchange: {{\n        title: "Atelier Sizing Assurance & Smart Exchange Policy",\n        html: "{sf_exchange_js_html}"\n      }}'

sf_content = re.sub(sf_target_pattern, sf_replacement, sf_content)
with open(storefront_path, "w", encoding="utf-8") as f:
    f.write(sf_content)

print("SUCCESS: Updated Meenu_Label_Desktop_Storefront.html with Smart Exchange Policy!")
