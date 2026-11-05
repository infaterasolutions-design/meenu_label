import subprocess
import json

cmd1 = ['git', 'show', '71ae1af:index.html']
c1 = subprocess.check_output(cmd1).decode('utf-8', errors='replace')
p1_idx = c1.find('{"id": "JAA26DR03942"')
p1_end = c1.find('{"id": "SET916"', p1_idx)

obj_str1 = c1[p1_idx:p1_end].strip().rstrip(',')
p1_data = json.loads(obj_str1)
print("71ae1af p1_data:")
for k, v in p1_data.items():
    if k == 'b64':
        print(f"  {k}: {v[:40]}... (len={len(v)})")
    else:
        print(f"  {k}: {repr(v)}")
