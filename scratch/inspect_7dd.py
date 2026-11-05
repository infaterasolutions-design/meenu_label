import subprocess
import json

cmd = ['git', 'show', '7dd386e:index.html']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
content = p.stdout.read().decode('utf-8', errors='replace')

start_tag = 'var productsData = '
start_idx = content.find(start_tag)
start_pos = start_idx + len(start_tag)
end_pos = content.find(';\n    var cart = [];', start_pos)
if end_pos == -1:
    end_pos = content.find(';    var cart = [];', start_pos)

print(f"In 7dd386e: start_pos={start_pos}, end_pos={end_pos}")
json_str = content[start_pos:end_pos].strip()

# Find JAA26DR03942
idx = json_str.find('JAA26DR03942')
print("Snippet around JAA26DR03942 in 7dd386e:")
print(repr(json_str[idx-40:idx+200]))
