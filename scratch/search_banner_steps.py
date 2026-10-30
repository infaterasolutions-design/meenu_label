import json

log_path = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Searching transcript for banner changes after step 100...")
for i in range(100, min(1000, len(lines))):
    try:
        obj = json.loads(lines[i])
        if obj.get('type') == 'USER_INPUT':
            txt = obj.get('content', '')
            if any(k in txt.lower() for k in ['banner', 'hero', 'slide', 'image', 'picture', 'text']):
                print(f"Step {i} USER: {txt[:120]}")
    except:
        pass
