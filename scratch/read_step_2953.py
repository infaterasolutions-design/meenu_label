import json

with open(r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') in [2953, 2954, 2955, 2956]:
            print(f"Step {obj.get('step_index')}: {obj.get('content') or obj.get('tool_calls')}")
