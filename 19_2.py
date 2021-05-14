def t2c(f):
    a = f[:1]
    b = f[1:]
    r = int(b)
    c = 'ABCDEFGH'.find(a) + 1
    return c, r


def c2t(k):
    (c, r) = k
    return 'ABCDEFGH'[c - 1] + str(r)


def possible_turns(f):
    (c, r) = t2c(f)
    temp = [(c + 2, r + 1), (c + 2, r - 1), (c - 2, r + 1), (c - 2, r - 1), (c + 1, r + 2), (c - 1, r + 2),
            (c + 1, r - 2), (c - 1, r - 2)]
    result = []
    for (a, b) in temp:
        if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
            result += [c2t((a, b))]
    return sorted(result)
