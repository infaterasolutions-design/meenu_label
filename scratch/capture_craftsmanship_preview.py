import subprocess, os, shutil

html_path = r'C:\Users\sande\Downloads\Meenu_Label_Desktop_Storefront.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Preview focusing on Craftsmanship Spotlight
craft_script = """
<script>
window.addEventListener('DOMContentLoaded', function() {
  setTimeout(function() {
    var el = document.querySelector('.craftsmanship-section');
    if (el) {
      el.scrollIntoView({behavior: 'instant', block: 'start'});
    }
  }, 100);
});
</script>
</body>
"""
preview_craft = text.replace("</body>", craft_script)
with open('scratch/craft_temp.html', 'w', encoding='utf-8') as f:
    f.write(preview_craft)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_png = r'C:\Users\sande\Downloads\Meenu_Label_Craftsmanship_Spotlight.png'
brain_dir = r'C:\Users\sande\.gemini\antigravity\brain\1d796c0f-b986-45c2-b599-b8a1dc691d66'

args = [
    chrome_path,
    "--headless=new",
    "--virtual-time-budget=2000",
    f"--screenshot={out_png}",
    "--window-size=1440,1150",
    f"file:///{os.path.abspath('scratch/craft_temp.html').replace(os.sep, '/')}"
]
subprocess.run(args, check=True)
print("Craftsmanship spotlight captured!")
shutil.copyfile(out_png, os.path.join(brain_dir, 'Meenu_Label_Craftsmanship_Spotlight.png'))

# 2. Preview showing Campaign Edit + Craftsmanship Spotlight transition
flow_script = """
<script>
window.addEventListener('DOMContentLoaded', function() {
  setTimeout(function() {
    var el = document.querySelector('.campaign-edit-section');
    if (el) {
      var top = el.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo(0, top);
    }
  }, 100);
});
</script>
</body>
"""
preview_flow = text.replace("</body>", flow_script)
with open('scratch/flow_temp.html', 'w', encoding='utf-8') as f:
    f.write(preview_flow)

out_flow_png = r'C:\Users\sande\Downloads\Meenu_Label_Editorial_And_Craftsmanship.png'
args_flow = [
    chrome_path,
    "--headless=new",
    "--virtual-time-budget=2000",
    f"--screenshot={out_flow_png}",
    "--window-size=1440,1800",
    f"file:///{os.path.abspath('scratch/flow_temp.html').replace(os.sep, '/')}"
]
subprocess.run(args_flow, check=True)
print("Editorial + Craftsmanship transition captured!")
shutil.copyfile(out_flow_png, os.path.join(brain_dir, 'Meenu_Label_Editorial_And_Craftsmanship.png'))
