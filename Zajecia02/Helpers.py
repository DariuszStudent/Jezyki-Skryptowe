
def userVariableINT(userVar):
    try:
        user = int(userVar)
        return user, True
    except Exception as e:
        print("Typ błędu: ", e)
        exit = input("Wciśnij enter aby kontynuować lub wpisz [Q] [exit], aby wyjść z programu: ").upper()
        if (exit == 'Q' or exit == 'EXIT'):
            quit()
        return False, False

def userVariableFloat(userVar):
    try:
        user = float(userVar)
        return user, True
    except Exception as e:
        print("Typ błędu: ", e)
        exit = input("Wciśnij enter aby kontynuować lub wpisz [Q] [exit], aby wyjść z programu: ").upper()
        if (exit == 'Q' or exit == 'EXIT'):
            quit()
        return False, False