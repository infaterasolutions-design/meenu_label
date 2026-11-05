import subprocess
import json

cmd2 = ['git', 'show', '7dd386e:index.html']
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')
p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

obj_str = c2[p2_idx:p2_end].rstrip().rstrip(',')
second_id = obj_str.find('"code": "JAA26DR03942"')

# If we remove the first '{"id": "JAA26DR03942",, "images": [' and replace with proper syntax, let's see what it was trying to be
print("Beginning of obj_str:", repr(obj_str[:80]))
print("End of images array:", repr(obj_str[second_id-40:second_id+40]))
