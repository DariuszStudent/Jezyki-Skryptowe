# =============================================
# M2Z04
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj licznik: ")
        licznik, exitWhile = helpers.userVariableINT(userVar)
    if licznik <= 0:
        print("Możesz zakończyć program.")
    while licznik > 0:
        print("licznik = ", licznik)
        licznik += -1
        # if (licznik == 3):
        #    break
        if (licznik < 7):
            continue
        print("Koniec ciała pętli")
    helpers.exitProgram()
    exitWhile = False

# =============================================
