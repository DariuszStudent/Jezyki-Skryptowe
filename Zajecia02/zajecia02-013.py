# =============================================
# M2Z13

import Helpers as helpers

exitWhile = False
while not exitWhile:
    number = 0
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj liczbę binarną: ")
        userNumber, exitWhile = helpers.userVariableZeroOne(userVar)

    cyfra = len(userNumber) - 1
    for i in userNumber:
        number = number + (int(i) * pow(2, cyfra))
        cyfra = cyfra - 1

    print(number)

    helpers.exitProgram()
    exitWhile = False

# =============================================