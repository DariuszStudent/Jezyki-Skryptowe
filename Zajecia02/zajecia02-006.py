# =============================================
# M2Z06
import Helpers as helpers

while True:
    print("################################################################################\n")
    ile = helpers.userVariableINT("Ilosc znakow: ")

    for i in range(1, ile+1):
        for j in range(0, i):
            print("x", end='')
        print()

    helpers.exitProgram()

# =============================================