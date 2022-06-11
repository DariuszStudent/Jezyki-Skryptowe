# =============================================
# M2Z11
import Helpers as helpers

znak = ' . '
while True:
    print("################################################################################\n")

    ilosc = helpers.userVariableINTstring("Podaj dlugosc macierzy kwadratowej <int>x<int>: ")
    userInput = input("Podaj znak, który chcesz użyć jako przekątna "
                        "(program przechwyci tylko pierwszy znak): ")
    znakUser = userInput[0]

    for i in range(0, ilosc):
        for j in range(0, ilosc):
            if i == j:
                print(' {} '.format(znakUser), end='')
            else:
                print(znak, end='')
        print()

    print()

    for i in range(0, ilosc):
        for j in range(0, ilosc):
            if j + i == ilosc - 1:
                print(' {} '.format(znakUser), end='')
            else:
                print(znak, end='')
        print()

    helpers.exitProgram()

# =============================================