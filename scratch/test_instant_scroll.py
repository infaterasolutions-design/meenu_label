import os
import shutil
import tempfile
import subprocess

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
file_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Force instant scrolling
html = html.replace('</head>', '<style>html, body { scroll-behavior: auto !important; }</style></head>')

# Scrolled View Y = 520
scrolled_script = """
<script>
window.addEventListener('load', function() {
    openProductPage('JAB26ST05010');
    window.scrollTo({ top: 520, left: 0, behavior: 'instant' });
    document.documentElement.scrollTop = 520;
    document.body.scrollTop = 520;
});
</script>
"""
path_scrolled = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\instant_scrolled.html'
with open(path_scrolled, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', scrolled_script + '</body>'))

# Scrolled View Y = 950 (accordions)
deep_script = """
<script>
window.addEventListener('load', function() {
    openProductPage('JAB26ST05010');
    window.scrollTo({ top: 950, left: 0, behavior: 'instant' });
    document.documentElement.scrollTop = 950;
    document.body.scrollTop = 950;
});
</script>
"""
path_deep = r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\instant_deep.html'
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
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        print(f"Captured {os.path.basename(out_png)}, code: {res.returncode}")
    except Exception as e:
        print("Snap error:", e)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

print("Snapping instant scrolled 520...")
snap(path_scrolled, os.path.join(artifacts_dir, 'sticky_verified_scroll520.png'))

print("Snapping instant deep 950...")
snap(path_deep, os.path.join(artifacts_dir, 'sticky_verified_scroll950.png'))

print("Completed!")
