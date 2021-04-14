number = input()
i, total = int(number[:4]), int(number[4:])
errors, true_total = [], 0
for i in range(i):
    number = input()
    price, amount, cost = int(number[:7]), int(number[8:12]), int(number[13:])
    if price * amount != cost:
        errors.append(i + 1)
    true_total += price * amount
print(total - true_total)
for x in errors:
    print(x, end=' ')
