# =============================================
# M2Z10

import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userWzrost = input("Podaj proszę swój wzrost w cm: ")
        wzrost, exitWhile = helpers.userVariableFloat(userWzrost)
        if exitWhile:
            exitWhile = False
            break
    while not exitWhile:
        userWaga = input("Podaj proszę swoją wagę w kg: ")
        waga, exitWhile = helpers.userVariableFloat(userWaga)

    bmi = waga / ((wzrost / 100) ** 2)
    print(round(bmi, 2))
    if bmi < 18.4:
        print('Niedowaga')
    elif bmi < 24.9:
        print("OK")
    elif bmi <= 29.9:
        print("nadwaga")
    elif bmi <= 34.9:
        print("Duża nadwaga")
    elif bmi <= 39.9:
        print("Bardzo duża nadwaga")
    else:
        print("OJ!")

    helpers.exitProgram()
    exitWhile = False

# =============================================
