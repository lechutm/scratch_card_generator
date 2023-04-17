import random
import os
from PIL import Image, ImageDraw, ImageFont

awards = ['nagroda_1', 'nagroda_2', 'nagroda_3', 'nagroda_4', 'nagroda_5', 'nagroda_6', 'nagroda_7', 'nagroda_8']


def get_file_list(dir):
    res = []
    for path_f in os.listdir(dir):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir, path_f)):
            res.append(path_f)
    return res


random.shuffle(awards)

icon_list = get_file_list('./icons/')
# print(icon_list)
a = (128 + 18) * 20
im = Image.new(mode="RGB", size=(1200, a), color=(255, 255, 255))

pos = 100
for idx, icon in enumerate(icon_list):
    drawn_award = awards.pop()

    frontImage = Image.open(f'./icons/{icon}')
    frontImage = frontImage.convert("RGBA")
    im.paste(frontImage, (10, pos), frontImage)
    im1 = ImageDraw.Draw(im)

    myFont = ImageFont.truetype('FreeMono.ttf', 42)
    im1.text((200, pos + 40), drawn_award, font=myFont, fill=(0, 0, 0))

    im1.line([(10, pos), (1100, pos)], fill="black", width=2)
    pos += 128 + 4

# im.show()
im.save("drawn_awards.png", format="png")
