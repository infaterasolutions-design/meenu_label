import zipfile
import os

zip_path = r'c:\Users\sande\Documents\antigravity\splendid-nobel\Meenu_Label_Shopify_Theme.zip'

with zipfile.ZipFile(zip_path, 'r') as z:
    infolist = z.infolist()
    print(f"Total files: {len(infolist)}")
    total_bytes = sum(i.file_size for i in infolist)
    print(f"Uncompressed size: {total_bytes / (1024*1024):.2f} MB")
    print(f"Compressed zip size: {os.path.getsize(zip_path) / (1024*1024):.2f} MB\n")
    
    dirs = {}
    for i in infolist:
        parts = i.filename.replace('\\', '/').split('/')
        top_dir = parts[0] if len(parts) > 1 else 'root'
        if top_dir not in dirs:
            dirs[top_dir] = []
        dirs[top_dir].append((i.filename, i.file_size))
        
    for d, flist in sorted(dirs.items()):
        total_d_bytes = sum(f[1] for f in flist)
        print(f"=== {d}/ ({len(flist)} files, {total_d_bytes / 1024:.1f} KB) ===")
        for fname, size in sorted(flist):
            print(f"  - {os.path.basename(fname)} ({size/1024:.1f} KB)")
