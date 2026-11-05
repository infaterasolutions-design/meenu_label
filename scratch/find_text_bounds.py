import numpy as np
from PIL import Image

src_path = r'c:\Users\sande\Downloads\Festive Maroon Elegance in Bloom.png'
im = Image.open(src_path)
arr = np.array(im)

# Look at rows 100..400 where MEENU LABEL and "Made for Your Special Moments" are located.
# The background is warm beige (approx 220-240, 180-210, 140-170).
# The text is dark burgundy/brown (low values, e.g., < 100).
dark_pixels = np.where((arr[100:600, :, 0] < 120) & (arr[100:600, :, 1] < 80))
min_x = np.min(dark_pixels[1])
max_x = np.max(dark_pixels[1])
print(f"Dark text/model pixels in y=100..600 exist from x={min_x} to x={max_x}")

# Let's inspect where the left text starts
left_dark = np.where((arr[100:600, :800, 0] < 120) & (arr[100:600, :800, 1] < 80))
min_text_x = np.min(left_dark[1])
max_text_x = np.max(left_dark[1])
print(f"Left text box starts at x={min_text_x} and ends at x={max_text_x}")

# And right model starts at:
right_dark = np.where((arr[100:600, 800:, 0] < 120) & (arr[100:600, 800:, 1] < 80))
min_model_x = 800 + np.min(right_dark[1])
max_model_x = 800 + np.max(right_dark[1])
print(f"Model outfit starts at x={min_model_x} and ends at x={max_model_x}")
