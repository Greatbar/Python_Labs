paper = int(input('Введите количество листков'))
spisok = [set(input() for _ in range(int(input()))) for _ in range(paper)]
result = spisok[0]
for i in spisok:
    result = result.intersection(i)
print(*sorted(result), sep='\n')
