base = []


def hello(name):
    print("Здравствуйте, ", name, "! Вашу карту ищут...", sep="")


def search_card(name):
    if name in base:
        print("Ваша карта с номером ", base.index(name) + 1, " найдена", sep="")
    else:
        print("Ваша карта не найдена")
