from random import random
from PIL import Image, ImageDraw
import colorsys
import sys

if len(sys.argv) < 2:
    print "Usage: python colors.py <path_to_wallpaper>"
    exit()

def dist(a, b):
    r = 0
    for i in range(3):
        r += (a[i] - b[i]) ** 2
    return r

def initMeans(k):
    means = []
    for i in range(k):
        means.append((int(random() * 256),
                      int(random() * 256),
                      int(random() * 256)))
    return means

def initClusters(k):
    clusters = []
    for i in range(k):
        clusters.append([])
    return clusters

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

out = Image.new("RGB", (99, 33))
draw = ImageDraw.Draw(out)
img = Image.open(sys.argv[1])
img = img.resize((200, 200), Image.ANTIALIAS)
px = img.load()

k = 3
means = initMeans(k)
while True:
    old = []
    for i in range(k):
        old.append(means[i])
    clusters = initClusters(k)
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

for i in range(k):
    if clusters[i]:
        draw.rectangle((i * 33, 0, i * 33 + 33, 33), fill=means[i])

img.show()
out.show()
