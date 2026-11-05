import os, shutil
from PIL import Image

artifacts_dir = r'C:\Users\sande\.gemini\antigravity\brain\fe03df0d-2244-4c45-b6ec-4503555ee17f'

# Copy simulated crops to artifacts
shutil.copyfile(r'scratch\sim_drape_desk.jpg', os.path.join(artifacts_dir, 'preview_drape_desk.jpg'))
shutil.copyfile(r'scratch\sim_drape_mob_center.jpg', os.path.join(artifacts_dir, 'preview_drape_mob_center.jpg'))
shutil.copyfile(r'scratch\sim_drape_mob_65.jpg', os.path.join(artifacts_dir, 'preview_drape_mob_65.jpg'))

print("Saved preview files to artifact directory!")
