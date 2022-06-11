# =============================================
# M2Z01
import Helpers as helpers

sto = 100
while True:
    print("################################################################################\n")
    print("Podaj swój wiek, program sprawdzi ile brakuje ci do 100 lat i czy jesteś pełnoletni")

    userNumber = helpers.userVariableINTstring("Podaj liczbę: ")

    missingYears = sto - userNumber
    if missingYears > 0:
        print("Do 100 lat brakuje Ci: {}".format(missingYears))
    elif missingYears == 0:
        print("Masz równo 100 lat")
    else:
        print("Masz ponad 100 lat czyli: {}".format(userNumber))
    if userNumber >= 18:
        print("PEŁNOLETNI")
    else:
        print("MŁODOCIANY")

    helpers.exitProgram()

# =============================================
