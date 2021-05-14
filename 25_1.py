from random import sample
import string

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    return ''.join(sample(symbols, m))


def main(n, m):
    i = set()
    while len(i) < n:
        i.add(generate_password(m))
    return i


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов")
print(*main(10, 15), sep="\n")
