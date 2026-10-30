import zipfile, sys

with zipfile.ZipFile(r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip", "r") as z:
    for target in ['sections/announcement-bar.liquid', 'snippets/cart-drawer.liquid', 'sections/main-product.liquid']:
        print(f"=== {target} ===")
        content = z.read(target)
        sys.stdout.buffer.write(content[:600])
        print("\n\n")
