import zipfile, sys

with zipfile.ZipFile(r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip", "r") as z:
    content = z.read('sections/main-product.liquid')
    sys.stdout.buffer.write(content)
