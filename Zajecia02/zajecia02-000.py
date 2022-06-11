# =============================================
# M2Z00
import Helpers as helpers

exitWhile = False
while True:
    print("################################################################################\n")
    print("Jeśli liczba jest większa od zera program wyświetli TAK, jeśli nie wyświetli NIE")

    userNumber = helpers.userVariableINTstring("Podaj liczbę: ")

    if userNumber == 0:
        print("Podana liczba jest równa 0")
    elif userNumber > 0:
        print("Podana liczba jest większa od zera")
    else:
        print("Liczba jest mniejsza od zera")

    helpers.exitProgram()

# =============================================
