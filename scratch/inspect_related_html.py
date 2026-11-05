with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'class="pdp-related-section"'
idx = text.find(target)
if idx != -1:
    print(text[idx-30:idx+500])
else:
    print("Not found")
