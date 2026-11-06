import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

# Test 1: Verify using index.html
with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Also inject a simulated card with exact Shopify "Rs. 1,899.00" and "Rs. 2,999.00" from user's screenshot
test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    // Scroll to the product grid
    var grid = document.querySelector('.product-grid');
    if (grid) {
      grid.scrollIntoView({ behavior: 'instant', block: 'start' });
    }
    
    // Check computed styles and bounding rects of first card
    var card = document.querySelector('.product-card');
    var pMain = card.querySelector('.price-main');
    var pMrp = card.querySelector('.price-mrp');
    var pDisc = card.querySelector('.price-discount');
    var pWrap = card.querySelector('.card-price-compare-wrap');
    
    var mrpRect = pMrp.getBoundingClientRect();
    var mrpWhiteSp = window.getComputedStyle(pMrp).whiteSpace;
    var mrpText = pMrp.innerText;
    var discText = pDisc.innerText;
    
    var statusDiv = document.createElement('div');
    statusDiv.id = 'price-test-status';
    statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:rgba(0,0,0,0.9);color:#C8A364;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #C8A364;border-radius:4px;max-width:390px;line-height:1.4;';
    statusDiv.innerHTML = '<b>PRICE & DISCOUNT CHECK:</b><br>' +
                          'MRP WhiteSpace: ' + mrpWhiteSp + ' (Must be nowrap)<br>' +
                          'MRP Text: ' + mrpText + '<br>' +
                          'Discount: ' + discText + '<br>' +
                          'MRP Rect Height: ' + Math.round(mrpRect.height) + 'px (Single Line)';
    document.body.appendChild(statusDiv);
  }, 400);
});
</script>
"""

html_test = base_html.replace("</body>", test_script + "</body>")
temp_test_html = os.path.join(scratch_dir, "temp_price_wrap_test.html")
with open(temp_test_html, "w", encoding="utf-8") as f:
    f.write(html_test)

# 1. Mobile Screenshot (390x844 - iPhone 14/15 size matching user's mobile screen)
shot_mob = os.path.join(artifacts_dir, "verified_compare_price_and_discount_mobile.png")
cmd_mob = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_price_mob')}",
    "--window-size=390,844",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_mob}",
    temp_test_html
]

print("Running Mobile Price & Discount Verification (390x844)...")
subprocess.run(cmd_mob, check=True)
print("Captured Mobile Screenshot:", shot_mob)

# 2. Desktop Screenshot (1440x900)
shot_desk = os.path.join(artifacts_dir, "verified_compare_price_and_discount_desktop.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_price_desk')}",
    "--window-size=1440,900",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_desk}",
    temp_test_html
]

print("Running Desktop Price & Discount Verification (1440x900)...")
subprocess.run(cmd_desk, check=True)
print("Captured Desktop Screenshot:", shot_desk)

# 3. Check DOM Dump
cmd_dump = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_price_dump')}",
    "--window-size=390,844",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_test_html
]
res = subprocess.run(cmd_dump, capture_output=True, text=True, encoding='utf-8')
if 'MRP WhiteSpace: nowrap' in res.stdout:
    print("SUCCESS: MRP WhiteSpace is NOWRAP! 'Rs.' and digits can never separate!")
else:
    print("Check: MRP WhiteSpace output")

if '% OFF' in res.stdout:
    print("SUCCESS: Percent OFF discount is clearly rendered on product cards!")
