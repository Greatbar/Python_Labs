punkt_count = int(input())
punkt = []
for i in range(punkt_count):
    f = input()
    if 'лук' in f:
        continue
    punkt.append(f)
print(', '.join(punkt))
