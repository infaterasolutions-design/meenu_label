import subprocess
import json

cmd2 = ['git', 'show', '7dd386e:index.html']
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')
p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

obj_str = c2[p2_idx:p2_end].strip()
if obj_str.endswith(','):
    obj_str = obj_str[:-1]

# Apply fix 1: remove double comma and duplicate data:image prefix
obj_str_fixed = obj_str.replace('{"id": "JAA26DR03942",, "images": ["data:image/jpeg;base64,data:image/jpeg;base64,', '{"id": "JAA26DR03942", "images": ["data:image/jpeg;base64,')

# Apply fix 2: add comma after images array before "code":
obj_str_fixed = obj_str_fixed.replace('"] "code": "JAA26DR03942"', '"], "code": "JAA26DR03942"')

try:
    p2 = json.loads(obj_str_fixed)
    print("SUCCESS! p2 parsed cleanly!")
    print("Keys in p2:", list(p2.keys()))
    print("Images count:", len(p2.get('images', [])))
    print("Name:", p2.get('name'))
    print("Price:", p2.get('price'))
except Exception as e:
    print("Error parsing p2:", e)
