# =============================================
# M3Z05

import random

tab = [random.randrange(1, 100, 1) for i in range(7)]

print(tab)
tab.sort()
print(tab)

print("Najwieksza libcza to:", tab[-1])
print("Najmniejsza liczba to:", tab[0])

# =============================================