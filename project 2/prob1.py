
def LargestSquare(mat):
    if not mat or not len(mat):
        return 0

    T = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
    max = 0
    alist = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            T[i][j] = mat[i][j]
            if i > 0 and j > 0 and mat[i][j] == 1:
                T[i][j] = min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1]) + 1
            if max < T[i][j]:
                max = T[i][j]

    result = [(i1 - max + 2, i2 - max + 2) for (i1, v1) in enumerate(T) for (i2, v2) in enumerate(v1) if v2 == max]

    return [result, "square size: ", max]



mat1 = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
    ]

mat2 = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1]
    ]

print("First test case:", LargestSquare(mat1))
print("Second test case:", LargestSquare(mat2))