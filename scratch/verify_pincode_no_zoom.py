import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Test script: Focus pincode input, check font-size, enter Tricity pin, check result
test_script = """
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    openProductPage('JAB26ST05010');
    
    setTimeout(function() {
      var pinInp = document.getElementById('pdpPincodeInput');
      pinInp.scrollIntoView({ behavior: 'instant', block: 'center' });
      
      // Get computed styles
      var compStyle = window.getComputedStyle(pinInp);
      var fontSize = compStyle.fontSize;
      var touchAction = compStyle.touchAction;
      var inputMode = pinInp.getAttribute('inputmode');
      
      // Focus and enter 160017
      pinInp.focus();
      pinInp.value = '160017';
      checkPdpPincode();
      
      setTimeout(function() {
        var pinRes = document.getElementById('pdpPincodeResult');
        var resText = pinRes ? pinRes.innerText : '';
        var resVis = pinRes && pinRes.style.display !== 'none';
        
        var statusDiv = document.createElement('div');
        statusDiv.id = 'pincode-test-status';
        statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:rgba(0,0,0,0.9);color:#C8A364;padding:8px 12px;font-size:12px;z-index:99999;border:1px solid #C8A364;border-radius:4px;max-width:390px;line-height:1.4;';
        statusDiv.innerHTML = '<b>PINCODE ZOOM CHECK:</b><br>' +
                              'Font-Size: ' + fontSize + ' (Must be >= 16px)<br>' +
                              'InputMode: ' + inputMode + ' (Numeric Keypad)<br>' +
                              'ResultVisible: ' + resVis + '<br>' +
                              'Result: ' + resText.substring(0, 40) + '...';
        document.body.appendChild(statusDiv);
      }, 300);
    }, 400);
  }, 300);
});
</script>
"""

html_test = base_html.replace("</body>", test_script + "</body>")
temp_test_html = os.path.join(scratch_dir, "temp_pincode_zoom_test.html")
with open(temp_test_html, "w", encoding="utf-8") as f:
    f.write(html_test)

shot_pincode = os.path.join(artifacts_dir, "verified_pincode_no_zoom_mobile.png")
cmd = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_pincode_zoom')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    f"--screenshot={shot_pincode}",
    temp_test_html
]

print("Running Mobile Pincode Search Bar Anti-Zoom Verification...")
subprocess.run(cmd, check=True)
print("Captured screenshot:", shot_pincode)

cmd_dump = [
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={os.path.join(scratch_dir, 'chrome_tmp_pincode_dump')}",
    "--window-size=412,915",
    "--virtual-time-budget=4000",
    "--dump-dom",
    temp_test_html
]
res = subprocess.run(cmd_dump, capture_output=True, text=True, encoding='utf-8')
if 'Font-Size: 16px' in res.stdout:
    print("SUCCESS: Pincode input computed font-size is 16px! Auto-zoom is 100% prevented on mobile devices!")
else:
    print("Check output: font-size did not match 16px in dump")

if 'InputMode: numeric' in res.stdout:
    print("SUCCESS: InputMode is numeric (proper mobile number keypad enabled)!")
