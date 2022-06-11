import random as rnd


def exitProgram():
    exit = input("\nWciśnij enter aby kontynuować lub wpisz [Q] [exit], aby wyjść z programu: ").upper()
    if exit == 'Q' or exit == 'EXIT':
        quit()


def userVariableINTnumber(textForUser):
    while True:
        userVar = input("{}".format(textForUser))
        try:
            user = int(userVar)
            return user
        except Exception as e:
            print("Typ błędu: ", e)
            exitProgram()


def randomList(rangeUser):
    listaUser = []
    for i in range(0, rangeUser):
        listaUser.append(rnd.randrange(0, 100))
    return listaUser


def userAddElementToList(rangeUser, lista):
    for i in range(0, rangeUser):
        element = userVariableINTnumber("Podaj wartość elementu: ")
        lista.append(element)
    return lista
