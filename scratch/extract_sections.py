import re

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's extract between body tags or major landmarks
# Exclude base64 images to keep output small
def clean_html(snippet):
    return re.sub(r'data:image\/[^;]+;base64,[a-zA-Z0-9+/=]+', '[BASE64_IMG]', snippet)

# Find sections
sections = ['campaign-edit-section', 'craftsmanship-section', 'catalog-section', 'founder-section', 'value-strip']

for s in sections:
    pattern = rf'(<section[^>]*class="[^"]*{s}[^"]*"[^>]*>[\s\S]*?<\/section>)'
    m = re.search(pattern, html)
    if m:
        snippet = clean_html(m.group(1))
        # Print first 1000 chars of snippet
        print(f"==================== SECTION: {s} ====================")
        print(snippet[:1200])
        print("...\n")
    else:
        # maybe div?
        pattern_div = rf'(<div[^>]*class="[^"]*{s}[^"]*"[^>]*>[\s\S]*?<\/div>\s*<\/div>)'
        m_div = re.search(pattern_div, html)
        if m_div:
            snippet = clean_html(m_div.group(1))
            print(f"==================== DIV: {s} ====================")
            print(snippet[:1200])
            print("...\n")
        else:
            print(f"NOT FOUND: {s}")

# Check value-strip or similar
m_val = re.search(r'(<div[^>]*class="[^"]*value[^"]*"[^>]*>[\s\S]*?<\/div>)', html)
if m_val:
    print("==================== VALUE ====================")
    print(clean_html(m_val.group(1))[:800])

# Check footer
m_foot = re.search(r'(<footer[\s\S]*?<\/footer>)', html)
if m_foot:
    print("==================== FOOTER ====================")
    print(clean_html(m_foot.group(1))[:1000])
