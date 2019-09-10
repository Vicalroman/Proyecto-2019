def valInt(*args):
    """Ayuda en funcion valInt en el modulo Validation:

    funcion valInt(objeto)
    |   valInt(entero) -> Booleano True si el tipo del objeto es entero False de lo contrario.
    |   valInt(entero, lista) -> Booleano True si el tipo del primer argumento es entero y esta dentro del intervalo
    |   descrito por el segundo argumento(Sin incluir los numeros de los extremos).
    |   valInt(entero, tupla) -> Booleano True si el tipo del primer argumento es entero y esta dentro del intervalo
    |   descrito por el segundo argumento(Incluyendo los extremos).
    |
    |   Retorna un booleano, en el caso de 1 argumento si este es un numero entero retorna True en caso contrario False.
    |   En el caso de 2 argumentos se divide en dos posibilidades, retorna True si el primer argumento es un entero
    |   y si el numero se encuentra dentro del intervalo abierto(Segundo argumento tipo lista), tambien retorna True
    |   si el primer argumento es entero y se encuentra dentro del intervalo cerrado (Segundo argumento tipo tupla).
    |   Retorna False en caso de que no sea entero, o no se encuentre dentro del argumento establecido."""
    isInt = False
    if len(args) == 1:
        if type(args[0]) is int:
            isInt = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1]) is tuple and len(args[1]) is 2:
                    isInt = args[0] > args[1][0] and args[0] < args[1][1]
                elif type(args[1]) is list and len(args[1]) is 2:
                    isInt = args[0] >= args[1][0] and args[0] <= args[1][1]
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente.")
        except TypeError:
            raise TypeError("El segundo argumento recibe tipo list o tuple y usted ingreso tipo {}.".format(type(args[1])))
    return isInt
def valFloat(*args):
    """Ayuda en funcion valFloat en el modulo Validation:

    funcion valFloat(objeto)
    |   valFloat(float) -> Booleano True si el tipo del objeto es float False de lo contrario.
    |   valFloat(float, lista) -> Booleano True si el tipo del primer argumento es float y esta dentro del intervalo
    |   descrito por el segundo argumento(Sin incluir los numeros de los extremos).
    |   valFloat(float, tupla) -> Booleano True si el tipo del primer argumento es float y esta dentro del intervalo
    |   descrito por el segundo argumento(Incluyendo los extremos).
    |
    |   Retorna un booleano, en el caso de 1 argumento si este es un numero float retorna True en caso contrario False.
    |   En el caso de 2 argumentos se divide en dos posibilidades, retorna True si el primer argumento es un float
    |   y si el numero se encuentra dentro del intervalo abierto(Segundo argumento tipo lista), tambien retorna True
    |   si el primer argumento es float y se encuentra dentro del intervalo cerrado (Segundo argumento tipo tupla).
    |   Retorna False en caso de que no sea float, o no se encuentre dentro del argumento establecido."""
    isFloat = False
    if len(args) == 1:
        if type(args[0]) is float:
            isFloat = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1]) is tuple and  len(args[1]) is 2:
                    isFloat = args[0] > args[1][0] and args[0] < args [1][1]
                elif type(args[1]) is list and len(args[1]) is 2:
                    isFloat = args[0] >= args[1][0] and args[0] <= args[1][1]
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente.")
        except TypeError:
            raise TypeError("El segundo argumento recibe tipo list o tuple y usted ingreso tipo {}.".format(type(args[1])))
    return isFloat
def valComplex(*args):
    """Ayuda en funcion valComplex en el modulo Validation:

    funcion valComplex(objeto)
    |   valComplex(numero complejo) -> Booleano True si el tipo del objeto es numero complejo False de lo contrario.
    |   valComplex(numero complejo, lista) -> Booleano True si el tipo del primer argumento es numero complejo y su norma esta dentro del intervalo
    |   descrito por el segundo argumento(Sin incluir los numeros de los extremos).
    |   valComplex(numero complejo, tupla) -> Booleano True si el tipo del primer argumento es numero complejo y su norma esta dentro del intervalo
    |   descrito por el segundo argumento(Incluyendo los extremos).
    |
    |   Retorna un booleano, en el caso de 1 argumento si este es un numero numero complejo retorna True en caso contrario False.
    |   En el caso de 2 argumentos se divide en dos posibilidades, retorna True si el primer argumento es un numero complejo
    |   y si el numero se encuentra dentro del intervalo abierto(Segundo argumento tipo lista), tambien retorna True
    |   si el primer argumento es numero complejo y se encuentra dentro del intervalo cerrado (Segundo argumento tipo tupla).
    |   Retorna False en caso de que no sea numero complejo, o no se encuentre dentro del argumento establecido."""
    isComplex = False
    comp = args[0]
    if len(args) == 1:
        if type(args[0]) is complex:
            isComplex = True
    if len(args) == 2:
        try:
            if args[1][0] < args[1][1]:
                if type(args[1]) is tuple and  len(args[1]) is 2:
                    isComplex = ((comp.real)**2 + (comp.imag)**2)**0.5 > args[1][0] and ((comp.real)**2 + (comp.imag)**2)**0.5 < args [1][1]
                elif type(args[1]) is list and len(args[1]) is 2:
                    isComplex = (((comp.real)**2 + (comp.imag)**2)**0.5) >= args[1][0] and (((comp.real)**2 + (comp.imag)**2)**0.5) <= args[1][1]
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente.")
        except TypeError:
            raise TypeError("El segundo argumento recibe tipo list o tuple y usted ingreso tipo {}.".format(type(args[1])))
    return isComplex
def valList(*args):
    """Ayuda en funcion valComplex en el modulo Validation:

    |   funcion valList(objeto)
    |   valList(Lista) -> Booleano True si el argumento corresponde con un tipo lista, caso contrario False.
    |   valList(Lista, Lista, "value") -> Booleano True si el primer y el segundo argumento son tipo lista y
    |   son totalmente equivalentes, en caso contrario retorna False.
    |   valList(Lista, entero, "len") -> Booleano True si el primer argumento es tipo lista y el segundo es tipo
    |   entero y ademas si la longitud de la lista coincide con el valor del numero entero, si no es el caso retorna False.
    |   
    |   Retorna un booleano, en caso de 1 argumento, si este es tipo lista, retorna True en caso contrario retorna False,
    |   en caso de 3 argumentos si el tercer argumento es 'value', el primer y segundo argumento son tipo lista, y son
    |   iguales retorna True, en caso que no cumpla False, si el tercer argumento es 'len' el primero es tipo lista, el
    |   segundo es un entero y la longitud de la lista coincide con el entero, retorna True, en caso de no cumplirse retorna,
    |   False."""
    isList = False
    if len(args) == 1:
        if type(args[0]) is list:
            isList = True
    if len(args) == 3:
        try:
            if args[0] is not list:
                isList = False
            elif args[2] == "len":
                if len(args[0]) is args[1]:
                    isList = True
            elif args[2] == "value":
                if args[0] == args[1]:
                    isList = True
            elif (type(args[1]) is not list or type(args[1]) is not int) and type(args[2]) is not str:
                raise TypeError
            else:
                raise ValueError("El tercer argumento admite 2 entradas (len, value) y usted indico {}.".format(args[2]))
        except TypeError:
            raise TypeError("Introdujo un argumento invalido para la funcion.")
    return isList
