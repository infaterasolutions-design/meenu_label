import os

theme_dir = r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme'

for f in ['founder-story.liquid', 'footer.liquid', 'featured-collection.liquid', 'header.liquid', 'announcement-bar.liquid']:
    p = os.path.join(theme_dir, 'sections', f)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"=== {f} ({len(content)} chars) ===")
        # print first 500 chars (ascii safe)
        print(content[:500].encode('ascii', 'replace').decode('ascii'))
        print("...\n")
