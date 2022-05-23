# =============================================
# M2Z06
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Ilosc znakow: ")
        ile, exitWhile = helpers.userVariableINT(userVar)

    for i in range(1, ile+1):
        for j in range(0, i):
            print("x", end='')
        print()

    helpers.exitProgram()
    exitWhile = False

# =============================================