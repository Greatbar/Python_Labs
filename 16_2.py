number = int(input())
coordinates = []
table = [[el for el in input().split(',')] for i in range(number)]
m = int(input())
for _ in range(m):
    coordinates = input().split(',')
    x = int(coordinates[0])
    y = int(coordinates[1])
    j = table[x][y]
    if ',' in table[x][y]:
        j = table[x][y]
        a = j[:j.find(',')]
        b = j[j.find(',') + 2:]
        print(','.join([a, b]))
    elif '\number' in table[x][y]:
        i = table[x][y]
        a = i[:i.find('\number')]
        b = i[i.find('\number') + 2:]
        print('\number'.join([a, b]))
    else:
        print(table[x][y])
