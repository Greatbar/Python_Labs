number = int(input())

mark = False
slash = False

char = 0
result = []

for i in range(number):
    string = input()
    while string[char] == " ":
        result.append(" ")
        char += 1
    for i_1 in range(char, len(string)):
        if not slash:
            if string[i_1] == "'":
                result.append(string[i_1])
                mark = not mark
            elif string[i_1] == "\\":
                result.append(string[i_1])
                slash = True
            elif string[i_1] == "#":
                if mark:
                    result.append(string[i_1])
                else:
                    break
            elif string[i_1] == " ":
                if mark:
                    result.append(string[i_1])
                else:
                    if i_1 + 1 != len(string):
                        if string[i_1 + 1] == " ":
                            result.append("")
                        else:
                            result.append(string[i_1])
            else:
                result.append(string[i_1])
        else:
            slash = False
            result.append(string[i_1])
    print("".join(result))
    result = []
    mark = False
    slash = False
    char = 0
