station_count = int(input())
s = [[]]
for i in range(station_count - 1):
    s.append([int(j) for j in input().split()])
station = input().split()
temp_1 = int(station[0])
temp_2 = int(station[1])
temp_3 = s[max(temp_1, temp_2)][min(temp_1, temp_2)]
result = -1
for i in range(station_count):
    if i != temp_1 and i != temp_2:
        if temp_3 > s[max(temp_1, i)][min(temp_1, i)] + s[max(i, temp_2)][min(i, temp_2)]:
            temp_3 = s[max(i, temp_2)][min(i, temp_2)] + s[max(i, temp_2)][min(i, temp_2)]
            result = i
if result != -1:
    print(result)
else:
    print(temp_1)
