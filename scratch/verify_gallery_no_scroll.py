import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Test script for PC Desktop Viewport (1440x900)
test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    // 1. Open product PDP
    openProductPage('JAB26ST05010');
    
    setTimeout(function() {
      // 2. Set scroll to viewing position where main image is visible
      window.scrollTo(0, 80);
      var initialScrollY = window.pageYOffset || document.documentElement.scrollTop;
      
      // 3. Find NEXT button and click it 3 times
      var nextBtn = document.querySelector('.shopify-gallery-next');
      if (nextBtn) {
        nextBtn.click();
        
        setTimeout(function() {
          var afterClick1 = window.pageYOffset || document.documentElement.scrollTop;
          nextBtn.click();
          
          setTimeout(function() {
            var afterClick2 = window.pageYOffset || document.documentElement.scrollTop;
            var prevBtn = document.querySelector('.shopify-gallery-prev');
            if (prevBtn) prevBtn.click();
            
            setTimeout(function() {
              var finalScrollY = window.pageYOffset || document.documentElement.scrollTop;
              var isLocked = (initialScrollY === finalScrollY) && (initialScrollY === afterClick1) && (initialScrollY === afterClick2);
              
              var statusDiv = document.createElement('div');
              statusDiv.id = 'gallery-scroll-test-status';
              statusDiv.style.cssText = 'position:fixed;bottom:20px;right:20px;background:rgba(0,0,0,0.92);color:#C8A364;padding:12px 18px;font-size:14px;z-index:99999;border:1px solid #C8A364;border-radius:6px;max-width:440px;line-height:1.4;box-shadow:0 8px 24px rgba(0,0,0,0.3);';
              statusDiv.innerHTML = '<b>DESKTOP GALLERY SCROLL TEST:</b><br>' +
                                    'Initial ScrollY: ' + initialScrollY + 'px<br>' +
                                    'After Next 1: ' + afterClick1 + 'px<br>' +
                                    'After Next 2: ' + afterClick2 + 'px<br>' +
                                    'Final ScrollY: ' + finalScrollY + 'px<br>' +
                                    '<b>Screen Scroll Locked: ' + (isLocked ? 'YES (0px Shift)' : 'NO (Shifted!)') + '</b>';
              document.body.appendChild(statusDiv);
            }, 300);
          }, 300);
        }, 300);
      }
    }, 400);
  }, 300);
});
</script>
"""

html_test = base_html.replace("</body>", test_script + "</body>")
temp_test_html = os.path.join(scratch_dir, "temp_gallery_scroll_test.html")
with open(temp_test_html, "w", encoding="utf-8") as f:
    f.write(html_test)

shot_desk = os.path.join(artifacts_dir, "verified_gallery_no_scroll_desktop.png")
cmd_desk = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_gallery_scroll')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_desk}",
    temp_test_html
]

print("Running Desktop Gallery Next/Prev Button No-Scroll Test (1440x900)...")
subprocess.run(cmd_desk, check=True)
print("Captured Desktop Screenshot:", shot_desk)

cmd_dump = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_gallery_dump')}",
    "--window-size=1440,900",
    "--virtual-time-budget=5000",
    "--dump-dom",
    temp_test_html
]
res = subprocess.run(cmd_dump, capture_output=True, text=True, encoding='utf-8')
if 'Screen Scroll Locked: YES (0px Shift)' in res.stdout:
    print("SUCCESS: Screen Scroll Locked: YES (0px Shift)! Clicking Next/Prev button does NOT scroll down the screen at all!")
else:
    print("Warning: Check gallery test output")
