# =============================================
# M2Z09
import Helpers as helpers

while True:
    print("################################################################################\n")
    while True:
        try:
            userVar1, userVar2, userVar3 = input("Podaj trzy liczby oddzielone spacjami: ").split(' ')
        except Exception as e:
            print(e)
            helpers.exitProgram()
            continue
        userNumber1 = helpers.userVariableFloat(userVar1)
        userNumber2 = helpers.userVariableFloat(userVar2)
        userNumber3 = helpers.userVariableFloat(userVar3)
        if type(userNumber1) == float and type(userNumber2) == float and type(userNumber3) == float:
            break

    lista = [userNumber1, userNumber2, userNumber3]
    print("Najmniejsza podana liczba to: {:.2f}".format(min(lista)))

    helpers.exitProgram()

# =============================================