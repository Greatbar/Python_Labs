mediana = []
moda = []
all = []
for j in range(int(input())):
    number = list(map(int, input().split()))
    number.sort()
    temp_1 = number[len(number) // 2]
    temp_2 = 0
    temp_3 = 0
    for i in number:
        if number.count(i) > temp_2:
            temp_2 = number.count(i)
            temp_3 = i
    mediana.append(temp_1)
    moda.append(temp_3)
    for i in number:
        all.append(i)
all.sort()
print(*mediana)
print(*moda)
mediana.sort()
moda.sort()
print(mediana[len(mediana) // 2])
print(moda[len(moda) // 2])
print(all[len(all) // 2])
temp_2 = 0
temp_3 = 1234
for i in all:
    if all.count(i) > temp_2:
        temp_2 = all.count(i)
        temp_3 = i
print(temp_3)
