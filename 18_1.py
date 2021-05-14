def print_shrug_smile():
    print("¯\_(ツ)_/¯")


def print_ktulhu_smile():
    print("{:€")


def print_happy_smile():
    print("(͡° ͜ʖ ͡°)")


for i in range(3):
    func = input()
    if func == '1':
        print_shrug_smile()
    elif func == '2':
        print_ktulhu_smile()
    elif func == '3':
        print_happy_smile()
