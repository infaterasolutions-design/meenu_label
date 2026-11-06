import subprocess, os, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
artifacts_dir = r"C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f"
scratch_dir = r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch"

with open(r"c:\Users\sande\Documents\antigravity\splendid-nobel\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

def make_test_html(slide_idx):
    script = f"""
    <script>
    window.addEventListener('load', function() {{
        var t = document.getElementById('sliderTrack');
        if (t) {{
            t.style.transition = 'none';
        }}
        goToSlide({slide_idx});
        if (typeof stopAutoSlide === 'function') stopAutoSlide();
    }});
    </script>
    """
    return base_html.replace("</body>", script + "</body>")

# Generate test HTML files for all 4 slides
for idx in [0, 1, 2, 3]:
    p = os.path.join(scratch_dir, f"temp_slide_{idx}.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(make_test_html(idx))

# Captures to take:
# Slide 3 (Everyday Dresses): Desktop & Mobile
# Slide 4 (Chic Yellow Co-Ord): Desktop & Mobile
targets = [
    ("Slide 3 (Everyday Dresses) Desktop", 2, 1440, 900, "verified_hero_slide3_desktop.png"),
    ("Slide 3 (Everyday Dresses) Mobile", 2, 390, 844, "verified_hero_slide3_mobile.png"),
    ("Slide 4 (Chic Yellow Co-Ord) Desktop", 3, 1440, 900, "verified_hero_slide4_desktop.png"),
    ("Slide 4 (Chic Yellow Co-Ord) Mobile", 3, 390, 844, "verified_hero_slide4_mobile.png"),
]

for label, s_idx, w, h, fname in targets:
    html_file = os.path.join(scratch_dir, f"temp_slide_{s_idx}.html")
    out_file = os.path.join(artifacts_dir, fname)
    user_dir = os.path.join(scratch_dir, f"chrome_tmp_s{s_idx}_{w}")
    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        f"--user-data-dir={user_dir}",
        f"--window-size={w},{h}",
        "--virtual-time-budget=2000",
        f"--screenshot={out_file}",
        html_file
    ]
    print(f"Capturing {label}...")
    subprocess.run(cmd, check=True)
    print(f"  -> Saved {out_file} ({os.path.getsize(out_file):,} bytes)")

print("\nDone capturing exact slides!")
