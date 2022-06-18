# =============================================
# M5Z03
import Helper as helper

liczba = 32.1234
dane = 342
n = 16

def main(args):
    while True:
        print("################################################################################\n")
        print("Dane wynoszą: {}".format(dane))
        print("Dane wynoszą: {}, a liczba jest równa: {:.15f} cali".format(dane, liczba))
        print("Dane wynoszą: {}, a liczba jest równa: {:.3f} cali".format(dane, liczba))
        print("Dane = {:>10}, liczba = {:.15f} cali".format(dane, liczba))
        print("Dane = {:0>10}, liczba = {:0>20.15f} cali".format(dane, liczba))
        print("Szesnastkowo 16 to jest", hex(n))
        print("Szesnastkowo 16 to jest", oct(n))

        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

# =============================================