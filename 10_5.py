while True:
    word = input("Введите слово: ")
    example = (word[0])
    if example == "а" or example == "А":
        print("Подходит")
    elif example != "а" or example != "А":
        break
