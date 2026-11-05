import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_wish_test")
os.makedirs(temp_dir, exist_ok=True)

with open("C:/Users/sande/Downloads/Meenu_Label_Desktop_Storefront.html", "r", encoding="utf-8") as f:
    html = f.read()

test_js = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    var plusBtn = document.querySelector('.snitch-plus-trigger');
    if (plusBtn) {
      openQuickSizePopup(plusBtn);
      setTimeout(function() {
        var wishBtn = document.getElementById('snitchSizeWishlistBtn');
        console.log('BEFORE_CLICK_WISH:', wishBtn.className, window.wishlist ? window.wishlist.length : 'no-wishlist');
        wishBtn.click();
        setTimeout(function() {
          var wishBadge = document.getElementById('headerWishlistCount');
          var wishCountVal = wishBadge ? wishBadge.textContent : 'none';
          var wishDisp = wishBadge ? window.getComputedStyle(wishBadge).display : 'none';
          var isAct = wishBtn.classList.contains('active');
          console.log('AFTER_CLICK_WISH:', isAct, 'WISHLIST_LEN:', window.wishlist ? window.wishlist.length : 'none', 'BADGE:', wishCountVal, wishDisp);
          var resDiv = document.createElement('div');
          resDiv.id = 'WISH_TEST_RESULT';
          resDiv.textContent = 'ACTIVE=' + isAct + ';COUNT=' + wishCountVal + ';DISP=' + wishDisp + ';LEN=' + (window.wishlist ? window.wishlist.length : 'none');
          document.body.appendChild(resDiv);
        }, 300);
      }, 500);
    }
  }, 400);
});
</script>
"""

html_test = html.replace("</body>", test_js + "</body>")
temp_html_path = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "temp_wish_click_test.html")
with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_test)

url = f"file:///{temp_html_path.replace(os.sep, '/')}"

cmd = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--virtual-time-budget=4000",
    "--dump-dom",
    url
]
res = subprocess.run(cmd, capture_output=True)
out = res.stdout.decode('utf-8', errors='ignore')
idx = out.find('id="WISH_TEST_RESULT"')
if idx != -1:
    print(out[idx:idx+120])
else:
    print("WISH_TEST_RESULT not found")
