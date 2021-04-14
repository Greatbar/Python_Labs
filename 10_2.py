step = int(input())
word = str(input())

for i in word:
    if chr(ord(i)) == ' ' or chr(ord(i)) == '!':
        print(i, end='')
    else:
        base = ord('А') if i.isupper() else ord('а')
        print(chr((ord(i) + step - base) % 33 + base), end='')
