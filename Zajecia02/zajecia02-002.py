# =============================================
# M2Z02
import Helpers as helpers

wikK = 60
wiekMan = 65

imie = input("Podaj imię: ")

plec = ''
while plec != 'K' and plec != 'M':
    plec = input("Podaj płeć [m/k]: ")
    plec = plec.upper()
    if plec != 'M' and plec != 'K':
        print("Błąd, podaj płeć ponownie")

exitWhile = False
while not exitWhile:
    userVar = input("Podaj liczbę: ")
    wiek, exitWhile = helpers.userVariableINT(userVar)

print("Twoje imię", imie, "wiek", wiek, "plec", plec)

if plec != 'K':
    if wiek >= 65:
        print("Emerytura")
    else:
        print("ZUS")
else:
    if wiek >= 60:
        print("Emerytura")
    else:
        print("ZUS")

# =============================================
