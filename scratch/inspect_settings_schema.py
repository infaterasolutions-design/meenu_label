with open('config/settings_schema.json', 'r', encoding='utf-8') as f:
    c = f.read()

if '99888' in c or 'whatsapp' in c.lower():
    print('Found in settings_schema.json')
    idx = c.lower().find('whatsapp')
    print(c[idx:idx+300])
else:
    print('Not in settings_schema.json')
