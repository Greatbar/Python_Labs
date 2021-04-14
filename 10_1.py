s = str(input())
n = int(input())
print(s[n - 1] if 0 < n <= len(s) else 'ОШИБКА')
