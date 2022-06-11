# =============================================
# M2Z08
import Helpers as helpers

while True:
    print("################################################################################\n")
    liczba = helpers.userVariableINTstring("Podaj liczbę naturalną nie większą niż 128, wyświętlę ją jako wartość binarna: ")

    if liczba > 128 or liczba < 1:
        print("Podana liczba nie jest z zadanego przedziału")
        helpers.exitProgram()
        continue

    i = 128
    print("Liczba {} to liczba w zapisie binarnym:".format(liczba), end=" ")
    while i > 0:
        if liczba & i > 0:
            print("1", end="")
        else:
            print("0", end="")
        i = i >> 1
    print()

    helpers.exitProgram()

# =============================================