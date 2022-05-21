# =============================================
# M2Z05

e = -1
licznik = 1
suma = srednia = 0
_max = _min = 0

print("Podaj liczny całkowite, 0 kończy.")

while (e != 0):
    print("Podaj element nr ", licznik, ":", end='')
    e = int(input(""))
    if (e == 0):
        licznik -= 1
        break
    if (e != 0):
        suma += e
    if (licznik == 1):
        _max = _min = e
    if (e > _max):
        _max = e
    if (e < _min and e != 0):
        _min = e
    if (licznik != 0):
        licznik += 1

print("Ilość elementów:", licznik, "Suma", suma, "max", _max, "min", _min)
print("Srednia: %0.2f, suma %05d"%(suma/licznik, suma))
print("Maksimum: {0:4d}, Minimum: {1:4d}".format(_max,_min))


# =============================================