with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('header_liquid =')
if pos != -1:
    end = text.find('"""', pos + 20)
    print(text[pos:end+3].encode('ascii', errors='replace').decode('ascii'))
