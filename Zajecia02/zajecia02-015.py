# =============================================
# M2Z15
import Helpers as helpers
import random as rnd

while True:
    print("################################################################################\n")
    intervalFirst = helpers.userVariableIntNEW("Podaj początek przedziału, musi być dodatnia: ")
    intervalLast = helpers.userVariableIntNEW("Podaj koniec przedziału: ")

    if intervalFirst > intervalLast or intervalFirst < 0:
        print("Podane wartości są błędne, pierwsza liczba musi być dodatnia i mniejsza od drugiej liczby.")
        helpers.exitProgram()
        continue

    pseudoNumber = rnd.randrange(intervalFirst, intervalLast + 1)
    userNumber = -1
    counter = 1

    while userNumber != pseudoNumber:
        print("Podany zakres to: <{} : {}>".format(intervalFirst, intervalLast))
        userNumber = helpers.userVariableIntNEW("Zgadnij Liczbę: ")
        if userNumber < intervalFirst or userNumber > intervalLast:
            print("Liczba jest z poza zakresu, spróbuj jeszcze raz")
            continue
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

# =============================================