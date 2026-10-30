with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
body_start = text.find('<body')
body_end = text.find('</body>')

tags = re.findall(r'<([a-zA-Z0-9]+)(\s+id="[^"]*")?(\s+class="[^"]*")?[^>]*>', text[body_start:body_start+4000])
for t in tags[:30]:
    print(t)
