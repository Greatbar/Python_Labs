temp_1 = {}
classmates = int(input())
for i in range(classmates):
    name = input().split()
    if name[2] in temp_1:
        temp_1[name[2]].append([name[0], name[1]])
    else:
        temp_1[name[2]] = [[name[0], name[1]]]

month_number = int(input())
arr = [input() for _ in range(month_number)]

for month in arr:
    if month in temp_1:
        arr = sorted(temp_1[month], key=lambda x: (int(x[1]), x[0]))
        result = ''
        for x in arr:
            result += ' '.join(x) + ' '
        print(result.rstrip())
    if month not in temp_1:
        print()
