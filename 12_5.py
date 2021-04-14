n = int(input())
result = 1
example_1 = []
example_2 = []
while result not in example_1:
    example_1.append(result)
    example_2.append(10 * result // n)
    result = 10 * result % n
print(*example_2[example_1.index(result):])
