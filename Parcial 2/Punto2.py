def mat_x(mat):
    mat_resultado = []
    s = len(mat)
    pocisionD = 0
    pocisionI = s

    for i in range(s):
        mat_resultado.append([])
        pocisionI -= 1

        for j in range(s):
            if j == pocisionD or j == pocisionI:
                valor = 1
            else:
                valor = 0

            mat_resultado[i].append(valor)
        pocisionD += 1

    return mat_resultado

mat = [[20, 57, 86, 70, 53],
       [16, 81, 28, 63, 57],
       [51, 58, 54, 56, 12],
       [46, 73, 58, 36, 35],
       [15, 50, 31, 74, 88]]

print(mat_x(mat))