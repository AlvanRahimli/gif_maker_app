import imageio
from pathlib import Path


image_path = Path('source_images')
images = list(image_path.glob('*.png'))
image_list = []

for file_name in images:
    image_list.append(imageio.imread(file_name))
    print("\tFile:", file_name, "read")

print("Writing GIF")
imageio.mimwrite('result.gif', image_list, duration=0.3)
print("DONE")
