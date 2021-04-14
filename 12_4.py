string = input()
result = 0
i = 0
for i in range(len(string) - 1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            result += 1
        else:
            a = string[i]
            print(result, string[i])
            result = 1
print(result, string[i])
