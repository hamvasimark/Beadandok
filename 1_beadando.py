print("első feladat")


def hatvanyosszeg(szam):
    lista = []
    a = 0
    szam2 = szam
    while a != szam:
        i = 0
        while 2 ** i <= szam2:
            i += 1
        szam2 -= 2 ** (i - 1)
        lista.append(i - 1)
        a += 2 ** (i - 1)
    return sorted(lista)


szam = 69
print(hatvanyosszeg(szam))
