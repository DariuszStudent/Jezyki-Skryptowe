# =============================================
# M2Z00

print("Jeśli liczba jest większa od zera program wyświetli TAK, jeśli nie wyświetli NIE")
userNumber = input("Podaj liczbę: ")
try:
    userNumber = int(userNumber)
    if userNumber == 0:
        print("Podana liczba jest równa 0")
    elif userNumber > 0:
        print("Podana liczba jest większa od zera")
    else:
        print("Liczba jest mniejsza od zera")
except:
    print("Nie podałeś liczby całkowitej, tylko: {}"
          "\n Koniec programu".format(userNumber))


# =============================================
