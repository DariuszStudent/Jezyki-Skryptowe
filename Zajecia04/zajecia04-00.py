# =============================================
# M4Z00
def napis(linia = True):
    if linia:
        endl = '\n'
    else:
        endl = ''
    print("Dzielenie przez zero", end=endl)


def main(args):
    x = int(input("Podaj liczbę: "))
    if x == 0:
        napis()
    else:
        napis(False)
    print("Koniec programu!")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# =============================================
