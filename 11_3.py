message = input().lower()
number = int(input()) - 1
latter = input().lower()
if (0 < number <= len(message)) and (latter in message) and (len(latter) == 1):
    print('ДА') if message[number] == latter else print('НЕТ')
else:
    print('ОШИБКА')
