import subprocess, os, shutil

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Instead of scrolling which might be delayed, we can also extract or scroll before rendering:
script = """
<script>
window.addEventListener('load', function() {
  var el = document.querySelector('.craftsmanship-section');
  if (el) {
    var rect = el.getBoundingClientRect();
    window.scrollTo(0, window.pageYOffset + rect.top - 20);
  }
});
</script>
</body>
"""
preview_html = text.replace('</body>', script)
with open('scratch/craft_focus.html', 'w', encoding='utf-8') as f:
    f.write(preview_html)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
out_png = r'C:\Users\sande\Downloads\Meenu_Label_Craftsmanship_Spotlight.png'
target_url = f"file:///{os.path.abspath('scratch/craft_focus.html').replace(os.sep, '/')}"

args = [
    chrome_path,
    '--headless=new',
    '--window-size=1440,1100',
    f'--screenshot={out_png}',
    target_url
]
subprocess.run(args, check=True)

brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'
shutil.copyfile(out_png, os.path.join(brain_dir, 'Meenu_Label_Craftsmanship_Spotlight.png'))
print('Captured and copied successfully!')
