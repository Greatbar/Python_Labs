soldier_count = int(input())
names = [input() for i in range(soldier_count)]
executed = int(input())
result = []
while 1:
    if len(names) > 0:
        result.append(names[0])
        names.pop(0)
        soldier_count -= 1
    else:
        break
    t = 1
    for i in range(soldier_count // executed):
        result.append(names[((i + 1) * executed) - t])
        names.pop(((i + 1) * executed) - t)
        soldier_count -= 1
        t += 1
for i in range(len(result)):
    print(result[i])
