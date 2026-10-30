import os
import glob

search_dirs = [
    r'C:\Users\sande\Downloads',
    r'c:\Users\sande\Documents\antigravity\splendid-nobel',
    r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'
]

print("Searching for banner images...")
for d in search_dirs:
    for ext in ['*.jpg', '*.png', '*.webp']:
        for p in glob.glob(os.path.join(d, '**', ext), recursive=True):
            fname = os.path.basename(p).lower()
            if 'banner' in fname or 'hero' in fname or 'slide' in fname or 'drop' in fname:
                print(f"{p} ({os.path.getsize(p)} bytes)")
