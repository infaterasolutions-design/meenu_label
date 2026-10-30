import shutil

src = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html"
backup = r"C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront_backup.html"
shutil.copyfile(src, backup)
print("Backup created successfully at:", backup)
