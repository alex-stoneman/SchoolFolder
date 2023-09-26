from PIL import Image
import random
WIDTH = 30
HEIGHT = 30
colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

img = Image.new("RGB", (WIDTH, HEIGHT), color = "blue")
img.save("NewImage.png")

pixValues = list(img.getdata())
print(pixValues)

imgModified = Image.new(img.mode, img.size)
for i in range(len(pixValues)):
    pixValues[i] = random.choice(colours)
imgModified.putdata(pixValues)
imgModified.show()