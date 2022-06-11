# =============================================
# M2Z18
import Helpers as helpers
import random as rnd

user = 0
computer = 0

while True:
    print("################################################################################\n")
    userInput = helpers.userVariableIntNEW("Określ ilość rzutów kostką, wpisz liczbę: ")
    oczek1 = oczek2 = oczek3 = oczek4 = oczek5 = oczek6 = 0

    for i in range(1, userInput + 1):
        los = rnd.randrange(1, 7)
        print("Rzut nr: {:>3} Wyrzucono: {}".format(i, los))
        if los == 1:
            oczek1 += 1;
        if los == 2:
            oczek2 += 1;
        if los == 3:
            oczek3 += 1;
        if los == 4:
            oczek4 += 1;
        if los == 5:
            oczek5 += 1;
        if los == 6:
            oczek6 += 1;

    print("Statystyka rzutów:")
    print("Oczek:  1 ilość: {:>2}".format(oczek1))
    print("Oczek:  2 ilość: {:>2}".format(oczek2))
    print("Oczek:  3 ilość: {:>2}".format(oczek3))
    print("Oczek:  4 ilość: {:>2}".format(oczek4))
    print("Oczek:  5 ilość: {:>2}".format(oczek5))
    print("Oczek:  6 ilość: {:>2}".format(oczek6))

    helpers.exitProgram()

# =============================================
