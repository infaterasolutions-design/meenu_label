import sys
import shutil
import re
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
backup_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.backup_snitch_pdp.html'

shutil.copy2(file_path, backup_path)
print("Backup created at:", backup_path)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update html, body overflow-x to clip
target_overflow = """html, body {
      width: 100% !important;
      max-width: 100% !important;
      overflow-x: hidden !important;
      position: relative !important;
      margin: 0 !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }"""

replacement_overflow = """html, body {
      width: 100% !important;
      max-width: 100% !important;
      overflow-x: clip !important;
      position: relative !important;
      margin: 0 !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }"""
assert target_overflow in content, "target_overflow not found"
content = content.replace(target_overflow, replacement_overflow, 1)

# 2. Update pdp-grid and pdp-info-col CSS
target_pdp_css = """    /* 2-Column Luxury PDP Layout */
    .pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 56px;
      align-items: flex-start;
    }
    @media (max-width: 992px) {
      .pdp-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    /* Left Gallery */
    .pdp-gallery-col {
      position: sticky;
      top: 100px;
    }"""

replacement_pdp_css = """    /* 2-Column Luxury PDP Layout (Snitch-Style Sticky Media & Scrollable Right Side) */
    .pdp-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 48px;
      align-items: start;
    }
    @media (max-width: 992px) {
      .pdp-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    /* Left Gallery: Sticky on Desktop so image remains constantly in view */
    .pdp-gallery-col {
      position: sticky;
      top: 85px;
      align-self: start;
    }

    /* Right Column: Scrollable on Desktop like Snitch */
    @media (min-width: 993px) {
      .pdp-grid {
        align-items: start;
      }
      .pdp-gallery-col {
        position: sticky;
        top: 85px;
        align-self: start;
      }
      .pdp-info-col {
        max-height: calc(100vh - 105px);
        overflow-y: auto;
        overflow-x: hidden;
        padding-right: 14px;
        scrollbar-width: thin;
        scrollbar-color: #D1C7BD transparent;
      }
      .pdp-info-col::-webkit-scrollbar {
        width: 4px;
      }
      .pdp-info-col::-webkit-scrollbar-track {
        background: transparent;
      }
      .pdp-info-col::-webkit-scrollbar-thumb {
        background: #D1C7BD;
        border-radius: 4px;
      }
      .pdp-info-col::-webkit-scrollbar-thumb:hover {
        background: var(--text-main);
      }
    }

    .pdp-atelier-guarantee {
      margin-top: 14px;
      background: var(--bg-surface, #FAF8F5);
      border: 1px solid var(--border-color, #E8E2D9);
      border-radius: 8px;
      padding: 14px 16px;
    }
    .pdp-guarantee-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 8px;
      border-bottom: 1px dashed rgba(0,0,0,0.1);
    }
    .pdp-guarantee-grid {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }
    .pdp-guarantee-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 11.5px;
      line-height: 1.4;
      color: var(--text-muted, #78716C);
    }
    .pdp-guarantee-item strong {
      display: block;
      color: var(--text-main, #1C1917);
      font-size: 12px;
      font-weight: 600;
    }
    .pdp-guar-icon {
      font-size: 15px;
      line-height: 1;
      margin-top: 1px;
    }"""
assert target_pdp_css in content, "target_pdp_css not found"
content = content.replace(target_pdp_css, replacement_pdp_css, 1)

# 3. Add Atelier Guarantee card under trust pills in HTML
target_trust_pills = """          <!-- Trust Badges -->
          <div class="pdp-trust-pills">
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#10024;</span>
              <span>Chandigarh Atelier</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Handcrafted Precision</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128666;</span>
              <span>Free 24-Hr Express</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Tricity Priority Courier</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128207;</span>
              <span>Complimentary Fit</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Studio Hem Adjustments</span>
            </div>
          </div>"""

guarantee_card_html = """          <!-- Trust Badges -->
          <div class="pdp-trust-pills">
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#10024;</span>
              <span>Chandigarh Atelier</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Handcrafted Precision</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128666;</span>
              <span>Free 24-Hr Express</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Tricity Priority Courier</span>
            </div>
            <div class="pdp-trust-pill">
              <span class="pdp-trust-pill-icon">&#128207;</span>
              <span>Complimentary Fit</span>
              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Studio Hem Adjustments</span>
            </div>
          </div>

          <!-- Atelier Quality & Authenticity Guarantee -->
          <div class="pdp-atelier-guarantee">
            <div class="pdp-guarantee-header">
              <span style="font-size:11.5px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-main,#1C1917);">&#10024; Meenu Label Atelier Promise</span>
              <span style="font-size:11px; font-weight:700; color:var(--accent-gold,#B8860B);">&#10003; 100% Authentic Handloom</span>
            </div>
            <div class="pdp-guarantee-grid">
              <div class="pdp-guarantee-item">
                <span class="pdp-guar-icon">&#129525;</span>
                <div>
                  <strong>Pure Artisanal Weaves</strong>
                  <span>Handcrafted from Jaipur chanderi silk with organza dupatta. Zero synthetic polyester blends.</span>
                </div>
              </div>
              <div class="pdp-guarantee-item">
                <span class="pdp-guar-icon">&#9986;&#65039;</span>
                <div>
                  <strong>Complimentary Atelier Fitting</strong>
                  <span>Custom hem, sleeve, or kurta alterations tailored directly in our Sector 17 studio.</span>
                </div>
              </div>
              <div class="pdp-guarantee-item">
                <span class="pdp-guar-icon">&#9889;</span>
                <div>
                  <strong>Express Priority Dispatch</strong>
                  <span>Same-day hand-pressing and complimentary 24-hr courier delivery in Chandigarh Tricity.</span>
                </div>
              </div>
            </div>
          </div>"""
assert target_trust_pills in content, "target_trust_pills not found"
content = content.replace(target_trust_pills, guarantee_card_html, 1)

# Check div balance
open_divs = len(re.findall(r'<div\b', content, re.IGNORECASE))
close_divs = len(re.findall(r'</div>', content, re.IGNORECASE))
print(f"Div balance: Open={open_divs}, Close={close_divs}, Diff={open_divs - close_divs}")
assert open_divs == close_divs, "Div tags are not balanced!"

# Check script syntax
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', content, re.DOTALL)
for i, s in enumerate(scripts):
    res = subprocess.run(['node', '--check', '-'], input=s, text=True, capture_output=True, encoding='utf-8', errors='ignore')
    assert res.returncode == 0, f"Script #{i} error: {res.stderr}"
print("All JS scripts verified valid!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Meenu_Label_Desktop_Storefront.html updated with Snitch-style scrollable layout!")
