# =============================================
# M2Z02
import Helpers as helpers

WIEK_K = 60
WIEK_M = 65

imie = input("Podaj imię: ")

plec = ''
while (plec != 'K' and plec != 'M'):
    plec = input("Podaj płeć [m/k]: ")
    plec = plec.upper()
    if (plec != 'M' and plec != 'K'):
        print("Błąd, podaj płeć ponownie")

exit = False
while (exit == False):
    userVar = input("Podaj liczbę: ")
    wiek, exit = helpers.userVariableINT(userVar)

print("Twoje imię",imie,"wiek",wiek,"plec",plec)

if (plec == 'K'):
    if (wiek >= 60):
        print("Emerytura")
    else:
        print("ZUS")
else:
    if (wiek >= 65):
        print("Emerytura")
    else:
        print("ZUS")

# =============================================
