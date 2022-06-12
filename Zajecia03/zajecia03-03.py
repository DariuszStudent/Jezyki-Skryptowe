# =============================================
# M3Z03

import random

tab = [random.randrange(1, 10, 1) for i in range(7)]
iloscliczb = len(tab)
liczba_min = _min = tmp = 0


print("Tablica przed sortowaniem:")
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