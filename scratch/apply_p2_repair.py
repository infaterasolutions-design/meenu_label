import subprocess
import json

# 1. Get clean JAA26DR03942 from 71ae1af
cmd1 = ['git', 'show', '71ae1af:index.html']
c1 = subprocess.check_output(cmd1).decode('utf-8', errors='replace')
p1_idx = c1.find('{"id": "JAA26DR03942"')
p1_end = c1.find('{"id": "SET916"', p1_idx)
clean_p2 = c1[p1_idx:p1_end].strip()
if not clean_p2.endswith(','):
    clean_p2 += ','

# 2. In index.html, find current JAA26DR03942
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cur_p2_idx = content.find('{"id": "JAA26DR03942"')
cur_p2_end = content.find('{"id": "SET916"', cur_p2_idx)

new_content = content[:cur_p2_idx] + clean_p2 + ' ' + content[cur_p2_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Saved repaired index.html successfully!")
