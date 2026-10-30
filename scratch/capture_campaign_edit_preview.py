import subprocess, os

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
out_png = r'C:\Users\sande\Downloads\Meenu_Label_Campaign_Edit_Section.png'

# Create a small preview wrapper that focuses directly on the campaign edit section
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Scroll directly to campaign-edit-section on load
script_inject = """window.onload = function() {
  var el = document.querySelector('.campaign-edit-section');
  if (el) el.scrollIntoView();
};"""

preview_html = text.replace("window.onload = function() {", script_inject)
preview_path = 'scratch/campaign_preview_temp.html'
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
brain_png = os.path.join(brain_dir, 'Meenu_Label_Campaign_Edit_Section.png')
import shutil
shutil.copyfile(out_png, brain_png)
print(f"Copied to {brain_png}")
