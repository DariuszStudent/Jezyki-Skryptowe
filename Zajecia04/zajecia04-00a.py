# =============================================
# M4Z00a
import Helper as helper

def dziel_nat(liczba):
    if liczba == 0:
        return -1
    if liczba < 0:
        return -2
    return 1/liczba

def main(args):
    x = helper.userVariableFloatString('Podaj liczbę')
    wynik = dziel_nat(x)
    if wynik == -1:
        print("Liczba równa zero")
    elif wynik == -2:
        print("Liczba ujemna")
    else:
        print("Wynik: ", wynik)
    print("***********")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# =============================================