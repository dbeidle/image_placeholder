
from PIL import Image, ImageDraw, ImageFont


def new_image(width, height, name):
    if "'" in name:
        name = name.replace("'", "")
    if " " in name:
        fname = name.replace(" ", "_")
    else:
        fname = name

    i = Image.new(mode="RGB", size=(width, height), color=(70, 130, 180))
    draw = ImageDraw.Draw(i)
    if name is not None:
        txt = name.replace("_", " ")
    else:
        txt = f"{width} X {height}"
    font = ImageFont.truetype("Arial.ttf", 20)

    textwidth, textheight = draw.textsize(txt, font)
    x = width/2-textwidth/2
    y = height/2-textheight

    draw.text((x, y), name, font=font)

    i.save(f"temp/{fname}.jpeg")
    i.close()
    return f"temp/{fname}.jpeg"
