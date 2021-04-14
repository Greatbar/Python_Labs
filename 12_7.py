length = int(input())
width = int(input())
list_1 = []
list_2 = []
for i in range(length):
    list_1.append(input())
for i in list_1[::2]:
    list_2.append(i[::2])
length = length // 2
width = width // 2
for i in list_2:
    print(i)
