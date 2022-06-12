# =============================================
# M4Z05
import Helper as helper
import time


def silnia_i(n):
    wynik = 1
    if n in(0, 1):
        return 1
    else:
        for i in range(2, n+1):
            wynik = wynik * i
        return wynik


def silnia_r(n):
    if n > 1:
        return n * silnia_r(n-1)
    else:
        return 1


def main(args):
    while True:
        print("################################################################################\n")
        dane = helper.userVariableINTstring("Podaj liczbę: ")
        wynik = silnia_i(dane)
        print("Silnia z {} to {}".format(dane, wynik))
        wynik2 = silnia_r(dane)
        print("Silnia z {} to {}".format(dane, wynik2))
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))



# =============================================