import json

log_path = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Find user messages in the last 50 lines
for i, line in enumerate(lines[-50:]):
    try:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT' or 'media' in obj:
            print(f"Line {len(lines)-50+i}:", obj.get('content', '')[:100], "Media:", obj.get('media'))
    except Exception as e:
        pass
