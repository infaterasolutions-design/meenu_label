import re

p = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

# Find header
h_start = text.find('<header')
h_end = text.find('</header>') + 9
print("=== HEADER HTML ===")
print(text[h_start:h_end][:800])
print("...\nLength:", h_end - h_start)

# Find announcement bar
a_start = text.find('<!-- Top Marquee -->')
if a_start == -1: a_start = text.find('class="announcement-bar"')
print("=== ANNOUNCEMENT BAR HTML ===")
print(text[a_start:a_start+400])
