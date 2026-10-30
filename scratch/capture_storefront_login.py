import subprocess, os

# Create a small wrapper HTML that loads the storefront and immediately opens the login modal
html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Auto-open account modal for screenshot
preview_content = content.replace("window.onload = function() {", "window.onload = function() {\n      setTimeout(openAccountModal, 100);")

preview_file = 'scratch/storefront_login_open.html'
with open(preview_file, 'w', encoding='utf-8') as f:
    f.write(preview_content)

out_png = r'C:\Users\sande\Downloads\Meenu_Label_Snitch_Login_Live.png'

# Take screenshot with Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
args = [
    chrome_path,
    "--headless=new",
    f"--screenshot={out_png}",
    "--window-size=1440,900",
    f"file:///{os.path.abspath(preview_file).replace(os.sep, '/')}"
]

subprocess.run(args, check=True)
print(f"Captured live screenshot to {out_png}")

# Also copy to brain artifacts
brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'
brain_png = os.path.join(brain_dir, 'Meenu_Label_Snitch_Login_Live.png')
import shutil
shutil.copyfile(out_png, brain_png)
print(f"Copied to {brain_png}")
