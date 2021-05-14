def golden_ratio(x):
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    k = abs(len(fibonacci) - x)
    for i in range(x):
        if x > len(fibonacci):
            for gg in range(k + 1):
                fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci[x] / fibonacci[x - 1])
