import shutil, os

src = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
dst = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f\festive_maroon_preview.png'
shutil.copyfile(src, dst)
print("Copied to artifact dir:", os.path.exists(dst), os.path.getsize(dst))
