# =============================================
# M2Z13

liczba_d = 0
liczba_b = "01111111"

i = len(liczba_b) - 1

for cyfra in liczba_b:
    liczba_d = liczba_d + (int(cyfra) * pow(2, i))
    i = i - 1

print(liczba_d)

# =============================================