def matrixProduct(a,b):
    """DocString"""
    if len(a[0]) == len(b):
        row_1 = len(a) #Filas de a
        row_2 = len(b) #Filas de b
        column_1 = len(a[0]) #Columnas de a
        column_2 = len(b[0]) #Columnas de b
        product = []
        for i in range(row_1):
            aux_list = []
            for j in range(column_2):
                x = 0
                for k in range(row_1):
                    x = x + a[i][k] * b[k][j]
                aux_list.append(x)
            product.append(aux_list)
    return product
def matrixProduct_2(a,b):
    """DocString"""
    if len(a[0]) == len(b):
        row_1 = len(a) #Filas de a
        row_2 = len(b) #Filas de b
        column_1 = len(a[0]) #Columnas de a
        column_2 = len(b[0]) #Columnas de b
        product = [[sum([a[i][k] * b[k][j] for k in range(row_1)]) for j in range(column_2)]for i in range(row_1)]
    return product
def gaussJordan(a):
    """DocString"""
    if len(a) == len(a[0]):
        mat = [i for i in a] #
        ident = [[1 if i == j else 0 for i in range(len(a))] for j in range(len(a))]
        fil = len(mat)
        col = len(ident[0])
        det = 1
        for i in range(col - 1):
                k = i
                for j in range(i + 1, fil):
                        if abs(mat[j][i]) > abs(mat[k][i]):
                                k = j
                if k != i:
                        mat[i], mat[k] = mat[k] , mat[i]
                        ident[i], ident[k] = ident[k], ident[i]
                        det = -det
                for j in range(i + 1, fil):
                        t = mat[j][i]/mat[i][i]
                        for k in range(i + 1, fil):
                                mat[j][k] -= t*mat[i][k]
                        for k in range(col):
                                ident[j][k] -= t*ident[i][k]
        for i in range(fil - 1, -1, -1):
                for j in range(i + 1, fil):
                        t = mat[i][j]
                        for k in range(col):
                                ident[i][k] -= t*ident[j][k]
                t = 1/mat[i][i]
                det *= mat[i][i]
                for j in range(col):
                        ident[i][j] *= t
        for i in range(fil):
            for j in range(fil):
                ident[j][i] = round(ident[j][i] , 2)
        return ident
def vectorProduct(a,b):
    """DocString"""
    vector_1 = [i for i in a]
    vector_2 = [i for i in b]
    vector_r = []
    for i in range(3):
        for j in range(3):
            if j > i and i + j != 2:
                vector_r.append((vector_1[i] * vector_2[j] - vector_2[i] * vector_1[j]))
            elif j > i and i + j == 2:
                vector_r.append((vector_1[i] * vector_2[j] - vector_2[i] * vector_1[j]) * (-1))
    vector_r = list(reversed(vector_r))
    return vector_r
def transposition(a):
    """DocString"""
    matr = [i for i in a]
    rows = len(matr)
    column = len(matr[0])
    trans = []
    for i in range(column):
        aux = []
        for j in range(rows):
            aux.append(matr[j][i])
        trans.append(aux)
    return trans
def transposition_2(a):
    """DocString"""
    matr = [i for i in a]
    rows = len(matr)
    column = len(matr[0])
    trans = [[matr[j][i] for j in range(rows)] for i in range(column)]
    return trans
def linealEquationsSol(a,b):
    """DocString"""
    matr = [i for i in a]
    matr_2 =[i for i in b]
    inv_matr = gaussJordan(matr )
    result = matrixProduct_2(inv_matr, matr_2)
    return result
def determinant(*args):
    """DocString"""
    if len(args) == 2 and type(args[1]) is int:
        mat = [i for i in args[0]] #
        ident = [[1 if i == j else 0 for i in range(args[1])] for j in range(args[1])]
        fil = len(mat)
        col = len(ident[0])
        det = 1
        for i in range(col - 1):
                k = i
                for j in range(i + 1, fil):
                        if abs(mat[j][i]) > abs(mat[k][i]):
                                k = j
                if k != i:
                        mat[i], mat[k] = mat[k] , mat[i]
                        ident[i], ident[k] = ident[k], ident[i]
                        det = -det
                for j in range(i + 1, fil):
                        t = mat[j][i]/mat[i][i]
                        for k in range(i + 1, fil):
                                mat[j][k] -= t*mat[i][k]
                        for k in range(col):
                                ident[j][k] -= t*ident[i][k]
        for i in range(fil - 1, -1, -1):
                for j in range(i + 1, fil):
                        t = mat[i][j]
                        for k in range(col):
                                ident[i][k] -= t*ident[j][k]
                det *= mat[i][i]
    return det
