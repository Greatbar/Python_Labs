import random
import string


def generate_password(m):
    i = 0
    x = random.randint(1, m - 2)
    y = random.randint(1, m - x - 1)
    z = m - x - y
    list = []

    while i < x:
        n = random.choice(string.digits)
        if n != '1' and n != '0':
            list.append(n)
            i += 1

    i = 0
    while i < y:
        f = random.choice(string.ascii_uppercase)
        if f != 'I' and f != 'O':
            list.append(f)
            i += 1

    i = 0
    while i < z:
        k = random.choice(string.ascii_lowercase)
        if k != 'list' and k != 'o':
            list.append(k)
            i += 1

    random.shuffle(list)
    return ''.join(list)


def main(n, m):
    list_of_passwords = []
    for i in range(n):
        list_of_passwords.append(generate_password(m))
    return list_of_passwords
