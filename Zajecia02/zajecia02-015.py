# =============================================
# M2Z15
import Helpers as helpers
import random as rnd

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj początek przedziału, musi być dodatnia: ")
        intervalFirst, exitWhile = helpers.userVariableINT(userVar)
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj koniec przedziału: ")
        intervalLast, exitWhile = helpers.userVariableINT(userVar)
    if intervalFirst > intervalLast or intervalFirst < 0:
        print("Podane wartości są błędne, pierwsza liczba musi być dodatnia i mniejsza od drugiej liczby.")
        helpers.exitProgram()
        exitWhile = False
        continue

    pseudoNumber = rnd.randrange(intervalFirst, intervalLast + 1)
    userNumber = -1
    counter = 1

    while userNumber != pseudoNumber:
        exitWhile = False
        while not exitWhile:
            print("Podany zakres to: <{} : {}>".format(intervalFirst, intervalLast))
            userVar = input("Zgadnij Liczbę: ")
            userNumber, exitWhile = helpers.userVariableINT(userVar)
            if userNumber < intervalFirst or userNumber > intervalLast:
                print("Liczba jest z poza zakresu, spróbuj jeszcze raz")
                exitWhile = False
        if userNumber == pseudoNumber:
            print("TAK! Ilość prób", counter)
        else:
            if userNumber > pseudoNumber:
                print("Za dużo")
                intervalLast = userNumber - 1
            elif userNumber < pseudoNumber:
                print("Za mało")
                intervalFirst = userNumber + 1
            counter += 1

    helpers.exitProgram()
    exitWhile = False

# =============================================