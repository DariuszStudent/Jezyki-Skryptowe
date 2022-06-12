# =============================================
# M4Z03
import Helper as helper


def dec2bin(liczba):
    mask = 128
    ile = 0
    strliczba = ""
    while mask > 0:
        if liczba & mask > 0:
            strliczba = strliczba + '1'
            ile += 1
        else:
            strliczba += '0'
        mask = mask >> 1
    return strliczba, ile

#def zlicz_bity(liczba):
#    ile = 0
#    while liczba != 0:
#        if liczba & 0x1:
#            ile += 1
#    return ile


def main(args):
    while True:
        print("################################################################################\n")
        dane = helper.userVariableINTstring("Podaj liczbę: ")
        s = dec2bin(dane)
        print(s)
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


# =============================================