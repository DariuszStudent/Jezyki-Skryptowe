# =============================================
# M2Z05
import Helpers as helpers

exitWhile = False
while not exitWhile:
    e = -1
    licznik = 1
    suma = srednia = 0
    maximum = minimum = 0

    print("################################################################################\n")
    print("Podaj liczby całkowite, 0 kończy.")

    while e != 0:
        while not exitWhile:
            print("Podaj element nr", licznik, ": ", end='')
            userVar = input()
            e, exitWhile = helpers.userVariableINT(userVar)
        if e == 0:
            licznik -= 1
            break
        if e != 0:
            suma += e
        if licznik == 1:
            maximum = minimum = e
        if e > maximum:
            maximum = e
        if e < minimum and e != 0:
            minimum = e
        if licznik != 0:
            licznik += 1
        exitWhile = False

    print("Ilość elementów:", licznik, "Suma", suma, "max", maximum, "min", minimum)
    print("Srednia: %0.2f, suma %05d" % (suma / licznik, suma))
    print("Maksimum: {0:4d}, Minimum: {1:4d}".format(maximum, minimum))

    helpers.exitProgram()
    exitWhile = False

# =============================================
