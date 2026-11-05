from PIL import Image

im = Image.open(r'C:\Users\sande\Downloads\Modern Ethnic Elegance Banner.png')
w, h = im.size # 1920, 819

# Function to simulate background-size: cover with background-position (pos_x, pos_y)
def simulate_cover(im, target_w, target_h, pos_x=0.5, pos_y=0.5):
    # scale factor
    scale = max(target_w / im.size[0], target_h / im.size[1])
    new_w = int(round(im.size[0] * scale))
    new_h = int(round(im.size[1] * scale))
    resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Crop
    crop_x = int(round((new_w - target_w) * pos_x))
    crop_y = int(round((new_h - target_h) * pos_y))
    cropped = resized.crop((crop_x, crop_y, crop_x + target_w, crop_y + target_h))
    return cropped

# 1. Desktop 1280x600 (center center)
desk = simulate_cover(im, 1280, 600, 0.5, 0.5)
desk.save(r'scratch\sim_desktop_cover.jpg', quality=90)

# 2. Mobile 375x550 (center center)
mob_center = simulate_cover(im, 375, 550, 0.5, 0.5)
mob_center.save(r'scratch\sim_mob_center.jpg', quality=90)

# 3. Mobile 375x550 (pos_x = 0.55)
mob_55 = simulate_cover(im, 375, 550, 0.55, 0.5)
mob_55.save(r'scratch\sim_mob_55.jpg', quality=90)

print("Simulations saved!")
