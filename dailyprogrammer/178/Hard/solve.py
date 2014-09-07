from PIL import Image
import sys
import re

sz = 400
img = Image.new("RGB", (sz, sz))

def testPixels(x, y, sz, s):
    if sz == 1:
        if re.match(sys.argv[1], s):
            img.putpixel((x, y), (255, 255, 255))
        return
    nsz = sz >> 1
    for i in range(4):
        testPixels(x + nsz * (not(i % 3)), y + nsz * (i > 1), nsz, s + str(i + 1))

testPixels(0, 0, sz, "")

img.save("out.png")
