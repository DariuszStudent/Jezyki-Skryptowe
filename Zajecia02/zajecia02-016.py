# =============================================
# M2Z16
import Helpers as helpers
import random as rnd
import time

user = 0
computer = 0

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Losowanie, wpisz [o] lub [r] (orzeł lub reszka), lub "
                        "wpisz [q] aby wyjść z programu: ").lower()
        userInput, exitWhile = helpers.userVariableROQ(userVar)

    los = rnd.choice(["o", "r"])
    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)
    if los == "o":
        show = "Orzeł"
    else:
        show = "Reszka"
    print("Wylosowana strona monety to {}".format(show))

    if los == userInput:
        user += 1
    else:
        computer += 1

    print("Wyniki:\n"
          "Użytkownik = {},\n"
          "Komputer   = {}".format(user, computer))

    helpers.exitProgram()
    exitWhile = False

# =============================================
