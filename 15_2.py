string = input()
temp = 0
for i in string:
    if i != ' ' and i != '\t':
        temp += 1
print(temp)
