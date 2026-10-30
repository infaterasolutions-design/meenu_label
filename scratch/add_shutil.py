with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = "import shutil\n" + text

with open('scratch/build_shopify_theme.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added import shutil!')
