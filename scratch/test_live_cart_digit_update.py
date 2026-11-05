import subprocess
import os
import time
from PIL import Image

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_cart_test")
os.makedirs(temp_dir, exist_ok=True)

with open("C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html", "r", encoding="utf-8") as f:
    html = f.read()

# Auto-open popup and click size 'M'
test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger');
    if (plusBtn) {
      openQuickSizePopup(plusBtn);
      setTimeout(function() {
        // Find the 'M' row in snitchSizeList and click it
        var rows = document.querySelectorAll('#snitchSizeList .snitch-size-row');
        for (var i = 0; i < rows.length; i++) {
          if (rows[i].textContent.includes('M')) {
            rows[i].click();
            break;
          }
        }
      }, 500);
    }
  }, 400);
});
</script>
"""

html_test = html.replace("</body>", test_script + "</body>")
temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_cart_digit_test.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_test)

url = f"file:///{temp_html_path.replace(os.sep, '/')}"

shot_path = os.path.join(artifacts_dir, "verified_cart_digit_updated_live.png")
cmd = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--window-size=1440,950",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_path}",
    url
]
subprocess.run(cmd, check=True)
print("Saved screenshot of live cart digit update:", shot_path)

# Let's crop the header cart icon area
im = Image.open(shot_path)
# Header cart icon is on the top right: x ~ 1250-1420, y ~ 0-80
w, h = im.size
crop_header_cart = im.crop((w - 220, 0, w - 20, 90))
crop_path = os.path.join(artifacts_dir, "verified_header_cart_digit_badge.png")
crop_header_cart.save(crop_path)
print("Saved cropped header cart badge:", crop_path)
