import csv
import os
import random
from PIL import Image, ImageDraw, ImageFont

def get_file_list(dir):
    res = []
    for path_f in os.listdir(dir):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir, path_f)):
            res.append(path_f)
    return res

list_of_icons = get_file_list('./icons/')

POSITIONS = [(558, 472), (758, 472), (958, 472), (558, 650), (758, 650), (958, 650)]

for card_id, icon in enumerate(list_of_icons):
    selected_icons = [icon] * 3
    list_of_icons_temp = list_of_icons.copy()
    list_of_icons_temp.remove(icon)
    while len(selected_icons) < 6:
        chosen = random.choice(list_of_icons_temp)
        if selected_icons.count(chosen) < 3:
            selected_icons.append(chosen)

    random.shuffle(selected_icons)
    print(selected_icons)
    print('--' * 10)

    background = Image.open(f'source_image/source_card-0{random.randint(1, 4)}.png')
    background = background.convert("RGBA")
    for idx, position in enumerate(POSITIONS):
        frontImage = Image.open(f'./icons/{selected_icons[idx]}')
        frontImage = frontImage.convert("RGBA")
        background.paste(frontImage, position, frontImage)

    I1 = ImageDraw.Draw(background)
    myFont = ImageFont.truetype('FreeMono.ttf', 32)
    serial_number = str(card_id + 1).zfill(8)
    I1.text((1000, 826), serial_number, font=myFont, fill=(0, 0, 0))

    # # Save this image
    card_file_name = f'{serial_number}_{icon}'
    background.save(f"./output/{card_file_name}", format="png")


    with open('output_info.csv', 'a', encoding='UTF8') as f:
        data = [serial_number, f'{card_file_name}', icon]
        writer = csv.writer(f)
        writer.writerow(data)
