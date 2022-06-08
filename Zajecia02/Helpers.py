import turtle as t


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


def userVariableZeroOne(userInput):
    for i in userInput:
        if i == "0" or i == "1":
            continue
        else:
            print("Liczba binarna to ciąg jedynek i zer, jeśli będziesz kontynuował,"
                  "możesz spróbować jeszcze raz. ;)")
            exitProgram()
            return False, False
    return userInput, True


def userVariableFloat(userInput):
    try:
        user = float(userInput)
        return user, True
    except Exception as e:
        print("Typ błędu: ", e)
        exitProgram()
        return False, False


def userVariableROQ(userInput):
    userVar = userInput[0]
    if userVar == "o" or userVar == "r":
        return userVar, True
    elif userVar == "q":
        quit()
    else:
        print("Zostały podane złe dane")
        exitProgram()
        return False, False


def turtleXY(lenght):
    t.speed(1000)
    t.penup()
    t.goto(-lenght//2, 0)
    t.pendown()
    t.forward(lenght)
    t.penup()
    t.goto(0, lenght//2)
    t.right(90)
    t.pendown()
    t.forward(lenght)
    t.penup()
    t.left(90)
    t.speed(10)