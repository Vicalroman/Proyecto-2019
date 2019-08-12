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
