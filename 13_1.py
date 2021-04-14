number = int(input())
list_1 = [''] * number
for i in range(number):
    list_1[i] = input()
k = int(input())
for i in range(k):
    x = int(input())
    temp = [''] * x
    for j in range(x):
        temp[j] = list_1[int(input()) - 1]
    list_1 = temp
for i in range(len(list_1)):
    print(list_1[i])
