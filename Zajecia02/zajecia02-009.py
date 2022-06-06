# =============================================
# M2Z09

import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        try:
            userVar1, userVar2, userVar3 = input("Podaj trzy liczby oddzielone spacjami: ").split(' ')
        except Exception as e:
            print(e)
            helpers.exitProgram()
            continue
        intervalFirst, exitWhile = helpers.userVariableFloat(userVar1)
        if not exitWhile:
            continue
        intervalLast, exitWhile = helpers.userVariableFloat(userVar2)
        if not exitWhile:
            continue
        userNumber3, exitWhile = helpers.userVariableFloat(userVar3)

    lista = [intervalFirst, intervalLast, userNumber3]
    print("Najmniejsza podana liczba to: {:.2f}".format(min(lista)))

    helpers.exitProgram()
    exitWhile = False

# =============================================