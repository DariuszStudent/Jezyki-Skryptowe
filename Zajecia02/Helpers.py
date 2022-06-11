import turtle as t


def exitProgram():
    exit = input("\nWciśnij enter aby kontynuować lub wpisz [Q] [exit], aby wyjść z programu: ").upper()
    if exit == 'Q' or exit == 'EXIT':
        quit()


def userVariableINTvariable(userVar):
    while True:
        try:
            user = int(userVar)
            return user
        except Exception as e:
            print("Typ błędu: ", e)
            exitProgram()


def userVariableINTstring(textForUser):
    while True:
        userVar = input("{}".format(textForUser))
        try:
            user = int(userVar)
            return user
        except Exception as e:
            print("Typ błędu: ", e)
            exitProgram()


def userVariableZeroOne(textForUser):
    exit = True
    while exit:
        userInput = input("{}".format(textForUser))
        for i in userInput:
            if i != "0" and i != "1":
                print("Liczba binarna to ciąg jedynek i zer, jeśli będziesz kontynuował,"
                    "możesz spróbować jeszcze raz. ;)")
                exit = True
                break
            else:
                exit = False
    return userInput


def userVariableFloatString(textForUser):
    while True:
        userVar = input("{}".format(textForUser))
        try:
            user = float(userVar)
            return user
        except Exception as e:
            print("Typ błędu: ", e)
            exitProgram()

def userVariableFloatvariable(userVar):
    while True:
        try:
            user = float(userVar)
            return user
        except Exception as e:
            print("Typ błędu: ", e)
            exitProgram()


def userVariableROQ(textForUser):
    while True:
        userInput = input("{}".format(textForUser))
        userVar = userInput[0]
        if userVar == "o" or userVar == "r":
            return userVar
            break
        elif userVar == "q":
            quit()
        else:
            print("Zostały podane złe dane")
            exitProgram()


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