from PIL import Image
import sys
import re

def fill(x, y, sz, s):
    [fill(x + sz * (not(i % 3)), y + sz * (i > 1), sz >> 1, s + str(i + 1)) for i in range(4) * bool(sz)]
    img.putpixel((x, y), tuple([bool(re.match(sys.argv[1], s)) * 255] * 3))

img = Image.new("RGB", (512, 512))
fill(0, 0, img.size[0] >> 1, "")
img.save("out.png")
