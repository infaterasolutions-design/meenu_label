import subprocess
import os

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = os.path.join(r"c:\Users\sande\Documents\antigravity\splendid-nobel\scratch", "chrome_temp_eval")

res = subprocess.run([
    chrome_exe,
    "--headless=new",
    "--disable-gpu",
    f"--user-data-dir={temp_dir}",
    "--virtual-time-budget=4000",
    "--dump-dom",
    f"file:///{os.path.abspath('scratch/temp_eval_test.html').replace(os.sep, '/')}"
], capture_output=True)

out = res.stdout.decode('utf-8', errors='ignore')
idx = out.find('id="TEST_OUTPUT_DIV"')
if idx != -1:
    print("RESULT FOUND:")
    print(out[idx:idx+150])
else:
    print("Not found")
