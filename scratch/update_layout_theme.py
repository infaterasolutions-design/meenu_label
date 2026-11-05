with open('layout/theme.liquid', 'r', encoding='utf-8') as f:
    text = f.read()

target = "{% render 'size-guide-modal' %}"
replacement = "{% render 'size-guide-modal' %}\n    {% render 'quick-size-modal' %}"

if target in text and "{% render 'quick-size-modal' %}" not in text:
    text = text.replace(target, replacement, 1)
    with open('layout/theme.liquid', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated layout/theme.liquid successfully!")
else:
    print("Already updated or target not found")
