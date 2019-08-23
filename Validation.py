def valInt(*args):
    """DocString"""
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
    """DocString"""
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
    """DocString"""
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
    """DocString"""
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
