img = __import__("PIL.Image").Image.open(__import__("sys").argv[1])
img.putdata([tuple([(r + g + b) / 3] * 3) for (r, g, b) in list(img.getdata())])
img.show()
