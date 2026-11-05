import subprocess

cmd1 = ['git', 'show', '71ae1af:index.html']
cmd2 = ['git', 'show', '7dd386e:index.html']

c1 = subprocess.check_output(cmd1).decode('utf-8', errors='replace')
c2 = subprocess.check_output(cmd2).decode('utf-8', errors='replace')

p1_idx = c1.find('{"id": "JAA26DR03942"')
p1_end = c1.find('{"id": "SET916"', p1_idx)

p2_idx = c2.find('{"id": "JAA26DR03942"')
p2_end = c2.find('{"id": "SET916"', p2_idx)

print("--- In 71ae1af (VALID): ---")
print("Length:", p1_end - p1_idx)
print(repr(c1[p1_idx:p1_idx+500]))

print("\n--- In 7dd386e (INVALID): ---")
print("Length:", p2_end - p2_idx)
print(repr(c2[p2_idx:p2_idx+500]))
