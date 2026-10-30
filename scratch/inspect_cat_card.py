with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\scratch\extracted_sections\catalog-section.html', 'r', encoding='utf-8') as f:
    cat = f.read()

# find first product card
import re
cards = re.findall(r'(<div class="product-card"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>)', cat)
if cards:
    print("Found", len(cards), "cards. First card:")
    print(cards[0][:1500].encode('ascii', 'replace').decode('ascii'))
else:
    print("No full card found, let's search snippet:")
    print(cat[:1500].encode('ascii', 'replace').decode('ascii'))
