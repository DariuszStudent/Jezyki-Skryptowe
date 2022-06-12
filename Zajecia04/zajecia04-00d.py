# =============================================
# M4Z00d
import Helper as helper


def szukaj(dane, elem):
    dlugosc = len(dane)
    wynik = []
    for i in range(dlugosc):
        if dane[i] == elem:
            wynik.append(i)
    if len(wynik) == 0:
        return -1
    else:
        return wynik

def szukaj_auto(dane, elem):
    dlugosc = len(dane)
    wynik = []
    typ = str(type(dane))
    if typ == "class 'set'>":
        if elem in dane:
            return True
        else:
            return False

    for i in range(dlugosc):
        if dane[i] == elem:
            wynik.append(i)
    if len(wynik) == 0:
        return -1
    else:
        return wynik

def szukaj_zb(zb, el):
    if el in zb:
        return True
    else:
        return False


def main(args):
    lista = [2, 3, 5, 6, 7, 2, 4, 5, 6]
    zb = {1, 2, 3, 4, 2, 4}
    print(szukaj(lista, 2))
    print(szukaj_zb(lista, 2))



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# =============================================