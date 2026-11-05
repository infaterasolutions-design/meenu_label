import subprocess

cmd2 = ['git', 'show', '7dd386e:index.html']
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')
p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

obj_str = c2[p2_idx:p2_end].strip()
import re
print("Matches of JAA26DR03942:", [m.start() for m in re.finditer(r'JAA26DR03942', obj_str)])

for m in re.finditer(r'JAA26DR03942', obj_str):
    pos = m.start()
    print("Match at", pos, ":", repr(obj_str[pos-30:pos+60]))
