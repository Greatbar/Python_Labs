import random

st1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
st2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
st3 = ['2', '3', '4', '5', '6', '7', '8', '9']
st4 = st1 + st2 + st3


def generate_password(m):
    password = [random.choice(st1), random.choice(st2), random.choice(st3)]
    for i in range(0, m - 3):
        password.append(random.choice(st4))
    random.shuffle(password)
    return ''.join(password)


def main(n, m):
    password_list = set()
    while len(password_list) < n:
        password_list.add(generate_password(m))
    return password_list
