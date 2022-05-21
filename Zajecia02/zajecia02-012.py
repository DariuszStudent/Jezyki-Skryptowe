# =============================================
# M2Z12

liczba_d = 5
liczba_b = ""

while (liczba_d != 0 ):
    r = liczba_d % 2
    #print(r, end='')
    liczba_b = str(r) + liczba_b
    liczba_d //= 2

print(liczba_b)

#zera wiodące!
# =============================================