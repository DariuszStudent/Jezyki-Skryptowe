# =============================================
# M2Z00
import Helpers as helpers

print("Jeśli liczba jest większa od zera program wyświetli TAK, jeśli nie wyświetli NIE")

exitWhile = False
while not exitWhile:
    userVar = input("Podaj liczbę: ")
    userNumber, exitWhile = helpers.userVariableINT(userVar)

if userNumber == 0:
    print("Podana liczba jest równa 0")
elif userNumber > 0:
    print("Podana liczba jest większa od zera")
else:
    print("Liczba jest mniejsza od zera")

# =============================================
