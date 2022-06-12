# =============================================
# M3Z06

tekst = input("Wpisz swój tekst:")

liczba_liter = 0
ilosc_liczb = 0
ilosc_znakow = 0

for i in tekst:
    if i.isalpha():
        liczba_liter += 1
    elif i.isdigit():
        ilosc_liczb += 1
    else:
        ilosc_znakow += 1

print("Liczba liter to: ", liczba_liter)
print("Ilość liczb to: ", ilosc_liczb)
print("Liczba znaków to: ", ilosc_znakow)

# =============================================