from random import random
from PIL import Image, ImageDraw
import sys

if len(sys.argv) < 2:
    print "Usage: python colors.py <path_to_wallpaper> [nb_of_means]"
    exit()

def dist(a, b):
    return (sum([(a[i] - b[i]) ** 2 for i in range(3)]))

def initMeans(k):
    return [tuple([int(random() * 256) for x in range(3)]) for i in range(k)]

def assignPts(k, px, means, clusters, sz):
    for y in range(sz[1]):
        for x in range(sz[0]):
            mind = 256 * 256 * 3
            mini = 0
            for i in range(k):
                tmpd = dist(px[x, y], means[i])
                if tmpd < mind:
                    mini = i
                    mind = tmpd
            clusters[mini].append((x, y))

def updateMeans(k, px, means, clusters):
    for i in range(k):
        if not clusters[i]:
            continue
        avg = [0, 0, 0]
        for pt in clusters[i]:
            avg[0] += px[pt][0]
            avg[1] += px[pt][1]
            avg[2] += px[pt][2]
        sz = len(clusters[i])
        means[i] = (avg[0] / sz, avg[1] / sz, avg[2] / sz)

k = 3 if len(sys.argv) < 3 else int(sys.argv[2])
out = Image.new("RGB", (100 * k, 100))
draw = ImageDraw.Draw(out)
img = Image.open(sys.argv[1])
img = img.resize((200, 200), Image.ANTIALIAS)
px = img.load()

means = initMeans(k)
while True:
    old = []
    for i in range(k):
        old.append(means[i])
    clusters = [[] for i in range(k)]
    assignPts(k, px, means, clusters, img.size)
    updateMeans(k, px, means, clusters)
    stable = True
    for i in range(k):
        if old[i] != means[i]:
            stable = False
        if len(clusters[i]) == 0:
            means[i] = initMeans(1)[0]
            stable = False
    if stable:
        break


indexes = sorted(range(len(clusters)), key=lambda c: len(clusters[c]), reverse=True)
x = 0
for i in indexes:
    width = len(clusters[i]) * out.size[0] / (img.size[0] * img.size[1])
    draw.rectangle((x, 0, x + width, out.size[1]), fill=means[i])
    x += width

img.show()
out.show()
