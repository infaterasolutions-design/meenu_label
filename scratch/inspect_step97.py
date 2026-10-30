import json

log_path = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(95, 105):
    obj = json.loads(lines[i])
    print(f"Step {i} ({obj.get('type')}, {obj.get('source')}):")
    if obj.get('content'):
        print(obj.get('content')[:300].encode('ascii', 'replace').decode('ascii'))
    if obj.get('media'):
        print("Media:", obj.get('media'))
