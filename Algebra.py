def matrixProduct(a,b):
    """DocString"""
    try:
        if len(a[0]) == len(b):
            m_1 = len(a) #Filas de a
            m_2 = len(b) #Filas de b
            n_1 = len(a[0]) #Columnas de a
            n_2 = len(b[0]) #Columnas de b
            lista = []
            for i in range(n_2):
                lista_aux = []
                for j in range(m_1):
                    x = 0
                    for k in range(n_1):
                        x = x + a[i][k] * b[k][j]
                    lista_aux.append(x)
                lista.append(lista_aux)
    except TypeError:
        None
    return lista
def matrixProduct(a,b):
    """DocString"""
    try:
        if len(a[0]) == len(b):
            m_1 = len(a) #Filas de a
            m_2 = len(b) #Filas de b
            n_1 = len(a[0]) #Columnas de a
            n_2 = len(b[0]) #Columnas de b
            lista = [[sum([a[i][k] * b[k][j] for k in range(n_1)]) for j in range(m_1)]for i in range(n_2)]
    except TypeError:
        None
    return lista
def gaussJordan(*args):
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
                t = 1/mat[i][i]
                det *= mat[i][i]
                for j in range(col):
                        ident[i][j] *= t
        return ident
def vectorProduct(a,b):
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
    matr = [i for i in a]
    rows = len(matr)
    column = len(matr[0])
    trans = [[matr[j][i] for j in range(rows)] for i in range(column)]
    return trans
print(transposition_2([[1,2,3],[4,5,6]]))
matrix = gaussJordan([[2,1],[5,3]], 2)
for i in range(2):
    for j in range(2):
        matrix[j][i] = round(matrix[j][i] , 3)
print(matrix)
