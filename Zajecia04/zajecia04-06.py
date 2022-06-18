# =============================================
# M4Z06
import Helper as helper


def odejmowanieEukalides(liczba1, liczba2):
    licznik = 0
    while liczba1 != liczba2:
        licznik += 1
        if liczba1 > liczba2:
            liczba1 = liczba1 - liczba2
        else:
            liczba2 = liczba2 - liczba1
    return liczba1, licznik


def dzielenieEukalides(liczba1, liczba2):
    licznik = 0
    if liczba2 == 0:
        print("najwiekszy wspolny dzielnik to:", liczba1)
    else:
        while liczba2 > 0:
            licznik += 1
            reszta = liczba1 % liczba2
            liczba1 = liczba2
            liczba2 = reszta
    return liczba1, licznik


def main(args):
    while True:
        print("################################################################################\n")
        print("METODA ODEJMOWANIA")
        user1 = helper.userVariableINTstring("Podaj pierwszą liczbę: ")
        user2 = helper.userVariableINTstring("Podaj drugą liczbę: ")
        liczba1, licznik = odejmowanieEukalides(user1, user2)
        print("pętla wykonana {} razy".format(licznik))
        print("najwiekszy wspolny dzielnik to:", liczba1)

        print("METODA DZIELENIA")
        user1 = helper.userVariableINTstring("Podaj pierwszą liczbę: ")
        user2 = helper.userVariableINTstring("Podaj drugą liczbę: ")

        liczba1, licznik = odejmowanieEukalides(user1, user2)
        print("pętla wykonana {} razy".format(licznik))
        print("najwiekszy wspolny dzielnik to:", liczba1)

        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================
