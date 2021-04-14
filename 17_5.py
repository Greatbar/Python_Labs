access = [input() for i in range(int(input()))]
paths = [input() for k in range(int(input()))]
list_access = [x.split('/')[1:] for x in access]
list_path = [x.split('/')[1:] for x in paths]


def check_permissions(access, file):
    for x in access:
        if len(file) < len(x):
            continue
        else:
            if x == file[:len(x)]:
                return 'YES'
    return 'NO'


for i in list_path:
    print(check_permissions(list_access, i))
