from PIL import Image

for name in ['hero_slide_1.jpg', 'hero_slide_2.jpg', 'hero_slide_3.jpg', 'hero_slide_4.jpg']:
    p = rf'c:\Users\sande\Documents\antigravity\splendid-nobel\assets\{name}'
    try:
        im = Image.open(p)
        print(f"{name}: {im.size}, aspect: {im.size[0]/im.size[1]:.2f}")
    except Exception as e:
        print(f"{name}: {e}")
