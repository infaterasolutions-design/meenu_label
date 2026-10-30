import subprocess, os, shutil

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Preview focusing on the Founder Section + Footer top
preview_founder_html = text.replace(
    '</head>',
    '<style>.snitch-hero-section, .campaign-edit-section, .craftsmanship-section, .catalog-section, .values-strip { display: none !important; }</style></head>'
)
with open('scratch/preview_founder.html', 'w', encoding='utf-8') as f:
    f.write(preview_founder_html)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'

out_founder_png = r'C:\Users\sande\Downloads\Meenu_Label_Founder_Section_Clean.png'
target_url = f"file:///{os.path.abspath('scratch/preview_founder.html').replace(os.sep, '/')}"

subprocess.run([
    chrome_path,
    '--headless=new',
    '--window-size=1440,780',
    f'--screenshot={out_founder_png}',
    target_url
], check=True)
shutil.copyfile(out_founder_png, os.path.join(brain_dir, 'Meenu_Label_Founder_Section_Clean.png'))
print('Clean founder section screenshot captured!')
