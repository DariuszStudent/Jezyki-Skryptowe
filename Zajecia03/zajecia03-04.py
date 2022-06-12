# =============================================
# M3Z04

liczba_min = _min = tmp = 0
licznik = 0
tab = []
iloscliczb = len(tab)

liczba_elementow = int(input("Ile ma być liczb? "))
for i in range(liczba_elementow):
    print("Podaj liczbę")
    element = int(input(""))
    licznik += 1
    tab.append(element)

print("Tablica nie posortowana:")
print(tab)

for tmp in range(0, iloscliczb - 1, 1):

    liczba_min = tmp
    minimum = tab[tmp]

    for i in range(tmp + 1, iloscliczb, 1):
        if (tab[i] < minimum):
            minimum = tab[i]
            ndx_min = i

    tab[liczba_min] = tab[tmp]
    tab[tmp] = minimum

print("Tablica po sortowaniu:")
print(tab)

# =============================================
