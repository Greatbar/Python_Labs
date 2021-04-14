work = int(input())
men_work = [input() for i in range(work)]
result = 0
for a in set(men_work):
    count = 0
    for name in men_work:
        if a == name:
            count += 1
    if count > 1:
        result += count
print(result)
