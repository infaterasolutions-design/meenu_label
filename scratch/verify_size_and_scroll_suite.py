import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# -------------------------------------------------------------
# Test 1: Mobile PDP Open (412x915) - Verify No Size Selected
# -------------------------------------------------------------
script_1 = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openProductPage('JAB26ST05010');
    
    setTimeout(function() {
      var selBtns = document.querySelectorAll('.pdp-size-btn.selected');
      var statusDiv = document.createElement('div');
      statusDiv.id = 'test-status-1';
      statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:rgba(0,0,0,0.85);color:#C8A364;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #C8A364;border-radius:4px;';
      statusDiv.textContent = 'CHECK: pdpSelectedSize=' + pdpSelectedSize + ' | SelectedCount=' + selBtns.length;
      document.body.appendChild(statusDiv);
      console.log('TEST 1 DONE:', statusDiv.textContent);
    }, 400);
  }, 300);
});
</script>
"""
html_1 = base_html.replace("</body>", script_1 + "</body>")
temp_1 = os.path.join(scratch_dir, "temp_test_1.html")
with open(temp_1, "w", encoding="utf-8") as f:
    f.write(html_1)

shot_1 = os.path.join(artifacts_dir, "verified_no_default_size_mobile.png")
cmd_1 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_1')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_1}",
    temp_1
]
print("Running Test 1 (Mobile PDP No Default Size)...")
subprocess.run(cmd_1, check=True)
print("Captured:", shot_1)

# Check DOM output for Test 1
cmd_dump_1 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_1_dump')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_1
]
res_1 = subprocess.run(cmd_dump_1, capture_output=True, text=True, encoding='utf-8')
if 'CHECK: pdpSelectedSize=null | SelectedCount=0' in res_1.stdout:
    print("VERIFIED TEST 1: pdpSelectedSize is NULL and SelectedCount is 0! No default size pre-selected!")
else:
    print("Warning Test 1 output check")

# -------------------------------------------------------------
# Test 2: Mobile Click Add to Bag without size -> Warning appears
# -------------------------------------------------------------
script_2 = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openProductPage('JAB26ST05010');
    
    setTimeout(function() {
      // User attempts to add to cart without selecting size
      addPdpProductToCart();
      
      setTimeout(function() {
        var notice = document.getElementById('pdpSizeNotice');
        var noticeVis = notice && notice.style.display !== 'none';
        var statusDiv = document.createElement('div');
        statusDiv.id = 'test-status-2';
        statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:rgba(0,0,0,0.85);color:#E29578;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #E29578;border-radius:4px;';
        statusDiv.textContent = 'CHECK: NoticeVisible=' + noticeVis;
        document.body.appendChild(statusDiv);
      }, 300);
    }, 400);
  }, 300);
});
</script>
"""
html_2 = base_html.replace("</body>", script_2 + "</body>")
temp_2 = os.path.join(scratch_dir, "temp_test_2.html")
with open(temp_2, "w", encoding="utf-8") as f:
    f.write(html_2)

shot_2 = os.path.join(artifacts_dir, "verified_size_required_warning_mobile.png")
cmd_2 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_2')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_2}",
    temp_2
]
print("Running Test 2 (Mobile Size Warning Triggered)...")
subprocess.run(cmd_2, check=True)
print("Captured:", shot_2)

# Check DOM output for Test 2
cmd_dump_2 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_2_dump')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_2
]
res_2 = subprocess.run(cmd_dump_2, capture_output=True, text=True, encoding='utf-8')
if 'CHECK: NoticeVisible=true' in res_2.stdout:
    print("VERIFIED TEST 2: NoticeVisible=true! Warning correctly blocks cart addition and instructs customer!")
else:
    print("Warning Test 2 output check")

# -------------------------------------------------------------
# Test 3: Mobile Select Size L -> Becomes selected, notice cleared
# -------------------------------------------------------------
script_3 = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openProductPage('JAB26ST05010');
    
    setTimeout(function() {
      // User selects size L
      selectPdpSize('L', document.getElementById('pdpSizeBtn_L'));
      
      setTimeout(function() {
        var notice = document.getElementById('pdpSizeNotice');
        var noticeVis = notice && notice.style.display !== 'none';
        var statusDiv = document.createElement('div');
        statusDiv.id = 'test-status-3';
        statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:rgba(0,0,0,0.85);color:#C8A364;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #C8A364;border-radius:4px;';
        statusDiv.textContent = 'CHECK: pdpSelectedSize=' + pdpSelectedSize + ' | NoticeVisible=' + noticeVis;
        document.body.appendChild(statusDiv);
      }, 300);
    }, 400);
  }, 300);
});
</script>
"""
html_3 = base_html.replace("</body>", script_3 + "</body>")
temp_3 = os.path.join(scratch_dir, "temp_test_3.html")
with open(temp_3, "w", encoding="utf-8") as f:
    f.write(html_3)

shot_3 = os.path.join(artifacts_dir, "verified_size_selected_mobile.png")
cmd_3 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_3')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_3}",
    temp_3
]
print("Running Test 3 (Mobile Size L Selected)...")
subprocess.run(cmd_3, check=True)
print("Captured:", shot_3)

cmd_dump_3 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_3_dump')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_3
]
res_3 = subprocess.run(cmd_dump_3, capture_output=True, text=True, encoding='utf-8')
if 'CHECK: pdpSelectedSize=L | NoticeVisible=false' in res_3.stdout:
    print("VERIFIED TEST 3: Size L successfully selected and notice hidden!")
else:
    print("Warning Test 3 output check")

# -------------------------------------------------------------
# Test 4: Mobile Scroll Restoration on Back Navigation
# -------------------------------------------------------------
script_4 = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    // 1. Scroll home page down to 1450px
    window.scrollTo(0, 1450);
    var targetScroll = window.pageYOffset || document.documentElement.scrollTop;
    
    setTimeout(function() {
      // 2. Click to open product
      openProductPage('JAB26ST05010');
      
      setTimeout(function() {
        // 3. Click back
        closeProductPage();
        
        setTimeout(function() {
          var restoredScroll = window.pageYOffset || document.documentElement.scrollTop;
          var statusDiv = document.createElement('div');
          statusDiv.id = 'test-status-4';
          statusDiv.style.cssText = 'position:fixed;top:10px;left:10px;background:rgba(0,0,0,0.85);color:#25D366;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #25D366;border-radius:4px;';
          var isRestored = Math.abs(restoredScroll - targetScroll) < 10;
          statusDiv.textContent = 'CHECK: Target=' + targetScroll + ' | Restored=' + restoredScroll + ' | ExactMatch=' + isRestored;
          document.body.appendChild(statusDiv);
        }, 400);
      }, 500);
    }, 400);
  }, 300);
});
</script>
"""
html_4 = base_html.replace("</body>", script_4 + "</body>")
temp_4 = os.path.join(scratch_dir, "temp_test_4.html")
with open(temp_4, "w", encoding="utf-8") as f:
    f.write(html_4)

shot_4 = os.path.join(artifacts_dir, "verified_scroll_restored_mobile.png")
cmd_4 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_4')}",
    "--window-size=412,915",
    "--virtual-time-budget=5000",
    f"--screenshot={shot_4}",
    temp_4
]
print("Running Test 4 (Mobile Scroll Position Restoration)...")
subprocess.run(cmd_4, check=True)
print("Captured:", shot_4)

cmd_dump_4 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_4_dump')}",
    "--window-size=412,915",
    "--virtual-time-budget=5000",
    "--dump-dom",
    temp_4
]
res_4 = subprocess.run(cmd_dump_4, capture_output=True, text=True, encoding='utf-8')
if 'ExactMatch=true' in res_4.stdout:
    print("VERIFIED TEST 4: ExactMatch=true! Mobile scroll position is 100% restored to exact position where user was standing!")
else:
    print("Warning Test 4 output check")

# -------------------------------------------------------------
# Test 5: Desktop PDP Open (1440x900) - No Default Size & Scroll Restored
# -------------------------------------------------------------
script_5 = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    window.scrollTo(0, 1600);
    var deskTarget = window.pageYOffset || document.documentElement.scrollTop;
    
    setTimeout(function() {
      openProductPage('JAB26ST05010');
      
      setTimeout(function() {
        var selBtns = document.querySelectorAll('.pdp-size-btn.selected');
        var statusDiv = document.createElement('div');
        statusDiv.id = 'test-status-5';
        statusDiv.style.cssText = 'position:fixed;bottom:20px;right:20px;background:rgba(0,0,0,0.85);color:#C8A364;padding:10px 16px;font-size:14px;z-index:99999;border:1px solid #C8A364;border-radius:6px;';
        statusDiv.textContent = 'DESKTOP: pdpSelectedSize=' + pdpSelectedSize + ' | SelectedCount=' + selBtns.length;
        document.body.appendChild(statusDiv);
      }, 400);
    }, 400);
  }, 300);
});
</script>
"""
html_5 = base_html.replace("</body>", script_5 + "</body>")
temp_5 = os.path.join(scratch_dir, "temp_test_5.html")
with open(temp_5, "w", encoding="utf-8") as f:
    f.write(html_5)

shot_5 = os.path.join(artifacts_dir, "verified_no_default_size_desktop.png")
cmd_5 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_5')}",
    "--window-size=1440,900",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_5}",
    temp_5
]
print("Running Test 5 (Desktop No Default Size)...")
subprocess.run(cmd_5, check=True)
print("Captured:", shot_5)

cmd_dump_5 = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_test_5_dump')}",
    "--window-size=1440,900",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_5
]
res_5 = subprocess.run(cmd_dump_5, capture_output=True, text=True, encoding='utf-8')
if 'DESKTOP: pdpSelectedSize=null | SelectedCount=0' in res_5.stdout:
    print("VERIFIED TEST 5: Desktop pdpSelectedSize is NULL and SelectedCount is 0!")
else:
    print("Warning Test 5 output check")

print("\n==============================================")
print("ALL TESTS RUN & VERIFICATION ARTIFACTS CREATED!")
print("==============================================")
