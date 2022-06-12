# =============================================
# M4Z00b
import Helper as helper

def is_hex(liczba):
    hextab = "0123456789ABCDEF"
    liczba = liczba.upper()
    for i in range(0, len(liczba)):
        if hextab.find(liczba[i]) == -1:
            return False
    return True

def main(args):
    while True:
        userInput = input("Podaj kod szesnastkowy: ")
        wynik = is_hex(userInput)
        if wynik:
            print("OK")
        else:
            print("Nie OK")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# =============================================