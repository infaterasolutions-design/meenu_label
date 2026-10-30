with open(r'c:\Users\sande\Documents\antigravity\splendid-nobel\meenu-label-shopify-theme\sections\header.liquid', 'r', encoding='utf-8') as f:
    hdr = f.read()

print("Header search button snippet:")
idx = hdr.find('header-search-btn')
print(hdr[idx-100:idx+400].encode('ascii', 'replace').decode('ascii'))

print("\nSearch overlay bar snippet:")
idx2 = hdr.find('searchOverlayBar')
print(hdr[idx2-50:idx2+600].encode('ascii', 'replace').decode('ascii'))
