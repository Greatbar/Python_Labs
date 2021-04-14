text = input()
example_1 = [' *   ', '* *  ', '***  ', '* *  ', '* *  ']
example_2 = ['**   ', '* *  ', '**   ', '* *  ', '**   ']
example_3 = [' *   ', '* *  ', '*    ', '* *  ', ' *   ']
for j in range(5):
    for i in range(len(text)):
        if text[i] == 'example_1':
            print(example_1[j], end='')
        elif text[i] == 'example_2':
            print(example_2[j], end='')
        else:
            print(example_3[j], end='')
    print()
