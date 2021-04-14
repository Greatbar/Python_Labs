array = [0]
number = int(input())
for i in range(number):
    count = 0
    for j in range(len(array)):
        if array[j] == array[-j - 1]:
            count += 1
    array.append(count)
for i in array[:-1]:
    print(i)
