# =============================================
# M2Z13
import Helpers as helpers

while True:
    number = 0
    print("################################################################################\n")
    userNumber = helpers.userVariableZeroOne("Podaj liczbę binarną: ")

    cyfra = len(userNumber) - 1
    for i in userNumber:
        number = number + (int(i) * pow(2, cyfra))
        cyfra = cyfra - 1

    print(number)

    helpers.exitProgram()

# =============================================