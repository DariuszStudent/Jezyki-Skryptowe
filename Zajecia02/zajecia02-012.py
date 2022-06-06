# =============================================
# M2Z12
import Helpers as helpers

exitWhile = False
while not exitWhile:
    number = ""
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj liczbę, program przetworzy jej wartość z dziesiętnych na binarny: ")
        userNumber, exitWhile = helpers.userVariableINT(userVar)

    while userNumber != 0:
        r = userNumber % 2
        number = str(r) + number
        userNumber //= 2

    print(number)

    helpers.exitProgram()
    exitWhile = False

# =============================================