import re

with open(r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html', 'r', encoding='utf-8') as f:
    html = f.read()

onclicks = re.findall(r'onclick="([^"]+)"', html)
print('Total onclick attributes found:', len(onclicks))

unique_calls = set()
for oc in onclicks:
    # Get the function name
    m = re.match(r'([a-zA-Z0-9_$]+)\s*\(', oc.strip())
    if m:
        unique_calls.add(m.group(1))
    else:
        unique_calls.add(oc.strip())

print('Unique onclick functions / expressions:')
for uc in sorted(unique_calls):
    print('  -', uc)
