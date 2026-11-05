from PIL import Image

p = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(p)
print("Size:", im.size)
print("Mode:", im.mode)

# Sample some pixel colors across the image to see what the image looks like
colors = im.resize((10, 5)).getdata()
print("Sample colors (top-left to bottom-right):")
for i, c in enumerate(colors):
    print(f"{i:2d}: {c}")
