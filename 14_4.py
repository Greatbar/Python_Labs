numbers = list(map(int, input().split()))

x_max = len(numbers)
y_max = max(numbers)

print('*' * (x_max + 2))
print('*' + ' ' * x_max + '*')
for i in range(1, y_max + 1):
    print(end='*')
    for j in numbers:
        if j >= y_max - i + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')
