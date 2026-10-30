with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Find announcement bar
m_promo = re.search(r'(<!-- TOP PROMO[\s\S]*?<\/div>\s*<\/div>)', html)
if not m_promo:
    m_promo = re.search(r'(<div[^>]*class="[^"]*announcement[^"]*"[\s\S]*?<\/div>\s*<\/div>)', html)
if m_promo:
    print("=== ANNOUNCEMENT BAR IN STOREFRONT ===")
    print(m_promo.group(1).encode('ascii', 'replace').decode('ascii'))
else:
    # search for any promo or announcement
    lines = [l for l in html.splitlines() if 'announcement' in l or 'CHANDIGARH' in l]
    print("Announcement matches in storefront:")
    for l in lines[:15]:
        print(l.encode('ascii', 'replace').decode('ascii'))

# Find Hero section in storefront
m_hero = re.search(r'(<section[^>]*class="[^"]*hero[^"]*"[\s\S]*?<\/section>)', html)
if m_hero:
    clean_hero = re.sub(r'data:image\/[^;]+;base64,[a-zA-Z0-9+/=]+', '[BASE64_IMG]', m_hero.group(1))
    print("\n=== HERO SECTION IN STOREFRONT ===")
    print(clean_hero.encode('ascii', 'replace').decode('ascii'))
