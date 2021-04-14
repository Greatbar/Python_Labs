phone = {}
for i in range(int(input())):
    val, key = input().split()
    if key in phone:
        phone[key].append(val)
    else:
        phone[key] = [val]

for i in range(int(input())):
    key = input()
    if key in phone:
        print('\n')
        print(*phone[key])
    else:
        print('Нет в телефонной книге')
