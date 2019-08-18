def mulMatrix(a,b):
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
def mulMatrix_2(a,b):
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
def GaussJordan(a,b):
    """DocString"""
    mat = [i for i in a] #
    ident = [[1 if i == j else 0 for i in range(b)] for j in range(b)]
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
        det *= a[i][i]
        for j in range(col):
            ident[i][j] *= t
    return ident
print(GaussJordan([[2,1],[5,3]],2))
