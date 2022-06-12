# =============================================
# M4Z10
import Helper as helper
from multipledispatch import dispatch


@dispatch(int, int)
def policz(a, b):
    print("Pole prostokąta int: ", a*b)


@dispatch(float, float)
def policz(a, b):
    print("Pole prostokąta: float", a*b)


@dispatch(float, int)
def policz(a, b):
    print("Pole prostokąta: float int", a*b)


@dispatch(int)
def policz(a):
    print("Pole kwadratu: int", a * a)


def main(args):
    while True:
        print("################################################################################\n")
        policz(11, 22)
        policz(11.0, 12.0)
        policz(10.0, 10)
        policz(5)
        helper.exitProgram()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


# =============================================