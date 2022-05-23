def exitProgram():
    exit = input("\nWciśnij enter aby kontynuować lub wpisz [Q] [exit], aby wyjść z programu: ").upper()
    if exit == 'Q' or exit == 'EXIT':
        quit()

def userVariableINT(userInput):
    try:
        user = int(userInput)
        return user, True
    except Exception as e:
        print("Typ błędu: ", e)
        exitProgram()
        return False, False

def userVariableFloat(usernInput):
    try:
        user = float(usernInput)
        return user, True
    except Exception as e:
        print("Typ błędu: ", e)
        exitProgram()
        return False, False
