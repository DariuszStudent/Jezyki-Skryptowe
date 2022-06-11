# =============================================
# M2Z17
import Helpers as helpers
import random as rnd
import time
import sympy
import math


def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def isprimeMath(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a+1
    return num > 1


while True:
    print("################################################################################\n")
    intervalFirst = helpers.userVariableIntNEW("Podaj początek przedziału: ")
    intervalLast = helpers.userVariableIntNEW("Podaj koniec przedziału: ")

    if intervalFirst > intervalLast:
        print("Podane wartości są błędne, pierwsza liczba musi mniejsza od drugiej liczby.")
        helpers.exitProgram()
        continue

    randomNumber = rnd.randrange(intervalFirst, intervalLast + 1)
    print(randomNumber)

    start1 = time.time()
    print("DEF- isprime :Czy liczba {} jest liczbą pierwszą: {}".format(randomNumber, isprime(randomNumber)))
    end1 = time.time()
    print(end1 - start1)

    start2= time.time()
    print("Math :Czy liczba {} jest liczbą pierwszą: {}".format(randomNumber, isprimeMath(randomNumber)))
    end2 = time.time()
    print(end2 - start2)

    start3 = time.time()
    print("sympry :Czy liczba {} jest liczbą pierwszą: {}".format(randomNumber, sympy.isprime(randomNumber)))
    end3 = time.time()
    print(end3 - start3)

    helpers.exitProgram()

# =============================================