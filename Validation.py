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
                    interv = [i for i in range(args[1][0] + 1, args[1][1])]
                    isInt = any([args[0] is i for i in interv])
                elif type(args[1]) is list and len(args[1]) is 2:
                    interv = [i for i in range(args[1][0], args[1][1] + 1)]
                    isInt = any([args[0] is i for i in interv])
            else:
                raise ValueError("El segundo argumento no esta ordenado de manera creciente.")
        except TypeError:
            raise TypeError("El segundo argumento recibe tipo list o tuple y usted ingreso tipo {}.".format(type(args[1])))
    return isInt
