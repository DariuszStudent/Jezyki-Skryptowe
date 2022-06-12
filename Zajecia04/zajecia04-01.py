# =============================================
# M4Z01
import Helper as helper
#w = 2


def km_mil(km):
    MILA = 1.6
    mila = km / MILA
    #global w   # read-only
    return mila


def main(args):
    while True:
        print("################################################################################\n")
        dane = helper.userVariableFloatString("Podaj odległość w km: ")
        if dane < 0:
            print("Wartość nie może być poniżej zera")
            helper.exitProgram()
            continue
        wynik = km_mil(dane)
        print("Podana odległość w milach:", wynik, "mil.")
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================
