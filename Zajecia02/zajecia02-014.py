# =============================================
# M2Z14
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj pierwszą liczbę ciągu n+1 która go otwiera: ")
        userNumber1, exitWhile = helpers.userVariableINT(userVar)
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj drugą liczbę ciągu n+1 która go zamyka: ")
        userNumber2, exitWhile = helpers.userVariableINT(userVar)
    if userNumber1 > userNumber2:
        print("Podane wartości są błędne, pierwsza liczba musi być większa od drugiej liczby.")
        helpers.exitProgram()
        exitWhile = False
        continue

    print("podany ciąg to: <{} : {}>".format(userNumber1, userNumber2))
    for i in range(userNumber1, userNumber2 + 1):
        if i % 2 == 0 and i % 7 == 0:
            print("Liczba {} jest podzielna przez 2 i 7 ".format(i))
        elif i % 2 == 0:
            print("Liczba {} jest podzielna przez 2".format(i))
        elif i % 7 == 0:
            print("Liczba {} jest podzielna przez 7".format(i))

    helpers.exitProgram()
    exitWhile = False

# =============================================