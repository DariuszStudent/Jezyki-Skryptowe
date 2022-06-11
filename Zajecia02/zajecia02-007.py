# =============================================
# M2Z07
import Helpers as helpers

while True:
    print("################################################################################\n")
    ile = helpers.userVariableINT("Podaj wysokość: ")

    for i in range(0, ile):
        for j in range(0, ile - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

    for i in range(0, ile // 3):
        for j in range(0, ile - (ile // 5)):
            print(end=" ")
        for j in range(0, ile // 5):
            print("*", end=" ")
        print()

    helpers.exitProgram()

# =============================================
