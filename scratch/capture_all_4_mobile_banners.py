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

targets = [
    ("Slide 1 (Modern Ethnic) Mobile", 0, 500, 844, "verified_hero_slide1_mobile.png"),
    ("Slide 2 (Grace in Every Drape) Mobile", 1, 500, 844, "verified_hero_slide2_mobile.png"),
    ("Slide 3 (Everyday Dresses) Mobile", 2, 500, 844, "verified_hero_slide3_mobile.png"),
    ("Slide 4 (Chic Co-Ord Sets) Mobile", 3, 500, 844, "verified_hero_slide4_mobile.png"),
]

for label, s_idx, w, h, fname in targets:
    html_content = make_test_html(s_idx)
    html_file = os.path.join(scratch_dir, f"temp_mob_slide_{s_idx}.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    out_file = os.path.join(artifacts_dir, fname)
    user_dir = os.path.join(scratch_dir, f"chrome_tmp_allmob_{s_idx}")
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

print("\nDone capturing all 4 mobile slides!")
