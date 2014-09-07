from PIL import Image
import sys
import re

sz = 512
img = Image.new("RGB", (sz, sz))

def testPixels(x, y, sz, s):
    sz >>= 1
    [testPixels(x + sz * (not(i % 3)), y + sz * (i > 1), sz, s + str(i + 1)) for i in range(4) * bool(sz)]
    r = bool(re.match(sys.argv[1], s))
    img.putpixel((x, y), (r * 255, r * 255, r * 255))

testPixels(0, 0, sz, "")

img.save("out.png")
