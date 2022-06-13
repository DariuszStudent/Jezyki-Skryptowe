# =============================================
# M4Z10
import Helper as helper
from multipledispatch import dispatch


@dispatch(int, int)
def policz(a, b):
    print("suma argumentów: ", a+b)


@dispatch(str, int)
def policz(a, b):
    print("Powielamy wpisane słowo: ", a*b)


@dispatch(float, float)
def policz(a, b):
    print("Dodajemy liczby rzeczywiste: float float", a+b)


def main(args):
    while True:
        print("################################################################################\n")
        a = helper.userVariableINTstring("Podaj wartość a (liczba całkowita): ")
        b = helper.userVariableINTstring("Podaj wartość b (liczba całkowita): ")
        policz(a, b)
        a = input("Podaj jakiś tekst: ")
        b = helper.userVariableINTstring("Podaj wartość b (liczba całkowita): ")
        policz(a, b)
        a = helper.userVariableFloatString("Podaj wartość rzeczywistą(0.25 np.): ")
        b = helper.userVariableFloatString("Podaj wartość rzeczywistą(5.55 np.): ")
        policz(a, b)
        print("policz(1, 1.0) to błąd tutaj")
        try:
            policz(1, 1.0)
        except Exception as e:
            print(e)
            print("Dzieje się tak dlatego, ponieważ nie mamy takiej funkcji, int. float")
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


# =============================================