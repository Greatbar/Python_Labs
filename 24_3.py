import sys

data = list(map(str.strip, sys.stdin))
data = [s.strip() for s in data]
comment = list(filter(lambda word: word[0] == '#', data))
for e in comment:
    print(f'Line {data.index(e) + 1}: {e[1:].strip()}')
