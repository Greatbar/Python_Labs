line = input().lower()
lines = line.split()
list = [sum(x in 'уеыаоэяию' for x in lin) for lin in lines]
result = ("Пам парам", "Парам пам-пам")[len(set(list)) == 1]
print(result)
