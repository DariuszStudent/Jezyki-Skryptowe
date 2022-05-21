# =============================================
# M2Z02

WIEK_K = 60
WIEK_M = 65

imie = input("Podaj imię: ")

plec = ''
while (plec != 'K' and plec != 'M'):
    plec = input("Podaj płeć [m/k]: ")
    plec = plec.upper()
    if (plec != 'M' and plec != 'K'):
        print("Błąd, podaj płeć ponownie")
try:
    wiek = int(input("Podaj wiek: "))
except ValueError:
    print("Błędny wiek:")
    exit(0)
else:
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
