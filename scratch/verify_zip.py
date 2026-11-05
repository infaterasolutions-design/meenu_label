import zipfile

zip_path = r'C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip'

with zipfile.ZipFile(zip_path, 'r') as z:
    names = z.namelist()

print(f"Total files in ZIP: {len(names)}")
print("Sections:")
for n in names:
    if n.startswith('sections/'):
        print("  -", n)

print("Key Assets:")
for n in names:
    if 'banner_festive_maroon' in n or 'hero_slide_1' in n:
        print("  -", n)
