# =============================================
# M2Z00
import Helpers as helpers

print("Jeśli liczba jest większa od zera program wyświetli TAK, jeśli nie wyświetli NIE")

exit = False
while (exit == False):
    userVar = input("Podaj liczbę: ")
    userNumber, exit = helpers.userVariableINT(userVar)

if userNumber == 0:
    print("Podana liczba jest równa 0")
elif userNumber > 0:
    print("Podana liczba jest większa od zera")
else:
    print("Liczba jest mniejsza od zera")

# =============================================
