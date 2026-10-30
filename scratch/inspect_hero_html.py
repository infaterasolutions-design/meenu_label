with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="snitch-hero-section"')
while pos != -1:
    if '<section' in text[pos-20:pos]:
        print(text[pos-20:pos+2500].encode('ascii', errors='replace').decode('ascii'))
        break
    pos = text.find('class="snitch-hero-section"', pos+30)
