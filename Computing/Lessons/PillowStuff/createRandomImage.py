import random

from PIL import Image

r=random.randint

im = Image.new("RGB", (602, 602))
count = 0
for x in range(im.size[0]):
    for y in range(im.size[1]):
        if count % 3 == 0:
            im.putpixel((y, x), (55, r(40, 200), r(0,255)))
        elif count % 3 == 1:
            im.putpixel((y, x), (100, r(0, 255), 255))
        else:
            im.putpixel((y, x), (r(0, 255), r(0, 255), r(0, 255)))
        count += 1
im.show()



im.save("images\\image2.png")