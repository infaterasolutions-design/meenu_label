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

test_content = content[:cur_p2_idx] + clean_p2 + ' ' + content[cur_p2_end:]

# Test parse productsData
start_tag = 'var productsData = '
start_idx = test_content.find(start_tag)
start_pos = start_idx + len(start_tag)
end_pos = test_content.find(';\n    var cart = [];', start_pos)
if end_pos == -1: end_pos = test_content.find(';    var cart = [];', start_pos)

json_str = test_content[start_pos:end_pos].strip()
try:
    data = json.loads(json_str)
    print(f"SUCCESS! All {len(data)} products in productsData are now 100% VALID JSON!")
    for i, p in enumerate(data):
        print(f"  [{i+1}] {p.get('id')}: {p.get('name')} (price: {p.get('price')})")
except json.JSONDecodeError as e:
    print(f"Still JSON error at {e.pos}: {e}")
    print("Around error:", repr(json_str[max(0, e.pos-80):min(len(json_str), e.pos+80)]))
