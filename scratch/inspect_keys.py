import subprocess

cmd2 = ['git', 'show', '7dd386e:index.html']
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')
p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

obj_str = c2[p2_idx:p2_end]
second_id = obj_str.find('"code": "JAA26DR03942"')
print("Snippet around second id:")
print(repr(obj_str[second_id-100:second_id+100]))
