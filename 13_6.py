f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
     'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
     'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
     'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
     'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
     'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
     'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
     'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
     'string': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
     'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
     'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
     'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
string = input()
for i in range(5):
    for k in string:
        print(f.get(k)[i], end='')
    print()
