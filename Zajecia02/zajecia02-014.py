# =============================================
# M2Z14
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj pierwszą liczbę ciągu n+1 która go otwiera: ")
        intervalFirst, exitWhile = helpers.userVariableINT(userVar)
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj drugą liczbę ciągu n+1 która go zamyka: ")
        intervalLast, exitWhile = helpers.userVariableINT(userVar)
    if intervalFirst > intervalLast:
        print("Podane wartości są błędne, pierwsza liczba musi być mniejsza od drugiej liczby.")
        helpers.exitProgram()
        exitWhile = False
        continue

    print("podany ciąg to: <{} : {}>".format(intervalFirst, intervalLast))
    for i in range(intervalFirst, intervalLast + 1):
        if i % 2 == 0 and i % 7 == 0:
            print("Liczba {} jest podzielna przez 2 i 7 ".format(i))
        elif i % 2 == 0:
            print("Liczba {} jest podzielna przez 2".format(i))
        elif i % 7 == 0:
            print("Liczba {} jest podzielna przez 7".format(i))

    helpers.exitProgram()
    exitWhile = False

# =============================================