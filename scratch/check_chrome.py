import subprocess
import os

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]

for p in chrome_paths:
    if os.path.exists(p):
        print("Found Chrome at:", p)
        break
else:
    print("Chrome not found in standard paths")
