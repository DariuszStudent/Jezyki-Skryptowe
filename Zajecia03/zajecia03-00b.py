# =============================================
# M3Z00b

print("\nTworzenie krotki (tuple)")
tup = ('jeden', 'dwa', 'trzy')
print(tup)

print("\nKrotki możesz tworzyć również w ten sposób")
tup2 = 'cztery', 'pięć', 'sześć'  # to też jest krotka, ale bez nawiasu
print(tup2)


print("\nKrotka stworzona z różnych typów")
tup_mixed = (1, 'dwa', [3, 4.1])
print(tup_mixed)

# =============================== podstawowe operacje
print("\npodstawowe operacje")
print(tup[0])    # odwołanie do pierwszego elementu krotki
print(tup[-1])   # odwołanie do ostatniego elementu
print(tup[1:])   # wyodrębnienie elementów krotki od drugiego do ostatniego

# Teraz pokażę Ci na prostym przykładzie podstawową różnicę między krotką a listą.
# Otóż krotki są niemodyfikowalne! Sprawdźmy to. Spróbujmy zastąpić jeden element krotki:

try:
    tup[1] = 'zmień element'
except Exception as e:
    print("\ntup[1] = 'zmień element'")
    print(e)

# ================================= łączenie i powielanie krotek
print("\nłączenie i powielanie krotek")
tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')
print(tup1 + tup2)

# lub:
tup_new = tup2 + tup1  # tutaj w odwrotnej kolejności
print(tup_new)

# ================================= metody wbudowane
print("nmetody wbudowane")
tup = ('jeden', 'dwa', 'trzy')
print(tup)
print("nlen() zwraca liczbę elementów krotki")
print(len(tup))

print("nindex() zwraca indeks pierwszego wystąpienia szukanego elementu w krotce")
print(tup.index('dwa'))

print("ncount() zwraca liczbę wystąpień elementu w krotce")
print(tup.count('dwa'))

print("min - prawda (True) jeśli element występuje, w przeciwnym przypadku fałsz (False)")
print('element' in tup)

print("min() i max() zwracają najmniejszy i największy element krotki")
tup_numbers = (1, 2, 3)  # żeby użyć tych metod krotka musi zawierać tylko elementy liczbowe
print(tup_numbers)
print(min(tup_numbers))
print(max(tup_numbers))

print("\nsum() zwraca sumę elementów krotki")
sum(tup_numbers)