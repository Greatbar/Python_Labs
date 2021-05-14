def image_filter(pixels, i, j):
    """Создает эффект сепии(делает RGB в светло-коричневых тонах, как на старых фотографиях)
    Чтобы получить сепию, нужно посчитать среднее значение и взять какой — нибудь коэффициент.
    По умолчанию установлен коэффициент - 50"""
    depth = 50
    r = pixels[i, j][0]
    g = pixels[i, j][1]
    b = pixels[i, j][2]
    middle = (r + g + b) // 3
    r = middle + depth * 2
    g = middle + depth
    b = middle
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    return ((i, j), (r, g, b))


help(image_filter)
