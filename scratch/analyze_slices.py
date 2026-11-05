import numpy as np
from PIL import Image

p = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(p)
w, h = im.size

# Let's see color variance across horizontal slices of 10%
img_arr = np.array(im)
print("Image shape:", img_arr.shape)

for i in range(10):
    start_x = int(i * w / 10)
    end_x = int((i + 1) * w / 10)
    slice_arr = img_arr[:, start_x:end_x]
    mean_color = slice_arr.mean(axis=(0,1))
    std_color = slice_arr.std(axis=(0,1))
    print(f"Slice {i} (x={start_x:4d}..{end_x:4d}): Mean RGB=({mean_color[0]:.1f}, {mean_color[1]:.1f}, {mean_color[2]:.1f}) Std=({std_color[0]:.1f}, {std_color[1]:.1f}, {std_color[2]:.1f})")
