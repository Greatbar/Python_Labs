def ask_password():
    password = 'password'

    for i in range(3):
        p = input()
        if p == password:
            print("Пароль принят")
            return
    print('В доступе отказано')

