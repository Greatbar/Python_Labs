number = int(input())
command_result = []
for i in range(number):
    command_result.append((input(), int(input())))

temp = len(command_result)
for i in range(temp - 1):
    for j in range(temp - i - 1):
        if command_result[j][1] > command_result[j + 1][1]:
            command_result[j], command_result[j + 1] = command_result[j + 1], command_result[j]

temp_2 = temp // 2
final = command_result[temp_2:]
first = command_result[: temp_2]
temp = len(final)
for i in range(temp - 1):
    for j in range(temp - i - 1):
        if final[j] > final[j + 1]:
            final[j], final[j + 1] = final[j + 1], final[j]

for i in final:
    print(i[0])

temp = len(first)
for i in range(temp - 1):
    for j in range(temp - i - 1):
        if first[j] > first[j + 1]:
            first[j], first[j + 1] = first[j + 1], first[j]

for i in first:
    print(i[0])
