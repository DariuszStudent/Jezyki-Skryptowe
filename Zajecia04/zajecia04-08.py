# =============================================
# M4Z08
import math

def ile_cyfr(l):
    if l <= 999999999999997:
        return int(math.log10(l)) + 1
    licznik = 15
    while l >= 10 ** licznik:
        licznik += 1
    return licznik


liczba = int(input("Podaj dowolną liczbę:"))
print("Liczba cyfr:", ile_cyfr(liczba))

# =============================================