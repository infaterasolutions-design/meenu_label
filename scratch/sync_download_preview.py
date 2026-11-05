import shutil, os

src = r'c:\Users\sande\Documents\antigravity\splendid-nobel\index.html'
dst = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

shutil.copyfile(src, dst)
print("Copied updated index.html to Meenu_Label_Desktop_Storefront.html:", os.path.exists(dst), os.path.getsize(dst))
