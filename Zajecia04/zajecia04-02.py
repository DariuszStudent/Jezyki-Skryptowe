# =============================================
# M4Z02
import Helper as helper


def dec2bin(liczba):
    mask = 128
    strliczba = ""
    while mask > 0:
        if liczba & mask > 0:
            strliczba = strliczba + '1'
        else:
            strliczba += '0'
        mask = mask >> 1
    return strliczba


def main(args):
    while True:
        s= ""
        print("################################################################################\n")
        dane = helper.userVariableINTstring("Podaj liczbę: ")
        s = dec2bin(dane)
        print(s)
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


# =============================================