# =============================================
# M4Z00c

import Helper as helper


def swap(a, b):
    return b, a


def main(args):
    a = helper.userVariableINTstring("Podaj a: ")
    b = helper.userVariableINTstring("Podaj b: ")
    wynik = swap(a, b)
    print(wynik)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# =============================================