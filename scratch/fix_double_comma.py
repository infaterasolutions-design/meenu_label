with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '{"id": "JAA26DR03942",, "images":'
replacement = '{"id": "JAA26DR03942", "images":'

if target in content:
    content = content.replace(target, replacement, 1)
    print("Replaced double-comma in index.html successfully!")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("Target not found!")
