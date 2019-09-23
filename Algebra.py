def matrixProduct(a,b):
    """La funcion matrixProduct recibe 2 argumentos de tipo lista los cuale
    simulen matrices, y calcula el producto entre esas dos matrices en el caso
    que cumplan la condicion, y retorna una lista simulando la matriz resultante
    del producto."""
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
    """La funcion matrixProduct recibe 2 argumentos de tipo lista los cuale
    simulen matrices, y calcula el producto entre esas dos matrices en el caso
    que cumplan la condicion, y retorna una lista simulando la matriz resultante
    del producto."""
    if len(a[0]) == len(b):
        row_1 = len(a) #Filas de a
        row_2 = len(b) #Filas de b
        column_1 = len(a[0]) #Columnas de a
        column_2 = len(b[0]) #Columnas de b
        product = [[sum([a[i][k] * b[k][j] for k in range(row_1)]) for j in range(column_2)]for i in range(row_1)]
    return product
def gaussJordan(a):
    """La funcion gaussJordan recibe 1 argumento del tipo lista, que recrea una matriz,
    la funcion determina y retorna la inversa de la matriz indicada."""
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
    """La funcion vectorProduct recibe 2 argumentos tipo lista que simulan vectores
    y determina y retorna el resultado del producto vectorial de los dos vectores"""
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
    """Recibe un argumento tipo lista que simule una matriz, y retorna su matriz transpuesta"""
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
    """Recibe un argumento tipo lista que simule una matriz, y retorna su matriz transpuesta"""
    matr = [i for i in a]
    rows = len(matr)
    column = len(matr[0])
    trans = [[matr[j][i] for j in range(rows)] for i in range(column)]
    return trans
def linealEquationsSol(a,b):
    """Recibe 2 argumentos de tipo lista que simulan una matriz y un vector, la matriz
    corresponde a la matriz de un sistema de ecuaciones y el vector al vector de resultados,
    la funcion linealEquationsSol determina la solucion del sistema de ecuaciones y lo retorna
    en forma de lista."""
    matr = [i for i in a]
    matr_2 =[i for i in b]
    inv_matr = gaussJordan(matr )
    result = matrixProduct_2(inv_matr, matr_2)
    return result
def determinant(*args):
    """Recibe como argumento una matriz y retorna su determinante."""
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
