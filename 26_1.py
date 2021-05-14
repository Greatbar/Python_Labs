from PIL import Image

def gradient(color):
    color = color.upper()
    im = Image.new("RGB", (512, 200), (0, 0, 0))
    pixels = im.load()
    r = 0
    g = 0
    b = 0
    if color == 'R':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                r += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'G':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                g += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    elif color == 'B':
        for i in range(512):
            if i % 2 == 0 and i != 0:
                b += 1
            for j in range(200):
                pixels[i, j] = r, g, b

    im.save('res.png')