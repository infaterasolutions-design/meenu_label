with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
m_hero = re.search(r'(<div class="snitch-track" id="sliderTrack">[\s\S]*?<\/div>\s*<!-- Navigation Chevrons -->)', html)
if m_hero:
    # remove base64
    clean = re.sub(r'data:image\/[^;]+;base64,[^\']+', 'HERO_IMG_SRC', m_hero.group(1))
    print(clean.encode('ascii', 'replace').decode('ascii'))
