def caesarCipher(a):
    """DocString"""
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
        """DocString"""
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
print("Cifra un mensaje.")
x = input("Escribe el mensaje a cifrar: \n")
print(caesarCipher(x))

print("Descifra un mensaje.")
y = input("Escribe el mensaje para descifrar: \n")
print(caesarDecipher(y))
