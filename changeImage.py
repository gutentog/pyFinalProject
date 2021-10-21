
#!/usr/bin/env python3
# Note: The raw images from images subdirectory contains alpha transparency layers.
# So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images.
# Use convert("RGB") method for converting RGBA to RGB image.
# You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
# Size: Change image resolution from 3000x2000 to 600x400 pixel
# Format: Change image format from .TIFF to .JPEG

import os
from PIL import Image

cwd = os.getcwd()
path = cwd + '/supplier-data/images/'
print(path)

for file in os.listdir(path):
    if not file.startswith('.'):
        if file.endswith('tiff'):
            im = Image.open(path + file)
            print(path + file)
            new_file = file.replace('tiff', 'jpeg')
            print(path + new_file)
            im.convert('RGB').resize((600, 400)).save(path + new_file, 'JPEG')
