# =============================================
# M2Z15
import random as rnd

try:
    lewy = int(input("Podaj początek przedziału: "))
    prawy = int(input("Podaj koniec przedziału: "))
except Exception as e:
    print(e)
    print("Błędne dane")
    exit(0)

liczba_pseudo_losowa = rnd.randrange(lewy, prawy + 1)
liczba_podana = -1
licznik = 1

while (liczba_podana != liczba_pseudo_losowa):
    liczba_podana = int(input("Zgadnij liczbę: "))
    if (liczba_podana == liczba_pseudo_losowa):
        print("TAK! Ilość prób", licznik)
    else:
        if (liczba_podana > liczba_pseudo_losowa):
            print("Za dużo")
        elif (liczba_podana < liczba_pseudo_losowa):
            print("Za mało")
        licznik += 1


# =============================================