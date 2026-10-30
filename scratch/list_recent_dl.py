import os
import glob

dl = r'C:\Users\sande\Downloads'
files = [os.path.join(dl, f) for f in os.listdir(dl) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

print("Recent images in Downloads:")
for f in files[:25]:
    print(f"{os.path.basename(f)} ({os.path.getsize(f)} bytes) - mtime: {os.path.getmtime(f)}")
