# =============================================
# M2Z00
import Helpers as helpers

print("Jeśli liczba jest większa od zera program wyświetli TAK, jeśli nie wyświetli NIE")

exit = False
while (exit == False):
    userNumber = input("Podaj liczbę: ")
    userVar, exit = helpers.userVariableINT(userNumber)

if userVar == 0:
    print("Podana liczba jest równa 0")
elif userVar > 0:
    print("Podana liczba jest większa od zera")
else:
    print("Liczba jest mniejsza od zera")

# =============================================
