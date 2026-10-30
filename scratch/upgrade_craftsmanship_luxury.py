import os, re, base64

def get_base64_img(path):
    if not os.path.exists(path):
        print(f"Warning: {path} not found")
        return ""
    ext = os.path.splitext(path)[1].lower().replace('.', '')
    if ext == 'jpg': ext = 'jpeg'
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:image/{ext};base64,{data}"

print("Script template ready for subagent output.")
