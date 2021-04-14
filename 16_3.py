n = int(input())
b = [[int(input()) for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    x = int(input())
    y = int(input())
    for _y in range(-1, 2):
        for _x in range(-1, 2):
            if (0 <= x + _x <= n - 1) and (0 <= y + _y <= n - 1):
                if _y == 0 and _x == 0:
                    if b[y + _y][x + _x] >= 8:
                        b[y + _y][x + _x] -= 8
                    else:
                        b[y + _y][x + _x] = 0
                else:
                    if b[y + _y][x + _x] >= 4:
                        b[y + _y][x + _x] -= 4
                    else:
                        b[y + _y][x + _x] = 0

for y in range(n):
    for x in range(n):
        print(b[y][x], end=' ')
    print('')
