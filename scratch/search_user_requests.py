import json

log_path = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Searching transcript for banner or strip requests...")
for i, line in enumerate(lines):
    try:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            txt = obj.get('content', '')
            if any(k in txt.lower() for k in ['banner', 'strip', 'hero', 'slide', 'promo', 'announcement']):
                print(f"Step {i} USER: {txt[:150]}")
    except:
        pass
