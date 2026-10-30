import os
import shutil
import tempfile
import subprocess

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Top View (Scroll = 0)
top_script = """
<script>
window.addEventListener('load', function() {
    openProductPage('JAB26ST05010');
    window.scrollTo(0, 0);
});
</script>
"""
path_top = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\proof_top.html'
with open(path_top, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', top_script + '</body>'))

# 2. Scrolled View (Scroll into pdpDescContent accordion)
scrolled_script = """
<script>
window.addEventListener('load', function() {
    openProductPage('JAB26ST05010');
    var el = document.getElementById('pdpPincodeInput');
    if (el) el.scrollIntoView();
});
</script>
"""
path_scrolled = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\proof_scrolled.html'
with open(path_scrolled, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', scrolled_script + '</body>'))

# 3. Deep Scrolled View (Scroll into pdpFabricContent)
deep_script = """
<script>
window.addEventListener('load', function() {
    openProductPage('JAB26ST05010');
    var el = document.getElementById('pdpFabricContent');
    if (el) el.scrollIntoView();
});
</script>
"""
path_deep = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\proof_deep.html'
with open(path_deep, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', deep_script + '</body>'))

def snap(in_html, out_png):
    temp_dir = tempfile.mkdtemp(prefix='snap_')
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
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
        print(f"Captured {os.path.basename(out_png)}, code: {res.returncode}")
    except Exception as e:
        print("Snap error:", e)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

print("Starting snap top...")
snap(path_top, os.path.join(artifacts_dir, 'proof_sticky_top.png'))

print("Starting snap scrolled...")
snap(path_scrolled, os.path.join(artifacts_dir, 'proof_sticky_scrolled.png'))

print("Starting snap deep...")
snap(path_deep, os.path.join(artifacts_dir, 'proof_sticky_deep.png'))

print("All snapshots done!")
