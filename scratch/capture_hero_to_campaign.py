import subprocess, os

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
out_png = r'C:\Users\sande\Downloads\Meenu_Label_Hero_To_Campaign_Edit.png'

# Create a small preview wrapper that scrolls slightly to showcase Hero bottom + Campaign Edit top
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

script_inject = """window.onload = function() {
  window.scrollTo(0, 500);
};"""

preview_html = text.replace("window.onload = function() {", script_inject)
preview_path = 'scratch/hero_campaign_temp.html'
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_html)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
args = [
    chrome_path,
    "--headless=new",
    f"--screenshot={out_png}",
    "--window-size=1440,1100",
    f"file:///{os.path.abspath(preview_path).replace(os.sep, '/')}"
]

subprocess.run(args, check=True)
print(f"Captured screenshot to {out_png}")

brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'
brain_png = os.path.join(brain_dir, 'Meenu_Label_Hero_To_Campaign_Edit.png')
import shutil
shutil.copyfile(out_png, brain_png)
print(f"Copied to {brain_png}")
