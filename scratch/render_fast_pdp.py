import subprocess
import os
from PIL import Image

workspace = r'c:\Users\sande\Documents\antigravity\splendid-nobel'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Read CSS and HTML styles from Meenu_Label_Desktop_Storefront.html
with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract <style>...</style> block
style_start = html.find('<style>')
style_end = html.find('</style>')
css_block = html[style_start:style_end+8]

# Extract PDP size and action HTML
pdp_start = html.find('<!-- Size Selection -->')
pdp_end = html.find('<!-- Pincode Checker -->')
pdp_snippet = html[pdp_start:pdp_end]

# Extract PDP JS functions
pdp_js_start = html.find('var activePdpProductId = null;')
pdp_js_end = html.find('function checkPdpPincode()')
js_snippet = html[pdp_js_start:pdp_js_end]

# State 1: Unselected (default on load)
html_unselected = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{css_block}
<style>
  body {{
    background: #FAF8F5;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }}
  .preview-card {{
    max-width: 420px;
    margin: 0 auto;
    background: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid var(--border-color, #E8E2D9);
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
  }}
</style>
</head>
<body>
  <div class="preview-card">
    <div style="font-size: 11px; font-weight:700; color: #78716C; margin-bottom: 4px; letter-spacing:0.08em;">STYLE #JAB26ST05010</div>
    <div style="font-size: 18px; font-family:'Cormorant Garamond', serif; font-weight:600; margin-bottom: 12px; color:#1C1917;">Jaipur Chanderi Silk Festive Suit</div>
    <div style="font-size: 20px; font-weight:700; margin-bottom: 16px; color:#1C1917;">₹2,299 <span style="font-size:14px; text-decoration:line-through; color:#A8A29E;">₹3,699</span></div>
    {pdp_snippet}
  </div>
  <script>
    var productsData = [{{ id: 'JAB26ST05010', code: 'JAB26ST05010', name: 'Jaipur Chanderi Silk Festive Suit', price: 2299 }}];
    var cart = [];
    function showToast(msg) {{ console.log(msg); }}
    function quickAddCart(id, size) {{ cart.push({{ id: id, size: size }}); }}
    function toggleCart() {{}}
    {js_snippet}
    activePdpProductId = 'JAB26ST05010';
  </script>
</body>
</html>"""

# State 2: Error Alert (customer clicked ADD TO SHOPPING BAG without selecting size)
html_alert = html_unselected.replace("</body>", """
  <script>
    addPdpProductToCart(); // triggers required alert
  </script>
</body>""")

# State 3: Selected Size L
html_selected_L = html_unselected.replace("</body>", """
  <script>
    selectPdpSize('L', document.getElementById('pdpSizeBtn_L'));
  </script>
</body>""")

file_unselected = os.path.join(workspace, 'scratch', 'render_pdp_unselected.html')
file_alert = os.path.join(workspace, 'scratch', 'render_pdp_alert.html')
file_selected = os.path.join(workspace, 'scratch', 'render_pdp_selected.html')

with open(file_unselected, 'w', encoding='utf-8') as f: f.write(html_unselected)
with open(file_alert, 'w', encoding='utf-8') as f: f.write(html_alert)
with open(file_selected, 'w', encoding='utf-8') as f: f.write(html_selected_L)

def capture(html_path, out_png):
    cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--screenshot={out_png}',
        '--window-size=440,650',
        f'file:///{os.path.abspath(html_path).replace(os.sep, "/")}'
    ]
    subprocess.run(cmd, check=True)
    # Crop clean card
    im = Image.open(out_png)
    cropped = im.crop((10, 10, 430, 640))
    cropped.save(out_png)
    print("Captured:", out_png)

shot1 = os.path.join(artifacts_dir, 'verified_pdp_size_unselected.png')
shot2 = os.path.join(artifacts_dir, 'verified_pdp_size_error_alert.png')
shot3 = os.path.join(artifacts_dir, 'verified_pdp_size_selected_L.png')

capture(file_unselected, shot1)
capture(file_alert, shot2)
capture(file_selected, shot3)

print("All 3 verification screenshots captured flawlessly!")
