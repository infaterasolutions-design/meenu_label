import subprocess
import os
from PIL import Image

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract CSS and HTML
style_start = html.find('<style>')
style_end = html.find('</style>')
css_block = html[style_start:style_end+8]

# Add the new Snitch-style scrollable right side and guarantee styles
new_css = """
<style>
  /* Snitch-Style Desktop Scrollable Right Area */
  @media (min-width: 993px) {
    .pdp-grid {
      display: grid !important;
      grid-template-columns: 1fr 1fr !important;
      gap: 40px !important;
      align-items: start !important;
    }
    .pdp-gallery-col {
      position: sticky !important;
      top: 20px !important;
      align-self: start !important;
    }
    .pdp-info-col {
      max-height: calc(100vh - 40px) !important;
      overflow-y: auto !important;
      overflow-x: hidden !important;
      padding-right: 18px !important;
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
      background: var(--text-main, #1A1A1A);
    }
  }

  .pdp-atelier-guarantee {
    margin-top: 14px;
    background: #FAF8F5;
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
    gap: 8px;
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
  }
  .pdp-guar-icon {
    font-size: 15px;
    line-height: 1;
    margin-top: 1px;
  }
</style>
"""

# Extract PDP HTML
pdp_start = html.find('id="productDetailView"')
pdp_end = html.find('<!-- Snitch-Style Luxury Login Interface -->', pdp_start)
if pdp_end == -1:
    pdp_end = html.find('id="productModalBackdrop"', pdp_start)
pdp_html = html[pdp_start:pdp_end]

# Extract sample image data from productsData
prod_b64_start = html.find('"b64": "data:image/jpeg;base64,') + 7
prod_b64_end = html.find('"', prod_b64_start)
sample_b64 = html[prod_b64_start:prod_b64_end]

# Guarantee card HTML
guarantee_html = """
          <!-- Atelier Quality & Authenticity Guarantee -->
          <div class="pdp-atelier-guarantee">
            <div class="pdp-guarantee-header">
              <span style="font-size:11.5px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-main,#1C1917);">Meenu Label Atelier Promise</span>
              <span style="font-size:11px; font-weight:700; color:var(--accent-gold,#B8860B);">&#10003; 100% Authentic Handloom</span>
            </div>
            <div class="pdp-guarantee-grid">
              <div class="pdp-guarantee-item">
                <span class="pdp-guar-icon">&#10024;</span>
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
          </div>
"""

# Inject guarantee card after pdp-trust-pills
pdp_html_mod = pdp_html.replace('<!-- Trust Badges -->\n          <div class="pdp-trust-pills">', '<!-- Trust Badges -->\n          <div class="pdp-trust-pills">')
target_badge_end = '<!-- Trust Badges -->\n          <div class="pdp-trust-pills">\n            <div class="pdp-trust-pill">\n              <span class="pdp-trust-pill-icon">&#10024;</span>\n              <span>Chandigarh Atelier</span>\n              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Handcrafted Precision</span>\n            </div>\n            <div class="pdp-trust-pill">\n              <span class="pdp-trust-pill-icon">&#128666;</span>\n              <span>Free 24-Hr Express</span>\n              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Tricity Priority Courier</span>\n            </div>\n            <div class="pdp-trust-pill">\n              <span class="pdp-trust-pill-icon">&#128207;</span>\n              <span>Complimentary Fit</span>\n              <span style="font-size:10px; color:var(--text-muted); font-weight:400;">Studio Hem Adjustments</span>\n            </div>\n          </div>'
replacement_badges = target_badge_end + '\n' + guarantee_html

if target_badge_end in pdp_html:
    pdp_html_mod = pdp_html.replace(target_badge_end, replacement_badges)
else:
    print("Warning: target_badge_end not matched exactly, injecting after pdp-trust-pills")
    pdp_html_mod = pdp_html.replace('</div>\n        </div>\n\n        <!-- Right:', '</div>\n' + guarantee_html + '\n        </div>\n\n        <!-- Right:')

# Full preview document
doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{css_block}
{new_css}
</head>
<body style="background:#FFFFFF; margin:0; padding:0;">
  <div {pdp_html_mod}
  <script>
    document.getElementById('productDetailView').style.display = 'block';
    document.getElementById('pdpMainImg').src = "{sample_b64}";
  </script>
</body>
</html>"""

test_file = os.path.join(workspace, 'scratch', 'test_pdp_snitch.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(doc)

out_desktop_top = os.path.join(artifacts_dir, 'verified_snitch_pdp_desktop_top.png')
cmd = [
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    f'--screenshot={out_desktop_top}',
    '--window-size=1280,850',
    f'file:///{os.path.abspath(test_file).replace(os.sep, "/")}'
]
print("Capturing desktop top...")
subprocess.run(cmd, check=True)
print("Captured:", out_desktop_top)

# Now capture scrolled state on right side:
# In right side, scroll to accordions
doc_scrolled = doc.replace("</script>", """
  var infoCol = document.querySelector('.pdp-info-col');
  if (infoCol) {
    infoCol.scrollTop = 450; // scroll down to accordions
  }
</script>""")
test_file_scrolled = os.path.join(workspace, 'scratch', 'test_pdp_snitch_scrolled.html')
with open(test_file_scrolled, 'w', encoding='utf-8') as f:
    f.write(doc_scrolled)

out_desktop_scrolled = os.path.join(artifacts_dir, 'verified_snitch_pdp_desktop_scrolled.png')
cmd_scrolled = [
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    f'--screenshot={out_desktop_scrolled}',
    '--window-size=1280,850',
    f'file:///{os.path.abspath(test_file_scrolled).replace(os.sep, "/")}'
]
print("Capturing desktop scrolled...")
subprocess.run(cmd_scrolled, check=True)
print("Captured:", out_desktop_scrolled)

print("Both test snapshots completed!")
