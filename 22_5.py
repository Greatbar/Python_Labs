def solve(*coefficients):
    if len(coefficients) == 3:
        discriminant = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
        if coefficients[0] == 0 and coefficients[1] == 0 and coefficients[2] == 0:
            x = ["all"]
        elif coefficients[0] == 0 and coefficients[1] == 0:
            x = ''
        elif coefficients[0] == 0:
            x = [-coefficients[2] / coefficients[1]]
        elif coefficients[1] == 0:
            x = [(coefficients[2] / coefficients[0]) ** 0.5]
        elif coefficients[2] == 0:
            x = [0, -coefficients[1] / coefficients[0]]
        else:
            if discriminant == 0:
                x = [-coefficients[1] / (2 * coefficients[0])]
            elif discriminant < 0:
                x = ''
            else:
                x = [float((-coefficients[1] - discriminant ** 0.5) / (2 * coefficients[0])),
                     float((-coefficients[1] + discriminant ** 0.5) / (2 * coefficients[0]))]
        print(x)
    elif len(coefficients) == 2:
        return [print(-coefficients[1] / coefficients[0])]
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return [print("all")]
        else:
            return []
    else:
        return [print("all")]


lst = [int(i) for i in input().split()]
if len(lst) == 1:
    solve(lst[0])
if len(lst) == 2:
    solve(lst[0], lst[1])
if len(lst) == 3:
    solve(lst[0], lst[1], lst[2])
