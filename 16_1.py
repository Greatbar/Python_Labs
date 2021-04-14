x = [0 for i in range(30001)]
position = 0
symbol = input()
print(symbol)
i = 0
while i < len(symbol):
    if symbol[i] == ">":
        position = position + 1
    elif symbol[i] == "<":
        position = position - 1
    elif symbol[i] == ".":
        print(x[position])
    elif symbol[i] == "+":
        x[position] = x[position] + 1
        if x[position] > 255:
            x[position] = 0
    elif symbol[i] == "-":
        x[position] = x[position] - 1
        if x[position] < 0:
            x[position] = 255
    elif symbol[i] == '[':
        if x[position] == 0:
            j = i + 1
            c = 1
            while (True):
                if symbol[j] == '[':
                    c += 1
                if symbol[j] == ']':
                    c -= 1
                if c == 0:
                    i = j
                    break
                j += 1
    elif symbol[i] == ']':
        c = -1
        j = i - 1
        while True:
            if symbol[j] == ']':
                c -= 1
            if symbol[j] == '[':
                c += 1
            if c == 0:
                i = j - 1
                break
            j -= 1

    i += 1
