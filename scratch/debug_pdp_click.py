import subprocess, os

# Let's inspect the console errors and DOM state when opening PDP in Chrome
test_script = """
<script>
window.addEventListener('DOMContentLoaded', () => {
  console.log('Testing openProductPage...');
  try {
    openProductPage('JAB26ST05010');
    console.log('openProductPage finished successfully');
    const pdp = document.getElementById('productDetailView');
    console.log('PDP display:', pdp ? pdp.style.display : 'not found');
    console.log('PDP height:', pdp ? pdp.offsetHeight : 0);
  } catch(err) {
    console.error('ERROR inside openProductPage:', err.stack || err.message);
  }
});
</script>
</body>
"""

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

preview_html = text.replace('</body>', test_script)
with open('scratch/debug_pdp.html', 'w', encoding='utf-8') as f:
    f.write(preview_html)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_png = r'C:\Users\sande\Downloads\Meenu_Label_PDP_Debug.png'
target_url = f"file:///{os.path.abspath('scratch/debug_pdp.html').replace(os.sep, '/')}"

cmd = [
    chrome_path,
    '--headless=new',
    '--window-size=1440,1200',
    f'--screenshot={out_png}',
    target_url
]
subprocess.run(cmd, check=True)
print("Debug screenshot captured to:", out_png)
