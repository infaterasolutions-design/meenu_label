import subprocess
import json

cmd2 = ['git', 'show', '7dd386e:index.html']
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')
p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

obj_str = c2[p2_idx:p2_end].strip()
if obj_str.endswith(','):
    obj_str = obj_str[:-1]

obj_str_fixed = obj_str.replace('{"id": "JAA26DR03942",, "images": ["data:image/jpeg;base64,data:image/jpeg;base64,', '{"id": "JAA26DR03942", "images": ["data:image/jpeg;base64,')
obj_str_fixed = obj_str_fixed.replace('"] "code": "JAA26DR03942"', '"], "code": "JAA26DR03942"')

pos = 71039
print("Around char 71039 in obj_str_fixed:")
print(repr(obj_str_fixed[pos-60:pos+60]))
