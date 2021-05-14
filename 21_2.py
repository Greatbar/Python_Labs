def transpose(matrix):
    result = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(m):
        tmp = []
        for k in range(n):
            tmp = tmp + [matrix[k][i]]
        result = result + [tmp]
    matrix[:] = result
