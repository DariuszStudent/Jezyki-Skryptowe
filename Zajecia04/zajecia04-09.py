# =============================================
# M4Z09
import Helper as helper


def isitPrime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def main(args):
    while True:
        print("################################################################################\n")
        userInput = helper.userVariableINTstring("Podaj liczbę, sprawdzimy czy jest to liczba pierwsza: ")
        if userInput < 1:
            print("Liczba musi być większa od 0")
            continue
        if isitPrime(userInput):
            print("Liczba {} to liczba pierwsza.".format(userInput))
        else:
            print("Liczba {} to nie jest liczba pierwsza.".format(userInput))
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================
