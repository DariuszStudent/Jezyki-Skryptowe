# =============================================
# M2Z11
import Helpers as helpers

znak = ' . '
exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj dlugosc macierzy kwadratowej <int>x<int>: ")
        ilosc, exitWhile = helpers.userVariableINT(userVar)
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
    exitWhile = False

# =============================================