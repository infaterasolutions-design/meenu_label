import subprocess
import json

for commit in ['71ae1af', '7dd386e', '63d7e46', 'HEAD']:
    cmd = ['git', 'show', f'{commit}:index.html']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    content = p.stdout.read().decode('utf-8', errors='replace')
    start_tag = 'var productsData = '
    start_idx = content.find(start_tag)
    start_pos = start_idx + len(start_tag)
    end_pos = content.find(';\n    var cart = [];', start_pos)
    if end_pos == -1: end_pos = content.find(';    var cart = [];', start_pos)
    json_str = content[start_pos:end_pos].strip()
    try:
        data = json.loads(json_str)
        print(f"Commit {commit}: VALID JSON! Product count = {len(data)}")
    except json.JSONDecodeError as e:
        print(f"Commit {commit}: INVALID JSON! Error at pos {e.pos}: {e}")
        print("   Snippet:", repr(json_str[max(0, e.pos-60):min(len(json_str), e.pos+60)]))
