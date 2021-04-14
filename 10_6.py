ulitka = input()
word = ulitka[0]
way = ulitka[1:].split('V')
num_spaces = 0
for move in way:
    if move and move[0] == '<':
        num_spaces -= len(move)
    print(' ' * num_spaces + word * (1 + len(move)))
    if move and move[0] == '>':
        num_spaces += len(move)
