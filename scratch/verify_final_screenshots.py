import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_wishlist_final")
os.makedirs(temp_dir, exist_ok=True)

with open(r"C:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    html = f.read()

test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger');
    openQuickSizePopup(plusBtn);

    // Ensure drawer transition finishes in headless test
    var drawer = document.getElementById('snitchSizeDrawer');
    if (drawer) drawer.style.transform = 'translateY(0)';

    setTimeout(function() {
      var wishBtn = document.getElementById('snitchSizeWishlistBtn');
      if (wishBtn) {
        // Toggle wishlist heart ON
        wishBtn.click();
      }

      setTimeout(function() {
        var wishBadge = document.getElementById('headerWishlistCount');
        var cartBadge = document.getElementById('headerCartCount');
        
        var d = document.createElement('div');
        d.id = 'wishlist-verified-banner';
        d.style = 'position:fixed; top:70px; left:20px; z-index:9999999; background:#111; color:#fff; padding:10px 16px; border-radius:8px; font-family:sans-serif; font-size:14px;';
        d.innerHTML = 'Heart Active: ' + wishBtn.classList.contains('active') + ' | Wishlist Count: ' + (wishBadge ? wishBadge.textContent : '0') + ' | Cart Display: ' + (cartBadge ? getComputedStyle(cartBadge).display : 'none');
        document.body.appendChild(d);
      }, 300);
    }, 400);
  }, 400);
});
</script>
"""

html_test = html.replace("</body>", test_script + "</body>")
temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_wishlist_final.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_test)

url = f"file:///{temp_html_path.replace(os.sep, '/')}"

# 1. Desktop Screenshot (1440x950)
desktop_shot = os.path.join(artifacts_dir, "verified_popup_wishlist_active_desktop.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_desk",
    "--window-size=1440,950",
    "--virtual-time-budget=4000",
    f"--screenshot={desktop_shot}",
    url
]
subprocess.run(cmd_desk, check=True)
print("Saved desktop screenshot:", desktop_shot)

# 2. Mobile Screenshot (412x915)
mobile_shot = os.path.join(artifacts_dir, "verified_popup_wishlist_active_mobile.png")
cmd_mobile = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}_mob",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={mobile_shot}",
    url
]
subprocess.run(cmd_mobile, check=True)
print("Saved mobile screenshot:", mobile_shot)
