import json

log_path = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

obj = json.loads(lines[97])
print("Step 97 full content:")
print(obj.get('content').encode('ascii', 'replace').decode('ascii'))
