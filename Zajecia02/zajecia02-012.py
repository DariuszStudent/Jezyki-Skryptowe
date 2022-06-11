# =============================================
# M2Z12
import Helpers as helpers

while True:
    number = ""
    print("################################################################################\n")
    userNumber = helpers.userVariableIntNEW("Podaj liczbę, program przetworzy jej wartość z dziesiętnych na binarny: ")

    while userNumber != 0:
        r = userNumber % 2
        number = str(r) + number
        userNumber //= 2

    print(number)

    helpers.exitProgram()

# =============================================