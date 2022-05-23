# =============================================
# M2Z01
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    print("Podaj swój wiek, program sprawdzi ile brakuje ci do 100 lat i czy jesteś pełnoletni")
    while not exitWhile:
        userVar = input("Podaj liczbę: ")
        userNumber, exitWhile = helpers.userVariableINT(userVar)

    missingYears = 100 - userNumber
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

    print("Nie podałeś liczby całkowitej, tylko: {}"
          "\n Koniec programu".format(userNumber))
    helpers.exitProgram()
    exitWhile = False

# =============================================
