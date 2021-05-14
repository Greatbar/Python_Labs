list = []
while True:
    try:
        words = str(input())
        if words == '':
            break
        list.append(words)
    except Exception as ex:
        break
print(*sorted(list, key=lambda word: sum([ord(i) + 1 - (ord('A')) for i in word.upper()])), sep='\n')
