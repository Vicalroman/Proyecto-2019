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
def GaussJordan(a, b):
    """DocString"""
    a = [i for i in a]
    b = [i for i in b]
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b
