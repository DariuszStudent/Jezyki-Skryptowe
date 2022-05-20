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

# instrukcja  if userNumber == 0: wykona się zawsze, jeśli jest prawidłowa inne instrukcje się nie wykonają
# wynika to z tego, że program działa kaskadowo, jeśli pierwsza operacja jest poprawna kolejne
# pomija czyli elif i else
# =============================================
