import shutil

src = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme.zip"
backup = r"C:\Users\sande\Downloads\Meenu_Label_Shopify_Theme_backup.zip"
shutil.copyfile(src, backup)
print("Shopify Theme backup created successfully at:", backup)
