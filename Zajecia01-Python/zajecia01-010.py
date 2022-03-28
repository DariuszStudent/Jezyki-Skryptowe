# =============================================
# M1Z10
from datetime import datetime

teraz = datetime.now()

print("Aktualnie mamy: ", teraz)

rok = int(input("Podaj rok urodzenia: "))
rok_aktualny = int(teraz.strftime("%Y"))
wynik = rok_aktualny - rok
print("Wiek: ", wynik)

# =============================================
