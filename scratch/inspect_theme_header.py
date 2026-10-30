with open('scratch/build_shopify_theme.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('header_liquid =')
end = text.find('{% endschema %}\n"""', pos) + len('{% endschema %}\n"""')
print(text[pos:end].encode('ascii', errors='replace').decode('ascii'))
