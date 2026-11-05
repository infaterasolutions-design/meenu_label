import subprocess
import os
from PIL import Image

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_card")
os.makedirs(temp_dir, exist_ok=True)

# Create a small script that scrolls directly to the product grid and takes screenshot
with open("C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html", "r", encoding="utf-8") as f:
    html = f.read()

scroll_script = """
<script>
window.addEventListener('load', function() {
  var grid = document.querySelector('.product-card');
  if (grid) {
    grid.scrollIntoView({ block: 'center' });
  }
});
</script>
"""
html_mod = html.replace("</body>", scroll_script + "</body>")
temp_html = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_card_scroll.html")
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_mod)

url = f"file:///{temp_html.replace(os.sep, '/')}"
shot_path = os.path.join(artifacts_dir, "verified_card_scrolled.png")

subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--window-size=1440,950",
    "--virtual-time-budget=3000",
    f"--screenshot={shot_path}",
    url
], check=True)

im = Image.open(shot_path)
# Let's crop the first card area
# Find card or crop center left
crop_card = im.crop((120, 200, 480, 800))
crop_card.save(os.path.join(artifacts_dir, "verified_product_card_with_plus_btn.png"))
print("Saved verified_product_card_with_plus_btn.png!")
