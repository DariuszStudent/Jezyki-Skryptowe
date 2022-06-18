# =============================================
# M5Z04
import Helper as helper


def main(args):
    while True:
        licznik = 0
        print("################################################################################\n")
        alfabet = "abcdefghijklmnopqrstuvwxyz"
        for i in alfabet:
            print(" {} => {}".format(i, i.upper()), end="")
            licznik += 1
            if licznik == 5:
                print()
                licznik = 0

        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================