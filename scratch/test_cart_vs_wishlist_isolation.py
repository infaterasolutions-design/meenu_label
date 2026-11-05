import subprocess
import os
import time
from PIL import Image

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_isolation")
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
temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_isolation_test.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_test)

url = f"file:///{temp_html_path.replace(os.sep, '/')}"

shot_path = os.path.join(artifacts_dir, "verified_cart_vs_wishlist_isolation.png")
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
print("Saved screenshot:", shot_path)

# Let's crop the header right action icons (search, cart, wishlist, user)
im = Image.open(shot_path)
w, h = im.size
crop_header_icons = im.crop((w - 240, 0, w - 10, 80))
crop_path = os.path.join(artifacts_dir, "verified_isolated_header_badges.png")
crop_header_icons.save(crop_path)
print("Saved cropped header badges:", crop_path)
