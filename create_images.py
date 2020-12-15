from PIL import Image, ImageDraw, ImageFont
import imageio
from pathlib import Path
import sys
from resizeimage import resizeimage

input_text = sys.argv[1]
lines = input_text.split('/')

original_image = Image.open('corona.jpg')
original_image = resizeimage.resize_height(original_image, 500)
original_image.save("resized.png")

resized_image = Image.open("resized.png")
(width, height) = resized_image.size
resized_image = resized_image.crop((width/2 - 250, height/2 - 250, width/2 + 250, height/2+250))
resized_image = resized_image.point(lambda p: p * 0.3)

draw = ImageDraw.Draw(resized_image)

def drawText(text, output_name, y = 50):
    font = ImageFont.truetype('rm_typerighter.ttf', size=60)
    x = 50
    color = 'rgb(255, 255, 255)'

    draw.text((x, y), text, fill=color, font=font)

    resized_image.save("source_images/" + output_name + ".png")
    print("\tCreated: " + output_name + ".png")

def drawLines(lines):
    y_value = 50
    scene_num = 1
    for line in lines:
        for i in range(1, len(line) + 1):
            partial = ""
            for j in range(i):
                partial += line[j]

            drawText(partial, "scene_" + str(scene_num), y_value)
            scene_num += 1
        y_value += 60

def makeGif():
    image_path = Path('source_images')
    images = list(image_path.glob('*.png'))
    image_list = []

    for file_name in images:
        image_list.append(imageio.imread(file_name))
        print("\tFile:", file_name, "read")

    print("Writing GIF")
    imageio.mimwrite('result.gif', image_list, duration=0.1)
    print("DONE")


drawLines(lines)
makeGif()

