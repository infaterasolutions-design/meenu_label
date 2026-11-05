with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r',,', content)]
print(f"Total occurrences of double-comma: {len(matches)}")
for pos in matches:
    print(pos, repr(content[pos-30:pos+30]))
