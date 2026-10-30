import subprocess, os, shutil

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Preview dedicated to Craftsmanship Spotlight
preview_craft_html = text.replace(
    '</head>',
    '<style>.snitch-hero-section, .campaign-edit-section { display: none !important; }</style></head>'
)
with open('scratch/preview_luxury_craft.html', 'w', encoding='utf-8') as f:
    f.write(preview_craft_html)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'

out_craft_png = r'C:\Users\sande\Downloads\Meenu_Label_Craftsmanship_Luxury_Spotlight.png'
target_craft_url = f"file:///{os.path.abspath('scratch/preview_luxury_craft.html').replace(os.sep, '/')}"

subprocess.run([
    chrome_path,
    '--headless=new',
    '--window-size=1440,1320',
    f'--screenshot={out_craft_png}',
    target_craft_url
], check=True)
shutil.copyfile(out_craft_png, os.path.join(brain_dir, 'Meenu_Label_Craftsmanship_Luxury_Spotlight.png'))
print('Luxury craftsmanship spotlight captured!')

# 2. Preview showing Campaign Edit + Luxury Craftsmanship transition
preview_flow_html = text.replace(
    '</head>',
    '<style>.snitch-hero-section { display: none !important; }</style></head>'
)
with open('scratch/preview_flow_lux.html', 'w', encoding='utf-8') as f:
    f.write(preview_flow_html)

out_flow_png = r'C:\Users\sande\Downloads\Meenu_Label_Editorial_To_Craftsmanship_Upgraded.png'
target_flow_url = f"file:///{os.path.abspath('scratch/preview_flow_lux.html').replace(os.sep, '/')}"

subprocess.run([
    chrome_path,
    '--headless=new',
    '--window-size=1440,2150',
    f'--screenshot={out_flow_png}',
    target_flow_url
], check=True)
shutil.copyfile(out_flow_png, os.path.join(brain_dir, 'Meenu_Label_Editorial_To_Craftsmanship_Upgraded.png'))
print('Flow preview captured!')
