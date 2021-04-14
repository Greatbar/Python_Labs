queue = []
for i in range(int(input())):
    string = input()
    if 'хватит тут стоять' in string:
        string = string.split(', ')
        queue.pop(queue.index(string[0]))
    elif 'будет за тобой' in string:
        string = string.split('! ')
        string_p, string_n = string[1].split(' будет'), string[0].split(', ')
        name_p, name = string_p[0], string_n[1]
        queue.insert(queue.index(name) + 1, name_p)
    else:
        queue.append(string.split(' в')[0])
print('\n'.join(queue))
