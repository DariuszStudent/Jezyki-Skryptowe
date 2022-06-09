# =============================================
# M3Z00

print("\nLista składająca się z kilku typów danych")
x = 3
nowa_lista = [1, 'dwa', 3.45, x]
print(nowa_lista)

print("\nLista może też być pusta (pusty zbiór elementów)")
pusta_lista = []
print(pusta_lista)

moja_lista = [1, 2, 3, 4, 5]

print("\nWywołanie elementu listy za pomocą indeksu")
print(moja_lista[1])  # zwróci nam wartość drugiego elementu listy, czyli tutaj liczba 2
print(moja_lista[3])  # = 4
try:
    moja_lista[10]  # Indeks poza zakresem listy, Python zwróci tutaj błąd: 'IndexError: list index out of range'
except Exception as e:
    print("moja_lista[10], indeks poza zakresem")
    print(e)

print("\nMożemy też wywołać element listy licząc ostatniego elementu")
print(moja_lista[-1])  # = 5
print(moja_lista[-2])  # = 4

print("\nWycinanie ('slicing') wybranego ciągu elementów z listy")
print(moja_lista[1:])  # Dostaniemy tutaj listę składającą się z czterech elementów [2,3,4,5]
print(moja_lista[1:3])  # Fragment listy obejmujący elementy od drugiego do trzeciego [2,3]

# =============================================== łączenie list
print("\nłączenie list")
print(moja_lista + ['nowy element'])  # dostaniemy [1,2,3,'nowy element']
print(moja_lista + [4, 5])  # = [1,2,3,4,5]

lista2 = ['a', 'b', 'c']
print(moja_lista + lista2)  # = [1,2,3,'a','b','c']

print("\nPrzypisanie na nowo zawartości listy")
moja_lista = moja_lista + ['dodaj element na stale']
print(moja_lista)

# ================================================== Powielanie list

print("\nPowielanie listy * 3")
moja_lista * 3
print(moja_lista)
print(moja_lista * 3)

# ================================================== Zastępowanie elementu listy

print("\nZastępowanie elementu listy")
moja_lista[0] = 'zastap element'
print(moja_lista)

# ================================================== Dodawanie elementów do listy

moja_lista = [1, 2, 3]

print("\nDługość listy (liczba elementów) [1, 2, 3]")
len(moja_lista)

print("\nDodawanie elementów do listy")
moja_lista.append('dodaj element')  # Dodawanie elementu na koniec listy
print(moja_lista)

moja_lista.insert(1, 'dodaj drugi element')  # Dodawanie elementu w miejsce o indeksie 1
print(moja_lista)

# =============================================     Usuwanie elementów z listy

nowa_lista = ['a', 'b', 'c', 'a']
print("\n", nowa_lista)
print("Usuwanie elementu listy za pomocą .pop()")
nowa_lista.pop()  # Usunięcie ostatniego elementu listy (odwrotność funkcji .append())
nowa_lista.pop(0)  # Usunięcie z listy elementu o indeksie 0
print(nowa_lista)

print("Usuwanie elementu listy za pomocą .remove()")
nowa_lista = ['a', 'b', 'c', 'a']
nowa_lista.remove('a')  # Usunięcie z listy pierwszego wystąpienia zmiennej 'a'
print(nowa_lista)

# ==============================================      Przeszukiwanie listy

nowa_lista = ['a', 'b', 'c', 'a']
print("\n", nowa_lista)
print("Przeszukiwanie listy")

print('a' in nowa_lista)  # Prawda (True) jeśli element występuje w liście, w przeciwnym przypadku fałsz (False)
print(nowa_lista.index('a'))  # Zwraca indeks pierwszego wystąpienia szukanego elementu w liście
print(nowa_lista.index('a', 1, 10))  # Jak wyżej tylko przeszukuje listę w zakresie indeksów od 1 do 10

print(nowa_lista.count('a'))    # Zwraca liczbę wystąpień elementu listy
print(max(nowa_lista))         # Zwraca największy element listy
print(min(nowa_lista))         # Najmniejszy element listy

# ===============================================       Modyfikowanbie kolejności elementów w liście

print("\nModyfikowanbie kolejności elementów w liście")
nowa_lista = ['a', 'b', 'c', 'a']

# Odwracanie kolejności listy
nowa_lista.reverse()
print(nowa_lista)

# Sortowanie elementów listy
nowa_lista.sort()
print(nowa_lista)

# ==================================================================================