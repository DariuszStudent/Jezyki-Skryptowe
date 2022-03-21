# =============================================
# M1Z2

# zmienne
liczba1 = 20
liczba2 = 30

#Działania
print("Działania")
suma = liczba1 + liczba2
iloczyn = liczba1 * liczba2
odejmowanie1 = liczba1 - liczba2
odejmowanie2 = liczba2 - liczba1
dzielenie1 = liczba1 / liczba2
dzielenie2 = liczba2 / liczba1
dzielenieCalkowite1 = liczba1 // liczba2
dzielenieCalkowite2 = liczba2 // liczba1

#Wyświetlenie czytelne dla użytkownika
print(str(liczba1) + " + " + str(liczba2) + " = " + str(suma))
print(str(liczba1) + " * " + str(liczba2) + " = " + str(iloczyn))
print(str(liczba1) + " - " + str(liczba2) + " = " + str(odejmowanie1))
print(str(liczba2) + " - " + str(liczba1) + " = " + str(odejmowanie2))
print("Dzielenie rzeczywiste")
print(str(liczba1) + " : " + str(liczba2) + " = " + str(dzielenie1))
print(str(liczba2) + " : " + str(liczba1) + " = " + str(dzielenie2))
print("Dzielenie całkowite")
print(str(liczba1) + " : " + str(liczba2) + " = " + str(dzielenieCalkowite1))
print(str(liczba2) + " : " + str(liczba1) + " = " + str(dzielenieCalkowite2))

# =============================================

# Dzielenie rzeczywiste robimy jednym znakiem "/"
# Dzielenie całkowite wykonujemy dwoma znakami "//"