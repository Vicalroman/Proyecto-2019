def caesarCipher(a):
    """Ka funcion caesarCipher recibe como argumento un dato tipo string, el cual
    cifrara usando el codigo de cesar que consiste en desplazar las letras una cantidad
    determinada de espacios en el abecedario, retorna el mensaje cifrado,"""
    a = list(a.lower())
    count = 0
    c = ""
    dictCipher = {}
    for i in list("abcdefghijklmnñopqrstuvwxyz"):
        dictCipher[i] = count
        count += 1
    dictDecipher = dict(enumerate(i for i in list("abcdefghijklmnñopqrstuvwxyz")))
    for i in a:
        if c == "":
            b = dictCipher['{}'.format(i)]
            c = c + dictDecipher[b + 1].upper()
        elif i is not ' ' and i is not 'z':
            b = dictCipher['{}'.format(i)]
            c = c + dictDecipher[b + 1]
        elif i == 'z':
            c = c + "a"
        else:
            c = c + " "
    return c
def caesarDecipher(a):
        """La funcion caesarDecipher recibe 1 argumento de tipo string, ek cual
        preferiblemente ya debe estar cifrado,la funcion decifra el mensaje y lo retorna como c"""
        a = list(a.lower())
        count = 0
        c = ""
        dictCipher = {}
        for i in list("abcdefghijklmnñopqrstuvwxyz"):
            dictCipher[i] = count
            count += 1
        dictDecipher = dict(enumerate(i for i in list("abcdefghijklmnñopqrstuvwxyz")))
        for i in a:
            if c == "":
                b = dictCipher['{}'.format(i)]
                c = c + dictDecipher[b - 1].upper()
            elif i is not ' ' and i is not 'a':
                b = dictCipher['{}'.format(i)]
                c = c + dictDecipher[b - 1]
            elif i == 'a':
                c = c + "z"
            else:
                c = c + " "
        return c
opcion = int(input("Elija una opcion:  \n1) Cifrar mensaje. \n2) Descifrar mensaje: \n "))
if opcion == 1:
    print("Cifra un mensaje.")
    x = input("Escribe el mensaje a cifrar: \n")
    print(caesarCipher(x))
elif opcion == 2:
    print("Descifra un mensaje.")
    y = input("Escribe el mensaje para descifrar: \n")
    print(caesarDecipher(y))
