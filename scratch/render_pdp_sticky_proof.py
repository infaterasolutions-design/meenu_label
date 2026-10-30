import subprocess
import os
import shutil
import tempfile
import time

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Top
scr_top = '''
<script>
window.addEventListener('load', () => {
    openProductPage('JAB26ST05010');
    window.scrollTo(0, 0);
});
</script>
'''
path_top = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\pdp_sticky_top_test.html'
with open(path_top, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', scr_top + '</body>'))

# 2. Scrolled 480px
scr_scroll = '''
<script>
window.addEventListener('load', () => {
    openProductPage('JAB26ST05010');
    setTimeout(() => {
        window.scrollTo(0, 480);
    }, 150);
});
</script>
'''
path_scroll = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\pdp_sticky_scroll_test.html'
with open(path_scroll, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', scr_scroll + '</body>'))

# 3. Scrolled 850px
scr_scroll2 = '''
<script>
window.addEventListener('load', () => {
    openProductPage('JAB26ST05010');
    setTimeout(() => {
        window.scrollTo(0, 850);
    }, 150);
});
</script>
'''
path_scroll2 = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\pdp_sticky_scroll850_test.html'
with open(path_scroll2, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', scr_scroll2 + '</body>'))

def snap(in_html, out_png):
    temp_dir = tempfile.mkdtemp(prefix='chrome_pdp_')
    cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        f'--user-data-dir={temp_dir}',
        f'--screenshot={out_png}',
        '--window-size=1280,880',
        'file:///' + in_html.replace(os.sep, '/')
    ]
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=12)
        print('Captured:', os.path.basename(out_png))
    except Exception as e:
        print('Error snapping:', e)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

snap(path_top, os.path.join(artifacts_dir, 'pdp_sticky_top.png'))
snap(path_scroll, os.path.join(artifacts_dir, 'pdp_sticky_scrolled_480.png'))
snap(path_scroll2, os.path.join(artifacts_dir, 'pdp_sticky_scrolled_850.png'))
print('All snapshots completed successfully!')
