with open('scratch/build_snitch_storefront.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_nav = text.find('id="navDrawerBackdrop"')
if pos_nav == -1:
    pos_nav = text.find('id="navDrawer"')
end_nav = text.find('</div>', text.find('</ul>', pos_nav)) + 6
end_backdrop = text.find('</div>', end_nav) + 6

print("Nav drawer chunk:")
print(text[pos_nav-50:end_backdrop+100].encode('ascii', errors='replace').decode('ascii'))
