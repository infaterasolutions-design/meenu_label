from PIL import Image

im = Image.open(r'C:\Users\sande\Downloads\Grace in Every Drape.png')

def simulate_cover(im, target_w, target_h, pos_x=0.5, pos_y=0.5):
    scale = max(target_w / im.size[0], target_h / im.size[1])
    new_w = int(round(im.size[0] * scale))
    new_h = int(round(im.size[1] * scale))
    resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    crop_x = int(round((new_w - target_w) * pos_x))
    crop_y = int(round((new_h - target_h) * pos_y))
    cropped = resized.crop((crop_x, crop_y, crop_x + target_w, crop_y + target_h))
    return cropped

# 1. Desktop 1280x600 (center center)
desk = simulate_cover(im, 1280, 600, 0.5, 0.5)
desk.save(r'scratch\sim_drape_desk.jpg', quality=90)

# 2. Mobile 375x550 (center center)
mob_center = simulate_cover(im, 375, 550, 0.5, 0.5)
mob_center.save(r'scratch\sim_drape_mob_center.jpg', quality=90)

# 3. Mobile 375x550 (pos_x = 0.65)
mob_65 = simulate_cover(im, 375, 550, 0.65, 0.5)
mob_65.save(r'scratch\sim_drape_mob_65.jpg', quality=90)

print("Simulations saved!")
